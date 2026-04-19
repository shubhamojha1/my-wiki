---
title: "Redis Cluster"
type: entity
tags: [redis, distributed-systems, cluster, sharding]
created: 2026-04-20
sources: [redis-cluster-architecture]
---

Redis Cluster is an active-passive cluster implementation for automatic sharding and high availability.

## Architecture

- **Master nodes**: Handle client requests and data storage
- **Slave nodes**: Replicate masters, promote on failure
- **Hash slots**: 16,384 slots distributed across masters

## Node Communication

Each node uses two TCP ports:
1. **Client port**: For client connections (e.g., 6379)
2. **Gossip port**: For node-to-node communication (client port + 10000)

## Cluster Modes

### 6-Node Cluster
- 3 masters + 3 slaves (one slave per master)
- Each master on separate server

### 3-Node Cluster (Cross-node)
- 3 masters + 3 slaves on different servers
- Each server runs 2 Redis instances
- Masters replicate to slaves on other nodes

## Hash Slot Distribution

With 3 masters:
- Master 1: slots 0-5500
- Master 2: slots 5501-11000
- Master 3: slots 11001-16383

## Failover Behavior

1. Master fails or becomes unreachable
2. Other masters vote via gossip protocol
3. Failed master's slave promoted to master
4. Failed master rejoins as slave