---
title: "Partial Order"
type: concept
tags: [distributed-systems, ordering]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Partial order is the natural state in distributed systems. Not all elements are comparable; some pairs have no defined relative order.

## Definition
A binary relation that is:
- Reflexive: `a ≤ a`
- Antisymmetric: if `a ≤ b` and `b ≤ a`, then `a = b`
- Transitive: if `a ≤ b` and `b ≤ c`, then `a ≤ c`

Not total: some pairs are incomparable.

## Example: Git Branches
Two branches from a common ancestor have no definite order - represent different histories that cannot be reduced to a single linear history.

## Distributed Systems Reality
Network and independent nodes don't guarantee relative order. Each node has local order but not global order.

## Implications
Must use coordination protocols to establish total order where required by application semantics.