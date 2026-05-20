---
title: "Full Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-05-11
updated: 2026-05-20
sources: [redis-data-replication]
---

# Full Replication

**Full replication** copies the entire dataset to every replica. Each replica holds a complete, independently-queryable copy of the database, so any read request can be served by any replica without routing to a specific node.

## Architecture

```
Primary (writes)
   │
   ├──[replicate ALL data]──→ Replica 1 (full copy, reads)
   ├──[replicate ALL data]──→ Replica 2 (full copy, reads)
   └──[replicate ALL data]──→ Replica 3 (full copy, reads)
```

Compare with partial/shard replication where each replica holds only a slice of the data.

## Trade-offs

| Pro | Con |
|-----|-----|
| Any replica handles any query (no routing logic) | Storage cost × number of replicas |
| Simple failover — any replica can become primary | Initial sync time proportional to full dataset size |
| Read scaling — add replicas to handle more reads | Write must propagate to every replica (N replicas = N writes) |
| Full redundancy — survive any N-1 replica failures | Network bandwidth for replication grows with write rate × replica count |

## Write Amplification

Every write to the primary generates N write operations (one per replica):
```
100 writes/sec × 3 replicas = 300 total replica writes/sec
100 writes/sec × 5 replicas = 500 total replica writes/sec
```

This limits full replication to write rates the network and replicas can sustain.

## Full vs Partial Replication

| Aspect | Full Replication | Partial / Shard |
|--------|-----------------|----------------|
| Data per replica | 100% | 1/N (where N = shard count) |
| Routing | Any replica for any query | Must route to the right shard |
| Storage | N × dataset size | ≈ dataset size total |
| Read scale | High | High |
| Write scale | Limited (all replicas see all writes) | Better (shards split write load) |

## When Full Replication Is Appropriate

- **Datasets that fit on one node**: No need to shard if data fits.
- **Read-dominated workloads**: Many readers, few writers; adding replicas is cheap.
- **Low write rate**: Replication overhead is manageable.
- **High availability requirement**: Any node can take over instantly.
- **Geographic read proximity**: Place full replicas in each region for local reads.

## Examples in Practice

- **MySQL/PostgreSQL read replicas**: Full replica per region for geo-distributed reads.
- **Redis replica**: Async full replica (or via Sentinel) for HA.
- **Elasticsearch replicas**: Each shard has N full replicas for resilience and parallel reads.

## Related Concepts

- [[Primary-Backup Replication]] — topology that uses full replication
- [[Partial Replication]] — replicate only selected data or hot data
- [[Replication Lag]] — the delay between primary write and replica visibility
- [[Database Sharding]] — alternative to handle write scale instead of full replication
