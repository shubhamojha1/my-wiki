---
title: "Race Conditions"
type: concept
tags: [concurrency, race-condition, thread-safety]
created: 2026-04-24
sources: [algomaster-introduction-to-concurrency, algomaster-race-conditions-and-critical-sections]
---

# Race Conditions

A **race condition** occurs when a program's behavior depends on the timing of uncontrolled events (thread interleaving), producing incorrect results.

> From AlgoMaster: "Concurrent access to shared data produces incorrect results" — outcome depends on which thread executes first.

## How Race Conditions Happen

### Read-Modify-Write
```python
counter = counter + 1  # 3 steps: read, add, write
```
Two threads read same value, both increment, both write → one increment lost.

### Check-Then-Act
```python
if balance >= withdrawal:  # Check
    balance -= withdrawal   # Act (another thread may have changed balance)
```

## Conditions for Race

1. **Multiple threads** access shared data
2. **At least one write** operation
3. **No synchronization** — uncoordinated timing

## Prevention

- **Mutual exclusion** — Only one thread in critical section
- **Atomic operations** — Single indivisible operation

## Related

- [[Critical Sections]] — Code where races occur
- [[Thread Safety]] — Correct behavior
- [[algomaster-Processes vs Threads]]