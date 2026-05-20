---
title: "Hash Slot"
type: concept
tags: [redis, sharding, partitioning, cluster]
created: 2026-04-20
updated: 2026-05-20
sources: [redis-cluster-architecture]
---

# Hash Slot

A **hash slot** is [[Redis Cluster]]'s fixed-granularity unit for key distribution. The entire key space is divided into 16,384 slots, and each master node owns a contiguous or non-contiguous range of slots.

## Key Space Division

Redis Cluster always uses exactly **16,384 hash slots** (2^14). The slot for a given key is:

```
slot = CRC16(key) % 16384
```

Redis uses a specific CRC16 variant (CCITT-FALSE polynomial) defined in the cluster specification.

## Slot Assignment

Slots are assigned to master nodes during cluster setup and can be migrated at runtime:

| Cluster Size | Slots per Node (approx.) |
|-------------|--------------------------|
| 3 masters | ~5,461 |
| 6 masters | ~2,730 |
| 10 masters | ~1,638 |

## How Clients Use Slots

1. Client requests key `foo`
2. Client computes `slot = CRC16("foo") % 16384 = 7638`
3. Client checks its slot-to-node routing table → slot 7638 is on node B
4. Client sends command directly to node B
5. If wrong (after resharding), node B replies with `MOVED 7638 <new-node-ip>:<port>`
6. Client redirects and updates its cache

## Scaling with Hash Slots

- **Add a node**: Move a subset of slots from existing nodes to the new node — only those keys move, no full resharding
- **Remove a node**: Move its slots to remaining nodes before shutdown
- **Compare to consistent hashing**: Hash slots are simpler to implement and easier to reason about at the cost of fixed granularity (16,384 max nodes)

## Hash Tags

`{user}.profile` and `{user}.settings` use the same hash tag `user` → same slot → can be used in multi-key operations (`MGET`, `EVAL`) which require co-location.

## Related Concepts

- [[Redis Cluster]] — the system that uses hash slots
- [[Consistent Hashing]] — alternative approach to key distribution
- [[Database Sharding]] — the general concept
- [[Data Rebalancing]] — moving slots between nodes
