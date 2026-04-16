---
title: "IO-Awareness"
type: concept
tags: [gpu, memory, optimization, algorithms, performance]
created: 2026-04-17
sources: [flash-attention.md]
---

# IO-Awareness

Designing algorithms that account for reads and writes between different levels of memory hierarchy. Critical for modern GPU performance where compute is faster than memory.

## Overview

**IO-awareness** = Designing algorithms that minimize data movement between fast and slow memory, considering the memory hierarchy explicitly.

### The Memory Wall Problem

Compute has improved faster than memory bandwidth:

| Year | Compute Improvement | Memory Improvement |
|------|-------------------|-------------------|
| 2012-2022 | ~100x (FLOPs) | ~4x (bandwidth) |

**Result**: Most operations are now **memory-bound**, not compute-bound.

## Memory Hierarchy

### GPU Memory Levels

```
┌────────────────────────────────────────────┐
│                  HBM                       │
│  80 GB, 1.5-2.0 TB/s                     │
│  (GPU Die + Package)                      │
└────────────────────┬───────────────────────┘
                    │
                    │ ~300-600 cycles
                    ▼
┌────────────────────────────────────────────┐
│              L2 Cache                      │
│  6-72 MB, ~200 cycles                     │
└────────────────────┬───────────────────────┘
                    │
                    │ ~34 cycles
                    ▼
┌────────────────────────────────────────────┐
│     L1 Cache / Shared Memory               │
│  128 KB/SM, ~5ns                         │
└────────────────────┬───────────────────────┘
                    │
                    │ ~1 cycle
                    ▼
┌────────────────────────────────────────────┐
│               Registers                    │
│  ~256 KB/SM, ~1 cycle                     │
└────────────────────────────────────────────┘
```

### A100 Memory Specifications

| Memory Type | Size | Bandwidth | Latency |
|-------------|------|-----------|---------|
| HBM | 40-80 GB | 1.5-2.0 TB/s | ~300-600 ns |
| L2 Cache | 40 MB | ~2.5 TB/s | ~200 cycles |
| L1 Cache | 128 KB/SM | ~19 TB/s | ~34 cycles |
| Registers | 256 KB/SM | ~19 TB/s | ~1 cycle |

**SRAM (L1 + Registers)**: 19 TB/s
**HBM**: 1.5-2.0 TB/s
**Gap**: ~10x speed difference!

## IO Complexity Analysis

### Definition

**IO complexity**: Number of data transfers between two levels of memory.

For algorithm A computing on data of size N with fast memory size M:

```
IO(A) = Number of reads/writes to slow memory
```

### Standard vs IO-Aware

#### Standard Attention

```
Algorithm:
1. S = QK^T      → Write N×N matrix to HBM
2. P = softmax(S) → Write N×N matrix to HBM
3. O = PV         → Write N×N matrix to HBM

Total: O(N²) HBM writes
```

#### IO-Aware (FlashAttention)

```
Algorithm:
1. Load Q, K, V blocks to SRAM
2. Compute attention incrementally
3. Write O and statistics to HBM

Total: O(Nd²/M) HBM writes (sub-quadratic)
```

## IO Complexity Results

### FlashAttention Theorem

For attention with sequence length N, head dimension d, SRAM size M:

| Algorithm | IO Complexity |
|-----------|---------------|
| Standard | O(Nd + N²) |
| FlashAttention | O(N²d²/M) |

For typical values:
- d = 64 (GPT-2)
- M = 192 KB (A100 per SM)
- d²/M = 64²/192K ≈ 20

**Result**: FlashAttention requires ~20x fewer HBM accesses.

### Lower Bound

**Proposition**: No exact attention algorithm can asymptotically improve FlashAttention's IO complexity for all SRAM sizes.

```
Proof sketch:
- For small M: Must make O(N²d²/M) accesses
- For large M: O(Nd) is optimal
```

## Why IO-Awareness Matters

### Example: Matrix Multiplication

