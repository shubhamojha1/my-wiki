---
title: "Cross-Shard Query"
type: concept
tags: [database, sharding, query, distributed-systems]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-sharding]
---

# Cross-Shard Query

A **cross-shard query** is a query that must access data spread across multiple shards — typically involving joins, aggregations, or WHERE clauses that don't align with the shard key. It is the primary operational cost of [[Database Sharding]].

## The Problem

```
Shard 1: users 1–1M      Shard 2: users 1M–2M      Shard 3: users 2M–3M
```

Query: "Find all orders with total > $500 across all users" must hit all three shards.

## Challenges

| Challenge | Description |
|-----------|-------------|
| **Latency** | Must wait for the slowest shard (fan-out to N shards) |
| **Partial failures** | If one shard is down, the query may fail or return incomplete results |
| **Distributed joins** | Join across shards requires data to be shipped to one node — expensive |
| **Consistent snapshots** | Obtaining a consistent view across shards at the same timestamp is difficult without distributed transactions |
| **Aggregation complexity** | COUNT, SUM, AVG must be computed per-shard and merged |

## Scatter-Gather Pattern

The most common approach:

```
Coordinator → parallel queries → Shard 1, Shard 2, Shard 3
                             ← results
Coordinator aggregates and returns final result
```

Works well for simple aggregations; expensive for joins.

## Mitigation Strategies

| Strategy | How | Trade-off |
|----------|-----|-----------|
| **Shard by query-aligned key** | Choose shard key matching most common queries | Re-sharding needed for new access patterns |
| **Data denormalization** | Embed related data in each shard | Data duplication, write amplification |
| **Read replicas** | Direct cross-shard queries to replicas | Still expensive; doesn't eliminate the fan-out |
| **Application-level join** | Fetch from each shard, join in application | Memory and bandwidth cost |
| **Global tables** | Keep small reference tables on every shard | Works for low-write, frequently-joined data |

## Related Concepts

- [[Database Sharding]] — the partitioning strategy that creates this problem
- [[Shard Key]] — choosing a good shard key minimizes cross-shard queries
- [[Data Denormalization]] — a mitigation strategy
- [[Map Reduce]] — distributed aggregation pattern
