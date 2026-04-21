---
title: "Shared Memory (GPU)"
type: concept
tags: [gpu, cuda, memory, optimization]
created: 2026-04-22
sources: [cs179_2026_lec06]
---

# Shared Memory (GPU)

Shared memory is a fast on-chip memory that is shared among threads within a CUDA block. It serves as a software-managed cache for frequently accessed data.

## Key Properties

- **Latency**: ~5ns (comparable to registers)
- **Scope**: Block-level (threads in same block can access)
- **Size**: Typically 48KB per block
- **Lifetime**: Block duration

## Bank Structure

- Divided into 32 banks
- Striped layout: consecutive 128-byte regions split across 32 banks
- Optimal access: each thread accesses a different bank (32-way parallelism)

## Bank Conflicts

When multiple threads in a warp access the same bank, access serializes:
- 2-way conflict: 2× slowdown
- 4-way conflict: 4× slowdown
- 32-way conflict: 32× slowdown

**Solution**: Add padding (1 value every 64 values) to shift bank access patterns.

## Use Cases

- [[Matrix Transpose (GPU)]]: Intermediate storage between global memory transfers
- [[Tiling]]: Cache frequently accessed data
- Reducing global memory bandwidth

## Pattern for Matrix Operations

```
1. Load from global memory (coalesced)
2. Store to shared memory (with padding)
3. __syncthreads()
4. Read from shared memory (transposed)
5. __syncthreads()
6. Store to global memory (coalesced)
```

## Related Concepts

- [[Bank Conflicts]]
- [[Tiling]]
- [[Memory Coalescing]]
- [[Matrix Transpose (GPU)]]
- [[Memory Hierarchy (GPU)]]
