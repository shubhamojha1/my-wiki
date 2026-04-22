---
title: "Sequential Scan"
type: concept
tags: [database, query, execution, access-method]
created: 2026-04-23
---

# Sequential Scan

A **sequential scan** reads all pages of a table from disk, checking each tuple against the query predicate.

## How It Works

1. Read pages from heap file in order
2. For each tuple, evaluate WHERE conditions
3. Return matching tuples

## When to Use

- Small tables
- No suitable index
- Query selects large portion of table
- Index scan would be more expensive

## Trade-offs

- **Pros**: Simple, no index needed, good for full scans
- **Cons**: Reads entire table, slow for selective queries

## Optimization

- **Parallel scan**: Read pages in parallel
- **Storage layout**: Cluster data on common access patterns

## Related

- [[Index Scan]] — Alternative access method
- [[Query Plan]] — Where sequential scan appears
- [[Heap File]] — Data source