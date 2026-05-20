---
title: "Reader-Writer Latch"
type: concept
tags: [database, concurrency, latch, synchronization]
created: 2026-04-23
updated: 2026-05-20
sources: [cmu_15-445_lec08]
---

# Reader-Writer Latch

A **reader-writer latch** (RW latch or shared-exclusive latch) is a synchronization primitive that allows either multiple concurrent readers **or** a single exclusive writer, but never both simultaneously. It optimizes read-heavy workloads by not serializing reads against each other.

## Modes

| Mode | Who Holds It | Concurrency |
|------|-------------|-------------|
| **Read (Shared)** | Multiple threads simultaneously | Any number of readers |
| **Write (Exclusive)** | One thread only | No other readers or writers |

```
State: No holders
  → Reader A acquires READ  → OK
  → Reader B acquires READ  → OK (shared with A)
  → Writer C requests WRITE → must wait for A and B to release

State: Writer C holds WRITE
  → Reader D requests READ  → must wait
  → Writer E requests WRITE → must wait
```

## Implementation Considerations

| Problem | Description | Solution |
|---------|-------------|---------|
| **Writer starvation** | Continuous readers may indefinitely block writers | Priority queuing: new readers block when a writer is waiting |
| **Reader starvation** | Long-running writes block readers | Time-limited write holds; write timeouts |
| **Fairness** | Threads blocked for a long time | Queue-based (FIFO) admission |

## Database Use Cases

- **B+Tree nodes** — multiple readers scan concurrently; writer splits/merges take exclusive lock
- **Buffer pool page table** — many threads look up pages (read), few threads install new pages (write)
- **Hash table buckets** — concurrent reads; exclusive for rehashing
- **Lock table** — high-concurrency metadata table in DBMS internals

## vs. Mutex

| | Mutex | Reader-Writer Latch |
|--|-------|---------------------|
| Readers in parallel | No | Yes |
| Writers in parallel | No | No |
| Overhead | Low | Slightly higher |
| Best for | Write-heavy | Read-heavy |

## Related Concepts

- [[Latch]] — the parent class of synchronization primitives in DBMSs
- [[Latch Crabbing]] — technique for safely traversing B+Tree with latches
- [[Critical Sections]] — what latches protect
- [[Thread Safety]] — the property achieved with reader-writer latches
