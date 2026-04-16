---
title: "Split-Q"
type: concept
tags: [gpu, parallelism, warps, flash-attention, optimization]
created: 2026-04-17
sources: [flash-attention-2.md]
---

# Split-Q

A warp partitioning scheme in FlashAttention-2 where the query matrix Q is split across warps instead of splitting K and V. Eliminates warp synchronization and shared memory communication.

## Overview

**Split-Q** = Partitioning the Q matrix across warps within a thread block, keeping K and V accessible to all warps.

**Benefit**: Each warp computes independently, no inter-warp communication needed.

## The Problem: Split-K in FlashAttention

### How Split-K Works

```
Thread Block with 4 Warps
         │
         ▼
┌────────────────────────────────────────┐
│  Warp 1: Q_all → computes partial_S_1  │
│  Warp 2: Q_all → computes partial_S_2  │
│  Warp 3: Q_all → computes partial_S_3  │
│  Warp 4: Q_all → computes partial_S_4  │
└────────────────────────────────────────┘
         │
         ▼ Sync (barrier)
         │
┌────────────────────────────────────────┐
│  Reduce partial_S values in shared mem  │
└────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────┐
│  Each warp: partial_O = partial_S @ V  │
└────────────────────────────────────────┘
         │
         ▼ Sync (barrier)
         │
┌────────────────────────────────────────┐
│  Reduce partial_O values                 │
└────────────────────────────────────────┘
```

### Why Split-K is Slow

1. **Multiple sync points**: Warps must synchronize twice
2. **Shared memory writes**: Each warp writes partial results
3. **Shared memory reads**: Warps read others' results to reduce
4. **Latency**: Synchronization barriers have overhead

### Measured Overhead

```
Timeline with Split-K:

Warp 1: [Compute][Write to SM][Sync][Read from SM][Reduce][Write][Sync][...]
Warp 2: [Compute][Write to SM][Sync][Read from SM][Reduce][Write][Sync][...]
         ↑___________________________↑
                    Sync stalls
```

## Split-Q: The Better Approach

### How Split-Q Works

```
Thread Block with 4 Warps
         │
         ▼
┌────────────────────────────────────────┐
│  Warp 1: Q_slice_1, K_all, V_all → O_1  │
│  Warp 2: Q_slice_2, K_all, V_all → O_2  │
│  Warp 3: Q_slice_3, K_all, V_all → O_3  │
│  Warp 4: Q_slice_4, K_all, V_all → O_4  │
└────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────┐
│  Each warp writes its own output slice   │
│  No synchronization needed!              │
└────────────────────────────────────────┘
```

### Why Split-Q is Fast

1. **No sync barriers**: Warps work independently
2. **No shared memory communication**: Each warp has its own Q slice
3. **Parallel execution**: All warps compute simultaneously
4. **Simple final output**: Concatenate output slices

## Mathematical Foundation

### Attention Computation

```
O = softmax(QK^T) @ V
```

### With Q Split Across Warps

```
Q = [Q_1; Q_2; Q_3; Q_4]  # Vertically concatenated
K = [K_1; K_2; K_3; K_4]  # Vertically concatenated
V = [V_1; V_2; V_3; V_4]

S = QK^T
   = [Q_1; Q_2; Q_3; Q_4] @ [K_1; K_2; K_3; K_4]^T
   = [Q_1K^T; Q_2K^T; Q_3K^T; Q_4K^T]

O = SV
   = [S_1; S_2; S_3; S_4] @ V
   = [S_1V; S_2V; S_3V; S_4V]

O = [O_1; O_2; O_3; O_4]
```

**Key**: Each O_i depends only on Q_i, all of K, all of V.

## Implementation Details

### Warp Assignment

