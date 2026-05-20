---
title: "Bloom Language"
type: concept
tags: [distributed-systems, programming, monotonicity]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book]
---

# Bloom Language

**Bloom** is a Ruby-embedded DSL for distributed programming built on the principles of the [[CALM Theorem]]. It enables developers to write distributed programs that automatically converge without coordination, while statically flagging the parts that do require it.

## Core Design Principles

- **Order-independent statements** — Bloom programs are sets of rules, not sequences; execution order does not affect correctness for monotonic parts
- **Collections and Lattices** — data is organized as sets and lattice-based structures ([[CRDT]]s), enabling merge without conflict
- **Monotonic by default** — the language encourages monotonic operations; non-monotonic operations are explicitly marked
- **Declarative style** — based on Datalog (via **Dedalus** — "Datalog in Time and Space")

## Key Feature: Confluence Analysis

Bloom performs static analysis to identify **points of order** — locations in the program where non-monotonic operations require coordination. This allows developers to:
- Identify the minimum set of coordination points needed
- Avoid unnecessary distributed locking or consensus
- Reason formally about which parts of the system can run in parallel without divergence

## Foundations

Bloom is grounded in **Dedalus**, a temporal extension of Datalog that models distributed computation over time. Dedalus provides the formal semantics; Bloom provides the practical Ruby embedding.

## Significance

Bloom is primarily a research language demonstrating that:
- Coordination in distributed systems can be **principled** rather than ad-hoc
- [[CALM Theorem]] is actionable, not just theoretical
- Many distributed programs have large monotonic cores that need no coordination

## Related Concepts

- [[CALM Theorem]] — the theoretical foundation
- [[CRDT]] — the data structures that make monotonic merges possible
- [[Eventual Consistency]] — the consistency guarantee for monotonic programs
- [[Consensus]] — required only at Bloom's "points of order"
