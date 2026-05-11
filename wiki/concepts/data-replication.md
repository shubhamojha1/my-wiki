---
title: "Data Replication"
type: concept
tags: [distributed-systems, replication, availability]
created: 2026-05-11
sources: [redis-data-replication]
---

# Data Replication

**Data replication** is the process of keeping copies of the same data synchronized across multiple locations, ensuring availability, consistency, and performance.

## Replication vs Backup

| Aspect | Replication | Backup |
|--------|------------|--------|
| Purpose | Availability during incidents | Recovery after incidents |
| Timing | Continuous, ongoing | Periodic snapshots |
| Granularity | Transaction-level | Point-in-time |
| Restore target | Replica takes over immediately | Must restore from snapshot |

## How It Works

1. **Initial state**: Full snapshot/baseline of primary database
2. **Change capture**: Via CDC (transaction log), timestamps, or triggers
3. **Apply to replicas**: Changes propagated synchronously or asynchronously

## Partial Resynchronization

If the link between primary and replica breaks, only missed commands replay from the replication log. If commands expired from the backlog, a full resync occurs (primary sends complete snapshot).

## Benefits

- **Reliability & DR**: Replicas hold recent data; [[RPO and RTO]] driven by replication strategy
- **Performance**: Replicas handle reads, primary focuses on writes
- **Geo-distribution**: Serve data from regionally close replicas
- **Engineering efficiency**: Automated sync instead of manual scripts

## Challenges

- [[Replication Lag]] — Stale reads in async setups
- Conflict resolution — LWW policies, CRDTs, or application rules
- Infrastructure cost — Additional compute and storage
- Bandwidth consumption — Log-based CDC reduces data in flight

## Related

- [[Replication (Distributed)]] — From Mixu's distributed systems
- [[Synchronous Replication]] — Strong consistency, higher latency
- [[Asynchronous Replication]] — High performance, eventual consistency
- [[Active-Active Geo Distribution]] — Multi-master with CRDTs
- [[Change Data Capture (CDC)]] — Common technique for change capture
