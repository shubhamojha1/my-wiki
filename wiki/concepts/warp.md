---
title: "Warp (CUDA)"
type: concept
tags: [gpu, cuda, threading, hardware]
created: 2026-04-22
sources: [cs179_2026_lec06]
---

# Warp (CUDA)

A warp is a group of 32 adjacent threads that execute in lockstep on NVIDIA GPUs.

## Key Properties

- **Size**: Always 32 threads (fixed by hardware)
- **Execution**: All threads in a warp execute the same instruction simultaneously
- **Divergence**: If threads take different paths, they serialize (see [[Warp Divergence]])

## Warp in Matrix Operations

In [[Matrix Transpose (GPU)]]:
- Each warp processes 32 threads
- Threads in a warp should read/write adjacent floats for coalesced access
- 32 warps handle one 64×64 tile (2048 threads total per tile)

## Memory Access

For optimal performance:
- All 32 threads should access contiguous memory addresses
- 128 bytes per warp transaction (32 threads × 4 bytes/float)
- Misaligned access wastes bandwidth

## Related Concepts

- [[Warp Divergence]]
- [[Warp Scheduler]]
- [[Streaming Multiprocessor]]
- [[SIMT]]
- [[Memory Coalescing]]
- [[Matrix Transpose (GPU)]]
