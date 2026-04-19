---
title: "Bloom Language"
type: concept
tags: [distributed-systems, programming]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Bloom is a Ruby DSL designed for distributed programming using the [[CALM Theorem]].

## Design
- Order-independent statements
- Collections and Lattices (CRDTs)
- Monotonic by default
- Non-monotonic functions supported

## Key Features
- Static analysis for monotonicity
- Identifies coordination boundaries
- Declarative style

## Foundations
Based on Dedalus (Datalog in Time and Space).

## Usage
For building distributed systems where coordination is minimized through monotonicity analysis.