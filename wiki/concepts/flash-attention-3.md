---
title: "FlashAttention-3"
type: concept
tags: [attention, transformers, gpu, hopper, h100, optimization, asynchrony]
created: 2026-04-17
sources: [flash-attention-3.md]
---

# FlashAttention-3

The third generation of FlashAttention, exploiting Hopper H100 GPU features to achieve 740 TFLOPs/s (75% utilization) and 1.2 PFLOPs/s with FP8.

## Overview

FlashAttention-3 advances the FlashAttention family by exploiting three key Hopper features:

1. **Asynchrony**: TMA and WGMMA are asynchronous
2. **Warp Specialization**: Split producers and consumers into separate warps
3. **Low Precision**: FP8 Tensor Cores with 2x throughput

**Result**: 1.5-2x faster than FlashAttention-2, reaching 75% of theoretical maximum.

## FlashAttention-2's Limitations

### Utilization Gap

| Implementation | H100 Utilization |
|----------------|----------------|
| Optimized GEMM | 80-90% |
| FlashAttention-2 | 35% |
| **FlashAttention-3** | **75%** |

### Why FA-2 Underperformed

1. **No Hopper-specific instructions**: Used Ampere-style code
2. **Synchronous model**: No overlap between data movement and compute
3. **No low-precision**: No FP8 support
4. **Uniform warp usage**: No specialization

## Core Innovation: Asynchrony

### Hopper Hardware Features

#### Tensor Memory Accelerator (TMA)

- Dedicated hardware unit for memory transfers
- Asynchronous: doesn't stall CUDA cores
- Can overlap with compute
- Loads directly to/from shared memory

```cuda
// TMA load (non-blocking)
asm volatile("ldg.global.f32 [%0], [%1];" : : "l"(dst), "l"(src));
```

#### Warpgroup-Wide MMA (WGMMA)

- Asynchronous matrix multiplication
- Sources operands directly from shared memory
- Can overlap with other operations
- FP8 support (2x throughput vs FP16)

### Producer-Consumer Pattern

```
Producer Warps:
┌─────────────────────────────────────────────┐
│  Issue TMA loads from HBM to SMEM          │
│  Don't wait for completion                  │
│  Continue issuing more loads                │
└─────────────────────────────────────────────┘
                    │
                    │ SMEM
                    ▼
┌─────────────────────────────────────────────┐
│  Consumer Warps:                           │
│  Execute WGMMA using data in SMEM          │
│  Don't need to wait for TMA to finish     │
└─────────────────────────────────────────────┘
```

## Algorithm: Warp-Specialized Pipelining

### Circular SMEM Buffer

```python
class Pipeline:
    def __init__(self, num_stages):
        self.num_stages = num_stages
        self.smem_buffer = [None] * num_stages
        self.barriers = barriers(num_stages)
    
    def produce(self, stage_idx, data):
        self.smem_buffer[stage_idx] = data
        self.barriers[stage_idx].commit()  # Notify consumers
    
    def consume(self, stage_idx):
        self.barriers[stage_idx].wait()  # Wait for producer
        return self.smem_buffer[stage_idx]
```

### Producer Warps (Producer Side)

```python
# Producer warpgroup
for i in range(T_c):
    # Wait for previous stage to be consumed
    wait(stage=(i % num_stages))
    
    # Issue TMA loads for K_i, V_i
    tma_load_async(K_i, smem_buffer[i])
    tma_load_async(V_i, smem_buffer[i])
    
    # Notify consumers
    commit(stage=i % num_stages)
```

### Consumer Warps (Consumer Side)

```python
# Consumer warpgroup
for i in range(T_c):
    # Wait for K_i to be loaded
    wait(stage=i % num_stages)
    
    # Execute WGMMA: S = Q @ K_i^T
    S_i = wgmma(Q, K_i.T)  # Async, doesn't block
    
    # Meanwhile, TMA is loading next K_(i+1)
    
    # Execute softmax, then WGMMA: O += P_i @ V_i
    O = compute_attention(S_i, O, V_i)
```

## Pingpong Scheduling: GEMM-Softmax Overlap

### The Problem: Exp is Slow

On H100:
| Operation | Throughput | Relative |
|-----------|------------|----------|
| FP16 matmul | 989 TFLOPs/s | 1x |
| FP16 exp | 3.9 TFLOPs/s | 254x slower |

For head dim 128:
- 512x more matmul FLOPs than exp
- But exp has 256x lower throughput
- **Result**: exp takes 50% of runtime!

### Solution: Warpgroup Pingpong

```
Timeline:

Warpgroup 1: [GEMM1][Softmax1][GEMM2][Softmax2][GEMM3][...]
                    ↓ overlap
Warpgroup 2: [Wait][GEMM1][Softmax1][GEMM2][Softmax2][...]
                    ↑
              Executed while WG1 does softmax
```

### How It Works

1. **Barrier synchronization**: Forces GEMM of WG1 to complete before WG2 starts
2. **Role swap**: WG1 does softmax while WG2 does GEMM
3. **Result**: Exp scheduled during matmul cycles

### Performance Impact

| Configuration | Without Overlap | With Overlap |
|---------------|-----------------|--------------|
| FP16, d=128, seq=8K | 570 TFLOPs/s | 661 TFLOPs/s |
| Improvement | - | +16% |

## Intra-Warpgroup Pipelining

