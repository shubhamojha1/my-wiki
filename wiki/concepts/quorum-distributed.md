---
title: "Quorum (Distributed)"
type: concept
tags: [distributed-systems, replication, consistency, availability]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book, "Dynamo Amazon's Highly Available Key-Value Store"]
---

# Quorum (Distributed)

A **quorum** is the minimum number of nodes that must agree on an operation for it to be considered valid. Quorum systems balance consistency and availability by requiring partial agreement rather than unanimous agreement.

## Parameters

- **N** — total number of replica nodes
- **R** — number of nodes that must respond to a read
- **W** — number of nodes that must acknowledge a write

## The Key Rule: R + W > N

When `R + W > N`, every read set and write set must overlap by at least one node. That overlapping node always has the latest write, guaranteeing the read sees the most recent data.

**Example** (N=3):

| R | W | R+W | Overlap? | Consistency |
|---|---|-----|----------|-------------|
| 2 | 2 | 4 | Yes (+1) | Strong |
| 1 | 3 | 4 | Yes (+1) | Strong (write all) |
| 3 | 1 | 4 | Yes (+2) | Strong (read all) |
| 1 | 2 | 3 | Maybe (=N) | Borderline |
| 1 | 1 | 2 | No | Eventual only |

## Tuning Consistency vs. Availability

| Configuration | Behavior | Use Case |
|--------------|----------|---------|
| W=N, R=1 | Write-heavy consistency, fast reads | Read-heavy workloads |
| W=1, R=N | Fast writes, read-heavy consistency | Write-heavy workloads |
| W=N/2+1, R=N/2+1 | Balanced (majority) | General-purpose |
| W=1, R=1 | Maximum availability, eventual only | Caches, non-critical data |

## Strict vs. Sloppy Quorum

- **Strict quorum**: Reads and writes must involve exactly the N designated replicas. No substitutions.
- **[[Sloppy Quorum]]** (Dynamo): Reads/writes use any N healthy nodes; deferred delivery via [[Hinted Handoff]] ensures eventual consistency.

## Real-World Settings

- **Cassandra**: configurable per-operation (`ONE`, `QUORUM`, `ALL`, etc.)
- **DynamoDB**: internally uses quorum reads; exposed as eventual vs. strong consistency
- **etcd / ZooKeeper**: use majority quorum (N/2+1) for all operations
- **Raft / Paxos**: built on majority quorum

## Related Concepts

- [[Sloppy Quorum]] — quorum with stand-in nodes for higher availability
- [[CAP Theorem]] — quorum settings affect the C/A trade-off
- [[Replication (Distributed)]] — the broader replication context
- [[Dynamo]] — popularized tunable quorums
