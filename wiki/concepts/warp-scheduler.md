---
title: "Warp Scheduler"
type: concept
tags: [gpu, hardware, scheduling, latency, parallelism]
created: 2026-04-17
sources: [cs179_2026_lec05.pdf]
---

# Warp Scheduler

Hardware units that manage execution of warps, hiding latency by rapidly switching between ready warps. Critical for GPU throughput.

## Overview

### What is a Warp Scheduler?

A warp scheduler is hardware that:
1. Monitors warps for readiness
2. Selects ready warps for execution
3. Switches between warps to hide latency

### Key Properties

- **Fast context switch**: ~1-2 cycles (1ns at 1GHz)
- **Per-SM**: Multiple schedulers per streaming multiprocessor
- **Multiple dispatch**: Can issue multiple instructions per cycle

## Warp Scheduler Architecture

### GK110 (Kepler) Architecture

```
Streaming Multiprocessor
├── Warp Scheduler 1 ──► Dispatch Unit 1 ──► Execution Units
│                       └──► Dispatch Unit 2 ──► Execution Units
├── Warp Scheduler 2 ──► Dispatch Unit 1 ──► Execution Units
│                       └──► Dispatch Unit 2 ──► Execution Units
├── Warp Scheduler 3 ──► Dispatch Unit 1 ──► Execution Units
│                       └──► Dispatch Unit 2 ──► Execution Units
└── Warp Scheduler 4 ──► Dispatch Unit 1 ──► Execution Units
                        └──► Dispatch Unit 2 ──► Execution Units
```

**Stats**: 4 schedulers, 2 dispatchers each = 8 issue slots per SM per clock.

### Dispatch Units

Each dispatcher can issue one instruction per cycle:
- **Dispatch 1**: First independent instruction
- **Dispatch 2**: Second independent instruction

This enables **dual-issue** for independent instructions.

## Scheduling Algorithm

### Round-Robin Priority

```cuda
// Warp states tracked by scheduler
enum WarpState {
    READY,      // Can execute next instruction
    WAITING,    // Waiting for memory/dependency
    STALLED,    // Long-latency operation pending
    COMPLETED   // Finished execution
};
```

### Scheduling Decision

```
Every clock cycle:
1. For each scheduler:
   a. Scan all warps assigned to this SM
   b. Find first READY warp
   c. Issue its next instruction
   d. Warp becomes WAITING/STALLED
```

### Context Switch Cost

| Switch Type | Cost |
|-------------|------|
| Warp → Warp (same SM) | ~1-2 cycles |
| CPU thread switch | ~100-1000 cycles |

**GPU advantage**: Register file is partitioned per warp — no register save/restore needed!

## Latency Hiding

### The Core Mechanism

GPU hides latency by running other warps while one waits:

```
Time ──────────────────────────────────────────────────────►

Warp 1: [Load 300 cycles........][Compute][...]
         ↑                       ↑
         └───────────────────────┘
              Warp 2 runs here

Warp 2:        [Load 300 cycles........][Compute][...]
                         ↑             ↑
                         └─────────────┘
                              Warp 3 runs here

Warp 3:                   [Load 300 cycles...][Compute][...]
```

### Latency Budget

For each latency type, need enough warps to hide it:

| Latency Type | Cycles | Warps Needed (1 warp/4 cycles) |
|--------------|--------|-------------------------------|
| Global memory | ~300 | 75 |
| L2 cache | ~200 | 50 |
| Shared memory | ~34 | 9 |
| FP32 add | ~4 | 1 |

### Warps Needed Calculation

```
Warps needed = Latency (cycles) / Issue rate

For memory (300 cycles, 1 issue/4 cycles):
  300 / 4 = 75 warps needed
```

## Multi-Issue Capability

### Independent Instruction Issue

Each scheduler can issue up to 2 independent instructions per cycle:

```cuda
// These can dual-issue:
a = x + y;  // Instruction 1: Add
b = z * 2;  // Instruction 2: Mul (independent!)

// Cannot dual-issue:
a = x + y;  // Instruction 1
b = a * 2;  // Instruction 2 (depends on 1)
```

