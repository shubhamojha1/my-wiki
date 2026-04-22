---
title: "Heap File"
type: concept
tags: [database, storage, heap]
created: 2026-04-23
---

# Heap File

A **heap file** (or heap) is an unordered collection of database pages that stores tuples without any inherent organization.

## Characteristics

- **Unordered**: Tuples are stored in the order they are inserted
- **Simple**: No index structure required
- **Full scan required**: To find a specific tuple, must scan all pages (unless an index exists)

## Operations

- **Insert**: Add new tuple to any page with free space
- **Delete**: Mark tuple as invalid or compact later
- **Scan**: Iterate through all tuples (expensive for large tables)

## Page Directory

Heap files maintain a **page directory** that tracks:
- Which pages exist
- How much free space each page has
- Page locations on disk

## Use Cases

Heap files are suitable for:
- Tables without indexes
- Sequential scans of entire tables
- Workloads dominated by appends

## Related

- [[Database Page]] — Fixed-size blocks making up the heap
- [[B-Tree Index]] — Ordered index structure for fast lookups
- [[Sequential Scan]] — Reading all pages in order
- [[SQLite]] — Uses heap file organization