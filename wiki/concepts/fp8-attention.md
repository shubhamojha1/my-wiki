---
title: "FP8 Attention"
type: concept
tags: [gpu, fp8, quantization, attention, low-precision]
created: 2026-04-17
sources: [flash-attention-3.md]
---

# FP8 Attention

Low-precision attention using 8-bit floating point (FP8) format on Hopper GPUs, achieving 2x throughput with hardware-accelerated Tensor Cores while maintaining accuracy through block quantization and incoherent processing.

## Overview

**FP8** = 8-bit floating point format with 4-bit exponent and 3-bit mantissa.

**Benefits**:
- 2x throughput vs FP16/BF16
- 2x more data fits in cache
- Hardware-accelerated on H100

**Challenges**:
- Higher numerical error
- Outlier features in LLMs
- Layout constraints

## FP8 Format

### FP8 Variants

| Format | Exponent | Mantissa | Range | Use Case |
|--------|----------|----------|-------|----------|
| E4M3 | 4 | 3 | ±448 | Forward (activations, weights) |
| E5M2 | 5 | 2 | ±57344 | Gradients (wider range) |

### Compared to FP16/BF16

| Format | Bits | Exponent | Mantissa | Range |
|--------|------|----------|----------|-------|
| FP16 | 16 | 5 | 10 | ±65504 |
| BF16 | 16 | 8 | 7 | ±3.4×10^38 |
| FP8 E4M3 | 8 | 4 | 3 | ±448 |

### Precision Loss

```
FP16: 10 bits mantissa ≈ 3 decimal digits
FP8:  3 bits mantissa ≈ 1 decimal digit
```

**Result**: Higher quantization error, especially for outliers.

## H100 FP8 Specifications

### Throughput

| Precision | TFLOPs/s | Relative |
|-----------|-----------|----------|
| FP16 | 989 | 1x |
| BF16 | 989 | 1x |
| FP8 | ~1900 | 2x |

### Memory

| Precision | Bytes/Element | Data in Cache |
|-----------|---------------|---------------|
| FP16 | 2 | 1x |
| FP8 | 1 | 2x |

## FP8 Layout Constraints

### WGMMA Requirements

FP8 WGMMA has stricter layout requirements than FP16:

| Operand | FP16 WGMMA | FP8 WGMMA |
|---------|-------------|------------|
| A (mn-major) | ✓ | ✗ |
| A (k-major) | ✓ | ✓ |
| B | k-major | k-major |
| Accumulator | Standard | Special layout |

**Key constraint**: FP8 requires **k-major format** for operands.

### Layout Transformation

```python
# Problem: Q, K, V are typically mn-major (contiguous in head dim)
Q: [seq_len, head_dim]  # mn-major

# For FP8 WGMMA, need k-major:
# For V: contiguous in sequence dimension, not head dimension
V: [head_dim, seq_len]  # k-major
```

### Solutions

1. **Pre-transpose**: Transpose V in memory (expensive)
2. **In-kernel transpose**: Transpose after loading to SMEM (FlashAttention-3 choice)

### In-Kernel Transpose

```cuda
// Producer warp: Load V tile
V_tile = tma_load(V, indices);  // mn-major in SMEM

// Producer warp: In-kernel transpose using LDSM/STSM
V_transposed = ldsm_transpose(V_tile);  // k-major

// Consumer warp: Use transposed V for WGMMA
O = wgmma_fp8(P, V_transposed);
```

### LDSM/STSM Instructions

```cuda
// LDSM: Load matrix from SMEM to registers
// 8x8 matrix with 16-bit entries
ldmatrix.sync.aligned.m8n8.shared.b16 {%Ra}, [%Rs];

// For FP8: pack 2 entries at a time
ldmatrix.sync.aligned.m8n8.trans.shared.b8 {%Ra}, [%Rs];
```

### Accumulator Layout Transformation

FP8 WGMMA has layout constraints on accumulator:
- First WGMMA accumulator: row-major layout
- Second WGMMA operand: different layout

**Solution**: Register permutation using byte permute instructions.

```python
# Accumulator layout: {d0, d1, d4, d5, d2, d3, d6, d7}
# Permute to match operand layout
P_permuted = permute(P_accumulator, {0, 1, 4, 5, 2, 3, 6, 7})

# V tile already transposed to match
O = wgmma_fp8(P_permuted, V_transposed);
```

## Accuracy Challenges

### The Outlier Problem

LLMs have **outlier features** — values much larger than typical:

```python
# Simulated distribution
x = Normal(0, 1) + Bernoulli(0.001) * Normal(0, 10)

# 99.9% of values: mean=0, std=1
# 0.1% of values: mean=0, std=10
```

### Impact on Quantization

```python
# Per-tensor quantization
scale = max(abs(Q))  # Dominated by outliers!
Q_int8 = round(Q / scale)

# Most values get poor precision
# Scale >> typical values
```

## Solution 1: Block Quantization

### Concept

Quantize per block instead of per tensor:

```python
# Per-tensor (bad)
scale = max(abs(Q))  # One scale for all

# Per-block (good)
block_size = 64 * 64  # e.g., 64 tokens × 64 dim
for i in range(0, N, block_size):
    block = Q[i:i+block_size]
    scale = max(abs(block))  # Local scale
    Q_int8[i:i+block_size] = round(block / scale)
```

