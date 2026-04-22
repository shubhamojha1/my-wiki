---
title: "Dirty Page"
type: concept
tags: [database, storage, buffer-pool]
created: 2026-04-23
---

# Dirty Page

A **dirty page** is a page in the [[Buffer Pool]] that has been modified (in memory) but has not yet been written back to disk.

## Characteristics

- **Modified**: Contains changes not on disk
- **Buffered**: Write-back cache delays writes for performance
- **Must flush**: Before eviction or checkpoint, dirty pages must be written

## Dirty Bit

The [[Page Table]] tracks dirty status with a flag:
- **Clean**: In sync with disk
- **Dirty**: Modified since last write

## Write-Back Policy

DBMS typically uses write-back caching:
1. Modify page in buffer pool (becomes dirty)
2. Write to disk later (during checkpoint or eviction)
3. This batches I/O for better performance

## Related

- [[Buffer Pool]] — Where dirty pages live
- [[Page Table]] — Tracks dirty status
- [[Checkpoint]] — Point where all dirty pages are flushed
- [[Write-Ahead Logging]] — Ensures durability before dirty pages flush