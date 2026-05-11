---
title: "RPO and RTO"
type: concept
tags: [distributed-systems, replication, disaster-recovery]
created: 2026-05-11
sources: [redis-data-replication]
---

# RPO and RTO

**Recovery Point Objective (RPO)** and **Recovery Time Objective (RTO)** are the two key metrics defining disaster recovery quality.

## RPO (Recovery Point Objective)

How much data loss is acceptable — how far back you'd need to roll after a failure.

- **RPO = 0**: Zero data loss (requires synchronous replication)
- **RPO = 5 minutes**: Up to 5 minutes of data may be lost (async replication)

## RTO (Recovery Time Objective)

How long the system can be offline before the business impact becomes unacceptable.

- **RTO = 1 minute**: System must recover within 1 minute
- **RTO = 1 hour**: Up to 1 hour of downtime acceptable

## Relationship to Replication Strategy

| Strategy | RPO | RTO | Notes |
|----------|-----|-----|-------|
| Synchronous | Near-zero | Fast | Requires low-latency network |
| Asynchronous | Lag-dependent | Fast | Trade data for performance |
| Active-Active | Zero (CRDT) | Instant | All nodes active |

## Related

- [[Data Replication]] — General concept
- [[Replication Lag]] — Directly affects RPO in async setups
- [[Synchronous Replication]] — Near-zero RPO
- [[Active-Active Geo Distribution]] — Best of both
