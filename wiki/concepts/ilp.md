---
title: "ILP"
type: concept
tags: [gpu, cuda, performance, parallelism, pipelining]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# ILP (Instruction-Level Parallelism)

The ability to execute multiple independent instructions simultaneously by reordering them to avoid stalls. A key technique for maximizing GPU performance.

## Overview

### The Problem

Sequential code has dependencies that force order:

```cuda
a = x + y;   // Instruction 1
b = a * 2;   // Instruction 2 (depends on 1)
c = b + z;   // Instruction 3 (depends on 2)
```

**Result**: 3 instructions must execute in order.

### The ILP Solution

Reorder independent instructions to expose parallelism:

```cuda
// Original sequential code
x0 = x[0];
y0 = y[0];
z0 = x0 + y0;

// With ILP optimization
x0 = x[0];
x1 = x[1];
y0 = y[0];
y1 = y[1];
z0 = x0 + y0;  // Can overlap with loads above
z1 = x1 + y1;
```

**Result**: Parallel loads and computes.

## How ILP Works

### Instruction Scheduling

The compiler/hardware reorders instructions to:
1. **Fill latency bubbles**: Put independent work during wait times
2. **Expose parallelism**: Execute multiple operations per cycle
3. **Hide dependencies**: Schedule around true dependencies

### Memory Latency Hiding

```cuda
// Naive: Sequential with stalls
load x[0];         // 300 cycles waiting for memory
compute x[0] * 2;  // Can't start until load done

// With ILP: Overlap memory and compute
load x[0];         // Start load 0
load x[1];         // Start load 1 (while 0 is pending)
load x[2];         // Start load 2
compute x[0] * 2;  // By now, x[0] loaded
compute x[1] * 2;  // x[1] ready
compute x[2] * 2;  // x[2] ready
```

### Arithmetic Latency Hiding

```cuda
// Before: Chain of dependent operations
a = x + y;      // 4 cycles
b = a * 2;      // 4 cycles (wait for a)
c = b + z;      // 4 cycles (wait for b)
result = c / 2; // 4 cycles (wait for c)
Total: 16 cycles

// After: Parallel chains
t0_0 = x[0] + y[0];  // Chain 0
t0_1 = t0_0 * 2;
t0_2 = t0_1 + z;

t1_0 = x[1] + y[1];  // Chain 1 (independent!)
t1_1 = t1_0 * 2;
t1_2 = t1_1 + z;

Total: ~8 cycles (2 chains in parallel)
```

## ILP in CUDA

### The Compilation Transformation

```cuda
// Source code (appears sequential)
z0 = x[0] + y[0];
z1 = x[1] + y[1];
```

**Compiles to** (simplified assembly):
```
LD R1, [x+0]    ; Load x[0]
LD R2, [y+0]    ; Load y[0]
LD R3, [x+4]    ; Load x[1] (while R1, R2 pending)
LD R4, [y+4]    ; Load y[1]
ADD R5, R1, R2  ; Compute z[0] (R1, R2 ready)
ADD R6, R3, R4  ; Compute z[1] (R3, R4 ready)
```

### Warp-Level ILP

Within a warp, compiler can reorder independent instructions:

```cuda
// Sequential appearance:
float a = data[i];
float b = a * 2.0f;
float c = b + 1.0f;
float d = c * 3.0f;

// Compiler sees:
// - b depends on a
// - c depends on b
// - d depends on c
// => Must be sequential (within thread)
```

### Instruction Dual-Issue

Modern GPUs can issue multiple instructions per cycle:

```cuda
// Kepler: 2 dispatchers per scheduler
// Can issue 2 independent instructions simultaneously
LD.f32 R1, [x+0]    ; Floating load
LD.f32 R2, [x+4]    ; Floating load (parallel!)
```

## ILP vs Thread-Level Parallelism

### ILP (Fine-Grained)

- Reorder instructions within a thread
- Exploits instruction overlap
- Limited by dependencies

### TLP (Coarse-Grained)

- Run multiple threads simultaneously
- GPU has 1000s of threads
- Hides latency via thread switching

