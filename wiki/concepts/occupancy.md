---
title: "Occupancy"
type: concept
tags: [gpu, performance, parallelism, resources]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# Occupancy

The ratio of active warps to maximum possible warps per SM. Critical for hiding latency and achieving peak GPU performance.

## Definition

```
Occupancy = (Active Warps per SM) / (Max Warps per SM) × 100%
```

### Key Formula

```cuda
Occupancy = min(
    blocks_per_SM * warps_per_block,
    max_warps_per_SM
) / max_warps_per_SM
```

## Why Occupancy Matters

### Latency Hiding

GPU hides latency by switching between warps:
- **High occupancy**: Always have ready warps → no stalls
- **Low occupancy**: Scheduler runs out of warps → idle cycles

### Throughput Connection

```
High Occupancy + Good ILP = Peak Performance
High Occupancy + Poor ILP = Good Performance  
Low Occupancy + High ILP = Medium Performance
Low Occupancy + Poor ILP = Poor Performance
```

## H100/H200 Specifications

| Resource | H100/H200 |
|----------|-----------|
| Max threads per SM | 2048 (64 warps) |
| Max threads per block | 1024 (32 warps) |
| Max warps per block | 32 |
| Max blocks per SM | 32 |
| 32-bit registers per SM | 65536 |
| Max shared memory per SM | 228 KB |

## Occupancy Examples (H100)

### 100% Occupancy

```cuda
// Configuration achieving 100% occupancy
threads_per_block = 1024  // 32 warps
blocks_per_SM = 2         // 2 × 32 = 64 warps = 100%
registers_per_thread = 32
shared_memory_per_block = 114 KB
```

### 50% Occupancy

```cuda
// Configuration achieving 50% occupancy
threads_per_block = 1024  // 32 warps
blocks_per_SM = 1         // 1 × 32 = 32 warps = 50%
registers_per_thread = 64   // More registers
shared_memory_per_block = 228 KB
```

### 25% Occupancy

```cuda
threads_per_block = 1024
blocks_per_SM = 1
registers_per_thread = 128  // Heavy register usage
// or
threads_per_block = 256
blocks_per_SM = 2
// Result: 16 warps = 25%
```

## Resource Limits

### What Limits Occupancy

| Resource | How It Limits |
|----------|---------------|
| Registers | More per thread = fewer threads |
| Shared Memory | More per block = fewer blocks |
| Threads/Block | Fixed size affects warp count |
| Hardware Maximum | Can't exceed 64 warps/SM |

### The Trade-off

```
More Resources per Thread
         ↓
Fewer Threads per SM
         ↓
Lower Occupancy
         ↓
But potentially better per-thread performance
```

## Calculating Occupancy

### Step 1: Threads Per SM

```cuda
threads_per_SM = blocks_per_SM * threads_per_block
               = 2 * 1024 = 2048 threads
```

### Step 2: Warps Per SM

```cuda
warps_per_SM = threads_per_SM / 32
             = 2048 / 32 = 64 warps
```

### Step 3: Resource Check

```cuda
// Check all limits
max_warps_from_threads = 2048 / 32 = 64
max_warps_from_registers = 65536 / regs_per_thread
max_warps_from_shared = (228 * 1024) / shared_per_block
max_warps_from_hardware = 64

occupancy_warps = min(all_limits)
occupancy_pct = occupancy_warps / 64 * 100
```

### Example Calculation

```cuda
kernel_config:
  threads_per_block = 256
  blocks_per_SM = 8
  registers_per_thread = 16
  shared_per_block = 16 KB

threads_per_SM = 8 * 256 = 2048 (✓ <= 2048)
warps_per_SM = 2048 / 32 = 64 (✓)
regs_needed = 16 * 2048 = 32768 (✓ <= 65536)
shared_needed = 16 * 8 = 128 KB (✓ <= 228 KB)

Occupancy = 64 / 64 = 100%
```

## Launch Bounds

### Controlling Resource Usage

```cuda
// Tell compiler our constraints
__global__
__launch_bounds__(max_threads_per_block, min_blocks_per_SM)
void myKernel(...) {
    // Compiler optimizes for these bounds
}

// Example: Prefer high occupancy
__launch_bounds__(256, 8)  // 256 threads, 8 blocks minimum
void lowRegKernel(...) {
    // Compiler limits registers to fit 8 blocks
}

// Example: Prefer low occupancy, high registers
__launch_bounds__(1024, 1)  // 1024 threads, 1 block max
void highRegKernel(...) {
    // Compiler can use more registers
}
```

### Trade-off: Occupancy vs Registers

