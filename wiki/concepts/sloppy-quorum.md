---
title: "Sloppy Quorum"
type: concept
tags: [distributed-systems, replication, quorum, availability]
created: 2026-04-21
updated: 2026-05-20
sources: ["Dynamo Amazon's Highly Available Key-Value Store"]
---

# Sloppy Quorum

A **sloppy quorum** is a quorum variant used in highly available systems (notably [[Dynamo]]) where read/write operations are performed on the first **N healthy nodes** from the preference list, rather than requiring responses specifically from the N designated replica nodes.

## vs Strict Quorum

| | Strict Quorum | Sloppy Quorum |
|--|---------------|---------------|
| Node selection | Must include the designated N replicas | Any N healthy nodes from the ring |
| Behavior on failure | Blocks until designated nodes respond | Routes to stand-in nodes with [[Hinted Handoff]] |
| Consistency guarantee | Stronger (overlap guaranteed) | Weaker (temporary divergence possible) |
| Availability | Lower during failures | Higher |

## Parameters

- **N** — total designated replicas per key
- **R** — minimum nodes that must respond to a read
- **W** — minimum nodes that must acknowledge a write
- **R + W > N** — when this holds, read and write sets overlap, providing consistency

Typical Dynamo setting: N=3, R=2, W=2.

## How It Works

If 2 of the 3 designated replicas for key `k` are unavailable:

1. Coordinator selects the next 2 healthy nodes from the ring as stand-ins
2. Writes proceed to the 2 stand-ins plus any available designated replica
3. Each stand-in stores the replica with a [[Hinted Handoff]] hint pointing to the true owner
4. When the designated replica recovers, the stand-in delivers and deletes its copy

## Trade-off

Sloppy quorum maximizes write availability ("always writeable") at the cost of potentially reading stale data during the handoff window. It is the right choice when availability is paramount and temporary inconsistency is acceptable (eventual consistency).

## Related Concepts

- [[Quorum (Distributed)]] — the strict quorum baseline
- [[Hinted Handoff]] — the mechanism that delivers deferred writes
- [[Dynamo]] — the system where sloppy quorum was popularized
- [[Eventual Consistency]] — the consistency model that results
- [[CAP Theorem]] — sloppy quorum favors A over C during partitions
