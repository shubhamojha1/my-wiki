---
title: "Paxos"
type: entity
tags: [distributed-systems, consensus, algorithm]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Paxos is a family of consensus algorithms designed to achieve agreement among distributed nodes despite failures. Named after the Greek island of Paxos, originally presented by Leslie Lamport in "The Part-Time Parliament" (1998).

## Properties

- **Consistency**: Maintains single-copy consistency
- **Partition tolerant**: Uses majority votes, tolerates minority failures
- **Safe**: Never violates consistency guarantees (gives up liveness if needed)

## Algorithm Structure

### Roles
- **Proposer**: Initiates consensus
- **Acceptor**: Votes on proposals
- **Learner**: Learns decided values

### Phases
1. **Prepare**: Proposer asks acceptors for highest numbered accepted proposal
2. **Accept**: Proposer proposes value (either new or highest from phase 1)
3. **Learn**: Value is chosen once majority accepts

### Epochs/Terms
Each period of operation uses a unique epoch number to identify outdated proposals.

## Variants
- Basic Paxos (single decision)
- Multi-Paxos (repeated decisions, efficient)
- Cheap Paxos
- Fast Paxos

## Usage
- Google Chubby lock service
- Google Spanner
- Google File System
- Apache Zookeeper (via ZAB)

## Tradeoffs
- Difficult to implement correctly
- Requires majority (N/2+1) of nodes operational
- High latency due to multiple rounds