### Kepler Dual-Issue Examples

| Instruction Pair | Can Dual-Issue? |
|-----------------|-----------------|
| FMA + FMA | ✓ |
| FMA + LD (float) | ✓ |
| FMA + FMA (same warp) | ✗ (dependency) |
| LD + LD | ✗ (memory bandwidth) |

## Warp State Machine

### State Transitions

```
READY ───►[Issue]───► WAITING
  ▲                      │
  │                      │
  │            [Result Ready]
  │                      │
  └────[Next Instruction]┘
```

### Warp Stall Reasons

| Reason | Description |
|--------|-------------|
| Instruction fetch | Waiting for next instruction |
| Execution dependency | Waiting for result |
| Memory dependency | Waiting for memory load/store |
| Register dependency | Waiting for register |
| Sync | Waiting for __syncthreads() |

## Occupancy and Scheduling

### Low Occupancy = Problems

With few warps:
1. Scheduler runs out of ready warps
2. Execution units sit idle
3. Latency cannot be hidden

### High Occupancy = Better Scheduling

With many warps:
1. Always have ready warps
2. Scheduler keeps units busy
3. Latency fully hidden

### Scheduling Efficiency

```
Occupancy vs Throughput:

100% occupancy ─────────────────────────► Peak throughput
                                          (or near it)

50% occupancy  ─────────────────────────► May still be good
                                          (if ILP high)

10% occupancy ─────────────────────────► Poor throughput
                                          (units idle)
```

## SM Resources for Scheduling

### Resources per SM

| Resource | Limit | Affects |
|----------|-------|---------|
| Registers | 65536 (32-bit) | Threads per SM |
| Shared Memory | 48-128 KB | Blocks per SM |
| Warps | 64 max | Scheduling flexibility |
| Threads | 2048 max | Scheduling flexibility |

### Scheduling with Limited Resources

```cuda
// High register usage per thread
__global__
__launch_bounds__(256, 4)  // 256 threads, 4 blocks max
void highRegKernel(...) {
    float r0, r1, r2, r3, r4, r5, r6, r7;  // 8 registers
    // ...
}

// Result: Fewer threads, fewer warps → harder to schedule
```

## Practical Implications

### For Kernel Design

1. **Keep warps ready**: Have independent work for each warp
2. **Minimize stalls**: Reduce memory dependencies
3. **Balance occupancy**: Trade-off with register pressure
4. **Use full warps**: Don't waste scheduling slots

### Code Patterns That Help

```cuda
// Good: Independent work in each thread
__global__
void independentKernel(float *data) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    data[i] = data[i] * 2.0f;  // Independent
}

// Bad: Dependencies between threads
__global__
void dependentKernel(float *data) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i > 0) {
        data[i] = data[i-1] * 2.0f;  // Depends on previous!
    }
}
```

### Warp Convergence

GPU attempts to keep threads in same warp together:

```cuda
// Divergent code hurts scheduling
if (threadIdx.x < 16) {
    // Warp 0 only
} else {
    // Warp 0 stalls
}
```

**Best**: Keep all threads in warp on same path.

## Profiling Scheduling

### Nsight Compute Metrics

```bash
ncu --metrics sm__warps_active.avg.pct_of_peak_sustained \
               sm__warps_stalled_long_dmem.avg.pct_of_peak_sustained \
               sm__dispatch_stalls_sync_throttle.pct_of_sustained \
    ./a.out
```

### Key Metrics

| Metric | Good | Bad |
|--------|------|-----|
| Warps Active | >50% | <20% |
| Stalls (memory) | <30% | >50% |
| Dispatch Stalls | <10% | >30% |

## Related

- [[Occupancy]] — Warps per SM
- [[ILP]] — Instruction-level parallelism
- [[Instruction Dependencies]] — What causes stalls
- [[Memory Bandwidth]] — Common stall reason
