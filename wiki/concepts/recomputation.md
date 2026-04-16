---
title: "Recomputation"
type: concept
tags: [gpu, memory, optimization, gradient-checkpointing, deep-learning]
created: 2026-04-17
sources: [flash-attention.md]
---

# Recomputation

Computing intermediate results on-the-fly instead of storing them, trading extra compute for reduced memory usage.

## Overview

**Recomputation** = Trading FLOPs for memory by recalculating intermediate values rather than storing them.

**Synonyms**: Gradient checkpointing, selective recomputation, lazy checkpointing.

## The Memory-Compute Trade-off

### Standard Forward Pass

```
Input → [Layer 1] → [Layer 2] → ... → [Layer N] → Output
              ↓           ↓                    ↓
           Store       Store                 Store
           (activations, intermediates)
```

**Memory**: O(N) for N layers

### With Recomputation

```
Input → [Layer 1] → [Checkpoint] ──┐
              ↓                      │
           Recompute                 │
              ↓                      │
           [Layer 2] ───────────────┤
              ↓                      │
           Recompute                 │
              ↓                      ▼
           [Layer 3] → ... → Output
```

**Memory**: O(√N) or O(1) for some algorithms

## Gradient Checkpointing

### Chen et al. (2016) Formulation

Divide network into segments:

```
Forward: A → B → C → D → E → F
                  ↓
              Checkpoint

Memory: Store A, B, C
FLOPs: Forward twice (A→B→C, then C→D→E→F)
```

### Trade-off Analysis

| Strategy | Memory | FLOPs |
|----------|--------|--------|
| No checkpointing | O(N) | O(N) |
| Checkpoint every layer | O(1) | O(2N) |
| Checkpoint every √N | O(√N) | O(1.5N) |

## FlashAttention Recomputation

### Standard Attention Backward

Forward pass stores:
- S = QK^T (N×N)
- P = softmax(S) (N×N)
- O = PV (N×d)

Backprop needs:
- dO (given)
- S, P (to compute dQ, dK, dV)

**Memory**: O(N²)

### FlashAttention Backward

Store:
- O (N×d) — attention output
- m (N) — row maximum
- ℓ (N) — row sum (normalization)
- Q, K, V (already stored as inputs)

**Memory**: O(Nd) — linear!

### Recomputation Steps

```python
def backward_flash_attention(dO, Q, K, V, O, m, l):
    # Recompute block by block
    for j in range(T_r):  # K, V blocks
        K_j = K[j * B_r : (j+1) * B_r]
        V_j = V[j * B_r : (j+1) * B_r]
        
        for i in range(T_c):  # Q blocks
            Q_i = Q[i * B_r : (i+1) * B_r]
            O_i = O[i * B_r : (i+1) * B_r]
            
            # Recompute on-chip
            S_ij = Q_i @ K_j.T
            P_ij = exp(S_ij - m[i]) / l[i]
            
            # Compute gradients
            dP_ij = dO_i @ V_j.T
            dQ_i += dP_ij @ K_j
            
            # Store dQ partial
            write_dQ(dQ_i)
```

## Why Recomputation Works in FlashAttention

### Insight 1: Cheap Recomputation

Computing S = QK^T is O(Nd²) — same as computing gradients.

### Insight 2: SRAM Speed

Recomputing from SRAM (fast) is faster than reading from HBM (slow).

```
Time to recompute S on-chip: ~200 cycles
Time to read S from HBM: ~300-600 cycles
```

### Insight 3: Natural Checkpoints

The tiling structure provides natural checkpoints:
- K_j, V_j loaded once
- Processed against all Q_i
- Then discarded

## Mathematical Details

### Forward Statistics

For block S_ij = Q_i @ K_j^T:

```
m_ij = rowmax(S_ij)  # Maximum per row in block
l_ij = rowsum(exp(S_ij - m_ij))  # Sum per row in block
```

### Backward Gradient Flow

