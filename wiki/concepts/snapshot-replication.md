---
title: "Snapshot Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-05-11
sources: [redis-data-replication]
---

# Snapshot Replication

**Snapshot replication** copies the state of data at a specific point in time to the replica. Nothing after the snapshot is captured.

## Characteristics

- **Point-in-time**: Captures exact state at a moment
- **Not continuous**: No ongoing changes after snapshot
- **Baseline use**: Often the first step before switching to incremental replication
- **Best for**: Low-volatility datasets or initial replica setup

## Comparison

| Aspect | Snapshot | [[Transactional Replication]] |
|--------|----------|-------------------------------|
| Timing | One-time or periodic | Continuous |
| Currency | Stale between refreshes | Near real-time |
| Overhead | Higher during snapshot | Lower ongoing |
| Use case | Initial baseline, static data | Live reporting, sync |

## Related

- [[Data Replication]] — General concept
- [[Transactional Replication]] — Continuous alternative
