---
title: "Consensus"
type: concept
tags: [distributed-systems, consensus, fault-tolerance]
created: 2026-05-11
sources: [medium-consensus-distributed-system]
---

# Consensus

**Consensus** is the problem of multiple nodes in a distributed system agreeing on a common value through message passing, despite possible failures.

## Properties

1. **Agreement**: All non-faulty nodes must agree on the same value
2. **Validity**: The agreed value must have been proposed by a non-faulty node
3. **Termination**: Every non-faulty node eventually decides on some value

## Failure Models

### Crash Failure
A node stops responding due to hardware, software, or network faults. Common and relatively easy to handle — the system can ignore the crashed node.

### Byzantine Failure
A node behaves arbitrarily or maliciously — sending conflicting messages to different peers, lying about its state, or colluding with other faulty nodes. Much harder to handle.

## Algorithms

### Voting-Based
- [[Paxos]] — Classic consensus (Lamport), safe but hard to understand
- [[Raft]] — Understandable consensus with leader election (Ongaro & Ousterhout)
- [[Practical Byzantine Fault Tolerance|pBFT]] — Handles Byzantine failures, 3-phase protocol, requires ≤ 1/3 faulty nodes
- [[ZAB]] — ZooKeeper Atomic Broadcast, used in ZooKeeper
- HotStuff — Modern BFT for blockchain

### Proof-Based
- Proof of Work (PoW) — Computational puzzle (Bitcoin)
- Proof of Stake (PoS) — Validator stake-weighted voting (Ethereum 2.0)

## Impossibility Results

- [[FLP Impossibility]] — No deterministic consensus in async systems with even one fault
- Consensus requires some synchrony assumptions (timeouts, partial synchrony)

## Related

- [[Failure Detector]] — Needed for termination in async systems
- [[Epoch]] — Logical time period for consensus rounds
- [[Byzantine Failure]] — Arbitrary/malicious node behavior
