---
title: "Database Sharding"
type: concept
tags: [database, sharding, scaling]
created: 2026-05-11
sources: [algomaster-sharding]
---

# Database Sharding

**Database sharding** is a horizontal scaling technique that splits a large database into smaller, independent pieces called **shards** distributed across multiple servers.

## Core Idea

Each shard holds a subset of data and operates independently. A single server only deals with its own shard, enabling the system to scale beyond the limits of a single machine.

## How It Works

1. **Sharding key** — column(s) determining data placement (e.g., `user_id`)
2. **Data partitioning** — split data across shards using a chosen strategy
3. **Shard mapping** — map shard keys to shard locations
4. **Shard management** — maintain consistency and integrity across shards
5. **Query routing** — intercept queries and direct to correct shard(s)

## Benefits

- **Performance** — reduced load per server
- **Scalability** — add shards as data grows
- **High availability** — single shard failure doesn't bring down the system
- **Geo-distribution** — place shards closer to users
- **Cost** — commodity hardware instead of vertical scaling

## Challenges

- [[Cross-Shard Query]] — joins and aggregations across shards are expensive
- [[Data Rebalancing]] — uneven data growth requires redistribution
- Complexity in planning and management
- Data consistency across shards

## Sharding Strategies

- [[Hash-Based Sharding]] — hash function distributes data evenly
- [[Range-Based Sharding]] — ranges of values (e.g., ID 1–10000)
- [[Geo-Based Sharding]] — geographic region placement
- [[Directory-Based Sharding]] — lookup table mapping keys to shards

## Related

- [[Partitioning]] — General concept of dividing datasets
- [[Consistent Hashing]] — Minimizes remapping when shards change
- [[Shard Key]] — The attribute used to distribute data
