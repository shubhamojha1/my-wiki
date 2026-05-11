---
title: "Hash-Based Sharding"
type: concept
tags: [database, sharding, hashing]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Hash-Based Sharding

**Hash-based sharding** distributes data by applying a hash function to the shard key and using the result modulo the number of shards.

## How It Works

```
shard = hash(shard_key) % number_of_shards
```

**Example**: `hash(user_id) % 2` distributes users across 2 shards.

## Pros and Cons

| Pro | Con |
|-----|-----|
| Even data distribution | Adding shards reshuffles all data (without consistent hashing) |
| Simple to implement | Range queries hit all shards |
| Good for random access patterns | Cannot route range predicates to a single shard |

## Related

- [[Database Sharding]] — General concept
- [[Consistent Hashing]] — Minimizes remapping when shards change
- [[Shard Key]] — The attribute passed to the hash function
