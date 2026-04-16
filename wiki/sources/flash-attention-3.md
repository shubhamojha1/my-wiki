---
title: "FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision"
type: source
tags: [attention, transformers, gpu, hoppers, h100, optimization]
created: 2026-04-17
sources: [flash-attention-3.pdf]
url: "https://arxiv.org/abs/2407.08608"
authors: [Jay Shah, Ganesh Bikshandi, Ying Zhang, Vijay Thakkar, Pradeep Ramani, Tri Dao]
institutions: [Colfax Research, Meta, NVIDIA, Georgia Tech, Princeton University, Together AI]
---

# FlashAttention-3: Fast and Accurate Attention with Asynchrony and Low-precision

## Paper Details

- **Authors**: Jay Shah, Ganesh Bikshandi (Colfax), Ying Zhang (Meta), Vijay Thakkar, Pradeep Ramani (NVIDIA), Tri Dao (Princeton/Together AI)
- **Published**: July 2024 (arXiv:2407.08608)
- **Code**: https://github.com/Dao-AILab/flash-attention

## Abstract

FlashAttention-3 builds on FlashAttention-2 with three techniques exploiting Hopper H100 GPU features:
1. **Producer-Consumer Asynchrony** via warp-specialization
2. **GEMM-Softmax Overlap** via pingpong scheduling
3. **FP8 with Block Quantization and Incoherent Processing**

**Results**:
- FP16: 740 TFLOPs/s (75% utilization) — 1.5-2x faster than FlashAttention-2
- FP8: ~1.2 PFLOPs/s
- 2.6x lower numerical error than baseline FP8

## Problem: FlashAttention-2 Underutilization

FlashAttention-2 achieves only 35% utilization on H100 vs 80-90% for optimized GEMM.

**Root causes**:
- Not using Hopper-specific instructions (TMA, WGMMA)
- Synchronous execution model
- No exploitation of asynchrony
- FP8 not supported

## Key Contributions

### 1. Producer-Consumer Asynchrony

Split warps into:
- **Producer warps**: Issue TMA loads from HBM to SMEM
- **Consumer warps**: Execute WGMMA for Tensor Core operations

Benefits:
- Overlaps data movement with computation
- Exploits asynchronous nature of TMA and WGMMA
- Uses `setmaxnreg` for register reallocation

### 2. GEMM-Softmax Overlap

**Problem**: Softmax operations (exp) have 256x lower throughput than matmul on H100.

**Solution**: Pingpong scheduling between 2 warpgroups:
- Warpgroup 1: Does softmax while Warpgroup 2 does GEMM
- Roles swap each iteration

### 3. FP8 with Block Quantization

**Layout Challenges**: FP8 WGMMA requires k-major format

**Accuracy Solutions**:
- Block quantization: per-block scaling factors
- Incoherent processing: random orthogonal matrix to spread outliers

## H100 Specifications

| Component | Value |
|-----------|-------|
| FP16 matmul | 989 TFLOPs/s |
| Special functions (exp) | 3.9 TFLOPs/s |
| FP8 matmul | ~1900 TFLOPs/s |
| GMEM bandwidth | 3.35 TB/s |
| SMEM per SM | 228 KB, 31 TB/s |
| SMs | 132 |

## Performance Results

### FP16 Results

| Configuration | vs FlashAttention-2 | vs PyTorch |
|---------------|--------------------|--------------|
| Forward (d=64) | 1.5-2.0x | up to 16x |
| Forward (d=128) | 1.5-1.8x | up to 16x |
| Backward | 1.5-1.75x | up to 16x |

**Max**: 740 TFLOPs/s (75% utilization)

### FP8 Results

- Head dim 64: Faster than cuDNN
- Head dim 128/256: Competitive with cuDNN
- ~1.2 PFLOPs/s

### Numerical Error

| Method | RMSE |
|--------|------|
| Baseline FP16 | 3.2e-4 |
| FlashAttention-2 FP16 | 1.9e-4 |
| FlashAttention-3 FP16 | 1.9e-4 |
| Baseline FP8 | 2.4e-2 |
| FlashAttention-3 FP8 | 9.1e-3 |

## Related

- [[FlashAttention-3]] — The algorithm
- [[Warp Specialization]] — Producer-consumer asynchrony
- [[GEMM-Softmax Overlap]] — Pingpong scheduling
- [[FP8 Attention]] — Low-precision techniques
