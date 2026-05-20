---
title: "Transactional Replication"
type: concept
tags: [distributed-systems, replication, cdc]
created: 2026-05-11
updated: 2026-05-20
sources: [redis-data-replication]
---

# Transactional Replication

**Transactional replication** streams changes from the primary to replicas as they are committed, preserving the exact transaction order. Each INSERT/UPDATE/DELETE is replicated individually (or in transaction batches) rather than shipping bulk snapshots. This keeps replicas near-current with the primary in real time.

## How It Works

```
Primary DB
  │
  │ Transaction committed → WAL / binlog entry written
  │
  ↓
Replication Agent / CDC reader (reads WAL)
  │
  ↓
Replica(s) apply changes in same order
  │
  └─ Replica is seconds or milliseconds behind primary (replication lag)
```

1. **Baseline snapshot**: Initial full copy of primary to new replica.
2. **Log streaming**: CDC agent (Debezium, Maxwell, pglogical) reads WAL/binlog in real time.
3. **Ordered apply**: Replica applies each change in the same transaction order, preserving referential integrity.

## Implementation Mechanisms

| Database | Mechanism | Tool |
|----------|-----------|------|
| **PostgreSQL** | Logical replication (WAL via publication/subscription) | pglogical, AWS DMS, Debezium |
| **MySQL** | Binlog streaming (row-based) | MySQL Replication, Debezium |
| **SQL Server** | Transactional replication (publisher/distributor/subscriber) | Native SQL Server replication |
| **MongoDB** | Oplog tailing | Built-in replica set replication |

## Characteristics

| Property | Value |
|----------|-------|
| Latency | Near real-time (milliseconds to seconds) |
| Completeness | Every change captured; no snapshots after baseline |
| Ordering | Guaranteed (same commit order) |
| Overhead | WAL/binlog read on source; network; write on target |

## Use Cases

- **Read replicas**: Route OLAP queries to replica, freeing primary for OLTP writes.
- **Data warehouses**: Near-real-time feed into Redshift, BigQuery, or Snowflake via CDC.
- **Cross-region replication**: Keep a replica in another region for geo-proximity reads.
- **Zero-downtime migrations**: Replicate to a new schema/database, cut over when lag is ~0.
- **Audit streams**: Feed every change to Kafka for event-driven consumers.

## Comparison with Snapshot Replication

| Aspect | Transactional | Snapshot |
|--------|--------------|---------|
| Currency | Near real-time (seconds) | Stale until next snapshot |
| Overhead | Continuous (low steady-state) | High during snapshot |
| Initial setup | Requires snapshot baseline | Just a snapshot |
| Use case | Live reporting, HA | Initial sync, static data |

## Related Concepts

- [[Change Data Capture]] — the mechanism that reads the WAL/binlog
- [[Snapshot Replication]] — one-time alternative for initial baseline
- [[Replication Lag]] — the delay inherent in async transactional replication
- [[Primary-Backup Replication]] — the topology transactional replication implements
