---
title: "Streaming Multiprocessor"
type: concept
tags: [gpu, hardware, nvidia]
created: 2026-04-16
sources: [cs179_2026_lec02.pdf]
---

# Streaming Multiprocessor (SM)

The fundamental processing unit in NVIDIA GPUs. Each SM can run at least 128 threads concurrently.

## Overview

A GPU contains approximately 100 Streaming Multiprocessors, each containing:
- Multiple processor cores (128 in modern Turing/Pascal architectures)
- Single instruction unit (shared program counter)
- Warp schedulers
- Cache and shared memory

## SM Architecture

```
Streaming Multiprocessor (SM)
 ├── Processor Core 1 ─┐
 ├── Processor Core 2 ─┤
 ├── Processor Core N ──┼── (share 1 instruction unit)
 │                     │
 ├── Warp Scheduler   │
 ├── Register File    │
 ├── L1 Cache         │
 └── Shared Memory    │
```

All processor cores within an SM must execute the exact same instruction at any given time.

## Warp Scheduling

The SM uses **Warp Schedulers** to manage execution:
- Assigns warps (32 threads) to execution units
- Switches between warps to hide memory latency
- Can run multiple warps concurrently

## Historical Context

| Architecture | Year | Cores/SM |
|--------------|------|----------|
| Fermi | 2010 | 32 |
| Pascal | 2016 | 128 |
| Turing | 2018 | 128 |

## Block-to-SM Assignment

When a kernel launches:
1. Blocks are assigned to available SMs
2. Each SM divides its blocks into warps
3. Warps are scheduled for execution

## Related

- [[Warp Divergence]] — Issue when threads in a warp take different paths
- [[SIMT]] — Execution model SMs use
- [[GPU Computing]] — Hardware context
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — Source lecture
