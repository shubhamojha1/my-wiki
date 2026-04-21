---
title: "Matrix Transpose (GPU)"
type: concept
tags: [gpu, cuda, memory, optimization]
created: 2026-04-22
sources: [cs179_2026_lec06]
---

# Matrix Transpose (GPU)

Matrix transpose on GPUs is a classic optimization problem: achieving memory-copy speeds for reorganizing matrix layout.

## The Challenge

- Input and output have different optimal access patterns
- Column-major storage makes naive transpose suboptimal
- Must balance global memory coalescing with transposed output

## Solution: Tiling with Shared Memory

### Step 1: Tile the Matrix
- Divide matrix into 64×64 tiles
- Process each tile independently

### Step 2: Load with Coalescing
- All 32 threads in a warp read adjacent floats
- 128 bytes per transaction (optimal for most GPUs)

### Step 3: Store to Shared Memory with Padding
- Add 1 value padding every 64 values
- Prevents [[Bank Conflicts]]

### Step 4: Read Transposed from Shared Memory
- Each thread reads from transposed position in shared memory

### Step 5: Store with Coalescing
- Write transposed data with optimal global memory access

## Performance Target

Goal: match memory copy bandwidth (not compute-bound)

## Related Concepts

- [[Tiling]]
- [[Memory Coalescing]]
- [[Shared Memory (GPU)]]
- [[Bank Conflicts]]
- [[Warp (CUDA)]]
