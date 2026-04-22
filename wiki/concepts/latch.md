---
title: "Latch"
type: concept
tags: [database, concurrency, data-structure]
created: 2026-04-23
---

# Latch

A **latch** is a short-duration lock that protects in-memory data structures during concurrent access.

## Characteristics

- **Short duration**: Held only during operation
- **No deadlock detection**: Designed to prevent deadlock
- **Binary**: Usually held or not held
- **Kernel bypass**: Often implemented with atomic instructions

## vs Locks

| Aspect | Latch | Lock |
|--------|-------|------|
| Duration | Short (operation) | Long (transaction) |
| Rollback | Not applicable | Can be rolled back |
| Deadlock | Prevention via design | Detection + handling |

## Implementations

- **Test-and-Set**: Fast, atomic
- **Mutex**: OS-provided
- **Reader-Writer**: Multiple readers, exclusive writer

## Related

- [[Lock]] — Transaction-level lock
- [[B+Tree]] — Data structure using latches
- [[Reader-Writer Latch]] — Concurrent access