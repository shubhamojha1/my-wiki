---
title: "Storage Manager"
type: concept
tags: [database, storage, io]
created: 2026-04-23
---

# Storage Manager

The **storage manager** is the DBMS component responsible for managing the physical storage of data on disk.

## Responsibilities

- **File management**: Create, read, write, delete database files
- **Space allocation**: Allocate/deallocate pages
- **Buffer management**: Manage the [[Buffer Pool]] (moving data between disk and memory)
- **Crash recovery**: Ensure durability of writes

## Key Operations

- `Read(page_id)` — Fetch a page from disk to memory
- `Write(page_id)` — Flush a modified page to disk
- `Allocate()` — Create a new page
- `Deallocate()` — Free a page

## Write-Ahead Logging (WAL)

The storage manager typically uses WAL to ensure durability:
1. Write modifications to a log first (durable)
2. Modify the data page in memory
3. Flush log on commit
4. Later, write modified pages to disk (checkpoint)

## Related

- [[Database Page]] — Unit of storage
- [[Buffer Pool]] — Memory cache
- [[Disk-Oriented DBMS]] — Architecture using storage manager
- [[Write-Ahead Logging]] — Durability mechanism