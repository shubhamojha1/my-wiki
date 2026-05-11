---
title: "MongoDB Atlas"
type: entity
tags: [mongodb, database, cloud, document-db]
created: 2026-05-11
sources: [mongodb-atlas-architecture, algomaster-15-db-types]
---

# MongoDB Atlas

**MongoDB Atlas** is a fully managed multi-cloud database service for MongoDB, available on AWS, Azure, and GCP.

## Architecture

Atlas follows a Well-Architected Framework with 5 pillars: Operational Efficiency, Security, Reliability, Performance, Cost Optimization.

### Replica Sets

Every cluster is deployed as a **replica set** with minimum 3 nodes across separate availability zones. Applications write to the primary; data replicates to all nodes. Automatic failover via replica set elections completes within seconds. Retryable writes re-attempt in-flight operations after failover.

### High Availability

- **Default**: 3-node replica set across AZs
- **Fault tolerance**: up to 7 electable nodes, 50 total nodes
- **Multi-region**: deploy across regions or cloud providers
- **Maintenance**: rolling updates, one node at a time
- **Write concern**: default `majority` — data persists on majority of electable nodes

### Scalability

- **Vertical**: upgrade tier with zero downtime (rolling promotion)
- **Horizontal**: sharding (ranged, hashed, zoned) for shared-nothing distribution
- **Auto-scaling**: compute and storage scale automatically based on CPU/memory
- **Low CPU option**: half vCPUs for memory-intensive workloads
- **Data tiering**: archive to low-cost storage, TTL indexes for auto-expiry

### Performance Tools

- **Performance Advisor**: automated index recommendations based on query patterns
- **Embedded config servers** (8.0+): reduces costs on small sharded clusters

## Deployment Paradigms

- **Single-region**: 3-node replica set
- **Multi-region**: cross-region replicas for low-latency reads
- **Multi-cloud**: withstand full cloud provider outages
- **Global clusters**: local reads/writes with zone sharding

## Related

- [[Document Database]] — MongoDB is the leading document DB
- [[Database Sharding]] — Horizontal scaling via sharding
- [[RPO and RTO]] — Recovery metrics for DR planning
- [[Replication (Distributed)]] — Replica set replication
