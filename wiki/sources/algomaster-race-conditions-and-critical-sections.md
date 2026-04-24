---
title: "Race Conditions and Critical Sections"
type: source
tags: [race-condition, critical-section, concurrency, interview]
created: 2026-04-24
sources: []
---

# Race Conditions and Critical Sections

**Source:** [AlgoMaster.io - Race Conditions and Critical Sections](https://algomaster.io/learn/concurrency-interview/race-conditions-and-critical-sections)

**Author:** Ashish Pratap Singh

## What is a Race Condition?

A race condition occurs when the outcome of a program depends on the timing of uncontrolled events (thread interleaving), producing incorrect results.

> Concurrent access to shared data produces incorrect results — outcome depends on which thread executes first.

## How Race Conditions Happen

### Read-Modify-Write
```python
counter = counter + 1  # 3 steps: read, add, write
```
If two threads interleave, both read the same value, both increment, both write → one increment lost.

### Check-Then-Act
```python
if balance >= withdrawal:  # Check
    balance -= withdrawal   # Act (but another thread may have changed balance)
```

## Critical Sections

A **critical section** is code that accesses shared data and must not be executed by more than one thread simultaneously.

From AlgoMaster: "A critical section is any piece of code that reads or writes shared state and must not be executed by more than one thread at the same time. If two threads enter that section together, you can end up with race conditions."

## Requirements for Critical Section Protection

1. **Mutual Exclusion** — Only one thread in critical section at a time
2. **Progress** — If no thread is in critical section, one should enter
3. **Bounded Waiting** — Thread can't wait indefinitely to enter

## Solutions

| Method | Use Case |
|--------|----------|
| **Mutex** | Default choice for mutual exclusion |
| **Semaphore** | Counting permits, resource control |
| **Atomic Operations** | Simple counters, flags |
| **Condition Variables** | Wait for conditions |
| **Lock-free** | High-performance, lock-free data structures |

## Related Concepts

- [[Race Conditions]]
- [[Critical Sections]]
- [[Thread Safety]]
- [[algomaster-Thread Lifecycle and States]]