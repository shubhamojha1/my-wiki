---
title: "CALM Theorem"
type: concept
tags: [distributed-systems, consistency, programming, monotonicity]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# CALM Theorem

**CALM** (Consistency As Logical Monotonicity) is a theorem that characterizes exactly which distributed programs can be made eventually consistent without coordination. Programs that are **logically monotonic** can run without coordination and still converge to the correct result.

## Monotonicity

A computation is **monotonic** if adding more input can only add to the output — it never retracts previous conclusions.

Formally: if φ can be inferred from premises Γ, it can also be inferred from any superset Γ' ⊇ Γ.

**Monotonic examples**: union, filter, join — adding more data only adds more results.

**Non-monotonic examples**: aggregation (COUNT, SUM), negation (NOT IN), set difference — require seeing all input before producing a final answer.

## The Theorem

> A program has a consistent, coordination-free execution if and only if it is monotone.

This means:
- **Monotonic programs** are safe to run across distributed nodes receiving data in any order; they converge automatically
- **Non-monotonic programs** require coordination (e.g., barrier synchronization, consensus) at each point where they become non-monotonic

## Practical Implications

| Operation | Monotonic? | Needs Coordination? |
|-----------|-----------|---------------------|
| Set union | Yes | No |
| Filtering (SELECT WHERE) | Yes | No |
| Joining two sets | Yes | No |
| COUNT / SUM / MAX | No | Yes (see all values first) |
| Negation (NOT EXISTS) | No | Yes (prove emptiness) |
| Global ordering | No | Yes (consensus) |

## Connection to CRDTs

[[CRDT]]s (Conflict-free Replicated Data Types) are concrete implementations of monotonic data structures. They exploit CALM: their merge operations are monotone (lattice join), so they converge without coordination.

## Bloom Language

[[Bloom Language]] is a Ruby DSL built on CALM. It uses static analysis to identify which parts of a program are monotonic (coordination-free) and flags non-monotonic "points of order" that require coordination. This lets developers minimize coordination to only what is strictly necessary.

## Related Concepts

- [[CRDT]] — monotonic data structures that embody CALM
- [[Bloom Language]] — language designed around CALM analysis
- [[Eventual Consistency]] — the consistency model achievable by monotonic programs
- [[Consensus]] — required for non-monotonic computations
- [[Relational Algebra]] — monotonic operations (selection, projection, join, union)
