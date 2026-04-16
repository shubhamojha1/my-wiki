---
title: "Tiling"
type: concept
tags: [gpu, memory, optimization, algorithms, parallelism]
created: 2026-04-17
sources: [flash-attention.md]
---

# Tiling

A technique that splits large data structures into blocks (tiles) that fit in fast memory, enabling efficient computation without excessive memory traffic.

## Overview

**Tiling** = Decomposing data and computation into blocks that fit in SRAM/cache.

**Purpose**: Minimize traffic to slow memory by processing data in chunks.

## Tiling in Matrix Operations

### Naive Matrix Multiply

```
For each i, j, k:
    C[i,j] += A[i,k] * B[k,j]
```

**Problem**: A and B repeatedly loaded from slow memory.

### Tiled Matrix Multiply

```
For i_block in range(0, N, BLOCK):
    For j_block in range(0, N, BLOCK):
        Load A[i_block:i_block+BLOCK, :] into SRAM
        For k_block in range(0, N, BLOCK):
            Load B[:, j_block:j_block+BLOCK] into SRAM
            Compute C[i_block:i_block+BLOCK, j_block:j_block+BLOCK] += ...
```

**Improvement**: Each A block loaded once, each B block loaded once per A row block.

## Tiling in FlashAttention

### Attention Structure

```
Standard: S = QK^T, P = softmax(S), O = PV

For sequence length N:
- Q: N × d (rows = tokens)
- K, V: N × d (columns = tokens)
- S: N × N (attention scores)
- P: N × N (attention weights)
- O: N × d (output)
```

**Problem**: S and P are N×N = O(N²) memory.

### FlashAttention Tiling

```
Divide Q into T_c blocks: Q_1, ..., Q_Tc (each: Tr × d)
Divide K into T_r blocks: K_1, ..., K_Tr (each: Br × d)
Divide V into T_r blocks: V_1, ..., V_Tr (each: Br × d)
```

### Processing Order

```
┌─────────────────────────────────────────────────┐
│ K_1, V_1 (Br × d) loaded to SRAM              │
│                                                 │
│ Process Q_1, Q_2, ..., Q_Tc against K_1, V_1   │
│ (Each Q block loaded once, used against K_1)     │
└─────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────┐
│ K_2, V_2 (Br × d) loaded to SRAM              │
│                                                 │
│ Process Q_1, Q_2, ..., Q_Tc against K_2, V_2   │
└─────────────────────────────────────────────────┘
                         │
                         ▼
┌─────────────────────────────────────────────────┐
│ K_3, V_3 (Br × d) loaded to SRAM              │
│ ...                                            │
└─────────────────────────────────────────────────┘
```

## Incremental Softmax via Tiling

### Standard Softmax

```python
def softmax(x):
    x_max = max(x)
    x_exp = exp(x - x_max)
    return x_exp / sum(x_exp)
```

### Tiled/Incremental Softmax

For blocks x^(1), x^(2), ..., x^(t):

```python
def tiled_softmax(blocks):
    # Initialize running statistics
    m = -inf  # row max
    l = 0     # row sum
    o = 0     # accumulated output
    
    for block in blocks:
        # Compute block statistics
        m_block = max(block)
        l_block = sum(exp(block - m_block))
        o_block = block  # placeholder for actual computation
        
        # Update running statistics
        m_new = max(m, m_block)
        l_new = exp(m - m_new) * l + exp(m_block - m_new) * l_block
        o_new = exp(m - m_new) * o + exp(m_block - m_new) * o_block
        
        m, l, o = m_new, l_new, o_new
    
    return o / l
```

### Mathematical Derivation

For concatenated vector x = [x^(1); x^(2)]:

```
softmax(x)_i = exp(x_i) / Σ_j exp(x_j)

Let:
  m^(1) = max(x^(1)),  ℓ^(1) = Σ exp(x^(1) - m^(1))
  m^(2) = max(x^(2)),  ℓ^(2) = Σ exp(x^(2) - m^(2))

Then:
  m = max(m^(1), m^(2))
  ℓ = exp(m^(1) - m) * ℓ^(1) + exp(m^(2) - m) * ℓ^(2)
```

**Key insight**: Can compute softmax one block at a time!

