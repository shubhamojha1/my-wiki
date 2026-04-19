---
title: "Redis"
type: entity
tags: [databases, in-memory, cache, key-value]
created: 2026-04-20
sources: [redis-cluster-architecture]
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

## Deployment Modes

### Standalone
Single Redis instance, no replication

### Master-Slave
One master, multiple read replicas

### Sentinel
Adds monitoring and automatic failover

### Cluster
Active-passive with hash-based sharding