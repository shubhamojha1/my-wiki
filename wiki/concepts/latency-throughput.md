---
title: "Latency vs Throughput"
type: concept
tags: [gpu, hardware, performance, cpu]
created: 2026-04-16
sources: [cs179_2026_lec04.pdf]
---

# Latency vs Throughput

Two fundamental performance metrics that characterize hardware design. CPUs optimize for latency; GPUs optimize for throughput.

## Definitions

### Latency

The **delay** from initiating an operation to receiving its result.

```
Time between request and response
Single operation completion time
```

### Throughput

The **maximum rate** at which work can be processed.

```
Operations per unit time
Sustained processing rate
```

## CPU vs GPU Philosophy

### CPU Design: Latency-Optimized

CPUs are designed to minimize latency:
- Fast single-thread performance
- Deep branch prediction
- Out-of-order execution
- Large caches
- Complex control logic

**Goal**: Complete each instruction as fast as possible.

### GPU Design: Throughput-Optimized

GPUs are designed to maximize throughput:
- Many simple cores
- Massive parallelism hides latency
- Simple control logic
- High memory bandwidth
- ILP and TLP exploited

**Goal**: Complete many operations per unit time.

## Quantified Comparison

### CPU (Modern Desktop)

| Metric | Value |
|--------|-------|
| Clock | ~3 GHz (3 clocks/ns) |
| Memory Latency | ~100+ ns |
| Arithmetic Latency | ~1+ ns |
| Cores | 4-16 |
| Threads | 8-32 |

### GPU (Modern)

| Metric | Value |
|--------|-------|
| Clock | ~1 GHz (1 clock/ns) |
| Memory Latency | ~300+ ns |
| Arithmetic Latency | ~10+ ns |
| Cores | ~10,000 |
| Threads | ~20,000+ |

## Why GPUs Have Higher Latency

### Single Operation Cost

| Component | CPU | GPU |
|-----------|-----|-----|
| Clock cycle | Faster (3 GHz) | Slower (1 GHz) |
| Arithmetic | ~1 ns | ~10 ns |
| Control overhead | Higher | Lower |

GPUs have slower individual operations because:
1. Simpler cores (less optimization per op)
2. More parallel (transistors go to cores, not optimization)
3. Longer pipelines (for throughput, not latency)

## How GPUs Hide Latency

### The Key Insight

GPU latency is **hidden** by running other threads while waiting.

```
Time ──────────────────────────────────────────────────────►

CPU:  [====Op1====][====Op2====][====Op3====]
      ◄─100ns─►   ◄─100ns─►   ◄─100ns─►

GPU:  [Op1][Op2][Op3]...[Op1000][Op1001]...
       ▲                      ▲
       └─ Latency (300ns) ────┘
      Many threads overlap latency
```

### Warp Scheduling

With 1000s of threads:
1. Thread warp hits memory load
2. Scheduler switches to another ready warp
3. While warp 2 runs, warp 1's data arrives
4. Scheduler switches back to warp 1

**Result**: Average throughput stays high even with high latency.

## The Latency Hiding Window

### Available Parallelism

```
Latency (cycles) × Throughput (ops/cycle) = Parallelism needed

GPU: 300 cycles × 32 ops/cycle = 9,600 threads needed
```

GPUs have 10,000+ threads, so latency is hidden.

### CPU Problem

```
CPU: 100 cycles × 1 op/cycle = 100 threads needed
CPU has: 8 threads
Result: Latency NOT fully hidden
```

## Practical Implications

### CPU Best For

| Workload | Why CPU Wins |
|----------|-------------|
| Single-threaded | Deep optimization per thread |
| Branching code | Better branch prediction |
| Random memory access | Larger caches, better latency |
| Low parallelism | Can't utilize 10,000 threads |

### GPU Best For

| Workload | Why GPU Wins |
|----------|-------------|
| Data-parallel | Thousands of parallel operations |
| Dense matrix ops | High arithmetic intensity |
| SIMD-friendly | Warps execute together |
| Throughput-focused | Batch processing |

## Comparing Performance

### Speed vs Throughput

| Metric | Formula | Unit |
|--------|---------|------|
| Latency | Single operation time | ns, cycles |
| Throughput | Operations / time | GFLOPS, GB/s |
| Speedup | Latency_old / Latency_new | ratio |
| Efficiency | Throughput / Power | GFLOPS/W |

### When to Optimize for Latency

1. Interactive applications
2. Real-time systems
3. Single-request latency (web serving)
4. When parallelism unavailable

### When to Optimize for Throughput

1. Batch processing
2. Large datasets
3. Data-parallel algorithms
4. Training/inference

## Throughput-Only Bottleneck

### GPU is I/O Limited

For H200:
- Compute: 900 TFLOPS (FP16 tensor)
- Memory: 4.8 TB/s

```
Arithmetic Intensity needed:
900 TFLOPS / 4.8 TB/s = 187.5 FLOPs/byte
```

**Challenge**: Most algorithms don't have this intensity.

**Result**: GPU is often waiting for memory.

## Optimization Strategies

### For Latency-Bound Code

1. Cache aggressively
2. Branch prediction hints
3. Prefetching
4. Single-thread optimization

### For Throughput-Bound Code

1. Increase parallelism
2. Batch operations
3. Hide memory latency with compute
4. Optimize memory coalescing

## The Roofline Connection

```
                    │
     Peak Compute   │─────── Flat (compute-bound)
                    │      ╱
                    │     ╱  Diagonal
                    │    ╱   (memory-bound)
                    │   ╱
                    │  ╱
                    │ ╱
                    └──────────────────────►
                         Intensity
```

- **Below diagonal**: Memory-bound, optimize memory access
- **Above diagonal**: Compute-bound, optimize compute

## Related

- [[Memory Bandwidth]] — The throughput bottleneck
- [[Computational Intensity]] — Ratio of compute to memory
- [[GPU Computing]] — Why GPUs prioritize throughput
- [[Occupancy]] — Thread count for latency hiding
