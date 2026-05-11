---
title: "Transactional Replication"
type: concept
tags: [distributed-systems, replication, cdc]
created: 2026-05-11
sources: [redis-data-replication]
---

# Transactional Replication

**Transactional replication** copies data changes in real time, preserving the exact order of changes made on the primary.

## How It Works

1. Full snapshot of primary database taken as baseline
2. Subsequent changes streamed as they occur (via CDC)
3. Changes applied to replica in the same transactional order

## Characteristics

- **Real-time**: Changes propagate as they happen
- **Ordered**: Transaction order preserved exactly
- **Incremental**: Only changed data sent after initial snapshot
- **Not a backup strategy**: Typically combined with actual backups

## Use Cases

- Reporting databases that must reflect the primary
- Data warehouses needing near-real-time updates
- Any scenario where every change must be reflected everywhere

## Related

- [[Data Replication]] — General concept
- [[Change Data Capture (CDC)]] — Implementation technique
- [[Snapshot Replication]] — Alternative one-time approach
