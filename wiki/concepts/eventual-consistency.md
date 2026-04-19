---
title: "Eventual Consistency"
type: concept
tags: [distributed-systems, consistency]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Eventual consistency means that if no new updates are made, all replicas will eventually agree on the same value.

## Problem
Without additional constraints, "eventually consistent" is too weak - trivial systems like "always return 42" are eventually consistent but useless.

## Two Questions to Answer
1. **How long?** Need bounds or typical convergence time.
2. **How?** Need reconciliation method.
   - Last-writer-wins (timestamp-based)
   - Vector clock resolution
   - CRDT merge

## Practical Systems
- [[Dynamo]]: R+W > N provides probabilistic overlap
- Amazon: allows both sides to accept writes during partition, reconciles later

## Types

### Probabilistic Guarantees (Dynamo)
- Can detect conflicts later
- May overwrite newer with older
- Anomalies expected

### Strong Guarantees (CRDTs)
- Guarantees converge to common value
- No anomalies
- Commutative properties required