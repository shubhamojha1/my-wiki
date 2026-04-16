---
title: "CUDA Synchronization"
type: concept
tags: [gpu, cuda, synchronization, parallelism, threads]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# CUDA Synchronization

Mechanisms for coordinating execution between GPU threads, blocks, and the host. GPU synchronization differs fundamentally from CPU synchronization due to hardware constraints.

## Overview

### Why Synchronization Matters

**Ideal parallelism**: No shared resources, no communication needed between threads.

**Reality**: Many parallel algorithms require shared data, leading to:
- Race conditions
- Data hazards
- Deadlock situations

### GPU vs CPU Synchronization

| Approach | CPU | GPU |
|----------|-----|-----|
| Locks | ✓ | ✗ (too expensive) |
| Semaphores | ✓ | ✗ |
| Condition Variables | ✓ | ✗ |
| Barriers | ✓ | ✓ (limited) |
| Atomics | ✓ | ✓ |

**Key difference**: GPU has separate address spaces per SM; can't synchronize across SMs.

## __syncthreads()

The primary CUDA synchronization primitive.

### Function Signature

```cuda
__syncthreads();
```

### Behavior

- All threads in a block wait until **all** threads reach this point
- Ensures memory visibility within block
- Required after shared memory loads before computation

### Rules

1. **Block-level only**: Cannot sync across blocks
2. **All threads must call**: Deadlock if any thread skips
3. **Barrier in divergent code**: Only threads in same execution path meet

### Use Cases

```cuda
__global__
void kernel(float *data) {
    __shared__ float tile[256];
    
    // Phase 1: Load into shared memory
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    tile[threadIdx.x] = data[i];
    
    // Wait for all threads to finish loading
    __syncthreads();
    
    // Phase 2: Process shared data
    float result = tile[threadIdx.x] * 2.0f;
    
    // Wait for all threads to finish processing
    __syncthreads();
    
    // Phase 3: Store results
    data[i] = result;
}
```

### Variants

```cuda
// Standard barrier
__syncthreads();

// Barrier with predicate (Fermi+)
// Waits only if predicate is true
__syncthreads_or(unsigned int predicate);

// Device-wide ( Volta+ )
// Sync all threads in device (expensive!)
__threadfence();
__threadfence_block();  // Same as __syncthreads()
__threadfence_system(); // CPU-GPU sync
```

## Deadlock

### What is Deadlock?

When threads wait for each other in a circular dependency, preventing any progress.

### Common Deadlock Scenarios

#### 1. Missing Synchronization

```cuda
// DEADLOCK PRONE
__global__
void deadlockExample(float *data) {
    __shared__ float tile[256];
    
    // Thread 0 loads, others skip
    if (threadIdx.x == 0) {
        tile[0] = data[0];
    }
    
    // All threads wait, but thread 0 already passed
    // Thread 0 never waits → deadlock!
    __syncthreads();
    
    // Use: if (threadIdx.x == 0) { ... } __syncthreads(); is fine
    // Problem: if (condition) { __syncthreads(); }
}
```

#### 2. Conditional Synchronization

```cuda
// DEADLOCK - DON'T DO THIS
if (threadIdx.x < 32) {
    __syncthreads();  // Only warp 0 calls
}
// Warp 2+ never calls → deadlock

// CORRECT - All threads call
__syncthreads();
if (threadIdx.x < 32) {
    // warp-specific work
}
```

#### 3. Nested Synchronization

```cuda
// Potential deadlock with nested syncs
__global__
void nestedBad(float *data) {
    __syncthreads();
    
    if (condition) {
        __syncthreads();  // Nested sync
    }
    __syncthreads();  // All threads must reach here
}
```

### Avoiding Deadlock

1. **All threads call `__syncthreads()`** or none do
2. **No conditional synchronization** within a block
3. **Simple sync patterns**: Load → sync → compute → sync → store
4. **Avoid nested syncs** when possible

## Synchronization Patterns

### Pattern 1: Producer-Consumer

```cuda
__global__
void producerConsumer(float *data) {
    __shared__ float buffer[256];
    
    // Producer: Thread 0 loads data
    if (threadIdx.x == 0) {
        buffer[0] = data[0];
    }
    __syncthreads();
    
    // Consumer: All threads use data
    float value = buffer[0];
    // Process...
}
```

### Pattern 2: Reduction with Sync

```cuda
__global__
void reduction(float *data, float *result) {
    __shared__ float sdata[256];
    
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    sdata[threadIdx.x] = data[i];
    __syncthreads();
    
    // In-block reduction
    for (int s = blockDim.x / 2; s > 0; s >>= 1) {
        if (threadIdx.x < s) {
            sdata[threadIdx.x] += sdata[threadIdx.x + s];
        }
        __syncthreads();
    }
    
    if (threadIdx.x == 0) {
        result[blockIdx.x] = sdata[0];
    }
}
```

### Pattern 3: Staged Computation

```cuda
// Three-stage pipeline
__global__
void stagedKernel(float *data) {
    __shared__ float stage1[256];
    __shared__ float stage2[256];
    
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    
    // Stage 1: Load
    stage1[threadIdx.x] = data[i];
    __syncthreads();
    
    // Stage 2: Process
    stage2[threadIdx.x] = stage1[threadIdx.x] * 2.0f;
    __syncthreads();
    
    // Stage 3: Store
    data[i] = stage2[threadIdx.x];
}
```

## Grid-Level Synchronization

### Problem: No Direct Grid Sync

- Blocks run independently on different SMs
- SMs are physically separate
- Cannot wait for other blocks' completion

### Workarounds

#### 1. Kernel Chaining

```cuda
// Instead of one kernel with grid sync
// Split into multiple kernels
kernel_stage1<<<grid, block>>>(data);
cudaDeviceSynchronize();  // Host waits
kernel_stage2<<<grid, block>>>(data);
cudaDeviceSynchronize();
kernel_stage3<<<grid, block>>>(data);
```

#### 2. Persistent Threads

```cuda
// Threads stay alive, process multiple items
__global__
void persistentKernel(float *queue, int *count) {
    __shared__ float tile[256];
    
    while (atomicAdd(count, 0) > 0) {
        // Process one item
        int idx = atomicAdd(count, -1) - 1;
        if (idx >= 0) {
            tile[threadIdx.x] = queue[idx];
            __syncthreads();
            // Process...
        }
        __syncthreads();
    }
}
```

## Host-Device Synchronization

### cudaDeviceSynchronize()

```cuda
// Wait for all device kernels to complete
cudaDeviceSynchronize();

// Alternative: cudaStreamSynchronize() for streams
cudaStream_t stream;
cudaStreamCreate(&stream);
kernel<<<grid, block, 0, stream>>>(data);
cudaStreamSynchronize(stream);
```

### cudaThreadSynchronize() (deprecated)

```cuda
// Legacy version
cudaThreadSynchronize();
```

## Best Practices

1. **Use `__syncthreads()` only when necessary** — synchronization has overhead
2. **Minimize sync points** — combine where possible
3. **All threads must participate** — avoid conditional sync
4. **Use shared memory for inter-thread communication** — faster than global
5. **Prefer block-level patterns** — cannot sync across blocks
6. **Profile synchronization cost** — use Nsight to measure impact

## Related

- [[Shared Memory]] — Where inter-thread communication happens
- [[Atomic Operations]] — For fine-grained synchronization
- [[Warp Scheduler]] — Related to thread scheduling
- [[Deadlock]] — Synchronization pitfall
