---
title: "Instruction Dependencies"
type: concept
tags: [gpu, cuda, performance, pipelining, parallelism]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# Instruction Dependencies

Constraints between instructions that force sequential execution. Understanding dependencies is critical for writing efficient GPU code.

## Overview

### What is an Instruction Dependency?

An instruction dependency exists when:
1. Instruction B uses result of instruction A
2. Instruction B must wait for A to complete

### Why Dependencies Matter

Dependencies limit **instruction-level parallelism (ILP)**:
- More dependencies → fewer instructions can execute simultaneously
- Dependencies create pipeline stalls
- Dependencies force sequential portions in code

## Types of Dependencies

### 1. Data Dependencies (True Dependency)

Instruction B reads data that instruction A writes.

```cuda
// RAW: Read After Write
a = x + y;     // Instruction A
b = a * 2;     // Instruction B depends on A's result
c = b + z;     // Instruction C depends on B
```

**Visual**:
```
[  a = x+y  ]──┐
               ├──►[ b = a*2 ]──┐
               │                 ├──►[ c = b+z ]
               └──►[ ... other work can happen ... ]
```

### 2. Anti Dependencies (Write After Read)

Instruction B writes data that instruction A reads.

```cuda
a = x + y;     // A reads x
x = b + c;     // B writes x (after A read it)
```

**Note**: This is a dependency on the *old* value of x.

### 3. Output Dependencies (Write After Write)

Both instructions write the same variable.

```cuda
x = a + b;     // A writes x
x = c + d;     // B writes x (after A)
```

**Note**: Must preserve order of writes.

## Dependency Chains

### Sequential Chain

```cuda
acc += x[0];  // Chain of 4 dependencies
acc += x[1];  // Each must wait for previous
acc += x[2];  // This is BAD for parallelism
acc += x[3];
```

**Problem**: Each addition depends on previous → 4 sequential steps.

### Parallel-Friendly Rewrite

```cuda
// Compute in parallel
t0 = x[0] + x[1];  // Independent
t1 = x[2] + x[3];  // Independent
result = t0 + t1;   // Final combine
```

**Result**: 2 parallel steps → 2x faster (ignoring overhead).

## Dependency Distance

### Short vs Long Dependencies

**Short dependency**:
```cuda
a = x + y;
b = a * 2;  // Immediate dependency
c = b + z;
```

**Long dependency**:
```cuda
a = x + y;     // Compute expensive result
...            // Many cycles later
...            // More independent work
...            // ...
result = a * 2;  // But we still need a's value
```

### Hiding Dependencies

**With ILP**: Long dependencies can be hidden if other instructions fill the gap.

**Without ILP**: Pipeline stalls waiting for dependency.

## Loop-Carried Dependencies

### Sequential Loop

```cuda
// Sequential (depends on previous iteration)
for (int i = 1; i < n; i++) {
    a[i] = a[i-1] + b[i];  // Dependency on a[i-1]
}
```

**Cannot parallelize directly**.

### Parallel Patterns

#### 1. Reduction (Safe to Parallelize)

```cuda
// No loop-carried dependency
float sum = 0;
for (int i = 0; i < n; i++) {
    sum += a[i];  // Each iteration independent (except on sum)
}
// Need atomic or reduction pattern
```

#### 2. Scan (Sequential to Parallel)

```cuda
// Naive: a[i] = a[i-1] + a[i-2]
// Parallel: use work-efficient parallel scan
```

#### 3. Stencil (Parallelizable)

```cuda
// Each output depends only on input
for (int i = 0; i < n; i++) {
    out[i] = (in[i-1] + in[i] + in[i+1]) / 3.0;
}
// Can parallelize: each i independent
```

## Dependency Analysis in CUDA

### Identifying Dependencies

```cuda
// Example: Vector addition
z[i] = x[i] + y[i];

// Thread i reads x[i], y[i]
// Thread i writes z[i]
// Thread i does NOT read/write other indices
// Therefore: threads are INDEPENDENT!
// Can execute in parallel!
```

### When Threads Share Data

```cuda
// PROBLEM: Thread 0 writes, Thread 1 reads
if (threadIdx.x == 0) {
    shared_data = data;
}
__syncthreads();
if (threadIdx.x == 1) {
    value = shared_data;  // Depends on thread 0!
}
```

### Cross-Warp Dependencies

```cuda
// Threads in DIFFERENT warps of SAME BLOCK
// Can use __syncthreads() to synchronize
__syncthreads();

// Threads in DIFFERENT BLOCKS
// Cannot synchronize directly!
// Use atomic operations or multiple kernels
```

## Breaking Dependencies

### Technique 1: Temporary Variables

```cuda
// BEFORE: Chain dependency
result = a + b;
result = result * c;
result = result / d;
result = result + e;

// AFTER: Independent computation
t1 = a + b;
t2 = c * d;
t3 = t1 / t2;
result = t3 + e;
```

### Technique 2: Instruction Reordering

```cuda
// BEFORE: Sequential loads
x0 = x[0];
y0 = y[0];
z0 = x0 + y0;

// AFTER: Parallel loads (compiler can do this)
x0 = x[0];
x1 = x[1];
y0 = y[0];
y1 = y[1];
z0 = x0 + y0;
z1 = x1 + y1;
```

### Technique 3: Loop Unrolling

```cuda
// BEFORE: Sequential iterations
for (int i = 0; i < 4; i++) {
    a[i] = a[i] * 2;
}

// AFTER: Parallelize iterations
a[0] = a[0] * 2;
a[1] = a[1] * 2;
a[2] = a[2] * 2;
a[3] = a[3] * 2;
// Compiler can schedule these in parallel
```

### Technique 4: Multiple Accumulators

```cuda
// BEFORE: One accumulator (sequential)
float sum = 0;
for (int i = 0; i < n; i++) {
    sum += data[i];  // Chain dependency!
}

// AFTER: Multiple independent accumulators
float sum0 = 0, sum1 = 0, sum2 = 0, sum3 = 0;
for (int i = 0; i < n; i += 4) {
    sum0 += data[i];
    sum1 += data[i+1];
    sum2 += data[i+2];
    sum3 += data[i+3];
}
float sum = sum0 + sum1 + sum2 + sum3;  // Final combine
```

## Performance Impact

### Dependency Chains and Latency

| Chain Length | Impact |
|--------------|--------|
| 1-2 cycles | Pipeline can hide |
| 5-10 cycles | May need ILP |
| 10+ cycles | Needs parallelism |

### Latency Hiding

GPU warp scheduler hides latency by switching to other ready warps:

```
Warp 1: [Instruction A (10 cycles)][B depends on A][...]
         ↑
         └─ Warp 2 runs during A's latency
```

**Key**: Need enough independent warps to hide latency.

## Compiler Optimizations

### What Compilers Do

1. **Reorder independent instructions**
2. **Rename registers to break false dependencies**
3. **Unroll loops to expose parallelism**
4. **Schedule instructions around latencies**

### Viewing Generated Code

Use Godbolt to see compiler output:

```cuda
// Source
float example(float a, float b, float c) {
    float t1 = a + b;
    float t2 = c * 2.0f;
    return t1 + t2;
}
```

**Compiler might**:
- Reorder: compute `c*2` while waiting for `a+b`
- Use FMA: `fma(a, 1.0, b) + c*2`

## Related

- [[ILP]] — Exploiting instruction-level parallelism
- [[Warp Scheduler]] — Hardware that hides latency
- [[Occupancy]] — Need enough parallelism
- [[CUDA Synchronization]] — Managing dependencies
