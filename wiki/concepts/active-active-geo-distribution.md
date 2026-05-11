---
title: "Active-Active Geo Distribution"
type: concept
tags: [redis, replication, multi-region, crdt]
created: 2026-05-11
sources: [redis-data-replication]
---

# Active-Active Geo Distribution

**Active-Active Geo Distribution** is a multi-region replication model where every node accepts reads and writes, processing them locally rather than routing to a single primary.

## How It Works

- All nodes accept both reads and writes
- Changes synchronize across regions continuously
- [[CRDT|CRDTs]] resolve most write conflicts automatically
- For String types, falls back to last-writer-wins (LWW)

## Key Properties

- **No cross-region write latency**: Writes processed locally
- **Always-on**: Every node serves live traffic (no standby)
- **Automatic conflict resolution**: CRDT-based merge
- **Resilient**: Nodes resync when coming back online

## Compared to Active-Passive

| Aspect | Active-Active | Active-Passive |
|--------|---------------|----------------|
| Write locations | All regions | Single primary |
| Failover | Instant (always on) | Requires promotion |
| Latency | Low (local writes) | Cross-region writes |
| Complexity | Higher (CRDTs, data type selection) | Lower |

## Availability

Available in Redis Cloud and Redis Software.

## Related

- [[Data Replication]] — General concept
- [[CRDT]] — Automatic merge data structures
- [[Merge Replication]] — Offline variant of independent writes
- [[Redis]] — Implementation platform
