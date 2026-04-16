---
title: "FlashAttention-2"
type: concept
tags: [attention, transformers, gpu, optimization, parallelism]
created: 2026-04-17
sources: [flash-attention-2.md]
---

# FlashAttention-2

An improved version of FlashAttention with better work partitioning, achieving 2x speedup and reaching 50-73% of theoretical GPU throughput.

## Overview

FlashAttention-2 improves upon FlashAttention by addressing three sources of inefficiency:

1. **Excessive non-matmul FLOPs** in the algorithm
2. **Low occupancy** for long sequences
3. **Unnecessary shared memory communication** between warps

**Result**: ~2x faster than FlashAttention, ~10x faster than PyTorch.

## FlashAttention's Problem

### Utilization Gap

| Implementation | % of Max Throughput |
|----------------|-------------------|
| Optimized GEMM | 80-90% |
| FlashAttention | 25-40% |
| **FlashAttention-2** | **50-73%** |

**Gap of 2x between FlashAttention and GEMM = room for improvement.**

### Hardware Context: Why Matmul Matters

On A100 GPU:

| Operation | Throughput | Relative Cost |
|-----------|------------|---------------|
| FP16 matmul | 312 TFLOPs/s | 1x (baseline) |
| Non-matmul FP32 | 19.5 TFLOPs/s | 16x |

**Key insight**: Each non-matmul FLOP costs 16x more than a matmul FLOP in time.

## Improvement 1: Reduce Non-Matmul FLOPs

### FlashAttention Forward Pass Issues

```python
# FlashAttention: Rescale at each step
for j in range(T_r):
    O = diag(l^(j))^-1 @ O^(j)  # Rescale
    O += diag(l^(j))^-1 @ S_ij @ V_j
```

Every iteration requires:
- Matrix scaling
- Diagonal matrix operations
- Multiple scaling factors

### FlashAttention-2: Unscaled Accumulation

```python
# FlashAttention-2: Keep O~ unscaled
for j in range(T_r):
    O_tilde = diag(m^(j-1))^-1 @ O_tilde^(j-1)  # Rescale once per row
    O_tilde += S_ij @ V_j  # No scaling!

# Only scale at the very end
O = diag(l^(last))^-1 @ O_tilde
```

**Benefits**:
- Fewer diagonal matrix operations
- Cleaner numerical properties
- Simpler code

### Storing Logsumexp Instead of Max and Sum

**FlashAttention stores**:
- `m` = row-wise maximum
- `ℓ` = row-wise sum of exponentials

**FlashAttention-2 stores**:
- `ℓ̃` = `m + log(ℓ)` = logsumexp

**Benefits**:
- One value instead of two
- Cleaner backward pass
- Same information content

## Improvement 2: Parallelization Along Sequence Length

### FlashAttention Parallelization

```
Parallelized over: batch size × number of heads
Each thread block: processes one attention head
```

**Problem**: For long sequences, batch size is small → few thread blocks → low occupancy.

### FlashAttention-2: Additional Sequence Parallelization

```
Forward Pass:
┌─────────────────────────────────────────────────────────┐
│  Thread Block 1  │  Thread Block 2  │  Thread Block 3  │
│  Row Block 1      │  Row Block 2      │  Row Block 3    │
│  (Q_1 @ K, V)    │  (Q_2 @ K, V)    │  (Q_3 @ K, V)  │
└─────────────────────────────────────────────────────────┘
Each thread block = one row block of the attention matrix
No communication between thread blocks!
```

```
Backward Pass:
┌─────────────────────────────────────────────────────────┐
│  Thread Block 1  │  Thread Block 2  │  Thread Block 3  │
│  Col Block 1      │  Col Block 2      │  Col Block 3    │
│  (Q @ K_1, V_1)  │  (Q @ K_2, V_2)  │  (Q @ K_3, V_3)  │
└─────────────────────────────────────────────────────────┘
Each thread block = one column block
Atomic adds to update dQ
```

**Key insight**: Forward and backward have complementary parallelization.

### When This Matters

| Scenario | Batch Size | Heads | Benefit |
|----------|-----------|-------|---------|
| Short sequences | Large | Many | Already efficient |
| Long sequences | Small | Few | **Huge improvement** |

## Improvement 3: Split-Q Instead of Split-K

### FlashAttention: Split-K

```
Thread Block
├── Warp 1: Q_all, K_1, V_1 → partial_S_1, partial_O_1
├── Warp 2: Q_all, K_2, V_2 → partial_S_2, partial_O_2
├── Warp 3: Q_all, K_3, V_3 → partial_S_3, partial_O_3
└── Warp 4: Q_all, K_4, V_4 → partial_S_4, partial_O_4
         ↓
    Sync threads
         ↓
    Reduce partial_O values
         ↓
    Write final O
```

**Problem**: Warps must communicate through shared memory.

### FlashAttention-2: Split-Q

