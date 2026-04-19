---
title: "Gossip Protocol"
type: concept
tags: [distributed-systems, synchronization]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Gossip is a probabilistic technique for replica synchronization where nodes randomly exchange updates.

## Properties
- No predetermined communication pattern
- Each node has probability p of contacting peer
- Every t seconds, pick random node to sync

## Advantages
- Scalable
- No single point of failure
- Handles failures gracefully

## Disadvantages
- Probabilistic guarantees only
- Eventually consistent but not deterministic

## Usage
- [[Dynamo]] anti-entropy
- Cassandra gossip
- Consul/rendezvous