---
title: "Range-Based Sharding"
type: concept
tags: [database, sharding, partitioning]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Range-Based Sharding

**Range-based sharding** distributes data based on contiguous ranges of the shard key (e.g., ID ranges, date ranges).

## How It Works

**Example**: Shard 1 stores IDs 1–10000, Shard 2 stores IDs 10001–20000, etc.

## Pros and Cons

| Pro | Con |
|-----|-----|
| Efficient range queries (single shard) | Uneven distribution (hot shards) |
| Simple to understand and debug | Can require manual splitting |
| Good for time-series data | Sequential keys cause append-only writes to last shard |

## When to Use

- Time-series data (e.g., shard by month)
- Sequential IDs with predictable access patterns
- Range scans are the primary query pattern

## Related

- [[Database Sharding]] — General concept
- [[Shard Key]] — The attribute defining range boundaries
- [[Hash-Based Sharding]] — Alternative strategy
