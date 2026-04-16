---
title: "Computational Intensity"
type: concept
tags: [gpu, performance, optimization, algorithms]
created: 2026-04-16
sources: [cs179_2026_lec04.pdf]
---

# Computational Intensity

The ratio of compute operations (FLOPs) to memory I/O (bytes). A key metric for determining whether an algorithm is compute-bound or memory-bound.

## Overview

**Computational Intensity (I)** = **Operations / Memory Access**

```
I = FLOPs / Bytes transferred
```

If I > 1, the same data is used in multiple computations (data reuse).

**Key insight**: To achieve high performance, you need sufficient intensity to keep compute units busy while waiting for memory.

## Why Intensity Matters

### The Memory Wall

GPUs can compute much faster than they can fetch data:

| Operation | Latency | Rate |
|-----------|---------|------|
| Global memory access | ~300-600ns | ~1 TFLOPS effective |
| FP16 Tensor Core | ~1ns | ~1000 TFLOPS |

**Gap**: Memory is ~1000x slower than compute!

### Making Up the Gap

For GPU to sustain 1000 GFLOPS with 1000 GFLOPS memory bandwidth:

```
Required Intensity = Peak Compute / Memory Bandwidth
                  = 1000 GFLOPS / 1000 GB/s
                  = 1 FLOP/byte
```

For H100 (FP16, 3958 TFLOPS, 3.35 TB/s):
```
Required Intensity = 3958 TFLOPS / 3.35 TB/s
                   = 1183 FLOPs/byte
```

## Compute-Bound vs Memory-Bound

### Memory-Bound Algorithms

- Intensity < required threshold
- GPU waits for memory, compute sits idle
- Example: Element-wise operations

```
y[i] = a[i] + b[i];  // 1 FLOP, 3 loads, 1 store = 1/8 intensity
```

### Compute-Bound Algorithms

- Intensity > required threshold
- Memory keeps up with compute
- GPU fully utilized
- Example: Large matrix multiplication

```
C[i][j] += A[i][k] * B[k][j];  // 2 FLOPs, 3 loads = 2/12 = 0.17
// But with tiling: reuse A[i][k] for all j → high intensity
```

## Intensity Examples

### Matrix Multiplication (C = A × B)

**Naive analysis**:
- FLOPs: 2 × n³ (multiply + add per element)
- Memory: 3 × n² (load A, B, store C)
- Intensity: (2n³) / (3n²) = (2/3)n

For n=1024:
```
Intensity = (2/3) × 1024 ≈ 683 FLOPs/byte
```

**This is why matrix multiply is compute-bound on GPUs!**

### N-Body Simulation

**Analysis**:
- FLOPs: n² (pairwise interactions)
- Memory: 3n (positions of n bodies)
- Intensity: n² / 3n = n/3

For n=1024:
```
Intensity = 1024 / 3 ≈ 341 FLOPs/byte
```

**Still compute-bound!**

### Vector Addition

**Analysis**:
- FLOPs: n
- Memory: 3n (load a, load b, store c)
- Intensity: n / 3n = 1/3

**Memory-bound!**

### Convolution

**Analysis**:
- FLOPs: n × k² (n output pixels, k×k filter)
- Memory: n + k²
- Intensity: (n × k²) / (n + k²)

For large n and small k:
```
Intensity ≈ k²
```

A 3×3 convolution has intensity ≈ 9.

## Roofline Model

A visual model showing performance bounds.

```
                    Performance
                    (GFLOPS)
                        │
                        │     ╱╲
                        │    ╱  ╲ Compute-bound
                        │   ╱    ╲ region
                        │  ╱      ╲
                        │ ╱        ╲───── Peak Performance
                        │╱          ╲
                        │            ╲
                        │             ╲ Memory-bound
                        │              ╲  region
                        │               ╲
                        │                ╲
                        └────────────────────────
                              Intensity (FLOPs/byte)
```

### Using Roofline

