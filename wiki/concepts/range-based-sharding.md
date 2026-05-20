---
title: "Range-Based Sharding"
type: concept
tags: [database, sharding, partitioning]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-sharding]
---

# Range-Based Sharding

**Range-based sharding** partitions data into contiguous key ranges, with each shard responsible for one range. Routing is a simple comparison: given a key K and a range table, find the shard whose `[min, max)` bracket contains K.

## How It Works

```
Shard 0: user_id ∈ [1,      100,000)
Shard 1: user_id ∈ [100000, 200,000)
Shard 2: user_id ∈ [200000, 300,000)
...

Query: user_id = 150,432 → Shard 1
Query: user_id BETWEEN 90,000 AND 110,000 → Shard 0 + Shard 1 only
```

Ranges don't need to be equal-sized; a shard can be split when it grows too large.

## Pros and Cons

| Pro | Con |
|-----|-----|
| Range queries hit one (or a few) shards — no scatter-gather | Sequential keys (timestamps, auto-increment IDs) funnel all new writes to the last shard (**hot shard**) |
| Simple, human-readable routing table | Uneven data distribution unless carefully managed |
| Easy to understand, debug, and tune | Shard splits require data migration |
| Natural for time-series partitioning (shard per month/year) | Requires range table management (unlike hash sharding) |

## The Hot Shard Problem

If the shard key is `created_at` or a monotonically increasing ID, all new writes land on the same shard — nullifying the benefit of sharding for writes. Solutions:

- **Compound shard key**: `(region, created_at)` — spreads writes across regions.
- **Random suffix**: Append a random digit to distribute writes across N sub-shards.
- **Hash-based on time bucket**: Hash `MONTH(created_at)` — even distribution + range at month granularity.

## Real-World Examples

| System | Range sharding use |
|--------|-------------------|
| **MongoDB** | Range-based chunks moved by the balancer between shards |
| **HBase / Bigtable** | Row key ranges partitioned into tablets/regions |
| **Cassandra** | Uses consistent hashing by default, but supports range-like ordering per partition |
| **CockroachDB** | Range-based replication groups (ranges ~64 MB); automatic splitting and rebalancing |

## Comparison

| Strategy | Range queries | Write hotspots | Distribution |
|----------|--------------|----------------|-------------|
| Range-based | Efficient (few shards) | Likely on seq keys | Uneven |
| Hash-based | Scatter-gather | Unlikely | Even |
| Consistent hashing | Scatter-gather | Unlikely | Even |

## Related Concepts

- [[Database Sharding]] — general sharding concepts
- [[Shard Key]] — the column whose value determines the range
- [[Hash-Based Sharding]] — uniform distribution at the cost of range query efficiency
- [[Cross-Shard Query]] — required when a range spans multiple shards
- [[Consistent Hashing]] — hash ring variant that minimizes resharding cost
