---
title: "Hash-Based Sharding"
type: concept
tags: [database, sharding, hashing]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-sharding]
---

# Hash-Based Sharding

**Hash-based sharding** routes each row to a shard by applying a hash function to the shard key and taking the result modulo the number of shards:

```
shard_id = hash(shard_key) % N
```

The hash function distributes keys pseudo-uniformly, so each shard receives roughly 1/N of the data regardless of the key's semantic value or distribution.

## Example

```
Users: IDs 1 – 10,000. N = 3 shards.

user_id=1001  → hash(1001) % 3 = 2  → Shard 2
user_id=2002  → hash(2002) % 3 = 0  → Shard 0
user_id=3003  → hash(3003) % 3 = 1  → Shard 1
```

Any query for a specific `user_id` knows which shard to hit in O(1).

## Pros and Cons

| Pro | Con |
|-----|-----|
| Even distribution (no hotspots by default) | Range queries (`WHERE id BETWEEN 100 AND 200`) must scatter to all shards |
| Simple routing: one arithmetic operation | Adding or removing shards remaps ~all keys (`mod N` changes) — use consistent hashing to mitigate |
| No central directory needed | Poor locality: adjacent keys may be on different shards |
| Predictable performance | Shard key choice is permanent without full data migration |

## The Resharding Problem

Adding a shard (N → N+1) changes most keys' shard assignment:

```
Before: shard = hash(k) % 3
After:  shard = hash(k) % 4
```

Most records must move. **[[Consistent Hashing]]** solves this by organizing the hash space as a ring — adding a node only remaps the fraction of keys between the new node and its predecessor.

## Choosing a Good Shard Key

- **High cardinality**: Many distinct values → even spread.
- **No hotspot**: Avoid timestamps or sequential IDs if writes concentrate on current values.
- **Immutable**: Changing a key requires moving the row to a new shard.
- **Query-aligned**: Frequently joined tables should shard on the same key so related rows co-locate.

## Comparison with Other Sharding Strategies

| Strategy | Distribution | Range queries | Resharding cost |
|----------|-------------|---------------|----------------|
| Hash-based | Even | Scatter-gather | High (full remap) |
| Range-based | Uneven (hotspots) | Efficient | Medium |
| Consistent hashing | Even | Scatter-gather | Low (1/N remapped) |
| Directory-based | Configurable | Configurable | Low (update map) |

## Related Concepts

- [[Consistent Hashing]] — hash ring variant that minimizes resharding
- [[Database Sharding]] — general sharding concepts
- [[Shard Key]] — the column passed to the hash function
- [[Hash Slot]] — Redis Cluster's variant (CRC16 % 16384)
- [[Cross-Shard Query]] — scatter-gather problem for range queries
