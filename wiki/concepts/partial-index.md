---
title: "Partial Index"
type: concept
tags: [database, index, optimization, sql]
created: 2026-04-23
updated: 2026-05-20
sources: [cmu_15-445_lec07]
---

# Partial Index

A **partial index** (also called a **filtered index**) is a database index built on a subset of rows in a table, defined by a predicate in a `WHERE` clause. Only rows satisfying the predicate are included.

## Syntax

```sql
-- PostgreSQL / SQLite
CREATE INDEX idx_active_users ON users(email) WHERE active = TRUE;

-- SQL Server
CREATE INDEX idx_pending_orders ON orders(created_at) WHERE status = 'PENDING';
```

## Benefits

| Benefit | Why |
|---------|-----|
| **Smaller index** | Fewer rows → less storage, faster scans |
| **Faster writes** | Only insert into index when predicate is true |
| **Query optimizer hint** | Highly selective on the filtered subset |
| **Targeted optimization** | Optimize for the most-queried slice of data |

## Use Cases

- **Status-filtered queries** — index only active/pending/open records (most queries target these)
  ```sql
  SELECT * FROM orders WHERE status = 'OPEN' AND user_id = 42;
  -- Index: orders(user_id) WHERE status = 'OPEN'
  ```
- **Non-null columns** — index only rows where an optional column is set
  ```sql
  CREATE INDEX idx_verified ON users(verified_at) WHERE verified_at IS NOT NULL;
  ```
- **Time-windowed data** — index recent records when older records are rarely queried
- **Soft-delete pattern** — index only `deleted_at IS NULL` (active) records

## When the Optimizer Uses It

The optimizer can use a partial index for a query **only if the query's WHERE clause implies the index's predicate**. For example, `WHERE status = 'OPEN' AND user_id = 42` implies `status = 'OPEN'`, so the partial index above applies.

## Comparison

| Index Type | Covers | Size | Best For |
|-----------|--------|------|---------|
| Full index | All rows | Large | General queries |
| Partial index | Filtered rows | Small | Specific high-frequency queries |
| [[Filtered Index]] | Same as partial | Small | Term used in SQL Server |

## Related Concepts

- [[Database Index]] — general concept
- [[Filtered Index]] — SQL Server terminology for same concept
- [[B-Tree]] — typical underlying structure
- [[Covering Index]] — another optimization; includes query columns in index
