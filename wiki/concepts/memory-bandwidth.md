---
title: "Memory Bandwidth"
type: concept
tags: [gpu, hardware, performance, memory]
created: 2026-04-16
sources: [gpu-deep-learning-guide.md]
---

# Memory Bandwidth

The rate at which data can be read from or written to GPU memory. Critical for deep learning because Tensor Cores spend ~50% of their time waiting for data.

## Overview

Memory bandwidth determines how fast data reaches the compute units (Tensor Cores). For large neural networks, it's often more important than raw compute (FLOPS).

**Key insight**: Tensor Cores can perform matrix multiplication in 1 cycle, but loading data from global memory takes ~380 cycles. The bottleneck is almost always memory, not compute.

## GPU Memory Bandwidth Comparison

| GPU | Architecture | Memory Bandwidth |
|-----|--------------|------------------|
| H100 SXM | Hopper | 3.35 TB/s |
| H100 PCIe | Hopper | 2.0 TB/s |
| A100 SXM | Ampere | 2.0 TB/s |
| A100 PCIe | Ampere | 1.9 TB/s |
| RTX 4090 | Ada | ~1.0 TB/s |
| RTX 3090 | Ampere | 936 GB/s |
| V100 SXM | Volta | 900 GB/s |

## Why Memory Bandwidth Matters

### The Tensor Core Utilization Problem

During GPT-3-sized training:
- Tensor Core utilization: **45-65%**
- This means Tensor Cores are **idle ~50% of the time**

**Why?** Matrix dimensions are large enough to fully utilize Tensor Cores, but memory can't feed them fast enough.

### Practical Implication

Two GPUs with the same Tensor Core count:

| GPU | Memory Bandwidth | Relative Performance |
|-----|------------------|---------------------|
| A100 | 2.0 TB/s | 1.0x (baseline) |
| V100 | 0.9 TB/s | ~0.5x |

The memory bandwidth ratio (2.0/0.9 = 2.22x) roughly predicts performance ratio.

## The Memory Hierarchy

GPU memory is organized in a hierarchy, from slow but large to fast but small:

| Level | Size | Latency | Speed vs Global |
|-------|------|---------|-----------------|
| Global Memory (HBM) | 24-80 GB | ~380 cycles | 1x (baseline) |
| L2 Cache | 6-72 MB | ~200 cycles | 1.5-2x |
| L1 Cache / Shared Memory | 128 KB/SM | ~34 cycles | 7-10x |
| Registers | ~256 KB/SM | ~1 cycle | ~200x |

### Speed Comparison for Matrix Multiplication

For a 32×32 matrix multiply:
- **Global memory only**: 504 cycles
- **With caches**: 235 cycles
- **With Tensor Cores + caches**: ~200 cycles

## What Increases Memory Bandwidth?

### 1. Faster Memory Technology
- HBM (High Bandwidth Memory): Used in data center GPUs (A100, H100)
- GDDR6X: Used in consumer GPUs (RTX 3090, 4090)
- HBM3: Newer, faster than HBM2e (H100)

### 2. Wider Bus
- More pins connecting GPU to memory
- H100: 5120-bit bus
- Consumer GPUs: 384-bit typical

### 3. Higher Clock Frequency
- More memory transactions per second
- Trade-off: More heat, more power

## How to Maximize Memory Bandwidth Utilization

### 1. Use Larger Batch Sizes
- Keep Tensor Cores busy
- Hide memory latency
- Diminishing returns after certain size

### 2. Optimize Data Layout
- Coalesced memory accesses
- Pitched memory for 2D arrays
- Avoid strided access patterns

### 3. Use Tensor Cores Effectively
- Match matrix dimensions to Tensor Core tiles
- Use appropriate data types (TF32, BF16)
- Enable structured sparsity when applicable

### 4. Leverage Cache
- L2 cache is crucial (especially Ada's 72MB)
- Reuse data multiple times
- Larger models benefit less from cache

## Memory Bandwidth vs FLOPs

For deep learning, which matters more?

| Scenario | Primary Bottleneck |
|----------|-------------------|
| Large models, large batch | Memory bandwidth |
| Small models, small batch | Compute (FLOPS) |
| Transformers, GPT-3 class | Memory bandwidth |
| CNNs, small models | Compute |
| Inference (small batch) | Compute |
| Training (large batch) | Memory bandwidth |

**Rule of thumb**: If your model is large enough that it doesn't fit in L2 cache easily, you need more memory bandwidth.

## Quantifying Impact

### Transformer Performance Formula

For transformers, approximate performance is bounded by:

```
Performance ≈ min(TensorCoreThroughput, MemoryBandwidth / bytes_per_element)
```

Where bytes_per_element depends on precision:
- FP32: 4 bytes
- FP16/BF16: 2 bytes
- FP8: 1 byte

### Example: RTX 4090 vs RTX 3090

| GPU | Memory BW | Theoretical Bound |
|-----|-----------|------------------|
| RTX 4090 | 1.0 TB/s | 500 TFLOPS (FP16) |
| RTX 3090 | 0.94 TB/s | 470 TFLOPS (FP16) |
| Actual difference | 7% | Matches ~10-15% |

The 7% memory bandwidth difference explains much of the performance gap.

## Related

- [[Tensor Cores]] — What memory bandwidth feeds
- [[L2 Cache]] — On-chip memory that helps hide latency
- [[H100]], [[A100]], [[RTX 4090]] — GPUs with different bandwidth
- [[GPU Deep Learning Guide]] — Source analysis
