---
title: "Primary-Backup Replication"
type: concept
tags: [distributed-systems, replication, availability]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Primary-Backup Replication

**Primary-backup replication** (also called master-slave or log shipping) routes all writes through a single designated primary node, which then propagates changes to one or more backup (replica) nodes. It is the most widely deployed replication topology in relational databases.

## How It Works

```
[Client] → Write → [Primary]
                      ↓ replication stream
               [Backup 1]  [Backup 2]
[Client] → Read  ↑ (or directly from Primary)
```

1. Client sends all writes to the primary
2. Primary applies the change and records it in the replication log (binlog, WAL)
3. Backups continuously consume the log and apply the same changes
4. Clients may read from backups (eventual consistency) or from primary (strong consistency)

## Variants

### Asynchronous Replication

- Primary commits and responds to client immediately
- Replication log is sent to backups in the background
- **Pros**: Low write latency
- **Cons**: Backups may lag; failover risks data loss (uncommitted on backup)

### Synchronous Replication

- Primary waits for at least one backup to acknowledge before responding to client
- **Pros**: Zero data loss on failover to the acknowledged backup
- **Cons**: Write latency includes round-trip to backup; backup slowness blocks primary

### Semi-Synchronous

- Primary waits for just one replica (out of many) to acknowledge
- Balances durability and latency

## Characteristics

- **Single writer**: All mutations go through primary; no write conflicts
- **Read scaling**: Multiple replicas serve read traffic
- **Replication lag**: Async replicas may be seconds or minutes behind primary
- **Automatic failover**: Typically requires external tooling (Orchestrator, Patroni, MHA)

## Problems

- **Split-brain**: During network partition, if a backup is promoted while primary is still alive, two primaries accept writes
- **Replication lag**: Stale reads from replicas; monotonic read guarantees may break
- **Manual/complex failover**: Detecting primary failure and electing a new one is error-prone

## Real-World Systems

| System | Default Mode |
|--------|-------------|
| MySQL | Async (semi-sync optional) |
| PostgreSQL | Async (sync optional via `synchronous_standby_names`) |
| MongoDB | Single-primary replica set (async) |

## Related Concepts

- [[Replication (Distributed)]] — general replication concepts
- [[Replication Lag]] — the delay between primary and backup
- [[Failover]] — promoting a backup to primary
- [[Synchronous Replication]] — zero-loss variant
- [[Asynchronous Replication]] — high-performance variant
