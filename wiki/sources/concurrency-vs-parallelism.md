---
title: "Concurrency vs Parallelism"
type: source
tags: [concurrency, parallelism, system-design, algomaster]
created: 2026-05-12
sources: []
---

# Concurrency vs Parallelism

An AlgoMaster article by Ashish Pratap Singh (Dec 2024) distinguishing concurrency (managing multiple tasks) from parallelism (executing multiple tasks simultaneously) with examples and code.

## Core Definitions

- **Concurrency** — Making progress on multiple tasks via rapid CPU context switching. Illusion of simultaneity on single core.
- **Parallelism** — Executing multiple tasks at the same instant using separate CPU cores or processing units.

## How Concurrency Works

Context switching: CPU saves current task state (program counter, registers), loads next task's state, executes. Overhead increases with excessive switching.

## How Parallelism Works

Break problem into independent subtasks, distribute across cores, execute simultaneously, aggregate results.

## The 4 Combinations

1. **Concurrent only** — Single core switching between tasks (single-chef kitchen)
2. **Parallel only** — One task's subtasks across multiple cores (video rendering)
3. **Neither** — Sequential execution, one task at a time
4. **Both** — Multiple tasks, each possibly subdivided across cores (modern web servers on multi-core)

## Examples

**Concurrency**: web browsers (render + fetch + respond), web servers (Apache/Nginx handling many requests), chat apps, video games (graphics + input + physics + audio).
**Parallelism**: ML training (batches across GPUs), video rendering (frames in parallel), web crawlers (URL chunks), Spark data processing, scientific simulations.

## Key Insight

Parallelism requires concurrency; concurrency doesn't guarantee parallelism. Single core = concurrent only. Multi-core = can be both.

## Source

- AlgoMaster: [Concurrency vs Parallelism](https://blog.algomaster.io/p/concurrency-vs-parallelism) (Dec 2024)
