---
title: "Block-Sparse Attention"
type: concept
tags: [attention, transformers, sparsity, optimization, approximation]
created: 2026-04-17
sources: [flash-attention.md]
---

# Block-Sparse Attention

An approximate attention algorithm that extends FlashAttention by skipping computation on zero blocks, achieving linear complexity and faster runtime than all existing approximate attention methods.

## Overview

**Block-sparse attention** = FlashAttention + sparsity mask that skips computation of zero blocks.

**Result**: Linear O(N) complexity instead of O(N²), with 2-4x speedup over FlashAttention.

## Motivation

### Standard Attention: O(N²)

```
For each token i:
  Compute attention to all N tokens
```

### Problem: Long Sequences

| Sequence Length | Attention Matrix | Memory |
|-----------------|-----------------|--------|
| 512 | 512 × 512 | 1 MB |
| 2048 | 2048 × 2048 | 16 MB |
| 4096 | 4096 × 4096 | 64 MB |
| 16384 | 16384 × 16384 | 1 GB |
| 65536 | 65536 × 65536 | 16 GB |

### Block Sparsity Solution

Skip attention to most tokens:

```
Dense:     O(N²) ─────────────────────────►
Sparse:    O(N·s) ──────────► where s < 1
```

## Block Sparsity Pattern

### Definition

Split attention matrix into blocks of size B_r × B_r:

```
┌────────────────────────────────────────────┐
│  Block  │  Block  │  Block  │  Block  │
│ (dense) │ (skip) │ (dense) │ (skip)  │
├─────────┼─────────┼─────────┼─────────┤
│  Block  │ (dense) │ (skip)  │ (dense) │
├─────────┼─────────┼─────────┼─────────┤
│  Block  │  Block  │ (dense) │ (skip)  │
└────────────────────────────────────────────┘

Dense blocks:  compute attention
Skip blocks:   zero → skip computation
```

### Formal Definition

Given mask M̃ ∈ {0,1}^(N×N), block-sparse attention computes:

```
S = QK^T ⊙ M̃
P = softmax(S ⊙ M̃)
O = PV
```

Where M̃ has block structure:
- Block size: B_r × B_r
- Blocks are either all 1s (compute) or all 0s (skip)

## Sparsity Patterns

### 1. Fixed Butterfly Pattern

From "Pixelated Butterfly" paper:

```
┌┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┬┐
┤│││││││││││││││││││││││││││││││││││││││
├┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┤
│││││││││││││││││││││││││││││││││││││││││
├┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┤
││││││││││││││││││││││││││││││││││││││││││
└┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┴┘
```

**Pattern**: Logarithmic sparsity — O(N log N) non-zeros

### 2. Learned Sparsity

Learn which blocks to keep during training:

```python
# Learnable mask
mask_logits = learnable_weight @ block_features
mask = sigmoid(mask_logits) > threshold
```

### 3. Local + Global

Combine local attention with sparse global attention:

```
┌────────────────────────────┐
│ G G G G G G G G G G G G G │  Global tokens
├────────────────────────────┤
│ G L L L L L L L L L L L G │
├────────────────────────────┤
│ G L L L L L L L L L L L G │
├────────────────────────────┤
│ G L L L L L L L L L L L G │
└────────────────────────────┘
G = Global attention
L = Local attention
```

## Algorithm: Block-Sparse FlashAttention

### Modification of FlashAttention

```python
def block_sparse_flash_attention(Q, K, V, block_mask):
    O = zeros(N, d)
    m = -inf(N)
    l = zeros(N)
    
    for j in range(T_r):
        K_j, V_j = load_blocks(j)
        
        for i in range(T_c):
            # Skip if entire block is zero
            if block_mask[i, j] == 0:
                continue
                
            Q_i, O_i, m_i, l_i = load_blocks(i)
            
            S_ij = Q_i @ K_j.T
            P_ij = exp(S_ij - m_i) / l_i
            O_i, m_i, l_i = update(O_i, m_i, l_i, P_ij, V_j)
            
            write_blocks(i, O_i, m_i, l_i)
    
    return O
```

### Key Difference

