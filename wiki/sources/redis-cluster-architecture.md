---
title: "Redis Cluster: Architecture, Replication, Sharding and Failover"
type: source
tags: [redis, distributed-systems, caching]
created: 2026-04-20
sources: []
---

Article by Sajal Jain (2019) explaining Redis Cluster architecture, replication, sharding and failover mechanisms.

## Evolution Path

1. **Redis Master-Slave** - Simple replication, single point of failure
2. **Redis Sentinel** - Master monitoring and failover
3. **Redis Cluster** - Automatic sharding and high availability

## Key Concepts Covered

- Redis Master/Slave replication
- Redis Sentinel for failover
- Redis Cluster active-passive architecture
- Hash slot partitioning (16,384 slots)
- Failover behavior
- 6-node vs 3-node cluster modes

## Architecture Summary

Redis Cluster uses:
- Master and slave nodes
- Hash partitioning into 16,384 key slots
- One slave per master for failover
- Automatic slave promotion on master failure

## Related Entities
- [[Redis]] in-memory data store
- [[Redis Cluster]] distributed implementation