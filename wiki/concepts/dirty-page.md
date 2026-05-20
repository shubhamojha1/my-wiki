---
title: "Dirty Page"
type: concept
tags: [database, storage, buffer-pool]
created: 2026-04-23
updated: 2026-05-20
---

# Dirty Page

A **dirty page** is a database page that has been modified in the [[Buffer Pool]] (RAM) but whose changes have not yet been written back to disk. The on-disk version is stale; the in-memory version is authoritative until flushed.

## Lifecycle

```
Disk page P ──[load into buffer pool]──→ Frame F (clean)
                                              │
                                    [UPDATE: modify row]
                                              │
                                              ↓
                                         Frame F (dirty)   ← "dirty page"
                                              │
                           ┌──────────────────┴──────────────────┐
                           │ eviction needed                      │ checkpoint
                           ↓                                      ↓
                     [flush to disk]                        [flush to disk]
                           │                                      │
                      Frame F (clean)                        Frame F (clean)
```

## Why Not Write Immediately?

**Write-back caching** defers flushes for performance:
- Multiple updates to the same page are batched into one disk write.
- If a page is updated and immediately evicted with no reads in between, only one I/O happens instead of N.
- Disk I/O is sequential-write friendly during checkpoint flushes (sorted by page ID).

Write-**through** (flush on every write) is an alternative — simpler but slower. Most DBMSes use write-back.

## WAL Requirement (Write-Ahead Logging)

A dirty page must **not** reach disk before its corresponding WAL (Write-Ahead Log) records do. This is the **WAL protocol / Steal+Force or No-Steal+No-Force** distinction:

- **No-Steal**: Never write dirty pages until commit (safe but uses unlimited buffer pool memory).
- **Steal**: Allow dirty pages to be flushed before commit (requires undo log entries for recovery).
- **No-Force**: Don't flush dirty pages at commit time (requires redo log for recovery).
- **Force**: Flush all dirty pages at commit (safe but slow — common in simpler systems).

Most production DBMSes use **Steal + No-Force** with WAL for maximum performance.

## When Dirty Pages Are Flushed

| Trigger | Description |
|---------|-------------|
| **Checkpoint** | Periodic: DBMS writes all dirty pages to disk, advances WAL recovery point |
| **Eviction** | When the buffer pool is full and a dirty frame must be reused |
| **Commit (No-Force)** | Only if Force policy — not common in modern DBMSes |
| **Background writer** | Some DBMSes (PostgreSQL bgwriter) proactively flush to reduce eviction stalls |

## Related Concepts

- [[Buffer Pool]] — holds dirty pages in RAM
- [[Page Table]] — tracks the dirty flag per frame
- [[Write-Ahead Logging]] — WAL must reach disk before the dirty page does
- [[Checkpoint]] — the event that flushes all dirty pages and truncates the WAL
- [[Frame (Buffer Pool)]] — the memory slot containing the dirty page
