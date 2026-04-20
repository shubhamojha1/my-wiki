---
title: "Dynamo: Amazon's Highly Available Key-Value Store"
type: source
tags: [distributed-systems, storage, nosql, eventual-consistency]
created: 2026-04-21
sources: []
---

*DeCandia, Hastorun, Jampani, Kakulapati, Lakshman, Pilchin, Sivasubramanian, Vosshall, Vogels — SOSP 2007*

## Summary

Dynamo is Amazon's internal highly available key-value storage system that powers core services like shopping cart and session management. It achieves "always-on" availability by sacrificing strong consistency, using eventual consistency with application-assisted conflict resolution. Key insight: push conflict resolution to reads so writes are never rejected.

## Core Techniques

| Problem | Technique |
|---------|-----------|
| Partitioning | Consistent hashing with virtual nodes |
| Replication | Sloppy quorum (N-replica) |
| Versioning | Vector clocks |
| Temp failures | Hinted handoff |
| Permanent failures | Merkle tree anti-entropy |
| Membership | Gossip protocol |

## Configuration

- **N**: Number of replicas
- **R**: Min nodes for read
- **W**: Min nodes for write
- **R + W > N**: Quorum-like consistency

## Key Insights

1. "Always writeable" — writes never rejected under failures
2. Vector clocks track causality, enable semantic reconciliation
3. Application-aware conflict resolution (not "last write wins")
4. Virtual nodes handle heterogeneity

## Production

- Shopping cart service: tens of millions requests, 3M+ checkouts/day
- Session state: hundreds of thousands concurrent sessions
- Multi-datacenter replication
- Zero-hop DHT (local routing for latency)

See also: [[Dynamo]], [[Consistent Hashing]], [[Vector Clocks]], [[Sloppy Quorum]], [[Merkle Tree]], [[Gossip Protocol]]