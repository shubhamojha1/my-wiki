---
title: "Vector Clocks"
type: concept
tags: [distributed-systems, time, causality, conflict-detection]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book, "Dynamo Amazon's Highly Available Key-Value Store"]
---

# Vector Clocks

**Vector clocks** extend [[Lamport Clocks]] with a per-node counter array, enabling precise causal ordering and detection of concurrent (unrelated) events. Where Lamport clocks can only say "event A might have caused event B," vector clocks can definitively determine causality.

## Structure

Each node maintains a vector `[t_1, t_2, ..., t_N]` — one counter per node in the system.

## Algorithm

1. **Local event**: increment own entry `VC[self]++`
2. **Send message**: attach current vector to the message
3. **Receive message** with vector `V_msg`:
   - `VC[i] = max(VC[i], V_msg[i])` for all i
   - Then increment own entry: `VC[self]++`

## Causal Comparison

Given two events `a` (with vector `Va`) and `b` (with vector `Vb`):

| Condition | Meaning |
|-----------|---------|
| `Va[i] ≤ Vb[i]` for all i | `a → b` (a causally precedes b) |
| `Va[i] ≥ Vb[i]` for all i | `b → a` (b causally precedes a) |
| Neither dominates | `a ∥ b` (concurrent — no causal relationship) |

## Example

```
Node A: [1,0,0]  sends to B
Node B: receives, merges → [1,1,0], then B does work → [1,2,0]
Node C: does work independently → [0,0,1]
B sends to C: C receives → [1,2,1], then → [1,2,2]

Compare: [1,2,0] (B's event) vs [0,0,1] (C's event):
  B[0]=1 > C[0]=0, but B[2]=0 < C[2]=1 → neither dominates → CONCURRENT
```

## Advantages over Lamport Clocks

- Can definitively detect concurrent events (not just order events)
- Enables conflict detection when two replicas diverge independently

## Limitations

- **O(N) size**: One entry per node; grows with cluster size
- **Garbage collection**: Old entries need pruning in large systems
- Some systems (e.g., Riak) use **dotted version vectors** to handle GC

## Use Cases

- **[[Dynamo]]** — used version vectors for conflict detection; returns all conflicting versions to client for resolution
- **Riak** — dotted version vectors
- **Voldemort** — vector clocks for conflict detection
- **CRDTs** — state-based CRDTs use version vectors to track causal history

## Related Concepts

- [[Lamport Clocks]] — simpler predecessor; cannot detect concurrency
- [[Partial Order]] — the ordering vector clocks capture
- [[CRDT]] — leverages causal history for merge
- [[Dynamo]] — canonical use case
