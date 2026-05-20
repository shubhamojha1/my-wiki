---
title: "Partial Order"
type: concept
tags: [distributed-systems, ordering, causality]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Partial Order

**Partial order** is the natural ordering state in distributed systems. Not all pairs of events have a defined relative order — some events are simply **concurrent** and incomparable.

## Formal Definition

A binary relation ≤ is a partial order if:
- **Reflexive**: `a ≤ a`
- **Antisymmetric**: if `a ≤ b` and `b ≤ a`, then `a = b`
- **Transitive**: if `a ≤ b` and `b ≤ c`, then `a ≤ c`

Unlike [[Total Order]], partial order does **not** require totality — some pairs `(a, b)` have neither `a ≤ b` nor `b ≤ a`.

## Concurrency

When two events are incomparable in a partial order, they are **concurrent**: neither caused the other. Concurrent events happened on independent nodes with no communication between them at the time.

## Example: Causal History

```
Node 1:  A ──→ B ──────────→ E
                              ↑
Node 2:       C ──→ D ───────┘
```

- `A → B` (same node, B after A)
- `B → E` (A's message triggered E)
- `C → D → E`
- `A` and `C` are **concurrent** (no causal relationship)
- `B` and `C` are **concurrent**

## Example: Git Branches

Two branches from a common ancestor have no definite order — they represent different histories that cannot be reduced to a linear sequence without merging. The merge commit is the first event that causally follows both branches.

## Why Partial Order Matters

Distributed systems inherently produce only a partial order of events because:
- Nodes observe events locally without global coordination
- Network communication establishes causal links but not between all events
- Achieving [[Total Order]] requires coordination (expensive)

[[Lamport Clocks]] and [[Vector Clocks]] both capture partial order information. Vector clocks additionally allow detecting whether two events are concurrent.

## Related Concepts

- [[Total Order]] — stronger ordering where every pair is comparable
- [[Lamport Clocks]] — assign timestamps consistent with partial order
- [[Vector Clocks]] — detect concurrency in partial orders
- [[Causal Consistency]] — consistency model based on partial order
- [[CRDT]] — data structures designed to merge concurrent (unordered) updates
