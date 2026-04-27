---
title: "AlgoMaster: Consistent Hashing"
type: source
tags: [system-design, partitioning, distributed-systems]
created: 2026-04-27
sources: ["algomaster.io/learn/system-design/consistent-hashing"]
author: Ashish Pratap Singh
---

# Consistent Hashing

**Source:** AlgoMaster.io System Design — Consistent Hashing Chapter

## The Problem: Traditional Hashing

**Traditional approach**: `hash(key) mod N`

- Node added/removed → **massive reshuffling**
- 2/3 of keys remapped when changing from 3→2 nodes
- Cache misses, performance degradation

## The Solution: Consistent Hashing

Distributed hashing that ensures **only small fraction** of keys reassigned when nodes change.

> When nodes change, only `k/n` keys reassigned (k=total keys, n=nodes)

---

## How It Works: Hash Ring

1. Map both servers and keys to points on a circular hash ring
2. For a key, walk clockwise to find first server
3. That server handles the key

```
          Server B
           ▲
           │
    Keys ▼  │
    K1     │
           │
    K2 ●───┴───▶ Server C
                    ▲
                    │
                    ● K3
```

---

## Key Properties

1. **Minimal remapping** — Only keys near added/removed node affected
2. **Load distribution** — Virtual nodes for even distribution
3. **Scalability** — Works well with dynamic scaling

---

## Virtual Nodes (VNodes)

Each physical server gets **multiple positions** on the ring.

**Without VNodes**: One position → uneven load
**With VNodes** (100-200 replicas): Even distribution, better fault tolerance

---

## Algorithm

```
1. Hash server name → multiple points on ring
2. Hash key → point on ring
3. Find closest clockwise server (bisect)
4. If past last server, wrap around to first
```

---

## When to Use

| Use Case | Why |
|----------|-----|
| Distributed cache | Cache locality matters |
| Dynamic scaling | Frequent add/remove nodes |
| Load balancing | Uneven backend capacities |

---

## Key Takeaways

1. **Hash ring** — Servers and keys on circular ring
2. **Minimal reshuffling** — Only k/n keys affected
3. **Virtual nodes** — Better load distribution
4. **Use for** — Caches, dynamic scaling