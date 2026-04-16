---
title: "Bank Conflicts"
type: concept
tags: [gpu, shared-memory, optimization, cuda, performance]
created: 2026-04-16
sources: [cs179_2026_lec04.pdf]
---

# Bank Conflicts

A performance issue in shared memory where multiple threads in a warp access memory banks in a way that forces sequential (serial) access instead of parallel access.

## Overview

Shared memory is divided into **32 banks** (typically). Each bank can service one access per cycle. When two or more threads access the same bank simultaneously, the accesses are serialized — this is a **bank conflict**.

**Bank conflicts = parallel-to-serial slowdown = bad for performance**

## How Shared Memory Banks Work

### Bank Structure

Shared memory is divided into 32 banks:
- Each bank handles one 32-bit (4-byte) access per cycle
- Element `i` is stored in bank `i % 32`
- Banks are interleaved at 4-byte granularity

```
Address:  0   4   8   12  16  20  24  28 ... (bytes)
Bank:     0   1   2   3   4   5   6   7 ...

Address:  128 132 136 140 144 148 152 156 ...
Bank:     0   1   2   3   4   5   6   7 ...
```

### Bank Conflict Scenarios

| Access Pattern | Result | Performance |
|---------------|--------|------------|
| Thread i → Bank i | No conflict | Optimal |
| 2 threads → Same bank | 2-way conflict | 2x slower |
| 32 threads → Same bank | 32-way conflict | 32x slower |

### Conflict-Free Patterns

**Broadcast**: All threads read the same address
- Single value broadcast to all threads
- Efficient: one access, shared result

**Sequential**: Threads access consecutive banks
- Thread 0 → Bank 0, Thread 1 → Bank 1, etc.
- No conflicts: parallel access

## Stride Impact on Bank Conflicts

Stride = distance from `thread[i]` address to `thread[i+1]` address.

### Stride 1 (Sequential)

```
Thread 0 → Bank 0
Thread 1 → Bank 1
Thread 2 → Bank 2
...
Thread 31 → Bank 31
```
**Result**: No conflicts (one access per bank)

### Stride 2

```
Thread 0 → Bank 0
Thread 1 → Bank 2  (conflict with Thread 0?)
Thread 2 → Bank 4  (conflict with Thread 1?)
...
```

Wait time:
```
Thread 0 → Bank 0 (cycle 1)
Thread 1 → Bank 0 (cycle 2) ← conflict
Thread 2 → Bank 0 (cycle 3) ← conflict
...
Thread 15 → Bank 0 (cycle 16) ← conflict
Thread 16 → Bank 2 (cycle 17)
...
```

**Result**: 16 pairs of 2-way conflicts = 2x slowdown

### Stride 4

```
Thread 0 → Bank 0
Thread 1 → Bank 4  (conflict with Thread 0)
Thread 2 → Bank 8  (conflict with Thread 1)
...
Thread 7 → Bank 28 (conflict with Thread 6)
Thread 8 → Bank 0  (conflict with Thread 0)
```

**Result**: 8 groups of 4-way conflicts = 4x slowdown

### Stride 32 (Worst Case)

```
Thread 0 → Bank 0
Thread 1 → Bank 0  (conflict)
...
Thread 31 → Bank 0  (conflict)
```

**Result**: 1 group of 32-way conflicts = **32x slowdown**

## Conflict Resolution

### Serial Execution

When a conflict occurs, the GPU serializes the accesses:

```
Without conflict:
[Bank 0]──→[Bank 1]──→[Bank 2]──→[Bank 3]──→ (parallel, 1 cycle)

With 4-way conflict:
[Bank 0]──→[Bank 0]──→[Bank 0]──→[Bank 0]──→ (serial, 4 cycles)
```

## Padding to Avoid Bank Conflicts

### The Problem: Stride 32

```cuda
// Transpose kernel - causes stride 32 conflict
__global__
void transpose(float *in, float *out, int width) {
    __shared__ float tile[32][32];
    
    int x = blockIdx.x * 32 + threadIdx.x;
    int y = blockIdx.y * 32 + threadIdx.y;
    
    // Load: stride 1 (OK)
    tile[threadIdx.y][threadIdx.x] = in[y * width + x];
    
    __syncthreads();
    
    // Store: stride 32 (BAD!)
    out[x * width + y] = tile[threadIdx.x][threadIdx.y];
}
```

### The Solution: Add Padding

```cuda
// Padding adds 1 column to avoid bank conflicts
__shared__ float tile[32][33];  // 33 instead of 32!

// Now:
// Thread 0 → Bank 0   (col 0)
// Thread 1 → Bank 1   (col 1)
// ...
// Thread 31 → Bank 31 (col 31)

// When accessing:
// out[x * width + y] = tile[threadIdx.x][threadIdx.y];

// tile[threadIdx.x][threadIdx.y] is at:
// (threadIdx.x * 33 + threadIdx.y) % 32
// = (threadIdx.x % 32 + threadIdx.y % 32) % 32  (no conflicts!)
```

### General Padding Rule

For a 2D array with N columns:
- Store in `N+1` columns (padding of 1)
- Now stride N becomes stride (N+1)
- N and N+1 are coprime when N is power of 2
- Result: accesses are spread across all banks

## Bank Modes

### 32-Bank Interleaving (Default)

- 4-byte interleaving
- Each consecutive 4 bytes = different bank
- Common for most applications

### 16-Bank Interleaving

- 8-byte interleaving
- Better for double precision (8 bytes)
- Can reduce conflicts for some access patterns

### Broadcast Mode

- Single address broadcast to all threads
- Useful when all threads read same value
- Always conflict-free

## CUDA API for Bank Mode

```cuda
// Set shared memory bank mode
// In kernel or cuda kernel launch config

// cudaFuncSetCacheConfig for global setting
cudaFuncSetCacheConfig(myKernel, cudaFuncCachePreferShared);

// For dynamic shared memory in kernel
extern __shared__ float s[];
cudaDeviceSetSharedMemConfig(cudaSharedMemBankModeFourByte);
// or
cudaDeviceSetSharedMemConfig(cudaSharedMemBankModeEightByte);
```

## Identifying Bank Conflicts

### NVIDIA Visual Profiler / Nsight

Look for:
- Shared memory efficiency < 100%
- High warp stall reasons related to shared memory

### Simulation

```cuda
#ifdef __CUDA_ARCH__
#if __CUDA_ARCH__ >= 200
// Fermi+ has shared memory
#endif
#endif
```

## Common Patterns and Solutions

### Matrix Transpose

| Pattern | Stride | Solution |
|---------|--------|----------|
| Naive transpose | 32 (columns) | Padding (32→33) |
| Shared tile load | 1 | No change needed |
| Shared tile store | 32 | Padding needed |

### Reduction

| Pattern | Stride | Solution |
|---------|--------|----------|
| Sequential access | 1 | No change |
| Strided access | warpSize | Sequential access |

### Convolution

| Pattern | Problem | Solution |
|---------|---------|----------|
| Filter kernel | Random access | Shared memory for kernel |

## Best Practices

1. **Use stride 1** when possible
2. **Pad shared memory arrays** when doing column access
3. **Minimize shared memory conflicts** in hot paths
4. **Test different configurations** with profiling
5. **Use broadcast** when all threads need same value
6. **Consider bank mode** (4-byte vs 8-byte) for your data type

## Related

- [[Shared Memory]] — Where bank conflicts occur
- [[Memory Coalescing]] — Similar concept for global memory
- [[Memory Hierarchy (GPU)]] — Context for shared memory
- [[GPU Deep Learning Guide]] — Memory optimization for DL
