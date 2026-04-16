---
title: "SIMT"
type: concept
tags: [gpu, cuda, parallelism, threading]
created: 2026-04-16
sources: [cs179_2026_lec02.pdf]
---

# SIMT

Single Instruction, Multiple Threads. A parallelism model used by [[CUDA]] that extends [[SIMD]] with thread-level abstraction.

## How SIMT Differs from SIMD

| Aspect | SIMD | SIMT |
|--------|------|------|
| Register sets | Single (vector) | Multiple (one per thread) |
| Memory access | Vector loads/stores | Parallel memory access |
| Control flow | No divergence | Divergence allowed (with cost) |
| Programming model | Explicit vectors | Threads (more natural) |

## Key Properties

1. **Single instruction, multiple register sets**: Each thread has its own registers, enabling independent data
2. **Parallel memory access**: Threads can access different memory addresses simultaneously
3. **Multiple flow paths allowed**: `if` statements work but cause [[Warp Divergence]]

## Warp Execution

SIMT threads are grouped into **warps** of 32 threads. All threads in a warp execute the same instruction in lockstep.

## Why SIMT Over SIMD?

- More natural programming model (think in threads, not vectors)
- Handles irregular access patterns better
- Allows branching (with performance caveat)
- Hardware hides memory latency via massive thread count

## Related

- [[SIMD]] — The underlying vector instruction concept
- [[Warp Divergence]] — Performance issue when threads diverge
- [[Streaming Multiprocessor]] — Hardware that executes SIMT
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — Source lecture
