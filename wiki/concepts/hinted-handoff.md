---
title: "Hinted Handoff"
type: concept
tags: [distributed-systems, failure-handling, replication, availability]
created: 2026-04-21
updated: 2026-05-20
sources: ["Dynamo Amazon's Highly Available Key-Value Store"]
---

# Hinted Handoff

**Hinted handoff** is a technique for maintaining write availability during transient node failures. When a write cannot reach its intended replica node, the data is temporarily stored on a different node with metadata ("hint") identifying the true owner. When the intended node recovers, the stand-in delivers the data and discards its copy.

## How It Works

```
Normal write (N=3 replicas: A, B, C):
  Coordinator → A, B, C

A is unavailable (hinted handoff):
  Coordinator → D (with hint: "intended for A"), B, C

A recovers:
  D detects A is alive → delivers stored replica to A
  D deletes its local copy
```

1. Write intended for node A fails because A is down
2. Coordinator writes to a stand-in node D with metadata hint: `{ intended_for: "A" }`
3. D stores the replica in a separate "hinted" storage area
4. D periodically checks if A is alive
5. When A recovers, D delivers the replica and deletes its local copy
6. System returns to normal replication topology

## Purpose

Hinted handoff preserves **write availability** during transient failures without requiring an immediate quorum write to succeed on all N intended replicas. The system satisfies `W = write quorum` using stand-in nodes, then self-heals when the intended replica returns.

## Trade-offs

| Aspect | Detail |
|--------|--------|
| **Maintains availability** | Writes succeed even when intended nodes are down |
| **Eventual consistency** | The hint recipient may serve stale reads until handoff completes |
| **Data loss risk** | If stand-in node D fails before delivering the hint, data is lost (unless D itself has replicas) |
| **Scope** | Designed for short-lived outages; longer outages use [[Merkle Tree]] anti-entropy for repair |

## Sloppy Quorum Relationship

Hinted handoff works alongside [[Sloppy Quorum]]: the coordinator picks the first N **healthy** nodes from the preference list (skipping unavailable ones), then uses hinted handoff to ensure eventual delivery to the true owners.

## Related Concepts

- [[Dynamo]] — canonical use case; described in the original paper
- [[Sloppy Quorum]] — the quorum strategy that pairs with hinted handoff
- [[Merkle Tree]] — handles permanent failures where hints can't be delivered
- [[Data Replication]] — the broader replication strategy
- [[Eventual Consistency]] — the consistency model maintained with hinted handoff
