---
title: "Warp Divergence"
type: concept
tags: [gpu, cuda, performance]
created: 2026-04-16
sources: [cs179_2026_lec02.pdf]
---

# Warp Divergence

A performance issue in [[SIMT]] architectures where threads within a warp take different execution paths due to branching (e.g., `if` statements).

## The Problem

All 32 threads in a warp must execute the same instruction. When threads encounter different conditions:

```cuda
if (threadIdx.x % 2 == 0) {
    // Path A
} else {
    // Path B
}
```

Both paths execute sequentially, with inactive threads receiving no-ops.

## How It Works

```
Instruction 1: if (condition)
               ↓
    Thread 0-15: Path A executes
    Thread 16-31: Wait (no-op)

Instruction 2: else clause
               ↓
    Thread 0-15: Wait (no-op)
    Thread 16-31: Path B executes
```

## Performance Impact

- Threads that take one branch wait while others execute
- Parallelism reduced to sequential execution within the warp
- Should be avoided when possible

## Strategies to Reduce Divergence

1. **Restructure conditionals**: Move divergent code to block level (different blocks = no divergence)
2. **Predicated execution**: Use masks instead of branches when possible
3. **Avoid fine-grained branching**: Coalesce similar operations

## Modern GPUs

Modern GPUs (Turing, Ampere) allow unlimited warp divergence with no branch limit, but performance still suffers. The key is minimizing divergence rather than eliminating it entirely.

## Related

- [[SIMT]] — The architecture where divergence occurs
- [[Streaming Multiprocessor]] — Hardware that executes warps
- [[CS 179: Intro to SIMD and GPU Internals - Lecture 2]] — Source lecture
