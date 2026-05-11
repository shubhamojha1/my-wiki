---
title: "Byzantine Failure"
type: concept
tags: [distributed-systems, fault-tolerance, byzantine]
created: 2026-05-11
sources: [medium-consensus-distributed-system]
---

# Byzantine Failure

A **Byzantine failure** occurs when a node in a distributed system behaves arbitrarily or maliciously — sending conflicting messages, lying about its state, or colluding with other faulty nodes. Named after the [[Byzantine Generals Problem]] (Leslie Lamport).

## Characteristics

- **Arbitrary behavior**: Faulty node can do anything — crash, send wrong data, send different messages to different peers
- **Undetectable intent**: Cannot distinguish malicious from benign faulty behavior
- **Collusion**: Multiple faulty nodes may coordinate

## Comparison with Crash Failure

| Aspect | Crash Failure | Byzantine Failure |
|--------|---------------|-------------------|
| Behavior | Node stops responding | Node sends arbitrary/conflicting messages |
| Detection | Easy (timeout) | Hard (may appear correct) |
| Tolerance threshold | ≤ n-1 (any number can crash) | ≤ n/3 (≤ 1/3 can be Byzantine) |
| Algorithm complexity | Simple (Paxos, Raft) | Complex (pBFT, HotStuff) |
| Application | Traditional distributed DBs | Blockchain, permissionless networks |

## Related

- [[Consensus]] — Requires handling Byzantine failures
- [[Practical Byzantine Fault Tolerance]] — Algorithm that tolerates Byzantine failures
- [[Byzantine Generals Problem]] — Classic formulation by Lamport
