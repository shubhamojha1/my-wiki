---
title: "Processes vs Threads"
type: concept
tags: [process, thread, concurrency]
created: 2026-04-24
sources: [introduction-to-concurrency]
---

# Processes vs Threads

Both enable concurrent execution but differ fundamentally in isolation and sharing.

## Process

A **process** is an instance of a running program with its own address space. The OS isolates processes from each other.

- **Separate address space** — Cannot access another process's memory
- **Heavyweight** — Full isolation, each process has own resources
- **Communication** — IPC (pipes, sockets, message queues)
- **Fault isolation** — Process crash doesn't affect others

## Thread

A **thread** is a unit of execution within a process. Each process has at least one main thread.

- **Shared address space** — All threads in a process share memory
- **Lightweight** — Create fast, switch fast
- **Communication** — Direct memory access (no IPC needed)
- **Fault risk** — One thread bug can corrupt shared memory

## Key Differences

| Aspect | Process | Thread |
|--------|---------|--------|
| **Address Space** | Separate | Shared |
| **Memory Isolation** | Yes | No |
| **Creation Cost** | High | Low |
| **Communication** | IPC required | Direct memory |
| **Fault Isolation** | Strong | Weak |
| **Context Switch** | Slow | Fast |

## When to Use Processes

- **Isolation needed** — Untrusted code, clean failure boundaries
- **Different address space** — Security sandboxing
- **Memory protection** — Prevent corruption from bugs

## When to Use Threads

- **Shared data** — Fast communication, low latency
- **Same address space** — Libraries requiring shared state
- **High-frequency spawning** — Thread pools for requests

## Hybrid Approaches

Real systems often use both:

- **Process pool pattern** — Preforked processes, shared accept() socket
- **Thread pool within process** — Handle concurrent requests

## Related

- [[Concurrency vs Parallelism]]
- [[Thread Safety]] — Correct behavior with shared memory
- [[Race Conditions]] — Incorrect behavior from unsynchronized access
- [[Introduction to Concurrency]]