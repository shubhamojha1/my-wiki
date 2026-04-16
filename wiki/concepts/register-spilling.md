---
title: "Register Spilling"
type: concept
tags: [gpu, registers, memory, optimization, cuda, performance]
created: 2026-04-16
sources: [cs179_2026_lec04.pdf]
---

# Register Spilling

A performance issue that occurs when a kernel uses more registers than available, causing excess variables to be stored in slow local memory (which resides in global memory).

## Overview

GPUs have a limited number of registers per thread. When a kernel exceeds this limit, variables "spill" from fast registers to slow local memory (stored in global memory).

**Impact**: 150x slowdown for spilled variables compared to registers.

## GPU Register Architecture

### Per-Thread Register Limits

| GPU Architecture | Max 32-bit Registers/Thread |
|-----------------|---------------------------|
| Most GPUs | 64 |
| Some (large kernels) | 32 |
| Minimum guaranteed | 16 |

### Per-SM Register Pool

- Each SM has a fixed register file size
- Registers are partitioned among active warps/threads
- More registers per thread = fewer concurrent threads
- Fewer registers per thread = more threads, but risk spilling

### Register Allocation

```cuda
__global__
void kernel(...) {
    float x;           // Register
    float y = x * 2;   // Register
    float z = y + 1;   // Register
    // ...
}
```

All three variables fit in registers → **No spilling**.

## When Spilling Occurs

### Triggers

1. **Too many local variables**: Large arrays, complex kernels
2. **High occupancy pressure**: Many threads competing for registers
3. **Large data structures**: Structures that don't fit in registers
4. **Debug builds**: Compiler keeps more variables

### Warning Signs

```bash
$ nvcc -Xptxas -v kernel.cu
ptxas info: Function properties for '_Z6kernelPfi'
  72 bytes stack frame, 12 bytes spill stores, 12 bytes spill loads
```

If you see "spill stores/loads" > 0, you're spilling.

## The Spill Penalty

### Memory Hierarchy Reminder

| Memory Type | Latency | Relative Speed |
|-------------|---------|---------------|
| Register | ~5ns | 1x (baseline) |
| Local Memory | ~300-600ns | ~150x slower |

### Spill Cost Calculation

**Register access**:
```cuda
z0 = x0 + y0;  // z0, x0, y0 in registers
```
1 instruction, 0 extra memory operations.

**Spill access**:
```cuda
// Assume x1 must be spilled
// Store x1 to local memory
st.local.f32 [spill_loc], x1;

// Later, load x1 back
ld.local.f32 x1, [spill_loc];

z1 = x1 + y1;
```
**Cost**: 2 memory operations + 2 dependent instructions per spill.

## Register Spilling Example

### Code

```cuda
__global__
void vectorAdd(float *x, float *y, float *z, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        // Assume only 3 free registers available
        float x0 = x[i];
        float y0 = y[i];
        float z0 = x0 + y0;  // OK: 3 registers
        
        float x1 = x[i + 1];  // Spill! Need 4th register
        float y1 = y[i + 1];
        float z1 = x1 + y1;
        
        z[i] = z0;
        z[i + 1] = z1;
    }
}
```

### With Enough Registers (Fast)

```
x0 = x[0]        // Load
y0 = y[0]        // Load
z0 = x0 + y0     // Compute
z[0] = z0        // Store
```

**4 operations, 0 memory spills.**

### With Register Pressure (Slow)

```
x0 = x[0]        // Load
y0 = y[0]        // Load
x1 = x[1]        // Load → No register free! Must spill x0.

// Spill x0:
st.local.f32 [loc0], x0

// Now load x1:
x1 = x[1]

// Spill y0 to make room:
st.local.f32 [loc1], y0
y1 = y[1]

// Continue...
z0 = x0 + y0    // Load spilled values
st.local.f32 [loc2], z0  // Spill result
z0 = x1 + y1
z[0] = z0
z[1] = load(loc2)
```

**Multiple loads/stores per variable = ~10x slower.**

## Strategies to Reduce Spilling

### 1. Use Smaller Data Types

```cuda
// BAD: float (4 bytes)
float x = data[i];

// GOOD: half (2 bytes) if precision allows
half x = data[i];
```

### 2. Reduce Thread Register Usage

```cuda
// BAD: Multiple large arrays per thread
float a[256], b[256], c[256];

// GOOD: Process in tiles
__shared__ float tile[256];
```

### 3. Enable Loop Unrolling

```cuda
// Hint to compiler
#pragma unroll
for (int i = 0; i < 4; i++) { ... }
```

### 4. Use Shared Memory for Large Arrays

```cuda
// BAD: Large local array
float local_array[1024];

// GOOD: Shared memory
__shared__ float shared_array[1024];
```

### 5. Separate Large Structures

```cuda
// BAD: Large struct in registers
struct LargeStruct { float a[16]; };

// GOOD: Pointer to global memory
float *data = large_struct_ptr;
```

### 6. Occupancy vs Register Pressure

There's a trade-off:

| Registers/Thread | Concurrent Threads | Register Pressure |
|-----------------|-------------------|------------------|
| 16 | 64 | Low |
| 32 | 32 | Medium |
| 64 | 16 | High (may spill) |

**Strategy**: If spilling occurs, reduce registers/thread to increase occupancy.

## Controlling Register Usage

### NVCC Flags

```bash
# Maximum registers per thread
nvcc -maxrregcount 32 kernel.cu

# Or use launch bounds
__global__
__launch_bounds__(256, 4)  // maxThreadsPerBlock, minBlocksPerMultiprocessor
void kernel(...) { ... }
```

### Launch Bounds

```cuda
// Hint to compiler
// Maximum 256 threads per block
// Minimum 4 blocks per SM
__global__
__launch_bounds__(256, 4)
void kernel(...) {
    // Compiler knows max threads = 256
    // Can allocate registers accordingly
}
```

### `volatile` for Critical Variables

```cuda
volatile float x;  // Compiler less likely to optimize away
```

## Diagnosing Spilling

### nvcc Verbose Output

```bash
nvcc -Xptxas -v source.cu
```

Output:
```
ptxas info: 8 bytes stack frame, 0 bytes spill stores, 0 bytes spill loads
ptxas info: Function '_Z6kernel1Pfi'
  72 bytes stack frame, 4 bytes spill stores, 4 bytes spill loads
```

### Nsight Compute

- Shared Memory section shows spill stats
- Warp Stall reasons include "lg sync" for local memory

### CUDA-MEMCHECK

```bash
compute-sanitizer ./a.out
```

Detects global memory accesses that should be registers.

## Impact on Occupancy

### Occupancy Formula

```
Occupancy = Active Warps / Max Warps per SM
```

### Register Pressure Effect

High registers/thread → Fewer active warps → Lower occupancy

```
Registers: 16 → Threads: 64 → Occupancy: 100%
Registers: 32 → Threads: 32 → Occupancy: 50%
Registers: 64 → Threads: 16 → Occupancy: 25% (+ spilling)
```

**Key insight**: Sometimes lower occupancy + no spilling = faster than higher occupancy + spilling.

## Related

- [[Registers (GPU)]] — What spilling replaces
- [[Local Memory]] — Where spilled data goes
- [[Shared Memory]] — Alternative for large arrays
- [[Occupancy]] — Trade-off with register pressure
