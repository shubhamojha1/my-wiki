---
title: "Consensus Problem"
type: concept
tags: [distributed-systems, consensus, agreement]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Consensus Problem

**Consensus** is the fundamental problem of getting all nodes in a distributed system to agree on a single value, despite the possibility of node failures and network unreliability.

## Formal Properties

A consensus algorithm must satisfy all four:

1. **Agreement** — every correct (non-crashed) process decides the same value
2. **Integrity** — each process decides at most one value; once decided, it does not change
3. **Termination** (Liveness) — all non-faulty processes eventually decide
4. **Validity** — the decided value must have been proposed by some process (no values appear out of thin air)

## Why It's Hard

- Nodes may crash at any time
- Messages may be delayed arbitrarily (in asynchronous models)
- No global clock; nodes cannot agree on real time
- The [[FLP Impossibility Result]] proves it cannot be solved deterministically in a fully asynchronous system with even one crash

## Applications

Consensus is the foundation for many distributed primitives:

| Application | How Consensus Is Used |
|------------|----------------------|
| Leader election | Agree on which node is leader |
| Atomic broadcast | All nodes deliver the same messages in the same order |
| Distributed lock | Agree on which process holds the lock |
| Database transactions | [[Two-Phase Commit]] for coordinating distributed commits |
| Replication | Log replication in [[Raft]], [[Paxos]], [[Zab]] |

## Practical Solutions

Real systems escape [[FLP Impossibility Result]] by assuming **partial synchrony** (the network is eventually well-behaved):

- **[[Paxos]]** — the classic solution; safety always, liveness when timing allows
- **[[Raft]]** — designed for understandability; leader-based log replication
- **[[Zab]]** — used in ZooKeeper; optimized for primary-backup replication
- **[[Two-Phase Commit]]** — simpler but blocking; coordinator is SPOF

## Safety vs. Liveness

Under poor network conditions, practical consensus algorithms prioritize **safety** (never decide wrong) over **liveness** (always make progress). They may block indefinitely rather than decide incorrectly.

## Related Concepts

- [[FLP Impossibility Result]] — proves consensus is impossible in pure async systems
- [[Raft]] — practical consensus algorithm
- [[Paxos]] — classic consensus algorithm
- [[CAP Theorem]] — related impossibility result for storage
- [[Quorum (Distributed)]] — mechanism used to achieve consensus
- [[Leader Election]] — a specific consensus problem instance
