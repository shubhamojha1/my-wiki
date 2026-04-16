---
title: "Prefix Sum"
type: concept
tags: [gpu, algorithms, parallel-computing, cuda]
created: 2026-04-16
sources: [cs179_2026_lec03.pdf]
---

# Prefix Sum

Also known as *scan*. An operation that computes running sums of array elements.

## Definition

For an input array `x` of length `n`, the prefix sum (exclusive scan) produces:

```
output[i] = sum(x[0:i])  for i in [0, n)
```

**Example**:
```
Input:  [1, 2, 1, 0, -1, 4, 10, 20]
Output: [0, 1, 3, 4, 4, 3, 7, 17]
```

## Variants

- **Exclusive scan**: `output[i]` excludes `input[i]`
- **Inclusive scan**: `output[i]` includes `input[i]`

## Parallel Algorithm

Blelloch's parallel prefix sum (1990) achieves O(log n) depth using O(n) processors.

### Work Complexity
- Serial: O(n)
- Parallel: O(n log n) total work, O(log n) depth

### GPU Implementation
O(N) time with:
- 2*(n-1) additions
- n-1 swaps

## Applications

- Radix sort
- Quicksort (stream compaction)
- Stream processing
- Histogram computation
- Solving PDEs
- Database operations (running totals)

## Why It Matters

Prefix sum is a fundamental parallel primitive. It demonstrates:
- How sequential algorithms can be parallelized
- Trade-offs between work and depth
- Tree-reduction patterns

## Related

- [[GPU Computing]] — Where parallel prefix sum runs
- [[CS179 Recitation 1 - GPU Overview and Prefix Sum]] — Source recitation
