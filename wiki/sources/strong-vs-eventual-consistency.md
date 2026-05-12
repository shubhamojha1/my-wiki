---
title: "Strong vs. Eventual Consistency"
type: source
tags: [consistency, distributed-systems, cap, algomaster]
created: 2026-05-12
sources: []
---

# Strong vs. Eventual Consistency

An AlgoMaster article by Ashish Pratap Singh (Jun 2025) explaining strong and eventual consistency models, their mechanics, client-centric variants, and a decision framework for choosing between them.

## The Problem

Data replicated across multiple nodes introduces replication lag — writes to Node A take time to propagate to Nodes B and C. During this window, different replicas serve different values.

## Strong Consistency

All reads reflect the latest write. Achieved via coordinated communication between replicas before confirming writes (consensus: Paxos, Raft).

**Pros**: Simple app logic, predictable behavior, data integrity.
**Cons**: Higher latency, reduced availability during partitions (CAP), complex infrastructure.
**Use cases**: Banking, inventory, distributed locking, unique ID generation.

## Eventual Consistency

Replicas converge to the same value eventually. Writes acknowledged immediately, propagated asynchronously.

**Pros**: Low latency, high availability, scalable globally.
**Cons**: Temporary staleness, app-level conflict resolution needed, read-after-write edge cases.
**Use cases**: Social media metrics, analytics, recommendations, DNS, CDNs, shopping carts.

## Client-Centric Variants (Stronger Eventual)

- **Causal Consistency** — Causally related operations seen in order (comment threads)
- **Read-Your-Writes** — Client sees its own writes immediately
- **Monotonic Reads** — Never see an older version after a newer one
- **Monotonic Writes** — Own writes executed in order

## Decision Framework

**Strong**: Critical data (financial), strict UX requirements, low latency tolerance, can sacrifice availability.
**Eventual**: High availability needed, massive scale, latency-critical, stale data acceptable.

## Conflict Resolution

Last Write Wins (LWW), CRDTs, custom merge logic.

## Source

- AlgoMaster: [Strong vs. Eventual Consistency](https://blog.algomaster.io/p/strong-vs-eventual-consistency) (Jun 2025)
