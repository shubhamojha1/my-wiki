---
title: "GPU Computing"
type: concept
tags: [gpu, parallel-computing, hardware]
created: 2026-04-16
sources: [cs179_2026_lec01.pdf]
---

# GPU Computing

General-purpose computing on GPUs (GPGPU). The practice of leveraging Graphics Processing Units for non-graphics computational tasks, particularly those with high parallelism.

## Motivation

GPUs evolved from fixed-function graphics pipelines to programmable shader-based systems. Hardware became powerful enough to function as "mini-supercomputers" capable of general computation.

## Architecture Comparison

### CPU Design
- Few cores (8 or fewer) optimized for sequential execution
- Complex branch prediction, out-of-order execution
- Large caches, low memory latency tolerance
- High context-switching penalty (~20,000 cycles)

### GPU Design
- Thousands of simple cores optimized for data parallelism
- Simple control flow, high thread count hides memory latency
- Massive thread count enables near-zero context-switch cost
- SIMD (Single Instruction, Multiple Data) paradigm

## Strengths

- **Massive parallelism**: Run ~20,000 simultaneous threads vs ~8 CPU threads
- **Throughput over latency**: Optimized for aggregate throughput
- **SIMD efficiency**: Single instruction operates on multiple data elements
- **Cost efficiency**: Floating-point performance per dollar exceeds CPUs

## Weaknesses

- **Sequential code**: Poor performance for branching, irregular access patterns
- **Memory transfer overhead**: CPU↔GPU copies are slow (must be amortized)
- **Debugging difficulty**: Limited tools, non-deterministic execution
- **Precision concerns**: Some applications need higher precision than GPUs provide

## Common Applications

- Deep learning / neural network training
- Scientific simulations (CFD, molecular dynamics)
- Ray tracing and rendering
- Signal processing
- Cryptocurrency mining
- PDE solving

## Related

- [[CUDA]] — Primary platform for GPU computing (NVIDIA)
- [[Kernel (GPU)]] — Parallel functions executed on GPU
- [[CS 179: Introduction to GPU Programming - Lecture 1]] — Course introducing these concepts
