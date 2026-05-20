---
title: "Replication Lag"
type: concept
tags: [distributed-systems, replication, consistency]
created: 2026-05-11
updated: 2026-05-20
sources: [redis-data-replication]
---

# Replication Lag

**Replication lag** is the delay between when a write is committed on the primary and when it is visible on a replica. In asynchronous replication, the primary does not wait for replicas before acknowledging the client — so replicas can be behind by milliseconds, seconds, or even minutes under load.

## Anatomy of Lag

```
Primary:  WRITE committed at T=0  →  WAL entry written  →  send to replica
Replica:  Receive WAL at T=50ms   →  Apply at T=55ms

Replication lag at T=50ms = 50ms
```

Sources of lag:
- **Network latency**: Distance between primary and replica (same DC: <1ms; cross-continent: 100ms+)
- **I/O bottleneck on replica**: Replica disk is slower than primary; applying log falls behind
- **High write rate**: Primary produces more log than replica can apply
- **Single-threaded apply**: Some databases (older MySQL) apply relay log serially

## Impacts

| Problem | Description |
|---------|-------------|
| **Stale reads** | Reading from replica shows data before the latest write |
| **Monotonic read violation** | User reads data from replica A, then replica B — B may be further behind, showing older data |
| **Data loss on failover** | If primary fails and a lagging replica is promoted, writes in the lag window are lost |
| **Incorrect reports** | Analytics running on replica undercount recent transactions |

## Mitigations

| Strategy | Trade-off |
|----------|---------|
| **Read-your-own-writes**: route reads to primary after user writes | Increases primary load |
| **Wait for replica**: wait until replica catches up before reading | Adds latency |
| **Synchronous replication**: primary waits for replica ACK before commit | Higher write latency; replica slowdown blocks primary |
| **Semi-sync**: primary waits for at least one replica | Balanced durability/latency |
| **Monotonic read sessions**: always read from same replica | May hit a slow replica |

## Measuring Lag

- **MySQL**: `SHOW SLAVE STATUS` → `Seconds_Behind_Master`
- **PostgreSQL**: `SELECT * FROM pg_stat_replication` → `write_lag`, `flush_lag`, `replay_lag`
- **Prometheus**: expose replica lag as a metric, alert when > threshold

## Lag and RPO

Replication lag directly determines the maximum **RPO** (Recovery Point Objective) on failover:

```
RPO ≈ replication lag at time of primary failure
```

If lag = 30 seconds and primary fails, up to 30 seconds of committed writes may be lost.

## Related Concepts

- [[Primary-Backup Replication]] — the topology where lag arises
- [[Asynchronous Replication]] — root cause of lag
- [[Synchronous Replication]] — eliminates lag at the cost of write latency
- [[Failover]] — lag determines RPO on failover
