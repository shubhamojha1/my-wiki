---
title: "Database Page"
type: concept
tags: [database, storage, page]
created: 2026-04-23
updated: 2026-05-20
---

# Database Page

A **database page** (also called a **block**) is the fundamental unit of I/O and memory management in a DBMS. All disk reads and writes happen in page-sized units; the [[Buffer Pool]] caches pages in RAM.

## Size and Alignment

| Database | Default page size | Configurable? |
|----------|------------------|--------------|
| PostgreSQL | 8 KB | At compile time only |
| MySQL / InnoDB | 16 KB | Yes (4–64 KB) |
| Oracle | 8 KB (OLTP) | Multiple block sizes allowed |
| SQLite | 4 KB | Yes (512 B – 65536 B) |
| SQL Server | 8 KB | No |

Pages are aligned to the OS page size (4 KB) so a single database page fetch = 1–4 OS I/O operations.

## Page Layout

```
┌──────────────────────────────────────────────┐
│  PAGE HEADER                                 │
│  page_id | lsn | checksum | free_space_ptr   │
│  page_type | num_slots | prev_page | next_page│
├──────────────────────────────────────────────┤
│  DATA REGION                                 │
│  Tuples / Index entries (grow →)             │
│                                              │
│  ← free space →                              │
│                                              │
│  Slot array (← grow)                        │
└──────────────────────────────────────────────┘
```

## Page Types

| Type | Contents |
|------|---------|
| **Heap (data) page** | Row tuples in [[Slotted Page]] format |
| **Index page** | B+Tree interior or leaf nodes |
| **Overflow page** | Large variable-length values (TOAST in PostgreSQL, row overflow in InnoDB) |
| **Free space map** | Which pages have free space |
| **Visibility map** | PostgreSQL: which pages have all-visible tuples (for index-only scans) |
| **System catalog page** | Schema metadata |

## Page Header Fields

| Field | Purpose |
|-------|---------|
| **Page ID** | Location on disk (file + offset) |
| **LSN** (Log Sequence Number) | Latest WAL record that modified this page; used for crash recovery |
| **Checksum** | Detect torn pages (partial writes due to power failure) |
| **Free space pointer** | Offset to start of free space region |
| **Page type** | Data, index, overflow, etc. |
| **Prev/Next page** | Doubly-linked list for heap files and B+Tree leaf chains |

## Why Pages Matter for Performance

- All reads/writes are quantized to page size — fetching one tuple fetches the whole page.
- Sequential pages on disk are read in bulk (prefetch), making scans fast.
- Random single-tuple reads cause one full page I/O each — minimizing random access is a primary DB design goal.
- Larger pages hold more tuples per I/O but waste space for small tables.

## Related Concepts

- [[Buffer Pool]] — caches pages in RAM to avoid repeated disk I/O
- [[Slotted Page]] — the standard layout for data pages
- [[Tuple]] — the rows stored inside data pages
- [[Heap File]] — an unordered collection of data pages
- [[Frame (Buffer Pool)]] — the in-memory slot that holds one page
