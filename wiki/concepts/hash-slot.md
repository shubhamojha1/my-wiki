---
title: "Hash Slot"
type: concept
tags: [redis, sharding, partitioning]
created: 2026-04-20
sources: [redis-cluster-architecture]
---

Hash slot is Redis Cluster's mechanism for distributing keys across master nodes.

## Key Space

Redis Cluster divides key space into **16,384 hash slots** (2^14).

## Distribution

Slots are distributed evenly across masters:
- 3 masters: ~5461 slots each
- 6 masters: ~2730 slots each

## Slot Calculation

```
slot = CRC16(key) % 16384
```

Where CRC16 is a specific CRC algorithm used by Redis.

## Use Case

Client routes requests to correct node based on hash slot, enabling:
- Horizontal scaling via new nodes
- Data locality within cluster
- Parallel processing