---
title: "Tensor Cores"
type: concept
tags: [gpu, deep-learning, nvidia, matrix-multiplication, hardware]
created: 2026-04-16
sources: [gpu-deep-learning-guide.md]
---

# Tensor Cores

Specialized hardware units in NVIDIA GPUs that perform matrix multiplication (MMA — Matrix Multiply-Accumulate) with extreme efficiency. They are the single most important GPU feature for deep learning.

## Overview

Tensor Cores perform a 4×4 matrix multiplication in **1 cycle**, compared to 4 cycles for a fused multiply-add (FFMA) operation. This 4x efficiency gain makes them transformative for neural network training and inference.

## How Tensor Cores Work

### Memory Hierarchy and Latency

Understanding Tensor Cores requires understanding GPU memory latency:

| Operation | Latency (cycles) |
|-----------|-----------------|
| Global memory access (~80GB) | ~380 |
| L2 cache access | ~200 |
| L1 cache / Shared memory (~128KB/SM) | ~34 |
| FFMA (fused multiply-add) | 4 |
| **Tensor Core operation** | **1** |

### Matrix Multiplication Without Tensor Cores

For a 32×32 matrix multiply using 8 SMs with 8 warps each:

```
Cost = 200 (global→shared) + 8×34 (shared memory) + 8×4 (FFMA)
     = 504 cycles
```

### Matrix Multiplication With Tensor Cores

```
Cost = 200 (global→shared) + 34 (shared→Tensor Core) + 1 (Tensor Core)
     = 235 cycles
```

**Result**: ~2x speedup from Tensor Cores alone

### Modern Optimizations: Asynchronous Copies & TMA

**RTX 30 (Ampere) and RTX 40 (Ada)** support asynchronous copies between global and shared memory.

**H100 (Hopper)** adds the **Tensor Memory Accelerator (TMA)**:
- Computes read/write indices in hardware
- Frees threads to focus on computation
- Overlaps memory transfer with computation
- Reduces average memory access to ~165 cycles instead of 200

```
With TMA: 165 (async copy) + 34 (shared) + 1 (Tensor Core) = 200 cycles
```

## Why Memory Bandwidth Matters More Than FLOPS

During GPT-3-sized training:
- Tensor Core utilization: **45-65%**
- Tensor Cores idle ~50% of the time waiting for memory

This means:
- Two GPUs with same Tensor Core count → the one with higher memory bandwidth is faster
- Memory bandwidth is the best predictor of large-model performance

## Tensor Core Generations

| GPU Series | Architecture | Tensor Core Version |
|------------|-------------|-------------------|
| V100 | Volta | 1st gen |
| RTX 20 | Turing | 2nd gen |
| RTX 30, A100 | Ampere | 3rd gen |
| RTX 40 | Ada Lovelace | 4th gen |
| H100 | Hopper | 4th gen+ |

## Precision Support

Tensor Cores have evolved to support more data types:

| Precision | Volta | Turing | Ampere | Ada/Hopper |
|-----------|-------|--------|--------|------------|
| FP32 | ✓ | ✓ | ✓ | ✓ |
| FP16 | ✓ | ✓ | ✓ | ✓ |
| BF16 | - | - | ✓ | ✓ |
| TF32 | - | - | ✓ | ✓ |
| INT8 | ✓ | ✓ | ✓ | ✓ |
| INT4 | - | - | - | ✓ |
| **FP8** | - | - | - | ✓ |

## Sparse Matrix Multiplication (Ampere+)

Since Ampere, Tensor Cores support **structured sparsity**:
- Weight matrices sliced into 4-element pieces
- 2 of 4 elements must be zero
- Auto-compressed to half size before computation
- **2x effective throughput** with no accuracy loss

## Recommendation

**Do not buy any GPU without Tensor Cores.** The performance difference is too large to justify the cost savings.

## Related

- [[GPU Deep Learning Guide]] — Tim Dettmers' comprehensive GPU analysis
- [[H100]] — GPU with most advanced Tensor Cores
- [[Memory Bandwidth]] — Why it matters more than raw FLOPS
- [[Sparse Network Training]] — Uses sparse Tensor Core feature
- [[BF16]], [[TF32]], [[FP8]] — Precision formats for Tensor Cores
