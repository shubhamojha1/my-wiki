---
title: "Snapshot Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-05-11
updated: 2026-05-20
sources: [redis-data-replication]
---

# Snapshot Replication

**Snapshot replication** copies the full state of a dataset at a point in time and ships that copy to one or more replicas. It captures no subsequent changes — the replica is current as of the snapshot moment and diverges from the source thereafter.

## How It Works

```
Source DB ──[snapshot at T0]──→ Replica
   │                              │
   │  (source continues writes)   │  (replica frozen at T0)
   │                              │
   [T1: source has new data]     [T1: replica still has T0 data]
```

For periodic refresh, a new snapshot is taken and applied in full (or the delta is shipped as a new snapshot).

## Mechanism

1. **Lock or MVCC read**: Acquire a consistent view of the data — either via a brief lock or a database MVCC snapshot (e.g., `REPEATABLE READ` transaction).
2. **Serialize**: Export data as a file (SQL dump, RDB file, Parquet, etc.).
3. **Transfer**: Copy the snapshot to the replica — over a network or shared storage.
4. **Apply**: Load the snapshot on the replica, replacing (or seeding) its data.

## Comparison with Continuous Replication

| Aspect | Snapshot | Transactional / Log-shipping |
|--------|----------|------------------------------|
| Timing | One-time or periodic | Continuous (near real-time) |
| Staleness | High between refreshes | Low (seconds or less) |
| Source overhead | High during snapshot | Low, steady |
| Network traffic | Full dataset each time | Incremental changes only |
| Use case | Initial seed, static datasets | Live read replicas, HA |
| Implementation | Simple | Requires change tracking (WAL, CDC) |

## Common Uses

- **Initial replica seeding**: Bootstrap a new replica before switching to log-based replication (e.g., Redis `FULLRESYNC` on first connect sends an RDB snapshot, then replication log delta).
- **Data warehouse loads**: Nightly full extract from OLTP into a data warehouse.
- **Backup/restore**: Point-in-time database backups are essentially snapshots.
- **Low-change datasets**: Reference tables (country codes, product catalog) that barely change.

## Snapshot in Redis Replication

Redis uses snapshot replication as the first phase of primary–replica sync:
1. Primary forks, child writes RDB snapshot to disk.
2. RDB file is sent to the replica.
3. Replica loads RDB, then primary sends the replication backlog accumulated during the snapshot.
4. Ongoing: replica follows the primary's replication stream (log-based from here).

## Related Concepts

- [[Transactional Replication]] — continuous, change-level replication
- [[Primary-Backup Replication]] — topology that uses snapshot for initial sync
- [[Data Replication]] — general replication concepts
- [[Change Data Capture]] — alternative for continuous incremental replication
