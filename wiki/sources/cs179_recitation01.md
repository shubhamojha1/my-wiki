---
title: "CS179 Recitation 1 - GPU Overview and Prefix Sum"
type: source
tags: [gpu, cuda, prefix-sum, nvidia]
created: 2026-04-16
sources: [cs179_2026_lec03.pdf]
---

# CS179 Recitation 1 - GPU Overview and Prefix Sum

## Details

- **Date**: 2025-04-04
- **Instructor**: Sam Foxman (Head TA)
- **Topics**: VS Code remote development, GPU hardware, prefix sum algorithm

## Summary

Recitation covering practical GPU setup (VS Code remote SSH) and introduction to the prefix sum (scan) algorithm as a GPU parallelization example.

## GPU Hardware Evolution

| GPU | Architecture | Notes |
|-----|--------------|-------|
| RTX 4090 | Ada Lovelace | Previous generation flagship |
| RTX 5090 | Blackwell | Current generation, referenced in NVIDIA whitepaper |

## Prefix Sum (Scan)

An operation computing running sums of array elements.

**Example** (exclusive scan):
```
Input:  [1, 2, 1, 0, -1, 4, 10, 20]
Output: [0, 1, 3, 4, 4, 3, 7, 17]
```

Where `output[i] = sum(input[0:i])`

### CPU Approach
Sequential loop, O(N) time complexity.

### GPU Approach
O(N) parallel algorithm with:
- 2*(n-1) additions
- n-1 swaps

Reference: NVIDIA's parallel scan paper (https://developer.download.nvidia.com/compute/cuda/2_2/sdk/website/projects/scan/doc/scan.pdf)

## Exponential Moving Average

Mentioned as a counter-example: an algorithm that is NOT easily parallelizable without expansion.

## VS Code Remote Development

SSH remote development setup for accessing Barr lab GPU machine.

## Related

- [[Prefix Sum]] — Parallel algorithm concept
- [[GPU Computing]] — Broader context
