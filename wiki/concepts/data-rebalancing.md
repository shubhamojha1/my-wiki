---
title: "Data Rebalancing"
type: concept
tags: [database, sharding, maintenance]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Data Rebalancing

**Data rebalancing** is the process of redistributing data across shards when the distribution becomes uneven (a "skewed" shard) or when shards are added or removed.

## Why Rebalancing Is Needed

- **Data growth skew** — some shards grow faster than others
- **Hot spots** — certain shards receive disproportionate query load
- **Cluster scaling** — adding or removing nodes requires redistribution
- **Access pattern changes** — usage shifts over time

## Challenges

- Data movement is expensive (network + disk I/O)
- Must minimize downtime or query impact
- Maintaining consistency during migration
- Rate-limiting migration to avoid overwhelming the cluster

## Techniques

- **Consistent hashing** — minimizes keys moved when topology changes
- **Virtual nodes** — smaller granularity for finer rebalancing
- **Background migration** — move data in batches with rate limiting
- **Weighted shards** — assign more capacity to faster-growing shards

## Related

- [[Database Sharding]] — General concept
- [[Consistent Hashing]] — Minimizes remapping during rebalancing
- [[Cross-Shard Query]] — Related operational challenge