**FlashAttention**: Process all blocks
**Block-sparse**: Skip zero blocks (O(N²) → O(N²s))

## IO Complexity

### Comparison

| Algorithm | IO Complexity |
|-----------|---------------|
| Standard Attention | O(Nd + N²) |
| FlashAttention | O(N²d²/M) |
| Block-Sparse FlashAttention | O(N²d²s/M) |

Where s = fraction of non-zero blocks (sparsity ratio)

### Analysis

- **s = 1**: Dense attention → same as FlashAttention
- **s < 1**: Sparse attention → faster by factor of s
- **s = O(1/N)**: Linear complexity!

## Sparsity Patterns for Transformers

### Sparse Transformers (Child et al., 2019)

Factorized attention with:
- Local attention (adjacent tokens)
- Strided attention (every k-th token)

### Longformer (Beltagy et al., 2020)

- Local + global + sliding window
- O(N) complexity

### BigBird (Zaheer et al., 2020)

- Random + local + global attention
- O(N) with theoretical guarantees

## Block-Sparse FlashAttention Results

### Benchmark: Long-Range Arena

| Model | ListOps | Text | Retrieval | Image | Pathfinder | Avg |
|-------|---------|------|-----------|-------|-----------|-----|
| Standard | 36.0 | 63.6 | 81.6 | 42.3 | 72.7 | 59.3 |
| FlashAttention | 37.6 | 63.9 | 81.4 | 43.5 | 72.7 | 59.8 |
| Block-Sparse | 37.0 | 63.0 | 81.3 | 43.6 | 73.3 | 59.6 |
| Linformer | 35.6 | 55.9 | 77.7 | 37.8 | 67.6 | 54.9 |
| Performer | 36.8 | 63.6 | 82.2 | 42.1 | 69.9 | 58.9 |

### Speedup

| Sparsity | Speedup vs FlashAttention |
|----------|---------------------------|
| 50% | ~2x |
| 75% | ~3x |
| 90% | ~4x |

## Path-X and Path-256

### Challenge

- Path-X: 128×128 images = 16K tokens
- Path-256: 256×256 images = 64K tokens
- Previous models: Out of memory or random performance

### Block-Sparse Solution

- Scale to 64K sequence length
- Achieves 63.1% on Path-256 (first non-random)

## Trade-offs

### Accuracy vs Speed

```
Higher sparsity ─────► Faster, lower accuracy
Lower sparsity ──────► Slower, higher accuracy
```

### Pattern Design

Good patterns:
- Preserve important connections
- Maintain global context
- Match model architecture

## Implementation

### Using FlashAttention

```python
from flash_attn import flash_attn_func

# Standard FlashAttention
O = flash_attn_func(Q, K, V)

# Block-sparse requires custom implementation
# or use extended version
from flash_attn.flash_attn_interface import flash_attn_func

# With block sparse mask
O = flash_attn_func(
    Q, K, V,
    blockSparseMode='variable',  # or 'fixed'
    blockSparseThreshold=0.5    # sparsity level
)
```

## Related Methods

### Approximate Attention

| Method | Complexity | Approximation |
|--------|------------|---------------|
| Linformer | O(N) | Low-rank |
| Performer | O(N) | Random features |
| Reformer | O(N log N) | Locality-sensitive hashing |
| **Block-Sparse** | O(Ns) | **Structured sparsity** |

### Why Block-Sparse is Different

- **Exact**: Same output as dense (for non-zero blocks)
- **Fast**: Skip computation entirely
- **Compatible**: Works with any sparsity pattern

## Future Directions

### Learned Patterns

Learn optimal sparsity patterns during training:

```python
# Differentiable sparsity
mask = gumbel_softmax(logits)
O = block_sparse_attention(Q, K, V, mask)
```

### Dynamic Sparsity

Adapt sparsity based on input:

```python
# Content-dependent sparsity
sparse_mask = content_router(Q)  # Learn which blocks matter
```

## Related

- [[FlashAttention]] — Base algorithm
- [[IO-Awareness]] — Why it's fast
- [[Attention]] — Base mechanism
- [[Sparse Network Training]] — Related sparsity concept
- [[FlashAttention Paper]] — Source paper
