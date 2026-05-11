---
title: "Gossip Protocol"
type: concept
tags: [distributed-systems, protocol, epidemic]
created: 2026-04-19
sources: [highscalability-gossip, mixu-distributed-systems-book]
---

# Gossip Protocol

**Gossip protocol** (or epidemic protocol) is a decentralized peer-to-peer communication technique where each node periodically sends messages to a random subset of other nodes. The entire system eventually receives the message with high probability. Convergence takes O(log n) rounds.

## Types

### Anti-Entropy
Nodes compare full state and patch differences. Used for database replication. Can use checksums, Merkle trees, or recent update lists to avoid transferring the entire dataset.

### Rumor-Mongering (Dissemination)
Nodes share only the latest updates. Messages are marked "removed" after a few rounds. More bandwidth-efficient but less thorough than anti-entropy.

### Aggregation
Computes system-wide aggregates (average, max, sum) by sampling and combining values across nodes.

## Strategies

| Strategy | When Efficient | Mechanism |
|----------|---------------|-----------|
| **Push** | Few update messages | Node sends to random subset |
| **Pull** | Many update messages | Node polls random subset for updates |
| **Push-Pull** | Optimal for both | Push in initial phase, pull in final phase |

## Performance

- **Fanout**: nodes contacted per round
- **Cycle**: rounds to propagate across cluster = O(log n) / log(fanout)
- Example: ~15 rounds to propagate across 25,000 nodes
- At 10ms interval → ~3 seconds for a datacenter
- 128 nodes: < 2% CPU, < 60 KBps bandwidth

## Implementation

- **Peer sampling service**: `/gossip/init` returns known nodes; `/gossip/get-peer` returns random peer
- **Seed nodes**: static nodes preventing logical divisions
- **Generation clock**: monotonically increasing number, incremented on restart
- **Gossip digest**: endpoint address + generation number + version number
- **Timer**: ensures eventual propagation even across partitions

## Advantages

- Scalable (fixed messages per node, independent of cluster size)
- Fault-tolerant (redundant paths, no SPOF)
- Decentralized and symmetric
- Bounded load on any single component

## Disadvantages

- Only eventual consistency
- Unaware of network partitions
- Hard to debug and test (non-deterministic)
- Can waste bandwidth via duplicate transmissions

## Real-World Uses

- [[Apache Cassandra]] — membership, token assignment, Merkle tree repair, failure detection
- [[Consul]] — SWIM gossip variant for group membership + leader election
- [[Redis Cluster]] — node metadata propagation
- [[Amazon Dynamo]] — failure detection, membership
- [[CockroachDB]] — node metadata propagation
- Amazon S3 — server state dissemination
- Bitcoin — nonce propagation across miners
- [[Riak]] — consistent hash ring state
- Hyperledger Fabric — group membership, ledger metadata

## Related

- [[Heartbeat]] — Failure detection via gossip
- [[Failure Detector]] — Gossip-based failure suspicion
- [[Merkle Tree]] — Used in anti-entropy for efficient diffing
- [[SWIM]] — Scalable Weakly-consistent Infection-style Process Group Membership