**Standard**: Load A, B, compute C, write C
**IO-aware (tiling)**: Load tiles, compute, write tiles

```cuda
// Standard matmul
for i in range(N):
    for j in range(N):
        for k in range(N):
            C[i,j] += A[i,k] * B[k,j]
// O(N³) compute, O(N²) memory ops

// Tiled matmul
for i in range(N/T):
    for j in range(N/T):
        load tile A[i], B[j] to shared memory
        compute C[i,j] from tiles
        write C[i,j]
// O(N³) compute, O(N²/T) memory ops
```

### Why Compiler Optimizations Fall Short

```python
# PyTorch: Fuses operations
y = F.relu(x)  # One kernel
y = F.softmax(x, dim=-1)  # Another kernel

# Problem: Intermediate values still written to HBM
# Can't fuse across operations that need intermediate storage
```

## IO-Awareness in Practice

### Kernel Fusion

**Traditional approach**: Multiple kernels with HBM writes between

```
[Load A] → [Kernel 1] → [Write A'] → [Load A'] → [Kernel 2] → [Write B]
```

**IO-aware**: Single fused kernel

```
[Load A] → [Kernel 1+2 fused] → [Write B]
```

### Case Study: Attention Operations

#### Standard Implementation (PyTorch)

```python
# Multiple HBM writes/reads
S = Q @ K.transpose(-2, -1)    # Write S to HBM
P = F.softmax(S, dim=-1)        # Read S, write P to HBM
if mask: P = P.masked_fill(...)  # Write P to HBM
O = P @ V                        # Read P, write O to HBM
```

#### FlashAttention

```cuda
// Single kernel, all in SRAM
__global__ void flash_attn_kernel(...) {
    // Load K, V block
    // Load Q block
    // Compute S = QK^T (SRAM)
    // Compute P = softmax(S) (SRAM)
    // Compute O = PV (SRAM)
    // Write O to HBM (single write)
}
```

## When to Apply IO-Awareness

### Memory-Bound Operations

An operation is **memory-bound** when:
```
Time = max(Time_compute, Time_memory)
Time_memory = Bytes / Bandwidth >> Time_compute
```

### Examples

| Operation | Bound | IO-Aware Gain |
|-----------|-------|---------------|
| Element-wise ops | Memory | High |
| Softmax | Memory | High |
| Attention | Memory | **Very High** |
| Large matmul | Compute | Low |
| Conv (large k) | Compute | Low |

### Roofline Model

```
                    Performance
                    (GFLOPS)
                        │     ╱╲
                        │    ╱  ╲ Compute-bound
                        │   ╱    ╲ region
                        │  ╱      ╲──── Peak FLOPs
                        │ ╱        ╲
                        │╱          ╲
                        │            ╲
                        │             ╲ Memory-bound
                        │              ╲ region
                        └───────────────────────►
                              Arithmetic Intensity
                              (FLOPs/byte)
```

## Implementing IO-Aware Algorithms

### Steps

1. **Profile**: Identify memory-bound operations
2. **Analyze**: Determine memory access patterns
3. **Tile**: Break data into blocks fitting in fast memory
4. **Fuse**: Combine operations into single kernel
5. **Verify**: Ensure correctness and performance

### CUDA Implementation Pattern

```cuda
__global__
void io_aware_kernel(float* slow_mem, int N, int block_size) {
    __shared__ float fast_mem[BLOCK][BLOCK];
    
    // 1. Load block from slow to fast memory
    load_block(slow_mem, fast_mem);
    
    // 2. Compute all operations in fast memory
    //    - No slow memory accesses here!
    compute_operations(fast_mem);
    
    // 3. Write result from fast to slow memory
    store_block(fast_mem, slow_mem);
}
```

## Related Concepts

- [[FlashAttention]] — IO-aware attention algorithm
- [[Tiling]] — Block-based memory access
- [[Kernel Fusion]] — Combining operations
- [[Computational Intensity]] — FLOPs/byte ratio
- [[Memory Hierarchy]] — Where IO happens
