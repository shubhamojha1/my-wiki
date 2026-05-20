---
title: "Critical Sections"
type: concept
tags: [concurrency, synchronization, threads, mutual-exclusion]
created: 2026-04-24
updated: 2026-05-20
sources: [algomaster-introduction-to-concurrency, algomaster-race-conditions-and-critical-sections]
---

# Critical Sections

A **critical section** is a region of code that accesses shared mutable state and must not be executed by more than one thread simultaneously. Failing to protect a critical section leads to [[Race Conditions]] and data corruption.

## Three Requirements (Dijkstra)

1. **Mutual Exclusion** — At most one thread is inside the critical section at any time
2. **Progress** — If no thread is in the critical section and some want to enter, one must be allowed to enter (no deadlock at the door)
3. **Bounded Waiting** — No thread should wait indefinitely to enter; starvation is prevented

## Structure

```
// entry section — acquire lock
mutex.lock()

// critical section
shared_counter += 1

// exit section — release lock
mutex.unlock()

// remainder section — non-critical code
```

## Synchronization Mechanisms

| Mechanism | Typical Use |
|-----------|-------------|
| **Mutex** | Protect a single critical section; binary lock |
| **Semaphore** | Control access to a pool of N resources |
| **Atomic operations** | Single-variable counters without a lock |
| **Condition variable** | Wait until a condition holds (used with mutex) |
| **Reader-writer lock** | Multiple concurrent readers, exclusive writers |

## Example: Race Without Protection

```python
# Two threads both run this:
shared_counter += 1  # NOT atomic: read, add, write
# Thread 1 reads 5, Thread 2 reads 5, both write 6 → counter is 6 not 7
```

## Common Mistakes

- **Forgetting to release** the lock (use `try/finally` or RAII)
- **Holding locks too long** — increases contention and reduces throughput
- **Lock ordering** — always acquire multiple locks in the same order to prevent deadlock
- **Using wrong granularity** — too coarse serializes everything; too fine is error-prone

## Related Concepts

- [[Race Conditions]] — the problem critical sections prevent
- [[Thread Safety]] — the property achieved by protecting critical sections
- [[Latch]] — a lightweight mutual exclusion primitive in databases
- [[Distributed Lock]] — critical sections spanning multiple processes/machines
- [[Atomic Operations]] — lock-free alternative for simple operations
