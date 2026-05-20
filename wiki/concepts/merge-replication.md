---
title: "Merge Replication"
type: concept
tags: [distributed-systems, replication, conflict-resolution]
created: 2026-05-11
updated: 2026-05-20
sources: [redis-data-replication]
---

# Merge Replication

**Merge replication** is a replication topology where multiple nodes can independently accept writes. Changes are periodically synchronized and merged across nodes, with conflicts resolved by a defined strategy. It trades conflict simplicity (primary-backup has none) for availability during disconnection.

## Architecture

```
Node A           Node B           Node C
[writes locally] [writes locally] [writes locally]
     │                │                │
     └────────────────┴────────────────┘
              periodic merge sync
              (resolve conflicts → unified state)
```

All nodes have writable replicas. Merging happens on reconnect or on a schedule.

## Workflow

1. **Snapshot**: Distribute initial dataset to all nodes.
2. **Diverge**: Each node accepts writes independently — even offline.
3. **Sync trigger**: Nodes reconnect or a scheduled sync runs.
4. **Detect conflicts**: Compare change logs (timestamps, version vectors, CRDTs) to identify conflicting updates.
5. **Resolve conflicts**: Apply resolution strategy per conflict.
6. **Converge**: All nodes reach consistent state after merge.

## Conflict Resolution Strategies

| Strategy | Description | Risk |
|----------|-------------|------|
| **Last-writer-wins (LWW)** | Latest timestamp takes precedence | Clock skew can discard valid updates |
| **First-writer-wins** | Earlier timestamp wins | Can discard more recent intent |
| **Application-defined** | Custom merge function per field/type | Complex to implement correctly |
| **CRDT-based** | Data types designed to merge without conflicts (counters, sets, maps) | Limited to CRDT-friendly data models |
| **User arbitration** | Surface conflicts to the user to resolve | Not scalable; requires human judgment |

## Merge Replication vs Other Topologies

| Topology | Writes | Conflicts possible | Availability during partition |
|---------|--------|-------------------|-------------------------------|
| **Primary-backup** | Primary only | No | Writes unavailable if primary down |
| **Multi-primary** | Any node | Yes (resolved immediately or logged) | Writes available |
| **Merge replication** | Any node (offline ok) | Yes (resolved on reconnect) | Writes available, even offline |

## Use Cases

- **Field teams offline**: Sales reps update orders on a laptop, sync when back in office.
- **Mobile apps**: CouchDB/PouchDB offline-first: edits sync to server on reconnect.
- **Distributed branches**: Git is the canonical example — branch, merge, resolve conflicts.
- **Multi-region active-active**: Cassandra (LWW), DynamoDB (last-writer-wins or custom).

## Related Concepts

- [[Primary-Backup Replication]] — single-writer alternative, no conflicts
- [[CRDT]] — data structures that enable conflict-free automatic merging
- [[Vector Clocks]] — track causality to detect concurrent (conflicting) writes
- [[Data Replication]] — general replication concepts
