---
title: "CRDT (Convergent Replicated Data Type)"
type: concept
tags: [distributed-systems, consistency, data-structures]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

CRDTs are data structures designed to guarantee convergence despite network delays, partitions, and message reordering.

## Mathematical Foundation
Based on semilattice properties:
- **Associative**: `(a+b)+c = a+(b+c)`
- **Commutative**: `a+b = b+a`
- **Idempotent**: `a+a = a`

## How It Works
Operations that form semilattices can merge in any order and always converge to the same result.

## Examples

### Counter: max()
- `max(3, max(5, 7)) = 7`
- `max(5, max(7, 3)) = 7`

### Set: union
- Merge by union operation

## Types

### Grow-Only Counter
- Merge = max(values)

### PN-Counter
- Two counters: positive and negative

### Two-Phase Set
- Add-set + remove-set
- Elements can be added once, removed once

### Last-Writer-Wins Register
- Timestamp-based merge

## Tradeoff
Must use appropriate data type matching application semantics.