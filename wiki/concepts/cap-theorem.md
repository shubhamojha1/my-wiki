---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, consistency, tradeoff]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

CAP theorem states that a distributed system can only provide two of: Consistency, Availability, Partition Tolerance.

## Three Properties

### Consistency (C)
All nodes see the same data at the same time.

### Availability (A)
Node failures do not prevent survivors from continuing to operate.

### Partition Tolerance (P)
System continues to operate despite message loss due to network/node failure.

## System Types

### CA (Consistency + Availability)
- Cannot tolerate partitions
- Example: [[Two-Phase Commit]], full strict quorum

### CP (Consistency + Partition Tolerance)
- Majority quorum protocols
- Example: [[Paxos]], [[Raft]]
- Minority partition becomes unavailable

### AP (Availability + Partition Tolerance)
- Conflict resolution
- Example: [[Dynamo]]
- Allows divergence during partition

## Practical Implications
During a partition, must choose between:
- Availability (allow writes on both sides → divergence)
- Consistency (disable writes → maintain single copy)

## Key Insight
"Consistency" is not singular: ACID ≠ CAP ≠ "oatmeal"