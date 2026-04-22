---
title: "Sort-Merge Join"
type: concept
tags: [database, query, join, algorithm]
created: 2026-04-23
---

# Sort-Merge Join

**Sort-merge join** is a join algorithm that sorts both tables on the join key, then merges them in a single pass.

## How It Works

1. **Sort**: Sort both tables on join key
2. **Merge**: Scan sorted tables, find matching ranges

## Characteristics

- **Sorted input**: If pre-sorted, skip sort phase
- **Range handling**: Good for inequality joins
- **Memory**: Need memory for sorting

## Complexity

- Sort: O(N log N + M log N)
- Merge: O(N + M)
- Total: O(N log N + M log N)

## Trade-offs

- **Pros**: Good for pre-sorted data, efficient merge
- **Cons**: Sorting cost if not pre-sorted

## Related

- [[Nested Loop Join]] — Simpler but slower
- [[Hash Join]] — Usually faster for equijoin
- [[External Sort]] — Sorting algorithm used