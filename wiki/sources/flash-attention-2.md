---
title: "FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning"
type: source
tags: [attention, transformers, gpu, optimization, parallelism]
created: 2026-04-17
sources: [flash-attention-2.pdf]
url: "https://arxiv.org/abs/2307.08691"
authors: [Tri Dao]
institutions: [Princeton University, Stanford University]
---

# FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning

## Paper Details

- **Author**: Tri Dao
- **Institution**: Princeton University, Stanford University
- **Published**: July 2023 (arXiv:2307.08691)
- **Code**: https://github.com/Dao-AILab/flash-attention

## Abstract

FlashAttention-2 improves upon FlashAttention with better work partitioning, achieving:
- 2x speedup over FlashAttention
- 50-73% of theoretical maximum FLOPs/s (vs 25-40% for FlashAttention)
- Up to 225 TFLOPs/s per A100 GPU (72% model FLOPs utilization)
- Up to 10x speedup vs PyTorch standard attention

## Problem: FlashAttention Underutilization

FlashAttention reaches only 25-40% of theoretical max throughput:
- Forward pass: 30-50% utilization
- Backward pass: 25-35% utilization

**Cause**: Suboptimal work partitioning between thread blocks and warps.

## Key Improvements

### 1. Reduced Non-Matmul FLOPs

- Store unscaled output O~ instead of repeatedly rescaling
- Store logsumexp ℓ instead of max + sum
- Reduces expensive non-matmul operations

### 2. Parallelization Along Sequence Length

- **Forward**: Parallelize over row blocks (each thread block = one row block)
- **Backward**: Parallelize over column blocks (atomic adds for dQ)
- Critical for long sequences with small batch

### 3. Split-Q Work Partitioning

- **FlashAttention**: Split K,V across warps (split-K) → needs synchronization
- **FlashAttention-2**: Split Q across warps → no warp communication needed

## Hardware Context

### A100 Specifications

| Metric | Value |
|--------|-------|
| Theoretical FP16 matmul | 312 TFLOPs/s |
| Non-matmul FP32 | 19.5 TFLOPs/s |
| Ratio | 16x |

**Key insight**: Non-matmul FLOPs are 16x more expensive than matmul FLOPs.

## Performance Results

### Attention Speed (A100 80GB)

| Configuration | FlashAttention | FlashAttention-2 | Speedup |
|---------------|---------------|------------------|---------|
| Forward (no mask, d=64) | ~40 TFLOPs/s | ~73% max | 1.8x |
| Backward (no mask, d=64) | ~40 TFLOPs/s | ~63% max | 1.6x |
| vs PyTorch | - | Up to 10x | - |

### End-to-End Training (GPT-style)

| Model | Baseline | FlashAttention | FlashAttention-2 |
|-------|----------|----------------|-------------------|
| 1.3B, 2k seq | 1.0x | ~2.8x | ~3.5x |
| 2.7B, 8k seq | 1.0x | ~2.8x | ~3.5x |

**Max**: 225 TFLOPs/s per A100 (72% utilization)

## Causal Mask Optimization

For auto-regressive models:
1. Skip blocks where all entries are masked (~half for long sequences)
2. Only apply mask to 1 block per row (not all blocks)

**Result**: 1.7-1.8x speedup with causal masking

## Related

- [[FlashAttention-2]] — The improved algorithm
- [[FlashAttention]] — Original algorithm
- [[Split-Q]] — Warp partitioning scheme
- [[Parallelism]] — Sequence-length parallelization
