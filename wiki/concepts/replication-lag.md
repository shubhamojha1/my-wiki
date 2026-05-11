---
title: "Replication Lag"
type: concept
tags: [distributed-systems, replication, consistency]
created: 2026-05-11
sources: [redis-data-replication]
---

# Replication Lag

**Replication lag** is the time delay between a write on the primary node and when that write is applied to a replica in an asynchronous replication setup.

## Impact

- Applications reading from a replica may see **stale data** immediately after a write
- A primary failure during the lag window can cause **data loss**
- Lag increases with geographic distance between nodes

## Mitigations

- **Read-your-own-writes**: Route reads to primary after a write
- **Synchronous replication** on critical paths
- **Eventual consistency patterns** at the application layer
- **Monitoring**: Track lag metrics and alert on anomalies

## Metrics

- **Recovery Point Objective (RPO)**: How much data could be lost
- **Recovery Time Objective (RTO)**: How long to fail over
- Asynchronous replication trades lower RTO for potentially higher RPO

## Related

- [[Data Replication]] — General concept
- [[Asynchronous Replication]] — Primary source of replication lag
- [[RPO and RTO]] — Recovery metrics driven by lag
