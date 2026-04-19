---
title: "Raft"
type: entity
tags: [distributed-systems, consensus, algorithm]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Raft is a consensus algorithm designed to be more understandable than Paxos while providing the same guarantees. Created by Diego Ongaro and John Ousterhout (2013).

## Design Goals
- **Understandable**: More clearly separated components
- **Complete**: Practical for implementation
- **Leader-based**: Uses elected leader for efficiency

## Components

### Leader Election
- Nodes start as followers
- On timeout, node becomes candidate, increments term
- Requests votes from majority
- Random wait times reduce election conflicts

### Log Replication
- All operations go through leader
- Leader sends entries to followers
- Commit after majority acknowledges

### Safety
- [[Epochs]] prevent outdated proposals
- Leader has exclusive right to commit
- Log consistency enforced

## Key Properties
- **Majority required**: N/2+1 nodes for decisions
- **Leader persistence**: Leader only valid within current term
- **Membership changes**: Supports cluster membership changes

## Usage
- etcd (CoreOS)
- Consul (HashiCorp)
- CockroachDB