---
title: "Concurrency vs Parallelism"
type: source
tags: [concurrency, parallelism, interview]
created: 2026-04-24
sources: []
---

# Concurrency vs Parallelism

**Source:** [AlgoMaster.io - Concurrency vs Parallelism](https://algomaster.io/learn/concurrency-interview/concurrency-vs-parallelism)

**Author:** Ashish Pratap Singh

## The Core Distinction

- **Concurrency** = Structuring a program to handle multiple tasks (dealing with multiple things at once)
- **Parallelism** = Actually executing multiple tasks simultaneously (doing multiple things at once)

Parallelism requires concurrent structure (independent tasks), but concurrency doesn't guarantee parallelism.

## Restaurant Analogy

### Scenario 1: Sequential
One chef, one dish at a time. Customers wait long.

### Scenario 2: Concurrent (One Chef)
Same chef, multiple dishes during overlapping periods: while soup simmers, chop vegetables. All dishes make progress. No parallelism.

### Scenario 3: Parallel (Multiple Chefs)
Three chefs, each working on a dish simultaneously. True simultaneous execution.

### Scenario 4: Concurrent + Parallel
Three chefs, each juggling multiple dishes, all working in parallel. Modern web servers.

## Key Relationships

- To run in parallel → need multiple independent tasks (concurrent structure)
- Concurrent structure doesn't guarantee parallel execution (single core = interleaved)
- Desktop web servers combine both: multiple threads, each handling connections

## Levels of Parallelism

| Level | Description |
|-------|------------|
| Bit-level | Word size optimization (32→64-bit) |
| Instruction-level | Pipelining, ILP |
| Data | Same operation on data chunks (SIMD) |
| Task | Independent subtasks (multi-threading) |

## Related Concepts

- [[Introduction to Concurrency]]
- [[Processes vs Threads]]
- [[Thread Safety]]