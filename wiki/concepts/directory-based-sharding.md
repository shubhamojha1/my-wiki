---
title: "Directory-Based Sharding"
type: concept
tags: [database, sharding, lookup]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-sharding]
---

# Directory-Based Sharding

**Directory-based sharding** uses an explicit lookup table (the **directory** or **shard map**) that maps each shard key (or range/tenant) to a specific shard. Every query first consults the directory to find the correct shard, then routes to it.

## Architecture

```
Client
  │
  ↓ key = "tenant_456"
[Shard Directory Service]
  key       → shard
  tenant_001 → Shard-A
  tenant_002 → Shard-A
  tenant_456 → Shard-C   ← returned
  tenant_789 → Shard-B
  │
  ↓ route to Shard-C
[Shard-C]
```

The directory is typically stored in a highly-available metadata store (Redis, etcd, ZooKeeper, or a dedicated metadata DB).

## Pros and Cons

| Pro | Con |
|-----|-----|
| Maximum flexibility — any key to any shard | Directory lookup adds one extra network hop per query |
| Move data between shards without clients knowing | Directory is a potential single point of failure (mitigate: replicate) |
| Handle uneven tenants — move large tenants to dedicated shards | Directory can become a bottleneck at high QPS (mitigate: cache aggressively) |
| Zero reshuffling — change the map entry, not the data | Hot directory entries require cache invalidation on shard moves |

## Directory Caching

Direct lookup on every request is too slow. Solutions:
- **Client-side cache**: Cache key→shard locally with a TTL; stale on shard moves.
- **Connection pool per shard**: Cache connections; reconnect on MOVED error.
- **Read-through cache** (Redis): Directory in Redis, cached for seconds.

## Comparison with Other Strategies

| Strategy | Directory needed | Resharding cost | Range queries |
|----------|-----------------|----------------|--------------|
| Directory-based | Yes | Low (update map only) | Configurable |
| Hash-based | No | High (all keys remap) | Scatter-gather |
| Range-based | Implicit (range table) | Medium | Efficient |
| Consistent hashing | No | Low (1/N remapped) | Scatter-gather |

## Use Cases

- **Multi-tenant SaaS**: Each tenant maps to a shard; large tenants get their own; migrations update the directory.
- **Data gravity migrations**: Move a customer's data to a shard geographically close to them by updating one map entry.
- **Custom co-location**: Ensure related data (user + orders) lives on the same shard via directory rules.

## Related Concepts

- [[Database Sharding]] — general sharding concepts
- [[Hash-Based Sharding]] — deterministic, no directory needed
- [[Shard Key]] — the key looked up in the directory
- [[Cross-Shard Query]] — still possible if directory routes to multiple shards
