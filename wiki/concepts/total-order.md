---
title: "Total Order"
type: concept
tags: [distributed-systems, ordering]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Total order defines an exact order for every element in a set. In a distributed system, requires either accurate clocks or explicit communication.

## Definition
A binary relation where for all elements a, b:
- `a ≤ b` or `b ≤ a` (totality)
- Antisymmetric and transitive

## Single Node Reality
On a single node, total order emerges by necessity - instructions execute in observable order.

## Distributed Challenge
Nodes experience the world independently. Total order requires either:
- Global clock (unrealistic)
- Communication to agree on order

## [[CAP Theorem]] Connection
Achieving total order often requires strong consistency protocols (coordination), which sacrifice availability and performance.