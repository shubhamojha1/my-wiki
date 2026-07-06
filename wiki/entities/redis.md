---
title: "Redis"
type: entity
tags: [databases, in-memory, cache, key-value]
created: 2026-04-20
sources: [redis-cluster-architecture, "https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

Redis is an in-memory data structure store, used as database, cache and message broker.

## Key Characteristics

- **In-memory**: Data stored in RAM for extreme speed
- **Key-Value Store**: Supports strings, hashes, lists, sets, sorted sets
- **Persistence**: Optional disk persistence (RDB/AOF)
- **Replication**: Built-in Master-Slave replication
- **Cluster**: Redis Cluster for distributed scaling

## Redis Cluster

[[Redis Cluster]] provides:
- Automatic data sharding across nodes
- High availability via slave replication
- Automatic failover when masters fail

## Rate Limiting Use

Redis is a common backing store for a [[Distributed Rate Limiter]] because it provides fast shared state for counters and [[Token Bucket]] fields. A gateway can store a per-client bucket as a Redis hash containing `tokens` and `last_refill`, with `EXPIRE` used to clean up idle buckets.

The important correctness point is atomicity. A naive flow that reads with `HMGET`, calculates locally, and writes with `MULTI/EXEC` can still race because the read occurs outside the transaction. Redis Lua scripts execute atomically and can wrap the entire read-calculate-update decision.

## Deployment Modes

### Standalone
Single Redis instance, no replication

### Master-Slave
One master, multiple read replicas

### Sentinel
Adds monitoring and automatic failover

### Cluster
Active-passive with hash-based sharding

### Active-Active Geo Distribution
Multi-region deployment using [[Active-Active Geo Distribution]] — all nodes accept writes, CRDT-based conflict resolution, zero cross-region write latency. Available in Redis Cloud and Redis Software.
