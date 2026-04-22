---
title: "Database Page"
type: concept
tags: [database, storage, page]
created: 2026-04-23
---

# Database Page

A **page** (or database page) is a fixed-size block of data that the DBMS uses to organize data on disk and in memory. It is the fundamental unit of I/O and storage allocation.

## Characteristics

- **Fixed size**: Typically 4KB-16KB (e.g., PostgreSQL 8KB, MySQL 16KB, Oracle ~8KB)
- **Self-contained**: Often includes all metadata needed to read the page
- **Contains**: Tuples, indexes, or metadata—but typically not mixed types

## Page Types

- **Data page**: Contains actual tuple/row data
- **Index page**: Contains B+Tree or other index entries
- **Page directory**: Metadata about other pages (used in heap files)

## Page Header

Each page typically includes:
- Page ID / address
- Checksum or magic number
- Size information
- Free space pointer

## Related

- [[Heap File]] — Pages organized as unordered collection
- [[Buffer Pool]] — Memory cache of pages
- [[Storage Manager]] — Component managing page I/O
- [[Tuple]] — Row data stored within pages