```cuda
__global__
void flash_attention_2_kernel(...) {
    // Thread block handles one row block Q_block (size B_r x d)
    
    int warp_id = threadIdx.x / 32;
    int num_warps = blockDim.x / 32;
    
    // Split Q across warps
    int rows_per_warp = B_r / num_warps;
    int row_start = warp_id * rows_per_warp;
    int row_end = row_start + rows_per_warp;
    
    // Each warp has its Q slice
    float* Q_slice = Q_block + row_start * d;
    
    // All warps share K and V
    extern __shared__ float K_shared[];
    extern __shared__ float V_shared[];
    
    // Compute attention for Q slice
    for (int j = 0; j < T_c; j++) {
        // Load K, V blocks to shared memory (all warps)
        load_KV_block(j, K_shared, V_shared);
        __syncthreads();
        
        // Each warp computes its slice
        float* O_slice = O_block + row_start * d;
        compute_attention_slice(Q_slice, K_shared, V_shared, O_slice);
        
        __syncthreads();
    }
    
    // Write output (each warp writes its slice)
    write_output_slice(O_block, row_start, row_end);
}
```

### Memory Access Pattern

| Data | Access Pattern | Warp |
|-------|---------------|------|
| Q_slice | Private to warp | 1 warp |
| K | Shared by all warps | All warps load |
| V | Shared by all warps | All warps load |
| O_slice | Private to warp | 1 warp writes |

### Shared Memory Usage

```cuda
// FlashAttention (Split-K):
// Shared memory per block: K, V, partial_S, partial_O
// = 4 * B_r * B_c * sizeof(float) + ...

// FlashAttention-2 (Split-Q):
// Shared memory per block: K, V only
// = 2 * B_r * B_c * sizeof(float)
// 50% reduction in shared memory!
```

## Performance Impact

### Theoretical Comparison

| Metric | Split-K (FA) | Split-Q (FA-2) |
|--------|-------------|-----------------|
| Sync points | 2 per iteration | 0 |
| SM writes | 2 per iteration | 0 |
| SM reads | 2 per iteration | 0 |
| Shared memory | High | Low |
| Independence | Low | High |

### Practical Speedup

For forward pass:
- **FlashAttention (Split-K)**: ~40 TFLOPs/s
- **FlashAttention-2 (Split-Q)**: ~73 TFLOPs/s
- **Improvement**: ~1.8x

## Backward Pass Considerations

### Split-Q for Backward

The backward pass is more complex because gradients have dependencies:

```python
# Forward: O = softmax(QK^T) @ V

# Backward gradients:
dV = P^T @ dO
dP = dO @ V^T
dS = dP * P - rowwise_sum(dP * P) * P
dQ = dS @ K
dK = Q^T @ dS
```

### Gradient Dependencies

```
dQ needs: dS and K
dK needs: dS and Q
dV needs: P and dO
```

**Problem**: dQ requires aggregating across column blocks.

### Solution: Atomic Updates

```cuda
// For dQ: use atomic adds across column blocks
for each column block j:
    // Thread block computes dQ_block_j
    for i in range(T_r):
        dQ_slice = compute_dQ_slice(...)
        // Atomic add to accumulate across column blocks
        atomicAdd(&dQ[i * B_r * d], dQ_slice);
```

**Note**: Forward pass has no atomic contention; backward pass does.

## Comparison with GEMM

### Matrix Multiply: Split-K is Optimal

In GEMM, C = A @ B:
- Each output element C[i,j] = sum over k of A[i,k] * B[k,j]
- Output rows have no independence
- Split-K is natural and efficient

### Attention: Split-Q is Better

In attention, O = softmax(QK^T) @ V:
- Each output row O[i,*] = sum over j of P[i,j] * V[j,*]
- Output rows are independent (given all K, V)
- Split-Q exploits this independence

**Key insight**: Attention is not a reduction along K, V dimension.

## Related

- [[FlashAttention-2]] — Algorithm using Split-Q
- [[FlashAttention]] — Original algorithm with Split-K
- [[Warp Scheduler]] — Hardware that manages warps
- [[Shared Memory]] — Where Split-K communication happens
