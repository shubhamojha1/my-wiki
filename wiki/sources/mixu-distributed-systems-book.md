---
title: "Distributed Systems: for fun and profit"
type: source
tags:
  - distributed-systems
  - fundamentals
  - tutorial
created: 2026-04-19
sources:
  - https://book.mixu.net/distsys/single-page.html
---

A comprehensive introduction to distributed systems by Mikito Takada (2013). Covers the fundamental concepts needed to understand modern distributed systems like Amazon Dynamo, Google's BigTable/MapReduce, and Apache Hadoop.

## Key Takeaways

Two consequences of distribution that distributed programming must handle:
1. Information travels at the speed of light
2. Independent things fail independently

## Chapter Summary

### Chapter 1: Basics
- Scalability (size, geographic, administrative)
- Availability and fault tolerance
- Performance and latency
- Partitioning vs replication

### Chapter 2: Abstractions and Impossibility Results
- System models (async/sync)
- CAP theorem (CA/CP/AP tradeoffs)
- FLP impossibility result
- Consistency models

### Chapter 3: Time and Order
- Clocks (global, local, logical)
- Vector clocks for causal ordering
- Failure detectors

### Chapter 4: Replication (Preventing Divergence)
- Primary/backup replication
- Two-phase commit (2PC)
- Paxos family (Paxos, Raft, ZAB)

### Chapter 5: Replication (Accepting Divergence)
- Eventually consistent systems
- Amazon Dynamo design
- CRDTs (Convergent Replicated Data Types)
- CALM theorem

## Core Systems Covered
- [[Dynamo]] - Amazon's highly available KVS
- [[Paxos]] - consensus algorithm
- [[Raft]] - consensus algorithm
- [[ZAB]] - Zookeeper atomic broadcast
- [[Two-Phase Commit]] - distributed transaction protocol