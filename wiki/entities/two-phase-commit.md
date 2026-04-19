---
title: "Two-Phase Commit (2PC)"
type: entity
tags: [distributed-systems, transaction, protocol]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Two-Phase Commit is a distributed transaction protocol ensuring atomic commit across multiple nodes.

## Algorithm

### Phase 1: Voting
- Coordinator sends prepare to all participants
- Participants vote commit or abort
- Participants store update in temporary area (write-ahead log)

### Phase 2: Decision
- If all vote commit: coordinator sends commit, all apply permanently
- If any vote abort: coordinator sends abort, all roll back

## Properties

### Advantages
- Ensures atomicity across nodes
- Prevents partial commits
- Participants can roll back during phase 1

### Disadvantages
- **Blocking**: Single node failure blocks until recovery
- **Not partition tolerant**: Cannot distinguish node failure from partition
- **CA system**: In CAP terms, choosesConsistency + Availability

### Limitations
- Coordinator failure during commit can block indefinitely
- No automatic recovery from partitions
- Sensitive to latency (write N-of-N approach)

## Usage
- MySQL Cluster
- Traditional distributed RDBMS
- JTA transactions