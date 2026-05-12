---
title: "Concurrency vs Parallelism"
type: concept
tags: [concurrency, parallelism]
created: 2026-04-24
sources: [algomaster-introduction-to-concurrency, algomaster-concurrency-vs-parallelism]
---

# Concurrency vs Parallelism

These terms are often used interchangeably but represent distinct concepts. Concurrency is about **managing** multiple tasks; parallelism is about **executing** multiple tasks at the same instant.

## Core Distinction

| Aspect | Concurrency | Parallelism |
|--------|-------------|-------------|
| **Definition** | Structuring a program to handle multiple tasks | Actually executing multiple tasks |
| **Goal** | Make progress on multiple tasks | Speed up by executing simultaneously |
| **Mechanism** | Context switching (interleaved) | Multi-core/processor execution |
| **Execution** | Interleaved on single core | Simultaneous on multiple cores |
| **Focus** | Dealing with multiple things at once | Doing multiple things at once |

## How Concurrency Works

A single CPU core achieves concurrency through **context switching**:
1. **Save** current task state (program counter, registers) to memory
2. **Load** next task's saved context
3. **Execute** until switch triggered (timer interrupt, I/O wait)
4. Repeat — switching so fast it creates illusion of simultaneity

**Cost**: context switching consumes CPU cycles. Excessive switching degrades performance.

## How Parallelism Works

1. **Divide** problem into independent subtasks
2. **Distribute** across multiple CPU cores or GPUs
3. **Execute** each subtask simultaneously on its own core
4. **Aggregate** results into final output

Requires hardware with multiple processing units (multi-core CPU, GPU cluster).

## Restaurant Analogy

### Scenario 1: Sequential
One chef. One dish at a time. Customers wait long times.

### Scenario 2: Concurrent (One Chef)
Same chef, working on multiple dishes during overlapping periods: while soup simmers, chop vegetables for salad. While mushroom rests, plate appetizer. All dishes make progress. This is concurrency without parallelism.

### Scenario 3: Parallel (Multiple Chefs)
Three chefs, each working on a dish simultaneously. All literally being prepared at same instant. Requires concurrent structure (independent tasks).

### Scenario 4: Concurrent + Parallel
Three chefs, each handling multiple dishes concurrently, all working in parallel. How modern web servers work: multiple threads/processes, each handling multiple connections.

## The 4 Combinations

| | Not Parallel | Parallel |
|---|---|---|
| **Concurrent** | Single core switching between tasks (single-chef kitchen) | Multiple tasks, each subdivided across cores (modern multi-core server) |
| **Not Concurrent** | Sequential execution, one at a time (simple script) | Single task's subtasks across cores (video rendering) |

## Real-World Examples

### Concurrency
- **Web browsers** — render HTML/CSS, fetch resources, respond to clicks simultaneously
- **Web servers** — Apache/Nginx handling many client requests via threads or async I/O
- **Chat apps** — process incoming messages, update UI, send outgoing messages
- **Video games** — graphics rendering, input processing, physics simulation, audio playback

### Parallelism
- **ML training** — dataset batches processed across multiple GPUs simultaneously
- **Video rendering** — frames rendered independently on separate cores
- **Web crawlers** — URL list chunked and fetched in parallel across nodes
- **Big data** — Apache Spark distributing computations across a cluster
- **Scientific simulations** — weather modeling, molecular dynamics divided across cores

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
- [[Context Switching]] — The mechanism underlying concurrency