---
title: "Consistency Model"
type: concept
tags: [distributed-systems, consistency]
created: 2026-04-19
sources: [mixu-distributed-systems-book, strong-vs-eventual-consistency]
---

# Consistency Model

A consistency model is a contract between programmer and system, guaranteeing predictable results if specific rules are followed. In distributed systems, where data is replicated across nodes, consistency models define when and where updates become visible, and in what order.

## The Core Problem

Replication lag: a write to Node A takes time to propagate to Nodes B and C. During this window, different replicas may serve different values. Consistency models define rules for how and when changes propagate.

## Strong Consistency

Guarantees that once a write completes, any read from any replica reflects that write or a newer one. Behaves as if a single globally synchronized copy exists.

### Mechanics
1. Write propagated from primary to replicas
2. Each replica acknowledges
3. Only after all (or quorum) acknowledgments is write confirmed
4. Subsequent reads always return the latest value

Implemented via consensus protocols like [[Paxos]] and [[Raft]].

### Trade-offs
- Simple application logic, predictable behavior
- Higher latency (coordination overhead)
- Reduced availability during network partitions ([[CAP Theorem]])

### When to Use
Banking, inventory management, distributed locking, unique ID generation — any system where inconsistencies cause incorrect decisions or data loss.

## Eventual Consistency

Guarantees that if no new updates are made, all replicas will eventually converge to the same value. No guarantee about how soon this happens.

### Mechanics
1. Write acknowledged immediately by one node
2. Updated value propagated asynchronously to other replicas
3. Reads during propagation may return stale data
4. System fully consistent once all replicas receive the update

### Trade-offs
- Low latency, high availability, easier global scaling
- Temporary staleness requires app-level handling
- Concurrent writes need conflict resolution ([[CRDT|CRDTs]], Last Write Wins)

### When to Use
Social media metrics, analytics, DNS, CDNs, product recommendations — scenarios where temporary inconsistency is acceptable.

## Client-Centric Consistency Variants

Stronger guarantees within an eventually consistent system:

- **Causal Consistency** — Causally related operations (A→B) seen in order by all processes. Unrelated operations can appear in any order.
- **Read-Your-Writes (RYW)** — After a client writes, subsequent reads by that same client reflect the write. Other clients may still see stale data.
- **Monotonic Reads** — Once a client reads a value, future reads never return an older version.
- **Monotonic Writes** — Writes from the same client are executed in order.

## Choice Tradeoffs

- Strong consistency = high latency, low availability during partition
- Weak consistency = low latency, high availability

### Decision Framework

| Factor | Choose Strong | Choose Eventual |
|--------|--------------|-----------------|
| Data criticality | Financial, inventory, locks | Likes, counts, recommendations |
| UX expectations | Immediate correctness | Optimistic UI, grace period |
| Latency needs | Can tolerate coordination overhead | Must be fast globally |
| Availability | Can sacrifice during partitions | Must stay up |
| Scalability | Limited by coordination | Easy horizontal/global |
| Dev complexity | Simpler app logic | Must handle staleness, conflicts |

## Related

- [[Eventual Consistency]] — Detailed model
- [[CAP Theorem]] — The consistency/availability trade-off
- [[CRDT]] — Conflict-free data types for eventual consistency
- [[Paxos]], [[Raft]] — Consensus protocols for strong consistency
