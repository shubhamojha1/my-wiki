---
title: "Partial Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-05-11
sources: [redis-data-replication]
---

# Partial Replication

**Partial replication** mirrors only selected data to each replica — typically the most recently updated records or data relevant to a specific region or workload.

## How It Works

- A headquarters database might replicate all records globally
- Regional offices replicate only locally accessed data
- Replicas stay smaller than the primary

## Characteristics

- **Selective**: Only subset of data per replica
- **Bandwidth-efficient**: Less data transferred
- **Storage-efficient**: Smaller replicas
- **Complex routing**: Requests crossing regions need coordination

## Trade-offs

| Pro | Con |
|-----|-----|
| Lower storage cost | Complex routing logic |
| Lower bandwidth | Cross-region requests expensive |
| Regional compliance friendly | Partial failover capability |

## Related

- [[Data Replication]] — General concept
- [[Full Replication]] — Alternative complete-copy approach
- [[Geo-Based Sharding]] — Related concept for geographic data placement
