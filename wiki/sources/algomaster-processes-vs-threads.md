---
title: "Processes vs Threads"
type: source
tags: [process, thread, concurrency, interview]
created: 2026-04-24
sources: []
---

# Processes vs Threads

**Source:** [AlgoMaster.io - Processes vs Threads](https://algomaster.io/learn/concurrency-interview/processes-vs-threads)

**Author:** Ashish Pratap Singh

## What is a Process?

A process is an instance of a running program with its own address space. The OS isolates processes.

- **Address space**: Private virtual memory (code, data, heap, stack)
- **Resources**: File handles, sockets, environment variables
- **Security context**: User ID, permissions, capabilities
- **Execution state**: PC, registers, stack pointer
- **Fault isolation**: Process A crash doesn't affect Process B

## What is a Thread?

A thread is a unit of execution within a process. Every process has at least one main thread.

- **Shared address space**: All threads share process memory
- **Own stack**: Each thread has private stack
- **Lightweight**: Create fast (~1ms), switch fast
- **Shared fate**: One thread crash kills entire process

## Key Differences

| Aspect | Process | Thread |
|--------|---------|--------|
| Address Space | Separate | Shared |
| Memory Isolation | Yes | No |
| Creation Cost | High (~100ms) | Low (~1ms) |
| Communication | IPC required | Direct memory |
| Fault Isolation | Strong | Weak (all die) |
| Context Switch | Slow (3-10µs) | Fast |

## Context Switching

**Process switch**: Save state → load next → **switch memory mappings** → cache disruption

**Thread switch**: Save state → load next (no address space change)

Processes require TLB flush + page table switch → more cache misses.

## When to Use Processes

- Fault isolation (browser tabs)
- Security sandboxing
- Untrusted code
- Independent restart

## When to Use Threads

- Shared memory access
- Low-latency communication
- High-frequency spawning
- Thread pools

## Hybrid Approaches

- **Process pool**: Preforked workers with shared accept()
- **Thread pool**: Concurrent request handling within process

## Related Concepts

- [[algomaster-Concurrency vs Parallelism]]
- [[Thread Safety]]
- [[Race Conditions]]