```
Thread Block
├── Warp 1: Q_1, K_all, V_all → O_1
├── Warp 2: Q_2, K_all, V_all → O_2
├── Warp 3: Q_3, K_all, V_all → O_3
└── Warp 4: Q_4, K_all, V_all → O_4
         ↓
    Each warp writes its own O slice
    No communication needed!
```

**Benefit**: No synchronization overhead, no shared memory reads/writes.

### Why Split-Q Works

1. Q is the "query" — different warps compute different output rows
2. K, V are "keys/values" — same for all warps
3. Each warp needs full K, V to compute its Q slice
4. Results are independent — no reduction needed

## Algorithm: FlashAttention-2 Forward Pass

```python
def flash_attention_2_forward(Q, K, V, B_r, B_c):
    # Block sizes: B_r for rows, B_c for columns
    T_r = N // B_r  # Number of row blocks
    T_c = N // B_c  # Number of column blocks
    
    # Parallelize over T_r row blocks (sequence length)
    for i in range(T_r):
        # Load Q_i to SRAM
        Q_i = load_block(Q, i, B_r, d)
        
        # Initialize running statistics
        m_prev = -inf
        l_prev = 0
        O_tilde = zeros(B_r, d)
        
        # Inner loop over K, V blocks
        for j in range(T_c):
            # Load K_j, V_j to SRAM
            K_j = load_block(K, j, B_c, d)
            V_j = load_block(V, j, B_c, d)
            
            # Compute attention scores
            S_ij = Q_i @ K_j.T  # B_r x B_c
            
            # Update running statistics
            m_ij = rowmax(S_ij)
            l_ij = rowsum(exp(S_ij - m_ij))
            
            m_new = max(m_prev, m_ij)
            l_new = exp(m_prev - m_new) * l_prev + exp(m_ij - m_new) * l_ij
            
            # Update unscaled output
            O_tilde = exp(m_prev - m_new) * O_tilde + exp(m_ij - m_new) * S_ij @ V_j
            
            m_prev, l_prev = m_new, l_new
        
        # Final scaling
        O_i = exp(m_prev) * O_tilde / l_new
        
        # Store logsumexp for backward
        l_tilde_i = m_prev + log(l_new)
        
        write_block(O, O_i, i)
        write_block(l_tilde, l_tilde_i, i)
```

## Performance Comparison

### Theoretical Utilization

| Algorithm | Forward | Backward |
|-----------|---------|----------|
| Standard PyTorch | 5-10% | 5-10% |
| FlashAttention | 30-50% | 25-35% |
| FlashAttention-2 | **50-73%** | **50-63%** |
| GEMM (peak) | 80-90% | 80-90% |

### Measured Speedup

| Configuration | vs FlashAttention | vs PyTorch |
|---------------|------------------|------------|
| Forward (no mask, d=64) | ~1.8x | ~10x |
| Forward (causal, d=64) | ~1.7x | ~8x |
| Backward (d=64) | ~1.6x | ~8x |

### End-to-End Training

| Model | Seq Length | FlashAttention | FlashAttention-2 |
|-------|------------|----------------|------------------|
| 1.3B | 2k | baseline | 1.3x faster |
| 2.7B | 8k | baseline | 1.3x faster |

**Result**: 225 TFLOPs/s per A100 (72% utilization)

## Causal Masking Optimization

### Problem: Standard Causal Mask

```python
# Naive: Apply mask to all entries
S = Q @ K.T
S = S.masked_fill(triu(ones(N, N), 1), -inf)
P = softmax(S)
```

### FlashAttention-2: Block Skipping

```python
# Identify blocks where ALL entries are masked
# For block (i, j) where i*B_r > (j+1)*B_c:
#   Skip entirely!

for i in range(T_r):
    for j in range(T_c):
        if row_start(i) > col_end(j):
            continue  # Skip this block
        # Compute attention for this block
```

**Benefit**: For long sequences, ~half the blocks are skipped.

### Per-Row Masking

```
For each row, only ONE block needs masking:
Row 0: blocks [0,1,2,...,N/B-1] → all masked except block 0
Row 1: blocks [0,1,2,...,N/B-1] → all masked except blocks 0,1
...
Row N: blocks [0,1,2,...,N/B-1] → no masking

Total masked entries: N(N-1)/2
But only N blocks need per-row masking (not N²)
```

**Result**: 1.7-1.8x speedup for causal attention.

## Implementation Details

### Block Size Selection

```python
# Choices: {64, 128} × {64, 128}
B_r = 64 or 128  # Row block size
B_c = 64 or 128  # Column block size

# Depends on:
# - Head dimension d
# - Device shared memory size
# - Register pressure
```

### Warp Configuration

```python
# Typical: 4 or 8 warps per thread block
warps_per_block = 4  # or 8

# FlashAttention-2: Split Q across warps
Q_slice = warp_id * (B_r / warps_per_block)
# Each warp computes B_r/warps rows of Q
```

## Related

- [[FlashAttention]] — Original algorithm
- [[IO-Awareness]] — Core principle
- [[Split-Q]] — Warp partitioning scheme
- [[Parallelism]] — Sequence-length parallelization
- [[FlashAttention-2 Paper]] — Source paper
