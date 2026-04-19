---
title: "Dynamo"
type: entity
tags: [distributed-systems, key-value-store, eventually-consistent]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Amazon's Dynamo is a highly available key-value store that prioritizes availability over consistency. It serves as the basis for many real-world systems including LinkedIn's Voldemort, Facebook's Cassandra, and Basho's Riak.

## Key Design Principles

- **Eventually consistent**: Does not guarantee single-copy consistency; replicas may diverge
- **Always writable**: Designed to never stop accepting writes even during failures
- **Partial quorums**: Uses sloppy quorums (R-of-N reads, W-of-N writes)

## Core Techniques

### Consistent Hashing
Maps keys to nodes via hashing, allowing clients to locate keys without system queries.

### Partial Quorums
Users choose R and W parameters:
- R = nodes contacted during read
- W = nodes required for write success
- Recommendation: R + W > N for read-write overlap

### Conflict Detection and Read Repair
- Uses [[Vector Clocks]] to track causal history
- At read time, detects conflicts and reconciles differences
- May return multiple values requiring client-side resolution

### Replica Synchronization
- [[Gossip Protocol]] for probabilistic sync
- [[Merkle Trees]] for efficient data comparison

## Derivatives
- Cassandra (Facebook, uses timestamps)
- Riak (Basho, uses vector clocks)
- Voldemort (LinkedIn)