### 2-Stage GEMM-Softmax Pipeline

```python
# Within one warpgroup, pipeline across iterations

S_cur = wgmma(Q, K_0.T)  # Stage 1
commit_and_wait()           # Wait for S_cur

# While computing S_next...
for i in range(1, T_c - 1):
    # Compute softmax for S_cur
    P_cur, m_cur, l_cur = softmax(S_cur)
    
    # Issue next GEMM (doesn't block)
    S_next = wgmma(Q, K_i.T)  # Stage 2
    commit(but_dont_wait())
    
    # Meanwhile, WGMMA for PV of previous iteration
    O = wgmma(P_prev, V_prev)
    commit_and_wait()
    
    # Wait for S_next to complete
    wait()
    
    # Update O with P_cur @ V_cur
    O = update_attention(O, P_cur, V_cur)
    
    S_cur = S_next  # Advance pipeline
```

### Benefits

1. **Overlaps softmax with next GEMM**
2. **Keeps WGMMA units busy**
3. **Hides softmax latency**

## FP8 Support

### Why FP8?

| Precision | Throughput | Memory |
|-----------|------------|--------|
| FP16/BF16 | 989 TFLOPs/s | 2 bytes/elem |
| FP8 | ~1900 TFLOPs/s | 1 byte/elem |

**Benefits**: 2x throughput, 2x more data in cache

### Layout Challenges

FP8 WGMMA requires **k-major format** for operands:
- A operand: mn-major or k-major
- B operand: **must be k-major**
- Accumulator: special layout

### In-Kernel Transpose

```python
# Problem: V is sequence-major in HBM
# Solution: Transpose V tiles in SMEM

# Producer warp: Load V tile
V_tile = tma_load(V, indices)

# Producer warp: In-kernel transpose using LDSM/STSM
V_transposed = ldsmtranspose(V_tile)  # Now k-major

# Consumer warp: Use transposed V for WGMMA
O = wgmma(P, V_transposed)
```

### Accumulator Layout Transformation

FP8 WGMMA has layout constraints:
- Accumulator: row-major
- Operand A: different layout

**Solution**: Register permutation using byte permute instructions.

## Accuracy: Block Quantization + Incoherent Processing

### The Problem: Outliers

LLMs have outlier features — values much larger than typical:

```python
# Simulated outlier distribution
x = Normal(0, 1) + Bernoulli(0.001) * Normal(0, 10)
# 0.1% of values have 10x larger magnitude
```

### Baseline: Per-Tensor Quantization

```python
# One scale factor for entire tensor
scale = max(abs(Q))  # Dominated by outliers
Q_int8 = round(Q / scale)
```

**Problem**: Outliers waste quantization range.

### Solution 1: Block Quantization

```python
# Per-block scaling
block_size = 32 * d  # e.g., 64 * 64

for i in range(0, N, block_size):
    block = Q[i:i+block_size]
    scale = max(abs(block))  # Local to block
    Q_int8[i:i+block_size] = round(block / scale)
```

**Benefit**: Better precision within each block.

### Solution 2: Incoherent Processing

```python
# Random orthogonal matrix M (Hadamard product of diagonal ±1)
M = random_hadamard() * random_sign()

# Multiply Q, K by M before quantizing
Q_tilde = Q @ M  # Orthogonal transform
K_tilde = K @ M

# Since (QM)(KM)^T = QKK^T, attention is unchanged!
# But outliers are "spread out" across all dimensions
```

**Why it works**: Each output of QM is a random sum of Q entries, spreading outlier influence.

### Combined Results

| Method | RMSE | Relative Error |
|--------|-------|----------------|
| Per-tensor FP8 | 2.4e-2 | baseline |
| Block quant only | 9.3e-3 | 2.6x better |
| Block + incoherent | 9.1e-3 | 2.6x better |

## Implementation Details

### Block Size Selection

| Head Dim | Block Size (B_r, B_c) |
|----------|------------------------|
| 64 | (64, 64) |
| 128 | (64, 64) or (128, 64) |
| 256 | (64, 128) |

### Register Pressure

2-stage pipeline requires:
- Extra S_next buffer
- Extra P buffer
- Multiple m, l statistics

**Trade-off**: Better overlap vs register spilling.

### CUTLASS Integration

Uses CUTLASS primitives for:
- WGMMA instructions
- TMA operations
- Register allocation

## Performance Summary

### FP16 Results

| Metric | FlashAttention-2 | FlashAttention-3 |
|--------|-------------------|-------------------|
| Forward (d=64) | ~400 TFLOPs/s | ~400-470 TFLOPs/s |
| Forward (d=128) | ~350 TFLOPs/s | ~600-650 TFLOPs/s |
| Backward (d=64) | ~300 TFLOPs/s | ~400-450 TFLOPs/s |
| Utilization | 35% | 75% |

### FP8 Results

- Up to 1.2 PFLOPs/s
- Competitive with cuDNN
- Head dim 64: Faster than cuDNN
- Head dim 128/256: At par without causal

## Related

- [[FlashAttention-2]] — Previous version
- [[Warp Specialization]] — Producer-consumer asynchrony
- [[GEMM-Softmax Overlap]] — Pingpong scheduling
- [[FP8 Attention]] — Low-precision techniques
- [[TMA]] — Tensor Memory Accelerator
- [[WGMMA]] — Warpgroup Matrix Multiply-Accumulate