```cuda
// With launch_bounds_(1024, 2): 50% occupancy, many registers
__launch_bounds__(1024, 2)
void kernelA(...) {
    float r[16];  // 16 registers = lots of spilling risk
}

// With launch_bounds_(256, 8): 100% occupancy, few registers
__launch_bounds__(256, 8)
void kernelB(...) {
    float r[4];   // Only 4 registers = fast
}
```

## Occupancy Levels

### What Occupancy Is Needed?

| Occupancy | Performance | Use Case |
|-----------|-------------|----------|
| 100% | Peak | General purpose |
| 75%+ | Very Good | Most applications |
| 50% | Good | Register-heavy kernels |
| 25% | Medium | Texture-heavy, large registers |
| <25% | Poor | Usually indicates problem |

### Memory-Bound vs Compute-Bound

| Kernel Type | Needed Occupancy |
|-------------|------------------|
| Memory-bound | Higher (50-100%) |
| Compute-bound | Can be lower (25-50%) |
| ILP-high | Can be lower |

**Reason**: Memory-bound kernels need more warps to hide long memory latency.

## Measuring Occupancy

### CUDA Profiler

```bash
# Nsight Compute
ncu --metrics sm__warps_active.avg.pct_of_peak_sustained ./a.out

# CUDA Visual Profiler (legacy)
nvvp ./a.out
```

### In-Kernel Query

```cuda
#include <cuda_runtime_api.h>

__global__
void measureOccupancy() {
    int active_warps;
    asm volatile("mov.u32 %0, %lanewarps.active;" : "=r"(active_warps));
    
    // active_warps / 64 = occupancy fraction
}
```

### CUDA Occupancy Calculator

NVIDIA provides an Excel/cuobjdump tool:
```bash
cuda-occ21 --kernel myKernel --threads 256 --registers 16 --shared 16
```

## Optimizing for Occupancy

### Reduce Register Usage

```cuda
// Bad: Many registers
__global__
void badKernel(float *data) {
    float r0, r1, r2, r3, r4, r5, r6, r7, r8, r9;
    // ...
}

// Good: Fewer registers
__global__
void goodKernel(float *data) {
    float r0, r1, r2, r3;
    // ...
}
```

### Reduce Shared Memory Usage

```cuda
// Bad: Large shared memory
__shared__ float tile[256][256];  // 256 KB

// Good: Smaller tiles
__shared__ float tile[64][64];    // 16 KB
```

### Adjust Block Size

```cuda
// Try different block sizes
threads = 256;   // Higher occupancy
threads = 1024;  // May be needed for registers
```

## Occupancy vs Performance

### Case Study: Memory-Bound Kernel

```cuda
// Naive: Low occupancy, slow
__global__
__launch_bounds__(64, 1)  // Only 2 warps = 3% occupancy
void slowKernel(float *data) {
    float a, b, c, d, e, f, g, h;  // Many registers
    // Heavy memory access
}

// Optimized: High occupancy, fast
__global__
__launch_bounds__(256, 8)  // 64 warps = 100% occupancy
void fastKernel(float *data) {
    float a, b;  // Fewer registers
    // Same memory access, but better latency hiding
}
```

### Case Study: Compute-Bound Kernel

```cuda
// Compute-bound: May not need 100% occupancy
__global__
__launch_bounds__(1024, 1)  // 32 warps = 50%
void computeKernel(float *data) {
    // Heavy arithmetic, few memory accesses
    // ILP might be enough to hide latency
}
```

## Common Pitfalls

### Over-Registering

```cuda
// DEADLY: Register spilling destroys performance
__global__
__launch_bounds__(1024, 1)
void badSpilling(...) {
    float array[1024];  // Will spill to local memory!
}
```

### Misaligned Launch Bounds

```cuda
// Block size not multiple of 32 = wasted warps
threads = 1000;  // 31.25 warps, 1 partially empty
threads = 1024;  // 32 warps exactly
```

### Ignoring Shared Memory

```cuda
// Large shared memory reduces blocks per SM
__shared__ float bigTile[65536];  // 256 KB > 228 KB limit!
// Won't compile if exceeds SM limit
```

## Best Practices

1. **Target 50-100% occupancy** for most kernels
2. **Profile before optimizing** — measure actual performance
3. **Use launch_bounds** to guide compiler
4. **Balance registers vs occupancy** — test different configs
5. **Reduce shared memory** if possible
6. **Use multiples of 32** for thread count
7. **Don't sacrifice ILP** for pure occupancy

## Related

- [[Warp Scheduler]] — Hardware that uses occupancy
- [[ILP]] — Can compensate for lower occupancy
- [[Register Spilling]] — Destroyer of performance
- [[Shared Memory]] — Affects occupancy limits
