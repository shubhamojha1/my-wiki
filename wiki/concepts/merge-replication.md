---
title: "Merge Replication"
type: concept
tags: [distributed-systems, replication, conflict-resolution]
created: 2026-05-11
sources: [redis-data-replication]
---

# Merge Replication

**Merge replication** allows each node to make independent changes that are later reconciled into a unified dataset.

## How It Works

1. Initial snapshot distributed to all nodes
2. Each node makes changes independently (potentially offline)
3. When nodes reconnect, changes merged via conflict resolution logic

## Conflict Resolution

Merge replication needs deterministic rules when two nodes modify the same record:
- **Last-writer-wins** — latest timestamp takes precedence
- **Application-defined** — custom merge logic
- **CRDT-based** — data types designed to merge automatically

## Use Cases

- Field teams working offline (sync on reconnect)
- Distributed branches with intermittent connectivity
- Mobile applications with offline-first architecture

## Related

- [[Data Replication]] — General concept
- [[CRDT]] — Structures enabling automatic merge
- [[Active-Active Geo Distribution]] — Always-online variant
