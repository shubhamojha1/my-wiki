---
title: "Latch Crabbing"
type: concept
tags: [database, concurrency, btree]
created: 2026-04-23
---

# Latch Crabbing

**Latch crabbing** (or **latch coupling**) is a protocol for safely accessing B+Tree nodes concurrently.

## Protocol

### Search
1. Acquire latch on root
2. Acquire latch on child
3. Release latch on parent (if safe to do so)
4. Continue down tree

### Insert/Delete
1. Acquire latches on path from root to leaf
2. Perform operation
3. Release latches from top down

## Safety Rules

- Can release parent latch when child is locked
- Child must not split/merge while parent released
- Write operations hold more latches than reads

## Optimizations

- **Read-only operations**: May use simplified protocol
- **leaf scans**: Some systems skip parent latches

## Related

- [[B+Tree]] — Index structure
- [[Latch]] — Lock type used in protocol