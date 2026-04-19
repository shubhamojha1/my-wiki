---
title: "CALM Theorem"
type: concept
tags: [distributed-systems, consistency, programming]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

CALM (Consistency as Logical Monotonicity) theorem states that logically monotonic programs are guaranteed to be eventually consistent.

## Monotonicity
If `φ` can be inferred from premises `Γ`, then it can also be inferred from any superset of `Γ`.

## Theorem
Monotonic computations are safe to run without coordination because:
- Results only get more accurate over time
- New information can't invalidate conclusions

## Non-Monotonicity
Requires coordination because:
- Aggregation requires seeing all values
- Negation requires proof of emptiness

## Connection
- [[Relational Algebra]]: monotonic (selection, projection, join, union)
- [[Datalog]]: monotonic with recursion
- Coordination protocols are themselves aggregations (voting)

## Practical Use
Confluence analysis in [[Bloom]] language identifies which parts of a program require coordination.