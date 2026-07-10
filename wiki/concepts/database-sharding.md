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

## Partitioning vs. Sharding

The terms are often used loosely, but the distinction is scope: **[[Partitioning]]** divides a large table into smaller pieces *within a single database instance* — horizontally (splitting rows) or vertically (splitting columns, see [[Vertical Partitioning]]). **Sharding** extends the same idea *across multiple independent machines*, where each shard is a separate database holding a subset of the data. Every sharding strategy is a form of partitioning; not every partitioning scheme involves sharding.

## Cross-Shard Transactions

[[Cross-Shard Query]] covers the read-side cost of spanning shards. The write side is a separate problem: a single logical transaction that must update rows on more than one shard cannot use a normal local database transaction. Three ways to handle it:

- **Avoid it by design** — choose a shard key ([[Shard Key]]) that keeps transactionally-related data on the same shard, so the problem never arises for the common case.
- **[[Two-Phase Commit (2PC)|Two-Phase Commit]]** — guarantees atomicity across shards, but blocks all participants until the slowest one responds and is not partition-tolerant.
- **[[Saga Pattern]]** — breaks the transaction into local steps with compensating actions, trading strict atomicity/isolation for availability. The common production choice when 2PC's blocking behavior is unacceptable.
- **Accept eventual consistency** — let the multi-shard state settle asynchronously (e.g. via events) when strict consistency isn't actually required for that workflow.

## Modern Database Solutions

Several databases handle sharding automatically rather than requiring the application to implement a strategy by hand:

| System | Approach |
|---|---|
| **Cassandra** | Consistent hashing with virtual nodes ([[Consistent Hashing]]) |
| **DynamoDB** | Hashes the partition key and auto-splits partitions as they grow |
| **MongoDB** | Range-based chunks with an automatic balancer (see [[Range-Based Sharding]]) |
| **Vitess** | Sharding middleware layer in front of MySQL |
| **Citus** | Sharding extension for PostgreSQL |

## Interview Approach

Avoid reaching for sharding prematurely — "a well-tuned single database can get you surprisingly far." Establish a specific bottleneck first (storage capacity exceeded, write throughput limited, or read throughput limited), then walk through: identify the bottleneck, propose a shard key aligned with actual access patterns, pick a distribution strategy, and name the trade-offs it introduces (expensive cross-shard queries chief among them).

## Related

- [[Partitioning]] — General concept of dividing datasets
- [[Consistent Hashing]] — Minimizes remapping when shards change
- [[Shard Key]] — The attribute used to distribute data
- [[Saga Pattern]] — Cross-shard transaction consistency without blocking
- [[Two-Phase Commit (2PC)]] — Blocking alternative for cross-shard atomicity
