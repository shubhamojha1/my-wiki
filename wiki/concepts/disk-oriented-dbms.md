---
title: "Disk-Oriented DBMS"
type: concept
tags: [database, storage, architecture]
created: 2026-04-23
---

# Disk-Oriented DBMS

A **disk-oriented DBMS** is a database management system architecture that assumes the primary storage location is non-volatile disk, not DRAM.

## Characteristics

- **Primary storage on disk**: Database lives on disk, not in memory
- **Explicit I/O**: Program must explicitly read/write pages to/from disk
- **Buffer pool**: Memory cache to hide disk latency
- **Designed for data larger than memory**: Can handle databases exceeding RAM

## Contrast with In-Memory DBMS

| Aspect | Disk-Oriented | In-Memory |
|--------|---------------|-----------|
| Primary storage | Disk | DRAM |
| Persistence | Built-in | Requires durability layer |
| Examples | PostgreSQL, MySQL, Oracle | MemSQL, SAP HANA |

## Design Goals

1. **Handle datasets larger than memory**: Move data between disk and memory
2. **Minimize disk I/O**: Read/write in large blocks, sequential access preferred
3. **Durability**: Survive crashes with [[Write-Ahead Logging]]

## Related

- [[Storage Manager]] — Manages disk I/O
- [[Buffer Pool]] — Memory cache for disk pages
- [[Database Page]] — Unit of disk I/O
- [[Write-Ahead Logging]] — Durability mechanism