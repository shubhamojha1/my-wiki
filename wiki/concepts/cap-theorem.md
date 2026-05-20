---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, consistency, tradeoff, availability, partition-tolerance]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book, "algomaster.io/learn/system-design/cap-theorem"]
---

# CAP Theorem

CAP theorem (Brewer's theorem) states that a distributed system can provide at most **two of three** guarantees simultaneously: **C**onsistency, **A**vailability, and **P**artition Tolerance.

## Three Properties

| Property | Meaning |
|----------|---------|
| **Consistency (C)** | Every read returns the most recent write, or an error. All nodes see the same data at the same time. |
| **Availability (A)** | Every request receives a non-error response (may not be the most recent write). |
| **Partition Tolerance (P)** | The system continues operating despite messages being dropped or delayed between nodes. |

## The Real Trade-Off

Network partitions are **inevitable** in any distributed system — hardware fails, links go down. Therefore, P is not optional in practice. The real choice is:

> **During a network partition, do you sacrifice Consistency or Availability?**

- **CP**: Sacrifice availability → refuse requests rather than return stale data (e.g., ZooKeeper, HBase, etcd)
- **AP**: Sacrifice consistency → return possibly-stale data rather than an error (e.g., Cassandra, DynamoDB, CouchDB)

## System Classification

| Type | Behavior During Partition | Examples |
|------|--------------------------|---------|
| CP | Returns error or timeout on some requests | ZooKeeper, HBase, MongoDB (default config) |
| AP | Returns potentially stale data | Cassandra, DynamoDB, Riak |
| CA | Only possible if partitions never happen (single node or perfect network) | Traditional RDBMS on single node |

## Nuances and Criticisms

- **CAP is binary** — in practice, consistency and availability exist on a spectrum. [[PACELC Theorem]] extends CAP to also model the latency–consistency tradeoff when there is *no* partition.
- **"Consistency" in CAP** differs from ACID consistency — CAP C means linearizability (all nodes agree on single latest value), not transaction integrity.
- Real systems tune their consistency level per operation (e.g., Cassandra quorum reads vs. eventual reads).

## Related Concepts

- [[Consistency Model]] — spectrum of consistency guarantees
- [[Eventual Consistency]] — the consistency model chosen by AP systems
- [[Availability]] — uptime and responsiveness
- [[Network Partition]] — the failure scenario CAP reasons about
- [[Quorum (Distributed)]] — mechanism to tune the CP/AP trade-off
- [[ACID Transactions]] — different meaning of "consistency"
