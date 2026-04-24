---
title: "Concurrency vs Parallelism"
type: concept
tags: [concurrency, parallelism]
created: 2026-04-24
sources: [algomaster-introduction-to-concurrency, algomaster-concurrency-vs-parallelism]
---

# Concurrency vs Parallelism

These terms are often used interchangeably but represent distinct concepts.

## Core Distinction

| Aspect | Concurrency | Parallelism |
|--------|-------------|-------------|
| **Definition** | Structuring a program to handle multiple tasks | Actually executing multiple tasks |
| **Goal** | Make progress on multiple tasks | Speed up by executing simultaneously |
| **Execution** | Interleaved on single core | Simultaneous on multiple cores |
| **Focus** | Dealing with multiple things at once | Doing multiple things at once |

## Restaurant Analogy

From AlgoMaster's detailed analogy:

### Scenario 1: Sequential
One chef. One dish at a time. Customers wait long times.

### Scenario 2: Concurrent (One Chef)
Same chef, working on multiple dishes during overlapping periods: while soup simmers, chop vegetables for salad. While mushroom rests, plate appetizer. All dishes make progress. This is concurrency without parallelism.

### Scenario 3: Parallel (Multiple Chefs)
Three chefs, each working on a dish simultaneously. All literally being prepared at same instant. Requires concurrent structure (independent tasks).

### Scenario 4: Concurrent + Parallel
Three chefs, each handling multiple dishes concurrently, all working in parallel. How modern web servers work: multiple threads/processes, each handling multiple connections.

## Key Relationships

- **Parallelism requires concurrency** (has independent tasks)
- **Concurrency doesn't guarantee parallelism** — depends on hardware and scheduler
- **Single core** = concurrent only (interleaved)
- **Multi-core** = can be both

## Levels of Parallelism

| Level | Description | Example |
|-------|-------------|---------|
| Bit-level | Word size optimization | 32-bit → 64-bit operations |
| Instruction-level | Pipelining, ILP | CPU pipeline stages |
| Data | Same operation on data chunks | SIMD, vectorization |
| Task | Independent subtasks | Multi-threading |

## When Each Applies

- **Concurrency**: I/O-bound tasks (network, disk) — waiting dominates, use async/await
- **Parallelism**: CPU-bound tasks (computation) — use multiple cores

## Related

- [[Processes vs Threads]] — Units enabling concurrency/parallelism
- [[Introduction to Concurrency]]