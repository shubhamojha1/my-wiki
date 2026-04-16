---
title: "CUDA"
type: entity
tags: [gpu, parallel-computing, nvidia]
created: 2026-04-16
sources: [cs179_2026_lec01.pdf]
---

# CUDA

Compute Unified Device Architecture. NVIDIA's parallel computing platform and API that enables general-purpose computing on NVIDIA GPUs.

## Overview

CUDA provides a C/C++ extension for writing GPU code, abstracting away hardware details while exposing GPU parallelism. It is the primary tool used in [[CS 179: Introduction to GPU Programming - Lecture 1|CS 179]] at Caltech.

## Key Concepts

- **Kernel**: A function that executes in parallel across many GPU threads
- **Thread hierarchy**: Threads organized into blocks, blocks into grid
- **Memory management**: Explicit allocation/copy between host (CPU) and device (GPU) memory
- **Thread indexing**: `threadIdx`, `blockIdx` provide unique identifiers

## Example: Array Addition

```cuda
// Host code
float *C = malloc(N * sizeof(float));
cudaMalloc(&d_A, N * sizeof(float));
cudaMemcpy(d_A, A, N * sizeof(float), cudaMemcpyHostToDevice);
// ... allocate d_B, d_C similarly
addKernel<<<blocks, threads>>>(d_A, d_B, d_C);
cudaMemcpy(C, d_C, N * sizeof(float), cudaMemcpyDeviceToHost);
```

```cuda
// Kernel (device code)
__global__
void addKernel(float *A, float *B, float *C) {
    int i = threadIdx.x + blockIdx.x * blockDim.x;
    C[i] = A[i] + B[i];
}
```

## Alternatives

- **OpenCL**: Cross-vendor heterogeneous computing framework
- **Vulkan**: Modern multiplatform compute (not covered in CS 179)
- **pyCUDA**: Python bindings for CUDA

## Related

- [[GPU Computing]] — The broader paradigm
- [[Kernel (GPU)]] — Functions executed on the GPU
- [[CS 179: Introduction to GPU Programming - Lecture 1]] — Source course
