---
title: "Asynchronous Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Asynchronous replication (also: lazy, passive, pull) responds immediately and replicates later.

## Communication Pattern
1. Client sends request
2. Master responds immediately (may store locally)
3. Later: master ships updates to replicas

## Properties

### Write Pattern
- 1-of-N approach
- Fast response to client
- Replication happens in background

### Fault Tolerance
- System available if at least one node up
- No durability guarantees

### Durability
- Weak/probabilistic
- Updates may be lost if only server fails

## Risk
- Divergence possible
- Reads may return different results
- Global constraints cannot be enforced