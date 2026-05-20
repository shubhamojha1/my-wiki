---
title: "Counting Bloom Filter"
type: concept
tags: [data-structure, probabilistic, set-membership]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-bloom-filters]
---

# Counting Bloom Filter

A **Counting Bloom Filter (CBF)** extends the standard [[Bloom Filter]] by replacing each single bit with a small integer counter (typically 3–4 bits). This enables **deletion**, which a standard Bloom Filter cannot support.

## Why Standard Bloom Filters Can't Delete

In a standard Bloom filter, insert sets k bits to 1. If you try to "delete" by clearing those k bits, you risk clearing bits that were also set by *other* elements — creating false negatives (telling you something isn't in the set when it is). The Bloom filter invariant (no false negatives) would be violated.

## How Counting Bloom Filter Works

Replace each bit with a counter:

```
Standard BF:   [0][1][0][1][1][0][1][0]    (bit array)
Counting BF:   [0][2][0][1][3][0][1][0]    (counter array)
```

| Operation | Action |
|-----------|--------|
| **Insert** element x | Compute `h_1(x)…h_k(x)`, **increment** each counter |
| **Delete** element x | Compute `h_1(x)…h_k(x)`, **decrement** each counter |
| **Query** element x | If all k counters > 0 → "probably present"; if any = 0 → "definitely absent" |

## Memory Trade-off

Standard Bloom filter: 1 bit per position  
Counting Bloom filter: 3–4 bits per position → 3–4× more memory

With 4-bit counters: max count per position = 15. Counter overflow (inserting the same element >15 times into the same bucket) would corrupt state. 4-bit counters are sufficient for typical cardinalities (overflow probability ≈ 10⁻¹⁵ with a well-chosen filter size).

## Pros and Cons

| Pro | Con |
|-----|-----|
| Supports deletion | 3–4× more memory than standard Bloom filter |
| Dynamic set membership | Still has false positives (same rate as Bloom filter) |
| Reversible: insert then delete leaves the filter unchanged | Counter overflow corrupts if same element inserted too many times |

## Alternatives

- **Cuckoo Filter**: Also supports deletion; more memory-efficient than CBF; O(1) lookup, O(1) delete.
- **XOR Filter**: Immutable but very compact.
- **Quotient Filter**: Cache-friendly, supports merge and resize.

## Related Concepts

- [[Bloom Filter]] — the standard filter CBF extends
- [[Deduplication Store]] — alternative for exact membership (no false positives)
