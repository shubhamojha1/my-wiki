---
title: "Processes vs Threads"
type: concept
tags: [process, thread, concurrency]
created: 2026-04-24
sources: [algomaster-introduction-to-concurrency, algomaster-processes-vs-threads]
---

# Processes vs Threads

Both enable concurrent execution but differ fundamentally in isolation and sharing.

## Process

A **process** is an instance of a running program with its own address space. The OS isolates processes from each other.

- **Separate address space** — Cannot access another process's memory
- **Resources** — Open file handles, sockets, environment variables
- **Security context** — User ID, permissions, capabilities
- **Program state** — PC, CPU registers, stack pointer
- **Communication** — IPC (pipes, sockets, message queues)
- **Fault isolation** — Process crash doesn't affect others

## Thread

A **thread** is a unit of execution within a process. Each process has at least one main thread.

- **Shared address space** — All threads in a process share memory
- **Own stack** — Each thread has private stack
- **Lightweight** — Create fast (~1ms), switch fast
- **Communication** — Direct memory access (no IPC needed)
- **Shared fate** — One thread crash terminates all

## Key Differences

| Aspect | Process | Thread |
|--------|---------|--------|
| **Address Space** | Separate | Shared |
| **Memory Isolation** | Yes | No |
| **Creation Cost** | High (~100ms) | Low (~1ms) |
| **Communication** | IPC required | Direct memory |
| **Fault Isolation** | Strong | Weak (all die) |
| **Context Switch** | Slow (3-10µs) | Fast |

## Context Switching

From AlgoMaster:

- **Process switch**: Save CPU state → load next state → **switch memory mappings** → potentially disrupt caches
- **Thread switch**: Save CPU state → load next state (no address space change)

Process switches require changing virtual address space → TLB flush → cache misses.

## When to Use Processes

- **Fault isolation** — One tab crash doesn't kill browser
- **Security sandboxing** — Untrusted plugins
- **Different privilege levels** — Minimal permissions
- **Independent restart** — Crash doesn't cascade

## When to Use Threads

- **Shared data** — Fast in-memory communication
- **High-frequency tasks** — Thread pools
- **Low latency** — No IPC overhead

## Hybrid Approaches

- **Process pool** — Preforked workers, shared accept() socket
- **Thread pool** — Handle concurrent requests within process

## Related

- [[Concurrency vs Parallelism]]
- [[Thread Safety]]
- [[Race Conditions]]