## Block Size Selection

### Constraints

1. **SRAM size**: Block must fit in fast memory
2. **Bandwidth**: Larger blocks = fewer transfers
3. **Occupancy**: Smaller blocks = more parallelism

### FlashAttention Block Sizes

```python
# SRAM size per SM: M bytes
# For A100: M ≈ 192 KB

# Block sizes (for matrix multiply and softmax)
B_r = min(M / (4*d), N)  # Block size for rows (Q)
B_c = min(M / (4*d), d)  # Block size for columns (K, V)

# For d=64, M=192KB:
# B_r = min(192K/(4*64), N) = min(768, N)
# B_c = min(192K/(4*64), 64) = min(768, 64) = 64
```

### Block Size Trade-offs

| Block Size | HBM Accesses | SRAM Utilization |
|------------|--------------|------------------|
| Small | Many | Low |
| Large | Few | High |
| Too Large | Won't fit | N/A |

## Tiling for Attention Backward

### Standard Backward

```
Forward: O = softmax(QK^T) @ V
Backward needs: S = QK^T, P = softmax(S)
```

### Tiled Backward

```
Store: O, m, ℓ (running statistics)

During backward:
1. Load Q, K, V blocks
2. Recompute S, P on-chip
3. Compute gradients
4. Write dQ, dK, dV
```

### Recomputation Formula

```python
# Recompute attention scores
S_block = Q_block @ K^T  # On-chip

# Recompute probabilities  
P_block = exp(S_block - m_row) / ℓ_row

# Compute local gradients
dP_block = dO_block @ V^T
```

## Benefits of Tiling

### Memory Reduction

| Operation | Without Tiling | With Tiling |
|-----------|--------------|--------------|
| Attention | O(N²) | O(N) |
| Matmul | O(N²) | O(N²) (same FLOPs) |
| Memory transfers | O(N²) | O(N²d/M) |

### Bandwidth Utilization

```
Without tiling:
  Load A, B → compute → write C
  Repeat for each element

With tiling:
  Load tile A, B → compute → write tile C
  Fewer loads/stores
```

## Tiling Patterns

### 1D Tiling

```
┌──────────────────────────────┐
│ Data                         │
├──────┬──────┬──────┬───────┤
│ Tile │ Tile │ Tile │ Tile  │
└──────┴──────┴──────┴───────┘
```

### 2D Tiling

```
┌──────────────────────────────┐
│         Data                  │
├────────────┬─────────────────┤
│   Tile     │    Tile         │
├────────────┼─────────────────┤
│   Tile     │    Tile         │
└────────────┴─────────────────┘
```

### 3D Tiling

Used for batched operations:
- Batch dimension
- Sequence dimension  
- Feature dimension

## Implementation in CUDA

### Shared Memory Tiling

```cuda
__global__
void tiled_attention_kernel(float *Q, float *K, float *V, float *O) {
    __shared__ float s_Q[BLOCK][BLOCK];
    __shared__ float s_K[BLOCK][BLOCK];
    __shared__ float s_V[BLOCK][BLOCK];
    
    int row = blockIdx.y * BLOCK + threadIdx.y;
    int col = blockIdx.x * BLOCK + threadIdx.x;
    
    // Load Q tile
    if (row < N && col < d) {
        s_Q[threadIdx.y][threadIdx.x] = Q[row * d + col];
    }
    __syncthreads();
    
    // Process against K, V tiles
    float result = 0.0f;
    for (int tile = 0; tile < N; tile += BLOCK) {
        // Load K, V tiles
        // Compute partial result
    }
}
```

## Tiling in Deep Learning

### FlashAttention Tiling

The key innovation: tiling enables:
1. Computing softmax without full matrix
2. Storing only running statistics
3. Recomputing during backward pass

### Other Tiled Operations

- Tiled matrix multiply (cuBLAS)
- Tiled convolution (cuDNN)
- Tiled reduction (thrust)
- Tiled convolution backward

## Related

- [[FlashAttention]] — Tiling applied to attention
- [[IO-Awareness]] — Why tiling matters
- [[Kernel Fusion]] — Combining tiled operations
- [[Memory Coalescing]] — Efficient memory access
- [[Shared Memory]] — Where tiles live
