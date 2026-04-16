---
title: "L2 Cache"
type: concept
tags: [gpu, hardware, memory, performance]
created: 2026-04-16
sources: [gpu-deep-learning-guide.md]
---

# L2 Cache (GPU)

On-chip cache memory shared across all Streaming Multiprocessors. Critical for reducing global memory access latency and enabling fast matrix multiplication.

## Overview

L2 cache sits between the massive but slow global memory (HBM) and the fast but tiny per-SM caches. It stores frequently accessed data closer to the compute units.

**Key property**: Larger L2 cache = more data reuse = less global memory traffic

## GPU L2 Cache Sizes by Architecture

| Architecture | GPUs | L2 Cache Size |
|--------------|------|---------------|
| Volta | V100, Titan V | 6 MB |
| Turing | RTX 20 series | 5.5 MB |
| Ampere | RTX 30, A100 | 6 MB |
| Ada | RTX 40 series | **72 MB** |
| Hopper | H100 | Largest (proprietary) |

**Ada has 12x more L2 cache than Ampere.**

## How L2 Cache Works

### Memory Hierarchy

```
Global Memory (HBM) ← 380 cycles → L2 Cache ← 200 cycles → L1/Shared ← 34 cycles → Registers
```

### Tile-Based Processing

For matrix multiplication:
1. Load tile from global memory to L2
2. Process tile from L2 (faster than global)
3. L2 automatically caches frequently used tiles

### Cache Behavior

**Cache hit**: Data already in L2 → Fast access (~200 cycles)
**Cache miss**: Need to fetch from global → Slow access (~380 cycles)

Larger L2 = Higher hit rate = Faster average access

## Why L2 Cache Matters for Deep Learning

### Tensor Core Latency Breakdown

Without cache optimization:
```
Global memory: 200 cycles
L1/Shared: 34 cycles
Tensor Core: 1 cycle
Total: 235 cycles
```

With perfect cache (Ada's advantage):
- Entire model fits in L2
- Reduces effective global memory access
- **Result: 1.5-2x speedup for certain models**

### Which Models Benefit Most?

| Model Type | L2 Cache Benefit |
|------------|------------------|
| BERT-Large | **High** (fits in L2) |
| GPT-2 Medium | Medium |
| GPT-3 class | Low (too large) |
| CNNs | Varies by size |

**Ada's 72MB L2**: BERT-Large training fits entirely in cache during matrix multiplication.

## L1 Cache and Shared Memory

While logically similar, L1 and L2 have different characteristics:

| Aspect | L1 Cache | L2 Cache |
|--------|----------|----------|
| Size | 128 KB per SM | 6-72 MB total |
| Location | Per SM | Shared across SMs |
| Latency | ~34 cycles | ~200 cycles |
| Programmable | Shared memory is | No (hardware) |

### Shared Memory

Shared memory is explicitly managed L1:
```cuda
__shared__ float tile[16][16];
```

- Programmers control data placement
- Enables data reuse within block
- Critical for high-performance kernels

## L2 Cache and Performance

### Memory Access Pattern Optimization

For maximum L2 utilization:
1. **Spatial locality**: Adjacent threads access adjacent memory
2. **Temporal locality**: Same data used multiple times
3. **Coalesced access**: Warp reads consecutive memory addresses

### Warp Memory Coalescing

When threads in a warp access consecutive memory:
```
Thread 0: reads addr 0-3
Thread 1: reads addr 4-7
...
Thread 31: reads addr 124-127
```

This triggers **one** L2 cache line fetch instead of 32 individual fetches.

## Cache Eviction and Thrashing

### The Problem

With small L2 (6MB), for large models:
1. Multiple tiles compete for cache space
2. Frequently used tiles get evicted
3. Cache hit rate drops
4. Performance suffers

### Ada's Advantage

72MB L2 can hold:
- Multiple weight matrix tiles
- Input activation tiles
- Gradient accumulation buffers

**Result**: Higher hit rate, more stable performance.

## Practical Optimization Tips

### 1. Choose Right GPU for Your Model

| Model Size | Recommended GPU |
|------------|-----------------|
| < 1B params | RTX 3090/4090 fine |
| 1-10B params | RTX 4090 better |
| 10B+ params | Need 80GB VRAM (A100/H100) |
| BERT-Large | RTX 4090 best value |

### 2. Optimize Memory Access

```python
# Bad: Non-coalesced access
for i in range(N):
    for j in range(M):
        result[i][j] = A[j][i]  # Column-major access

# Good: Coalesced access
for j in range(M):
    for i in range(N):
        result[i][j] = A[i][j]  # Row-major access
```

### 3. Use Mixed Precision

Smaller data types = more data in cache:
- FP32: 4 bytes/element
- FP16/BF16: 2 bytes/element
- FP8: 1 byte/element

**More cache = more data reuse = faster**

## L2 Cache and Multi-GPU

###nvLink Considerations

For multi-GPU training:
- L2 cache is per-GPU
- NVLink enables GPU-to-GPU communication
- L2 doesn't help with cross-GPU access

### Inference Serving

For inference with large batch sizes:
- L2 helps with weight reuse across requests
- Larger batch = more reuse opportunity
- Ada's large L2 is ideal for serving

## Related

- [[Memory Bandwidth]] — Related performance metric
- [[Tensor Cores]] — What L2 cache feeds
- [[RTX 4090]] — GPU with largest consumer L2
- [[GPU Deep Learning Guide]] — Source analysis
