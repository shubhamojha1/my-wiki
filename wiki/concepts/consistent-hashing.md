---
title: "Consistent Hashing"
type: concept
tags: [distributed-systems, partitioning, hashing, load-balancing]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book, "algomaster.io/learn/system-design/consistent-hashing", "https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Consistent Hashing

**Consistent hashing** maps keys to nodes on a circular hash ring such that adding or removing a node requires remapping only a small fraction of keys — `k/n` rather than almost all of them.

## The Problem with Naive Hashing

With `hash(key) mod N`:
- Remove 1 server → ~(N-1)/N of all keys must be reassigned
- Add 1 server → similar reshuffling
- Every node change causes a massive cache miss storm

## How It Works

```
         0°
    7  /   \  1
   6          2
    5  \   /  3
         4°
   (hash ring, values 0–7)

Nodes: A at 2, B at 5, C at 7
Key hashes to 3 → walk clockwise → lands on B (at 5)
Key hashes to 6 → walk clockwise → lands on C (at 7)
```

1. Hash both **server identifiers** and **keys** to the same 0–2³² ring
2. Each key is owned by the first server encountered clockwise
3. Adding a server: only keys between it and its counter-clockwise neighbor move
4. Removing a server: only its keys move to its successor

## Key Property

When node count changes by 1, only `k/n` keys are reassigned (k = total keys, n = nodes). All other keys stay put.

## Virtual Nodes

Physical servers get **multiple positions** (virtual nodes) on the ring:

- Achieves more uniform key distribution without needing perfectly spaced server hashes
- When a server is removed, its load spreads across many servers rather than just one successor
- The number of virtual nodes per server can be proportional to its capacity

## Use Cases

- **[[Dynamo]]** — each node owns a range of the hash ring; vnodes spread replicas across failure domains
- **Distributed caches** — Memcached, Redis clusters use consistent hashing to route keys to cache nodes
- **[[Database Sharding]]** — minimizes data movement during shard rebalancing
- **CDN routing** — consistent hashing directs requests for the same URL to the same edge node (cache locality)
- **[[Distributed Rate Limiter]]** - routes all checks for a user ID, IP address, or API key to the same Redis shard so rate-limit state is not split

## Limitations

- Hot spots if key distribution is uneven (vnodes help)
- More complex than modular hashing
- Requires coordination to update the ring membership

## Related Concepts

- [[Hash-Based Sharding]] — consistent hashing is the standard implementation
- [[Data Rebalancing]] — consistent hashing minimizes rebalancing cost
- [[Virtual Node (Vnode)]] — the technique for even distribution
- [[Dynamo]] — canonical use case
- [[Hash Slot]] — Redis's fixed-slot alternative to consistent hashing
