---
title: "Row Store"
type: concept
tags: [database, storage, row-oriented]
created: 2026-04-23
---

# Row Store

A **row store** (or **n-ary storage**) stores all attributes of a tuple contiguously in a single page. This is the traditional storage model used by most relational databases.

## How It Works

- Each row's attributes are stored together
- Pages contain multiple complete rows
- Row stored sequentially in [[Heap File]] or [[Slotted Page]]

## Characteristics

- **Fast row access**: Get full row with single I/O
- **Slow column aggregation**: Must read all rows to aggregate one column
- **Good for OLTP**: Point queries, updates, inserts

## Comparison with Column Store

| Aspect | Row Store | Column Store |
|--------|-----------|--------------|
| SELECT * | Fast | Slow (reconstruct) |
| COUNT(col) | Slow (scan all) | Fast (scan one column) |
| Point update | Fast | Slow (update multiple files) |
| Storage | Rows together | Columns separately |

## Use Cases

- Transaction processing (OLTP)
- Applications needing full rows
- Row-level security

## Related

- [[Column Store]] — Alternative storage model
- [[Tuple]] — Unit of storage in row store
- [[OLTP]] — Workload suited for row stores
- [[Slotted Page]] — Page organization