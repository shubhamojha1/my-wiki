---
title: "Memory Hierarchy (GPU)"
type: concept
tags: [gpu, memory, hardware, cuda, performance]
created: 2026-04-16
sources: [cs179_2026_lec04.pdf]
---

# Memory Hierarchy (GPU)

The organized layers of memory in a GPU, from fastest and smallest (registers) to slowest and largest (global memory). Understanding this hierarchy is critical for writing performant GPU code.

## Overview

GPUs have multiple types of memory, each with different:
- **Latency**: How long operations take
- **Bandwidth**: How much data can be transferred
- **Scope**: Which threads can access it
- **Persistence**: How long data survives

## Complete Memory Hierarchy

| Memory Type | Latency | Size | Scope | Bandwidth |
|-------------|---------|------|-------|-----------|
| Registers | ~5ns | ~256 KB/SM | Thread | Highest |
| Shared Memory | ~5ns | 48-128 KB/SM | Block | Very High |
| L1 Cache | ~34 cycles | 128 KB/SM | SM | High |
| L2 Cache | ~200 cycles | 6-72 MB | GPU | Medium |
| L3 Cache | > L2 | Varies | GPU | Medium-Low |
| Global Memory | ~300-600ns | 2-80 GB | Application | Lowest |

## Detailed Breakdown

### Registers

- **Fastest memory on GPU**
- ~5ns latency
- Thread-private: each thread has its own
- Lifetime: Thread execution
- Maximum: ~32-64 32-bit registers per thread
- Most stack variables in kernels go here

```cuda
__global__
void kernel(float x) {
    float y = x * 2;  // y lives in a register
}
```

### Local Memory

- **Everything that can't fit in registers**
- Actually stored in global memory (slow!)
- ~150x slower than registers
- Thread-private
- Lifetime: Thread execution
- Common causes: Large arrays, register spilling

```cuda
__global__
void kernel(float *data) {
    float large_array[1024];  // Goes to local memory
}
```

### Shared Memory

- **Fast, block-shared memory**
- ~5ns latency (same hardware as L1 cache)
- 48-128 KB per SM (varies by architecture)
- Threads in same block can share data
- Lifetime: Block execution
- Used for inter-thread communication within block

```cuda
__global__
void kernel(float *data) {
    __shared__ float tile[256];
    // All threads in block share this
}
```

### L1 Cache

- **Per-SM automatic cache**
- ~34 cycles latency
- ~128 KB per SM
- Caches local and global memory accesses
- Auto-managed by hardware

### L2 Cache

- **GPU-wide shared cache**
- ~200 cycles latency
- 6 MB (Ampere) to 72 MB (Ada)
- Caches all global and local memory
- Shared across all SMs

### Global Memory

- **Main GPU memory (HBM/GDDR)**
- ~300-600ns latency (slowest)
- 2-80 GB capacity
- Host and device can access
- Persistent across kernel launches
- Accessed via PCIe for host communication

```cuda
float *d_data;  // Global memory allocation
cudaMalloc(&d_data, size * sizeof(float));
```

### Constant Memory

- **Cached global memory for constants**
- ~64 KB user + ~64 KB compiler space
- Cached in constant cache per SM
- Broadcasts single address to all threads efficiently
- Set from host before kernel launch

```cuda
__constant__ int config[1024];  // Constant memory

// Host code
cudaMemcpyToSymbol(config, h_config, sizeof(config));
```

### Texture Memory

- **Optimized for 2D/3D spatial locality**
- Uses special texture cache
- Fast interpolation capabilities
- Integer-to-float conversion
- Common for image processing

## Latency Comparison

```
Registers:     5 ns    (1x)
Shared Mem:   5 ns    (1x)
L1 Cache:     ~50 ns  (10x)
L2 Cache:     ~200 ns (40x)
Global Mem:   300-600 ns (60-120x)
```

## Architecture Evolution

| Architecture | Shared Memory | L2 Cache |
|--------------|--------------|----------|
| Volta | 128 KB/SM | 6 MB |
| Turing | 96 KB/SM | 5.5 MB |
| Ampere | 128 KB/SM | 6 MB |
| Ada | 128 KB/SM | 72 MB |
| Hopper | 128 KB/SM | Largest |

## Memory Access Speed Factors

### What Makes Memory Fast?

1. **Proximity to compute**: Registers > Shared > Cache > Global
2. **Bandwidth**: Wider bus = faster
3. **Caching**: Frequently accessed data stays close
4. **Scope**: Smaller scope = more optimizations possible

### What Makes Memory Slow?

1. **Distance**: Global memory is physically separate from SMs
2. **Competition**: All SMs share memory bandwidth
3. **Uncoalesced access**: Poor access patterns waste bandwidth
4. **Bank conflicts**: Shared memory conflicts serialize access

## Best Practices

1. **Favor registers**: Most stack variables fit here
2. **Use shared memory**: For data shared within block
3. **Coalesce global access**: Adjacent threads → adjacent memory
4. **Avoid local memory**: Keep arrays small or use shared memory
5. **Leverage caches**: Good access patterns maximize cache hits

## Related

- [[Memory Coalescing]] — Optimizing global memory access
- [[Bank Conflicts]] — Shared memory optimization
- [[Register Spilling]] — When registers overflow
- [[Computational Intensity]] — Balancing compute and memory
- [[GPU Deep Learning Guide]] — How memory affects DL performance
- [[L2 Cache]] — Detailed cache analysis
