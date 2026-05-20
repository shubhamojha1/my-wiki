---
title: "Latch"
type: concept
tags: [database, concurrency, data-structure]
created: 2026-04-23
updated: 2026-05-20
---

# Latch

A **latch** is a lightweight synchronization primitive used by a DBMS to protect **in-memory data structures** from concurrent access. Unlike a transaction lock (which can be held for the duration of a transaction), a latch is held only for the duration of a single physical operation — typically microseconds.

## Latch vs Lock

| Aspect | Latch | Lock |
|--------|-------|------|
| What it protects | In-memory structures (B+Tree pages, buffer pool page table) | Logical database objects (rows, tables, pages) for transactions |
| Duration | Microseconds (one operation) | Milliseconds to seconds (transaction) |
| Held by | Thread (OS scheduler may preempt) | Transaction |
| Deadlock | Prevention by design (strict ordering, no-wait, or try-latch) | Detection + resolution (deadlock graph, waits-for graph) |
| Rollback on release | Not applicable | Can be rolled back |
| Concurrency modes | Read (shared), Write (exclusive) | S, X, IS, IX, SIX, and more |

## How Latches Are Implemented

| Implementation | Mechanism | Use case |
|---------------|-----------|---------|
| **Spin latch** | CAS (compare-and-swap) loop — no OS call | Very short critical sections; avoids context switch overhead |
| **Mutex** | OS futex (Linux) — blocks in kernel when contended | Longer waits; more efficient than spinning under high contention |
| **Reader-Writer latch** | Multiple shared (read) holders; exclusive (write) holder | Buffer pool page table, B+Tree interior nodes |

## Latching in B+Trees (Crabbing Protocol)

To safely traverse a B+Tree while other threads modify it, the DBMS uses **latch crabbing**:

**Read path**: acquire shared latch on child, release parent latch — always hold child before releasing parent.

**Write path**: acquire exclusive latch on each node; release parent latch only when child is confirmed safe (not going to split or merge).

This prevents corruption without blocking reads for the entire tree.

## Latch Modes

| Mode | Description | Conflict with |
|------|-------------|--------------|
| **Read (shared)** | Any number of threads can read simultaneously | Write only |
| **Write (exclusive)** | One thread writes; all others block | Read + Write |

## Where Latches Are Used

- [[Buffer Pool]] page table: reading/updating frame metadata
- [[B+Tree]] interior and leaf nodes: during traversal and modification
- [[Page Table]] hash buckets: concurrent page lookup
- WAL buffer: writing log records concurrently

## Related Concepts

- [[Lock]] — transaction-level concurrency control
- [[Reader-Writer Latch]] — the R/W variant with shared/exclusive modes
- [[B+Tree]] — uses latch crabbing during tree traversal
- [[Critical Section]] — the protected region a latch guards