### When to Use Each

| Scenario | Prefer |
|----------|--------|
| Many independent instructions | ILP |
| Memory-bound code | TLP |
| Compute-bound, long dependency chains | ILP |
| Limited threads (low occupancy) | ILP |

## Maximizing ILP

### Technique 1: Unroll Loops

```cuda
// Before: Single iteration
for (int i = 0; i < n; i++) {
    a[i] = b[i] + c[i];
}

// After: 4x unroll
for (int i = 0; i < n; i += 4) {
    a[i]   = b[i]   + c[i];
    a[i+1] = b[i+1] + c[i+1];
    a[i+2] = b[i+2] + c[i+2];
    a[i+3] = b[i+3] + c[i+3];
}
// More instructions to schedule → better ILP
```

### Technique 2: Separate Computation

```cuda
// Before: Chain
a = load_x();
a = a * 2;
a = a + y;
a = a * z;

// After: Interleave with other loads
t1 = load_x();      // Primary load
t2 = load_x2();     // Independent load
t3 = t1 * 2;        // Primary compute
t4 = t2 * 2;        // Independent compute
t5 = t3 + y;         // Continue primary chain
t6 = t4 + y2;       // Continue independent chain
```

### Technique 3: Multiple Independent Accumulators

```cuda
// Before: Single accumulator
float sum = 0;
for (int i = 0; i < n; i++) {
    sum += data[i];  // Chain dependency!
}

// After: Four independent accumulators
float s0 = 0, s1 = 0, s2 = 0, s3 = 0;
for (int i = 0; i < n; i += 4) {
    s0 += data[i];
    s1 += data[i+1];
    s2 += data[i+2];
    s3 += data[i+3];
}
float sum = s0 + s1 + s2 + s3;
```

### Technique 4: Software Pipelining

```cuda
// Before: Sequential stages
for (int i = 0; i < n; i++) {
    load(data[i]);      // Stage 1
    compute(data[i]);   // Stage 2
    store(data[i]);     // Stage 3
}

// After: Overlapped stages (software pipeline)
for (int i = 0; i < n; i++) {
    load(data[i]);         // Current load
    compute(data[i-1]);    // Previous compute
    store(data[i-2]);      // Store from 2 iterations ago
}
```

## ILP Limits

### Dependencies Limit ILP

```cuda
// Cannot parallelize: chain of dependent ops
result = a + b;
result = result * result;
result = result + result;
result = result * result;
result = result + result;
// Only 1 instruction per cycle
```

### Register Pressure

More ILP → More simultaneous values → More registers:

```cuda
// High ILP: Many live variables
t1 = a + b;   // t1 live
t2 = c + d;   // t2 live
t3 = e + f;   // t3 live
t4 = g + h;   // t4 live
result = (t1 + t2) * (t3 + t4);
// Need 4+ registers simultaneously
```

**Trade-off**: High ILP may cause register spilling.

## Measuring ILP

### Occupancy vs ILP

| ILP | Occupancy | Performance |
|-----|-----------|-------------|
| High | Low | Can be good |
| Low | High | Needs more warps |
| Low | Low | Poor performance |

### Profiling

```bash
# Nsight Compute
ncu --metrics sm__throughput.avg.pct_of_peak_sustained \
               warp__IPC_total.sum \
    ./a.out
```

### Warp Execution Efficiency

```bash
ncu --metrics sm__warps_executed.avg.pct_of_peak_sustained \
               sm__IPC.sum \
    ./a.out
```

## Practical Guidelines

1. **Write clear code first** — Compiler is often smarter than you
2. **Unroll small loops** — Exposes more ILP
3. **Avoid long dependency chains** — Break into stages
4. **Consider multiple accumulators** — For reductions
5. **Profile before optimizing** — Measure, don't guess
6. **Watch register pressure** — High ILP can cause spilling

## Related

- [[Instruction Dependencies]] — What limits ILP
- [[Warp Scheduler]] — Hardware that exploits ILP
- [[Occupancy]] — Trade-off with ILP
- [[Register Spilling]] — When ILP exceeds resources
