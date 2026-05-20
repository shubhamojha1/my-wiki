---
title: "Filtered Index"
type: concept
tags: [database, index, optimization]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Filtered Index

A **filtered index** (SQL Server term; PostgreSQL calls it a [[Partial Index]]) indexes only the rows that satisfy a predicate. Instead of indexing every row in the table, it maintains a smaller, more focused index over a specific subset.

## How It Works

```sql
-- SQL Server / PostgreSQL syntax:
CREATE INDEX idx_active_orders
ON orders (order_date)
WHERE status = 'active';
```

Only rows where `status = 'active'` appear in the index. The optimizer uses this index only when the query includes a compatible predicate.

## Why Use a Filtered Index

A typical `orders` table might have 10M rows: 9.5M completed, 0.5M active. An index on `(order_date)` over all 10M rows is large. A filtered index on active orders only is 5% the size:

```
Full index: 10M entries    → ~1.5 GB
Filtered:    500K entries  → ~75 MB   (20× smaller)
```

Benefits:
- **Smaller**: Fits in buffer pool; fewer I/O operations
- **Faster writes**: Only active orders require index maintenance on INSERT/UPDATE
- **Faster reads**: Index is denser — fewer pages to scan

## When the Optimizer Uses It

The query must include the filter predicate (or a compatible superset):

```sql
-- Uses the filtered index:
SELECT * FROM orders WHERE status = 'active' AND order_date > '2026-01-01';

-- Does NOT use the filtered index (status may not be 'active'):
SELECT * FROM orders WHERE order_date > '2026-01-01';
```

## Common Use Cases

| Pattern | Filtered Index |
|---------|---------------|
| **Soft deletes** | `WHERE deleted_at IS NULL` — index only live rows |
| **Active records** | `WHERE status = 'active'` — sparse active set in a large table |
| **Null exclusion** | `WHERE email IS NOT NULL` — avoid sparse column overhead |
| **Recent data** | `WHERE created_at > '2026-01-01'` — combined with partition pruning |
| **Unique partial key** | `WHERE deleted_at IS NULL` + UNIQUE — allows multiple deleted records with same email |

## Filtered Index vs Full Index vs Partial Index

| Term | Database | Notes |
|------|----------|-------|
| **Filtered index** | SQL Server | Standard term; same concept |
| **Partial index** | PostgreSQL | Identical concept, different name |
| **Full index** | All | No WHERE clause; indexes every row |

## Related Concepts

- [[Partial Index]] — same concept in PostgreSQL
- [[Covering Index]] — includes all query columns; can be combined with filtered
- [[Database Index]] — general index concepts
- [[Function-Based Index]] — orthogonal: indexes an expression rather than a column value