```python
# dO = d(softmax(QK^T)V)/dO
# P = softmax(S)

# Gradient w.r.t. P:
dP = dO @ V^T

# Gradient w.r.t. S:
# dS = P^T @ (diag(row_sum(dO*V)) - V @ dO^T @ P)
dS = P.T @ (diag(rowsum(dO * V)) - V @ (dO * P).T @ P)

# Gradient w.r.t. Q:
dQ = dS @ K
```

### Recomputing with Running Statistics

```python
# Instead of storing full S and P,
# recompute using stored m, l

def recompute_S_row(Q_row, K, m_row, l_row):
    # m_row, l_row are from forward pass
    S_row = Q_row @ K.T  # O(d²)
    
    # Compute softmax probabilities
    P_row = exp(S_row - m_row) / l_row
    
    return S_row, P_row
```

## Selective Gradient Checkpointing

### Chen et al. Approach

```python
class CheckpointFunction(torch.autograd.Function):
    @staticmethod
    def forward(ctx, run_function, x, blocks):
        ctx.run_function = run_function
        ctx.blocks = blocks
        # Save input and run function
        output = run_function(x)
        ctx.save_for_backward(output)
        return output
    
    @staticmethod
    def backward(ctx, grad_output):
        # Recompute
        output, = ctx.saved_tensors
        temp_activations = [output]
        
        for block in reversed(ctx.blocks):
            # Recompute block
            block_input = temp_activations[-1]
            block_output = ctx.run_function(block_input)
            # ...
```

### FlashAttention Extension

```python
# Store only statistics, not full activations
class FlashAttentionCheckpoint(torch.autograd.Function):
    @staticmethod
    def forward(ctx, Q, K, V):
        O, m, l = flash_attention(Q, K, V)
        ctx.save_for_backward(Q, K, V, O, m, l)
        return O
    
    @staticmethod
    def backward(ctx, dO):
        Q, K, V, O, m, l = ctx.saved_tensors
        # Recompute attention matrix using m, l
        dQ, dK, dV = flash_attention_backward(dO, Q, K, V, O, m, l)
        return dQ, dK, dV
```

## Performance Impact

### Memory Savings

| N | Standard (N×N) | FlashAttention (Nd) | Savings |
|---|----------------|---------------------|---------|
| 512 | 262K | 32K | 8x |
| 1024 | 1M | 65K | 16x |
| 4096 | 16M | 262K | 64x |
| 16384 | 268M | 1M | 256x |

### Compute Overhead

| Component | FLOPs |
|-----------|-------|
| Forward pass | O(N²d) |
| Backward pass (no recompute) | O(N²d) |
| Backward pass (recompute) | O(N²d) + O(Nd²) |

**Net**: Despite extra compute, **faster** due to memory bandwidth savings.

## Trade-offs

### When Recomputation Wins

- Memory is the bottleneck
- Recomputation is cheap (compute-bound)
- Fast memory available (SRAM)

### When Recomputation Loses

- Recomputation is expensive
- Memory bandwidth not the bottleneck
- Slow memory (cache miss-prone)

## Extensions

### Activation Checkpointing Frameworks

- PyTorch: `torch.utils.checkpoint`
- DeepSpeed: Gradient checkpointing
- Fairscale: FullyShardedCheckpoint

### Automatic Selection

Some frameworks auto-select recomputation points:

```python
# PyTorch automatic selection
model = ResNet50()
model = torch.utils.checkpoint.checkpoint_sequential(
    model.features,  # Layers to checkpoint
    segments=4,       # Number of checkpoints
    input           # Input tensor
)
```

## Related

- [[FlashAttention]] — Recomputation for attention
- [[Gradient Checkpointing]] — General recomputation technique
- [[IO-Awareness]] — Why recomputation helps
- [[Tiling]] — Enables efficient recomputation
- [[Memory Bandwidth]] — Bottleneck recomputation addresses
