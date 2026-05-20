---
title: "Covering Index"
type: concept
tags: [database, index, optimization]
created: 2026-04-23
updated: 2026-05-20
---

# Covering Index

A **covering index** includes all columns that a query needs — both for filtering/joining and for the SELECT list — so the database can answer the query entirely from the index without touching the table (an **index-only scan**).

## Why It Matters

A normal secondary index lookup requires two steps:
1. Traverse the index B-tree to find the matching key(s).
2. Follow each row pointer back to the table heap to fetch non-indexed columns (**bookmark lookup**).

Step 2 is random I/O, and for large result sets it is the dominant cost. A covering index eliminates it.

## Example

```sql
-- Table: orders(id, customer_id, status, total, created_at)

-- Query:
SELECT customer_id, total
FROM orders
WHERE status = 'pending';

-- Non-covering index (only status):
CREATE INDEX idx_status ON orders (status);
-- → index scan on status, then heap lookup for customer_id and total

-- Covering index:
CREATE INDEX idx_status_covering ON orders (status, customer_id, total);
-- → index-only scan; table never touched
```

## Column Ordering in a Covering Index

For a B-tree covering index, the key columns (used in WHERE, JOIN, ORDER BY) must come first; extra "payload" columns come after:

```
(key_col_1, key_col_2, ..., payload_col_1, payload_col_2)
```

In PostgreSQL, use `INCLUDE`:
```sql
CREATE INDEX idx_status_cover ON orders (status) INCLUDE (customer_id, total);
```
The `INCLUDE` columns are stored only in leaf pages, keeping interior nodes small.

## Trade-offs

| Aspect | Covering Index | Plain Secondary Index |
|--------|---------------|----------------------|
| Read performance | Faster (no heap lookup) | Slower (random I/O per row) |
| Index size | Larger (stores extra columns) | Smaller |
| Write overhead | Higher (more data maintained) | Lower |
| Maintenance | More expensive for UPDATE on covered cols | Less expensive |

## When to Use

- High-frequency queries that select a small fixed set of columns.
- Queries with large result sets where heap lookup dominates execution time.
- Read-heavy analytics on OLTP tables.
- Avoid for write-heavy tables or when covered columns change often.

## Database Support

| Database | Syntax |
|----------|--------|
| PostgreSQL 11+ | `INCLUDE (col1, col2)` |
| MySQL / MariaDB | Include columns in composite index naturally |
| SQL Server | `CREATE INDEX ... INCLUDE (col1, col2)` |
| Oracle | Index-organized tables; `covering` via composite key |

## Related Concepts

- [[Database Index]] — general index concepts
- [[Secondary Index]] — non-covering; requires heap lookup
- [[Index Scan]] — the access method used for covering queries
- [[Partial Index]] — covers a subset of rows; can be combined with covering
- [[Clustered Index]] — the table itself is the index; always "covering" for primary key lookups
