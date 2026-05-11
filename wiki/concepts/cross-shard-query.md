---
title: "Cross-Shard Query"
type: concept
tags: [database, sharding, query]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Cross-Shard Query

A **cross-shard query** is a query that needs to access data from multiple shards, typically involving joins or aggregations across shards.

## Challenges

- **Performance**: Data must be gathered from multiple servers and combined
- **Complexity**: Joins across shards are computationally expensive
- **Consistency**: Ensuring consistent snapshots across shards is hard
- **Network overhead**: Data transfer between nodes

## Mitigation Strategies

- **Data denormalization** — duplicate related data within each shard
- **Query federation** — scatter-gather pattern (send to all shards, merge results)
- **Application-level joining** — fetch from each shard, combine in app
- **Shard-aligned data** — keep related data in the same shard

## Related

- [[Database Sharding]] — General concept
- [[Data Rebalancing]] — Related operational challenge
