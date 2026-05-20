---
title: "Redis Sentinel"
type: concept
tags: [redis, failover, monitoring]
created: 2026-04-20
updated: 2026-05-20
sources: [redis-cluster-architecture]
---

# Redis Sentinel

**Redis Sentinel** provides high availability for Redis by monitoring a primary-replica topology and automatically promoting a replica to primary when the primary fails. It is the HA solution for single-shard Redis (not horizontally sharded — use Redis Cluster for that).

## Architecture

```
         ┌─────────────────────────────┐
         │    Sentinel Quorum (3+)     │
         │  [S1]  [S2]  [S3]          │
         └────┬───────┬───────┬───────┘
              │ monitor│       │
      ┌───────▼──┐  ┌──▼──────▼──┐
      │  Primary │  │  Replica 1  │  Replica 2
      │ (writes) │  │  (reads)    │  (reads)
      └──────────┘  └────────────┘
```

Multiple Sentinel processes form a quorum. Clients query any Sentinel to discover the current primary address.

## Responsibilities

| Role | Detail |
|------|--------|
| **Monitoring** | Sends PING to primary and replicas every `sentinel down-after-milliseconds` |
| **Failure detection** | "Subjective down" (SDOWN): one sentinel thinks primary is down; "Objective down" (ODOWN): quorum agrees |
| **Leader election** | Sentinels elect a leader (Raft-like) to coordinate failover |
| **Automatic failover** | Leader promotes the most up-to-date replica to primary |
| **Configuration provider** | Clients ask Sentinel `SENTINEL get-master-addr-by-name <name>` to discover current primary |
| **Notifications** | Pub/Sub messages on failover events |

## Failover Sequence

```
1. Primary stops responding for > down-after-milliseconds
2. Detecting sentinel marks it SDOWN (subjective down)
3. Detecting sentinel asks other sentinels: do you agree?
4. If ≥ quorum sentinels agree → mark ODOWN (objective down)
5. Sentinels elect a leader via Raft-like vote
6. Leader selects best replica (lowest replication lag)
7. Leader sends SLAVEOF NO ONE to chosen replica → becomes new primary
8. Other replicas reconfigured to replicate from new primary
9. Clients re-query Sentinel → reconnect to new primary
10. Old primary demoted to replica if it comes back
```

## Configuration

```conf
sentinel monitor mymaster 127.0.0.1 6379 2   # quorum = 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1            # replicas syncing at once
```

## Sentinel vs Redis Cluster

| Feature | Sentinel | Redis Cluster |
|---------|---------|--------------|
| Purpose | HA for single shard | Horizontal scaling + HA |
| Sharding | No (single primary) | Yes (16,384 hash slots) |
| Automatic failover | Yes | Yes |
| Client support | Sentinel-aware client required | Cluster-aware client required |
| Setup complexity | Lower | Higher |

## Limitations

- Single primary handles all writes — capacity limited by one machine.
- Failover takes seconds (detection + election + promotion): brief write unavailability.
- Split-brain possible if network partitions isolate sentinels (use odd quorum ≥ 3).

## Related Concepts

- [[Primary-Backup Replication]] — the replication topology Sentinel monitors
- [[Failover]] — the action Sentinel automates
- [[Quorum (Distributed)]] — how Sentinels agree on primary failure
- [[Redis Cluster]] — alternative for horizontal scaling
