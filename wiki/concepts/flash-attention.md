---
title: "FlashAttention"
type: concept
tags: [attention, transformers, gpu, optimization, efficiency]
created: 2026-04-17
sources: [flash-attention.md]
---

# FlashAttention

An IO-aware exact attention algorithm that computes self-attention with fewer memory accesses, achieving significant speedup and memory reduction over standard implementations.

## Overview

FlashAttention computes **exact** self-attention (same output as standard implementation) while:
- Avoiding materialization of the N×N attention matrix in HBM
- Using tiling to compute softmax incrementally
- Employing recomputation during backward pass

**Result**: Up to 7.6x faster, O(N) memory instead of O(N²).

## Standard Attention Implementation

Given Q, K, V ∈ R^(N×d):

```
S = QK^T           → Write N×N matrix to HBM
P = softmax(S)     → Write N×N matrix to HBM  
O = PV             → Write N×N matrix to HBM
```

**Problem**: Three N×N matrix writes/read to HBM. For N=4096, that's 67M elements per matrix.

## FlashAttention Algorithm

### Core Idea

Compute attention by blocks without ever storing the full N×N matrix:

```
Algorithm FlashAttention:

1. Divide Q into T_c blocks (each: Tr × d)
   Divide K, V into T_r blocks (each: Br × d)

2. Initialize O = zeros(N, d)
   Initialize m = -∞ (row max)
   Initialize l = 0 (row sum)

3. For each block K_j, V_j:
   a. Load block to SRAM
   
   b. For each block Q_i:
      - Load Q_i, O_i, m_i, l_i to SRAM
      - Compute S_ij = Q_i K_j^T
      - Compute rowmax ~m_ij, probs ~P_ij
      - Update running stats: m', l'
      - Update output: O_i'
      
   c. Write O, m, l to HBM

4. Return O
```

### Numerical Stability via Running Statistics

Standard softmax:
```
softmax(x)_i = exp(x_i) / Σ exp(x_j)
```

**Problem**: Large values overflow. Standard fix:
```
softmax(x)_i = exp(x_i - max(x)) / Σ exp(x_j - max(x))
```

**FlashAttention**: Compute incrementally with:
- `m` = running row maximum
- `l` = running row sum (normalization factor)
- `o` = accumulated output

### Incremental Softmax Formula

For two blocks x^(1), x^(2):

```
m = max(m^(1), m^(2))                    # New maximum
ℓ = exp(m^(1) - m) * ℓ^(1) + exp(m^(2) - m) * ℓ^(2)  # New sum
o = exp(m^(1) - m) * o^(1) + exp(m^(2) - m) * o^(2)    # New output
```

### Tiling for Softmax

Split attention into blocks:

```
┌─────────────────────────────────────┐
│        Full Attention Matrix         │
│  ┌─────┬─────┬─────┬─────┐        │
│  │ Q₁K₁│ Q₁K₂│ Q₁K₃│ Q₁K₄│  ...  │
│  ├─────┼─────┼─────┼─────┤        │
│  │ Q₂K₁│ Q₂K₂│ Q₂K₃│ Q₂K₄│        │
│  ├─────┼─────┼─────┼─────┤        │
│  │ Q₃K₁│ Q₃K₂│ Q₃K₃│ Q₃K₄│        │
│  └─────┴─────┴─────┴─────┘        │
└─────────────────────────────────────┘
         ↑
    Process one K,V block at a time
    (loads all Q blocks against it)
```

## Memory Access Pattern

### Standard Attention
```
HBM Read:  Q, K, V
HBM Write: S, P, O
HBM Read:  S, P, V (backward)
HBM Write: dQ, dK, dV
```

### FlashAttention
```
HBM Read:  Q, K, V (once)
HBM Write: O, m, ℓ (running stats)
HBM Read:  Q, K, V, O, m, ℓ (backward)
HBM Write: dQ, dK, dV
```

## Forward Pass Details

### Block Sizes

```python
# Choose block sizes to fit in SRAM
# A100: 192KB SRAM per SM

B_r = min(M / (4 * d), N)  # Block size for rows (Q)
B_c = min(M / (4 * d), d)  # Block size for columns (K, V)
```

For A100 with d=64, M=192KB:
- B_r ≈ 256
- B_c = 64

### Kernel Fusion

FlashAttention fuses all operations into one CUDA kernel:

```cuda
// Single fused kernel
__global__
void flash_attention_kernel(
    const float* Q, const float* K, const float* V,
    float* O, float* L,  // output and log-sum-exp
    int N, int d, int Br, int Bc
) {
    // 1. Load K, V blocks to shared memory
    // 2. For each Q block:
    //    a. Load Q block to shared memory
    //    b. Compute S = QK^T (tiled matmul)
    //    c. Compute P = exp(S - rowmax)
    //    d. Update running max and sum
    //    e. Update output: O = diag(ℓ^(-1)) @ (P @ V)
    // 3. Write results to HBM
}
```

## Backward Pass

### Recomputation Strategy

Standard backward needs S and P matrices to compute gradients:
```
dQ = dO @ K @ P^T - rowsum(dO * P) * P @ K^T
dK = P^T @ dO @ Q
```

### FlashAttention Backward

1. **Store** (instead of S, P):
   - O: attention output
   - m: row maximum
   - ℓ: row sum (normalization)

2. **Recompute** during backward:
   - Load Q, K, V blocks
   - Recompute S, P on-chip
   - Compute gradients

**Key insight**: Recomputation is faster than reading S, P from HBM due to high memory bandwidth cost.

## Correctness Proof Sketch

### Invariant

After processing K blocks 1 to j and Q blocks 1 to i:

```
O_ij = diag(ℓ_ij)^(-1) @ (P_ij @ V_j)
m_ij = rowmax(S_ij)
ℓ_ij = rowsum(exp(S_ij - m_ij))
```

Where S_ij = Q_i @ K_j^T and P_ij = exp(S_ij - m_ij) / ℓ_ij

### Proof by Induction

1. **Base case** (j=1, i=1): Trivial
2. **Inductive step**: Show that updating with new block preserves correctness

## Performance Characteristics

### Speedup Factors

| Factor | Impact |
|--------|--------|
| Fewer HBM writes | ~3x reduction |
| Better SRAM utilization | Full bandwidth use |
| Kernel fusion | Eliminates kernel launch overhead |

### Memory Usage

| Implementation | Memory |
|----------------|--------|
| Standard | O(N²) |
| FlashAttention | O(N) |
| Block-Sparse | O(Ns) where s < 1 |

### When FlashAttention Excels

- Long sequences (N > 512)
- Memory-constrained environments
- Large batch sizes
- Small head dimensions (d ≤ 128)

## Implementation Notes

### Dependencies

```python
# PyTorch integration (after installation)
pip install flash-attn

# Usage
from flash_attn import flash_attn_func

output = flash_attn_func(q, k, v, dropout_p=0.0, softmax_scale=None)
```

### Supported Features

- ✅ Exact attention (matches standard)
- ✅ Masking (causal, padding)
- ✅ Dropout (with reproducible seeds)
- ✅ Variable sequence length
- ✅ Multi-head attention
- ✅ Grouped-query attention (GQA)

## Related

- [[IO-Awareness]] — Core principle
- [[Tiling]] — Block-based computation technique
- [[Recomputation]] — Gradient checkpointing for attention
- [[Attention]] — Standard attention mechanism
- [[Block-Sparse Attention]] — Approximate variant
- [[FlashAttention Paper]] — Source paper
