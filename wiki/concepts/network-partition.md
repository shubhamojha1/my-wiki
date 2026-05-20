---
title: "Network Partition"
type: concept
tags: [distributed-systems, failures, fault-tolerance]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Network Partition

A **network partition** is a failure in which network links between nodes go down while the nodes themselves remain operational. The cluster splits into two or more groups that cannot communicate with each other.

## Characteristics

- Nodes stay active and continue serving local requests
- Nodes on each side of the partition may receive client requests
- A node cannot distinguish between "the remote node crashed" and "the network link failed"
- Partitions can be **asymmetric** (A can reach B but B cannot reach A)

## The Core Challenge

During a partition, each surviving group faces the same dilemma:

> Should I keep accepting writes (stay available) or refuse writes to avoid divergence (stay consistent)?

This is the core trade-off described by the [[CAP Theorem]].

## Behavioral Options

| Choice | Trade-Off | System Type |
|--------|-----------|-------------|
| Accept writes on both sides | Divergence; conflict resolution needed later | AP (e.g., Cassandra, DynamoDB) |
| Accept writes on majority side only | Minority side is unavailable | CP (e.g., Raft, ZooKeeper) |
| Reject all writes during partition | Maximum safety, maximum downtime | Strong CP |

## Majority-Based Systems (Raft, Paxos)

- **Majority partition**: continues accepting writes; has quorum
- **Minority partition**: stops accepting writes; cannot reach quorum
- Prevents divergence: only one group can make progress
- When partition heals, minority syncs from majority

## Partition vs. Node Failure

From any individual node's perspective, these look identical — absence of responses. This ambiguity is fundamental to why distributed consensus is hard. See [[FLP Impossibility Result]].

## Related Concepts

- [[CAP Theorem]] — the consistency/availability trade-off during partitions
- [[Quorum (Distributed)]] — mechanism for deciding which side proceeds
- [[FLP Impossibility Result]] — why partitions make consensus hard
- [[Fault Tolerance]] — broader category of handling failures
- [[Byzantine Failure]] — a different class of failure (node lies rather than crashes)
