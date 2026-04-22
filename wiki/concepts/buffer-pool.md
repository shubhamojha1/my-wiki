---
title: "Buffer Pool"
type: concept
tags: [database, storage, memory, cache]
created: 2026-04-23
---

# Buffer Pool

The **buffer pool** is the area of memory that caches database pages from disk. It is the core of the DBMS's memory management.

## Purpose

- **Hide I/O latency**: Memory access is ~100,000x faster than disk
- **Reduce disk I/O**: Cache frequently accessed pages
- **Manage concurrency**: Track which transactions have modified pages

## Key Operations

- **Fix (pin)**: Get a page into memory, prevent eviction
- **Unfix (unpin)**: Release a page, allowing eviction
- **Flush**: Write modified pages to disk

## Page States

- **Clean**: In sync with disk
- **Dirty**: Modified but not yet written to disk
- **Pinned**: Currently being used, cannot evict

## Replacement Policies

When the buffer pool is full, the DBMS must evict a page:
- **LRU** (Least Recently Used)
- **Clock** — Approximate LRU
- **LRU-K** — Considers last K accesses
- **CLOCK** — Common in production systems

## Related

- [[Storage Manager]] — Manages the buffer pool
- [[Database Page]] — Unit of caching
- [[Disk-Oriented DBMS]] — Architecture using buffer pools
- [[LRU]] — Common replacement policy