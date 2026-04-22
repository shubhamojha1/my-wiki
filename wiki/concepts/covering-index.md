---
title: "Covering Index"
type: concept
tags: [database, index, optimization]
created: 2026-04-23
---

# Covering Index

A **covering index** is an index that contains all columns needed to satisfy a query, eliminating the need to access the table.

## How It Works

- All SELECT columns in index
- Query answered entirely from index (index-only scan)
- No table I/O needed

## Implementation

- **MySQL/PostgreSQL**: Include non-key columns
- **Composite index**: Order columns for query coverage
- Trade-off: Larger index, slower writes

## Use Cases

- High-frequency queries on subset of columns
- Read-heavy workloads
- Avoid expensive table lookups

## Related

- [[Index Scan]] — Access method
- [[Index-Organized Table]] — Alternative approach
- [[Secondary Index]] — Non-covering index