1. Calculate algorithm's operational intensity
2. Find intersection with diagonal (memory bandwidth)
3. That point = achievable performance
4. If above diagonal: compute-bound
5. If below diagonal: memory-bound

## Maximizing Intensity

### 1. Increase Data Reuse

**Bad**: Load once, use once
```cuda
for (int i = 0; i < n; i++)
    for (int j = 0; j < n; j++)
        C[i][j] = A[i][j] + B[i][j];
```

**Good**: Load once, use many times (tiling)
```cuda
__shared__ float tileA[TILE][TILE];
__shared__ float tileB[TILE][TILE];

// Load A[i][k] once, use for all j
for (int k = 0; k < n; k += TILE) {
    // A[i][k..k+TILE] reused for all j
    // ...
}
```

### 2. Use Tiling to Increase Reuse

```cuda
__global__
void tiledMatMul(float *A, float *B, float *C, int n) {
    __shared__ float As[TILE][TILE];
    __shared__ float Bs[TILE][TILE];
    
    int row = blockIdx.y * TILE + threadIdx.y;
    int col = blockIdx.x * TILE + threadIdx.x;
    
    float cvalue = 0;
    
    for (int k = 0; k < n; k += TILE) {
        As[threadIdx.y][threadIdx.x] = A[row * n + k + threadIdx.x];
        Bs[threadIdx.y][threadIdx.x] = B[(k + threadIdx.y) * n + col];
        __syncthreads();
        
        // Multiply and accumulate
        for (int m = 0; m < TILE; m++) {
            cvalue += As[threadIdx.y][m] * Bs[m][threadIdx.x];
        }
        __syncthreads();
    }
    
    C[row * n + col] = cvalue;
}
```

**Result**: A[row][k] reused for all columns → high intensity.

### 3. Loop Unrolling

```cuda
// Unroll inner loop
#pragma unroll 8
for (int i = 0; i < 8; i++) {
    sum += data[i];
}
```

**Effect**: Better instruction-level parallelism, better register allocation.

## Intensity Thresholds

### For H100 (FP16 Tensor)

| Intensity | Bound | GPU Utilization |
|-----------|-------|----------------|
| < 1 | Memory | Low |
| 1-100 | Both | Medium |
| 100-1000 | Compute | High |
| > 1000 | Compute | Peak |

### Practical Thresholds

| Algorithm | Intensity | Bound |
|-----------|-----------|-------|
| Vector add | 0.3 | Memory |
| Convolution 3×3 | ~9 | Memory-Compute |
| Convolution 11×11 | ~121 | Compute |
| Matrix multiply | ~683 | Compute |
| FFT | ~2log(n) | Memory-Compute |
| Stencil (3D) | Varies | Memory |

## Memory-Bound → Compute-Bound

### Optimization Techniques

| Technique | Effect | When to Use |
|-----------|--------|-------------|
| Tiling | ↑ Reuse | Multiple passes over data |
| Loop fusion | ↓ Redundant loads | Redundant loads exist |
| Loop unrolling | ↑ ILP | Simple inner loops |
| Better algorithm | ↑ Arithmetic ops | If available |
| Lower precision | ↓ Bytes transferred | When precision allows |

### Example: Convolution Optimization

**Naive**: Intensity ≈ k²
**Tiled + Unrolled**: Can approach theoretical peak

## Measuring Intensity

### Roofline Performance Model

```python
# Calculate achievable GFLOPS
def roofline(peak_flops, bandwidth, intensity):
    ceiling = min(peak_flops, bandwidth * intensity)
    return ceiling
```

### Actual Performance

```bash
# Use ncu (Nsight Compute)
ncu --metrics sm__throughput.avg.pct_of_peak_sustained, \
                dram__bytes.sum, \
                sm__cycles_active.sum ./a.out
```

## Related

- [[Memory Bandwidth]] — The bottleneck for low intensity
- [[Tensor Cores]] — Compute unit for high intensity
- [[Memory Coalescing]] — Optimizing memory access
- [[Shared Memory]] — Enables data reuse
- [[GPU Deep Learning Guide]] — Intensity in neural networks
