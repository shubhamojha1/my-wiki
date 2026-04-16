---
title: "Kernel (GPU)"
type: concept
tags: [gpu, cuda, parallel-computing]
created: 2026-04-16
sources: [cs179_2026_lec01.pdf]
---

# Kernel (GPU)

A function that executes in parallel across many GPU threads. The fundamental unit of work in GPU computing.

## Definition

In CUDA/OpenCL terminology, a *kernel* is a specially-marked function that, when invoked, spawns a grid of threads, each executing the kernel code independently on different data elements.

## Thread Hierarchy

```
Grid
 └── Block 0            └── Block 1            └── Block N
      ├── Thread 0           ├── Thread 0           ├── Thread 0
      ├── Thread 1           ├── Thread 1           ├── Thread 1
      └── Thread M           └── Thread M           └── Thread M
```

- **Grid**: Entire set of threads for a kernel launch
- **Block**: Group of threads that share memory/synchronize
- **Thread**: Smallest execution unit with unique ID

## Thread Indexing

Each thread computes its unique index to determine which data to process:

```cuda
int i = threadIdx.x + blockIdx.x * blockDim.x;
// i ranges from 0 to (gridDim.x * blockDim.x - 1)
```

- `threadIdx`: Thread index within its block (x, y, z)
- `blockIdx`: Block index within the grid (x, y, z)
- `blockDim`: Dimensions of each block
- `gridDim`: Dimensions of the grid

## Example: Vector Addition

```cuda
__global__
void addKernel(float *A, float *B, float *C, int N) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < N) {
        C[i] = A[i] + B[i];
    }
}

// Launch: addKernel<<<numBlocks, blockSize>>>(d_A, d_B, d_C, N);
```

## Best Practices

1. **Bounds checking**: Always verify `i < N` to avoid out-of-bounds access
2. **Coalesced memory access**: Adjacent threads should access adjacent memory
3. **Shared memory**: Use `__shared__` for threads within a block to communicate
4. **Occupancy**: Maximize threads per block for hardware utilization

## Related

- [[CUDA]] — Platform where kernels are defined
- [[GPU Computing]] — The paradigm kernels enable
- [[CS 179: Introduction to GPU Programming - Lecture 1]] — Source lecture
