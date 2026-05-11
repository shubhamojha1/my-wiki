---
title: "Counting Bloom Filter"
type: concept
tags: [data-structure, probabilistic, set-membership]
created: 2026-05-11
sources: [algomaster-bloom-filters]
---

# Counting Bloom Filter

A **Counting Bloom Filter** extends the standard [[Bloom Filter]] by replacing each bit with a counter, enabling element **deletion**.

## How It Works

- Each position in the array is a small counter (typically 3–4 bits)
- **Insert**: increment all k counters
- **Delete**: decrement all k counters
- **Check**: all k counters > 0 → element probably present

## Trade-offs

| Pro | Con |
|-----|-----|
| Supports deletion | More memory (counters vs bits) |
| Dynamic set friendly | Counter overflow risk (small counters) |
| Reversible operations | Still has false positives |

## Use Cases

- Dynamic sets where elements are added and removed
- Sliding window membership (recent items expire)
- Cache eviction tracking

## Related

- [[Bloom Filter]] — Standard probabilistic membership filter