### Benefits

1. **Better precision**: Scale matches typical values
2. **Natural fit**: FlashAttention already operates on blocks
3. **No overhead**: Can fuse with preceding operations

### Integration with Attention

```python
# Scale S during attention
for each block (Q_i, K_j):
    # Get scales
    scale_Q = scales_Q[block_i]
    scale_K = scales_K[block_j]
    
    # Compute attention with scaling
    S_ij = (Q_i / scale_Q) @ (K_j / scale_K).T
    
    # Scale back
    S_ij = S_ij * scale_Q * scale_K
```

## Solution 2: Incoherent Processing

### Concept

Multiply Q and K by a random orthogonal matrix M before quantizing:

```python
# Random orthogonal matrix
M = random_hadamard() * random_sign()  # O(N log N) multiply

# Transform before quantization
Q_tilde = Q @ M
K_tilde = K @ M

# Quantize transformed values
Q_int8 = quantize(Q_tilde)
K_int8 = quantize(K_tilde)
```

### Why It Works

```python
# Mathematically equivalent
attention = softmax(Q @ K.T) @ V

# With M (orthogonal: M @ M^T = I)
attention = softmax((Q @ M) @ (K @ M).T) @ V
# = softmax(Q @ M @ M.T @ K.T) @ V
# = softmax(Q @ K.T) @ V  # Same result!
```

### Effect on Outliers

```
Before: Q has outlier columns → poor quantization
After: QM spreads outliers across all columns
       → Each column has ~similar magnitude
       → Better quantization
```

### Hadamard Transform

```python
# Fast Walsh-Hadamard Transform
def hadamard(x):
    N = len(x)
    while N > 1:
        N //= 2
        for i in range(0, N):
            for j in range(0, N):
                u = x[i + j]
                v = x[i + j + N]
                x[i + j] = u + v
                x[i + j + N] = u - v
    return x
```

**Complexity**: O(N log N) vs O(N²) for full orthogonal matrix.

### Fusing with Rotary Embeddings

```python
# In practice: fuse with RoPE
# M @ RoPE can be computed together
Q = (Q @ M) @ RoPE()
```

## Combined Results

### Numerical Error Comparison

| Method | RMSE | Improvement |
|--------|-------|-------------|
| Baseline FP16 | 3.2×10⁻⁴ | 1x |
| FlashAttention-2 FP16 | 1.9×10⁻⁴ | 1.7x |
| FlashAttention-3 FP16 | 1.9×10⁻⁴ | 1.7x |
| Baseline FP8 | 2.4×10⁻² | baseline |
| FA-3 FP8 (block quant) | 9.3×10⁻³ | 2.6x |
| FA-3 FP8 (full) | 9.1×10⁻³ | 2.6x |

### Why Better Than Baseline FP8

Baseline FP8 uses:
- Per-tensor quantization
- No incoherent processing
- FP16 accumulator for softmax

FlashAttention-3 FP8 uses:
- Block quantization
- Incoherent processing
- FP32 accumulator for softmax

## Performance Considerations

### Block Size Selection

```python
# Block quantization granularity
block_quant = {
    'Q': (seq_block, head_dim),  # e.g., (64, 64)
    'K': (seq_block, head_dim),
    'V': (head_dim, seq_block),
}
```

### Memory vs Accuracy Trade-off

```
Smaller blocks → Better accuracy, more scales
Larger blocks → Worse accuracy, fewer scales
```

### Fusing with Other Operations

```python
# Can fuse with rotary embedding
# Rotary is memory-bound, so no extra cost
Q = rotary(Q @ M)  # Combined operation
```

## FP8 vs FP16 Performance

### H100 Throughput

| Precision | Forward TFLOPs/s | Backward TFLOPs/s |
|------------|------------------|-------------------|
| FP16 | 740 | ~500 |
| FP8 | ~1200 | N/A |

### When to Use FP8

| Scenario | Recommendation |
|----------|----------------|
| Inference (throughput) | FP8 ✓ |
| Training | FP16 (better accuracy) |
| Long sequences | FP8 ✓ (more cache) |
| Small models | FP16 (less need) |

## Implementation in FlashAttention-3

### Kernel Structure

```python
def flash_attention_3_fp8(Q, K, V):
    # 1. Producer: Load and quantize
    Q_blocks = load_and_quantize(Q)  # Block quantization
    K_blocks = load_and_quantize(K)
    
    # 2. In-kernel transpose V
    V_transposed = transpose_in_smem(V)
    
    # 3. Consumer: FP8 WGMMA attention
    for i, j in attention_blocks():
        # FP8 matmul
        S = wgmma_fp8(Q_i, K_j.T)  # k-major K
        
        # Dequantize for softmax (FP32)
        S_fp32 = dequantize(S)
        
        # FP32 softmax
        P = softmax(S_fp32)
        
        # Quantize for next matmul
        P_fp8 = quantize(P)
        
        # FP8 matmul
        O = wgmma_fp8(P_fp8, V_transposed)
```

## Related

- [[FlashAttention-3]] — Uses FP8 attention
- [[FP8]] — FP8 format details
- [[Block Quantization]] — Per-block scaling
- [[Incoherent Processing]] — Orthogonal transform
- [[WGMMA]] — FP8 hardware support
