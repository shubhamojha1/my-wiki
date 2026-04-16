---
title: "Memory Coalescing"
type: concept
tags: [gpu, memory, optimization, cuda, performance]
created: 2026-04-16
sources: [cs179_2026_lec04.pdf]
---

# Memory Coalescing

An optimization technique where adjacent GPU threads access adjacent memory addresses, maximizing memory bandwidth by fully utilizing cache lines and minimizing transaction overhead.

## Overview

GPU memory accesses are performed in **warps** (32 threads). The hardware fetches memory in aligned chunks called **cache lines** (128 bytes on NVIDIA GPUs).

**Coalesced access** = All threads in a warp access a contiguous memory region = One or few cache line fetches.

**Non-coalesced access** = Threads access scattered addresses = Multiple cache line fetches = Wasted bandwidth.

## How GPU Memory Transactions Work

### Cache Line Structure

- **Size**: 128 bytes (32 floats, 32 ints)
- **Alignment**: All accesses are aligned to 128-byte boundaries
- **Granularity**: Memory transactions happen per warp

### Ideal Scenario: Perfect Coalescing

```
Thread 0 reads: address 0-3   ─┐
Thread 1 reads: address 4-7   ─┤
Thread 2 reads: address 8-11  ─┼─→ 1 cache line fetch (128 bytes)
...                            ─┤
Thread 31 reads: address 124-127 ─┘
```

All 32 threads access consecutive addresses → **1 transaction**.

### Worst Case: Fully Non-Coalesced

```
Thread 0 reads: address 0-3     ─┐
Thread 1 reads: address 1000-1003 ─┤
Thread 2 reads: address 2000-2003 ─┤
...                                ─┤→ 32 separate cache line fetches!
Thread 31 reads: address 31000-31003 ─┘
```

Each thread accesses a different cache line → **32 transactions**.

## Coalescing Rules

### Requirements for Perfect Coalescing

1. Threads access consecutive addresses
2. Access is sequential (thread i → address i)
3. Data type is 4 bytes or smaller (or properly aligned)
4. Starting address is aligned to cache line

### When Coalescing Breaks Down

1. **Misaligned access**: Starting address not aligned
2. **Strided access**: Thread i accesses address i * stride
3. **Scattered access**: Random/non-sequential addresses
4. **Large data types**: > 4 bytes may need multiple fetches

## Examples

### Good: Coalesced Access (Row-Major)

```cuda
__global__
void rowMajorAccess(float *data, int rows, int cols) {
    int row = blockIdx.x * blockDim.x + threadIdx.x;
    int col = threadIdx.y;
    
    if (row < rows && col < cols) {
        float val = data[row * cols + col];  // Coalesced!
    }
}
```

**Access pattern** (for fixed row):
- Thread 0 → data[row * cols + 0]
- Thread 1 → data[row * cols + 1]
- ...
- Thread 31 → data[row * cols + 31]

### Bad: Non-Coalesced Access (Column-Major)

```cuda
__global__
void colMajorAccess(float *data, int rows, int cols) {
    int row = threadIdx.x;
    int col = blockIdx.x * blockDim.x + threadIdx.y;
    
    if (row < rows && col < cols) {
        float val = data[row * cols + col];  // NOT coalesced!
    }
}
```

**Access pattern** (for fixed col):
- Thread 0 → data[0 * cols + col] = data[col]
- Thread 1 → data[1 * cols + col] = data[col + cols]
- Thread 2 → data[2 * cols + col] = data[col + 2*cols]
- ...

Each thread accesses memory `cols` bytes apart → **strided access**.

## Strided Access

Strided accesses cannot fully coalesce because threads in a warp access addresses that are `stride` apart.

### Impact of Stride

| Stride | Transactions Needed | Efficiency |
|--------|-------------------|------------|
| 1 | 1-2 | 100% |
| 2 | 2-4 | 50% |
| 4 | 4-8 | 25% |
| 32 | 32 | 3% |

### When Strides Happen

- **Column access**: `data[row * cols + col]` where col varies
- **Transposed matrix access**
- **FFT twiddle factors**
- **Gather operations**

## Optimization Strategies

### Strategy 1: Coalesce the Outer Loop

```cuda
// BAD: Column-wise access
for (int i = 0; i < rows; i++) {
    for (int j = 0; j < cols; j++) {
        process(data[i * cols + j]);  // Non-coalesced
    }
}

// GOOD: Row-wise access  
for (int j = 0; j < cols; j++) {
    for (int i = 0; i < rows; i++) {
        process(data[i * cols + j]);  // Coalesced
    }
}
```

### Strategy 2: Use Shared Memory Tiles

```cuda
__global__
void tiledAccess(float *data, int rows, int cols) {
    __shared__ float tile[BLOCK][BLOCK];
    
    int row = blockIdx.y * BLOCK + threadIdx.y;
    int col = blockIdx.x * BLOCK + threadIdx.x;
    
    // Coalesced load into shared memory
    tile[threadIdx.y][threadIdx.x] = data[row * cols + col];
    __syncthreads();
    
    // Strided access within block (shared mem is fast)
    float val = tile[threadIdx.x][threadIdx.y];  // Fast!
}
```

### Strategy 3: Restructure Data Layout

```cuda
// Array of Structures (AoS) - Bad for GPUs
struct Point { float x, y, z; };
Point points[N];

// Structure of Arrays (SoA) - Good for GPUs
float x[N], y[N], z[N];
```

## Alignment and Padding

### Alignment Requirements

Data should be aligned to:
- 4 bytes for single precision
- 8 bytes for double precision
- 16 bytes for vectors (float4, etc.)

### CUDA Alignment Macros

```cuda
__align__(16)  // Force 16-byte alignment
float4 vec;     // 16-byte vector type
```

### Zero Padding for Column Access

If you must do column access, add padding to make stride a power of 2:

```cuda
// Instead of stride = cols
// Pad to stride = cols + 1 (power of 2 alignment helps)
int stride = cols + 1;
```

## Measuring Coalescing

### NVIDIA Visual Profiler

Use `nvvp` or Nsight Compute to see:
- Achieved memory throughput
- Transaction efficiency percentage
- Warp execution efficiency

### Code Indicators

```cuda
// Check transaction efficiency
// Lower is better
unsigned int activecycles;
asm("mov.u32 %0, %lanewaitcnt;" : "=r"(activecycles));
```

## Common Mistakes

| Mistake | Symptom | Solution |
|---------|---------|----------|
| Column-major iteration | 1/32 efficiency | Swap loop order |
| Misaligned arrays | Extra transactions | Use `__align__` |
| Random access | Maximum waste | Restructure data |
| Large stride | Low efficiency | Use shared memory tiles |

## Best Practices Summary

1. **Design for row-major access** in kernel code
2. **Use SoA layout** for arrays of structs
3. **Coalesce loads first**, then use shared memory for irregular access
4. **Align all data** to at least 4-byte boundaries
5. **Avoid strided access** when possible
6. **Use shared memory** as intermediary for non-coalesced patterns

## Related

- [[Memory Hierarchy (GPU)]] — Where coalescing fits
- [[Bank Conflicts]] — Similar optimization for shared memory
- [[Shared Memory]] — Used for tiling to enable coalescing
- [[GPU Deep Learning Guide]] — Memory access in DL
