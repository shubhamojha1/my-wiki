---
title: "Critical Sections"
type: concept
tags: [concurrency, synchronization, critical-section]
created: 2026-04-24
sources: [algomaster-introduction-to-concurrency, algomaster-race-conditions-and-critical-sections]
---

# Critical Sections

A **critical section** is code that accesses shared data and must not be executed by more than one thread simultaneously.

From AlgoMaster: "A critical section is any piece of code that reads or writes shared state and must not be executed by more than one thread at the same time."

## Requirements

1. **Mutual Exclusion** — Only one thread executes at a time
2. **Progress** — If no thread in critical section, one should enter
3. **Bounded Waiting** — Thread can't wait indefinitely

## Solutions

| Method | Use Case |
|--------|----------|
| **Mutex** | Default mutual exclusion |
| **Semaphore** | Counting permits |
| **Atomic** | Simple counters |
| **Condition Variable** | Wait for conditions |

## Related

- [[Race Conditions]]
- [[Thread Safety]]
- [[Mutex]]