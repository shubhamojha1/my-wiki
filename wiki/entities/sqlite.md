---
title: "SQLite"
type: entity
tags: [database, embedded, file-based]
created: 2026-04-23
---

# SQLite

**SQLite** is a lightweight, embedded, file-based relational database engine. It is the most widely deployed database in the world.

## Characteristics

- **Single file**: Entire database stored in one file (`.db` or `.sqlite`)
- **Embedded**: No separate server process, runs in the application
- **Zero-configuration**: No setup or administration required
- **ACID compliant**: Provides atomic transactions despite being embedded

## Architecture

SQLite uses a [[Heap File]] organization where pages are stored sequentially in a single file. It includes:
- **Page cache**: In-memory buffer of pages
- **B-Tree indexes**: For fast lookups
- **WAL mode**: Write-Ahead Logging for concurrent reads/writes

## Use Cases

- Mobile apps (iOS, Android)
- Embedded systems
- Web browsers
- Desktop applications
- Testing and development

## Related

- [[Heap File]] — Storage organization
- [[Database Page]] — Storage unit
- [[BusTub]] — CMU's educational DBMS (similar architecture)