---
title: "Function-Based Index"
type: concept
tags: [database, index, function]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Function-Based Index

A **function-based index** (also called an expression index) is built on the result of a deterministic function or expression applied to one or more columns. The database stores and searches the pre-computed expression values rather than raw column data.

## How It Works

The index key is `f(column)`. At index time the database evaluates `f(col)` for every row and stores those values in the B-tree. At query time, a query predicate `WHERE f(col) = ?` can use the index — but `WHERE col = ?` cannot (they are different keys).

## Common Examples

```sql
-- Case-insensitive name lookup (PostgreSQL / Oracle)
CREATE INDEX idx_name_lower ON employees (LOWER(last_name));
SELECT * FROM employees WHERE LOWER(last_name) = 'smith';

-- Date part extraction
CREATE INDEX idx_year ON orders (EXTRACT(YEAR FROM created_at));
SELECT * FROM orders WHERE EXTRACT(YEAR FROM created_at) = 2024;

-- Computed column (total price)
CREATE INDEX idx_total ON order_items (quantity * unit_price);

-- JSON field (PostgreSQL)
CREATE INDEX idx_email ON users ((data->>'email'));
```

## Requirements

- The function **must be deterministic** — same input always gives same output. Non-deterministic functions (e.g., `NOW()`, `RANDOM()`) are rejected.
- The query must use the **exact same expression** as the index definition (the planner matches them textually or via equivalence rules).
- Most databases require the index owner to have execute privilege on the function.

## Advantages and Trade-offs

| Aspect | Detail |
|--------|--------|
| **Eliminates full table scan** | Queries that previously needed a sequential scan for `LOWER(col)` can now use the index |
| **Replaces computed columns** | Avoids adding a persisted computed column just for indexing |
| **Write overhead** | `f(col)` must be recomputed on every INSERT/UPDATE to the indexed column |
| **Planner awareness** | Query must match the expression exactly; use generated/virtual columns where planner matching is unreliable |

## Database Support

| Database | Syntax |
|----------|--------|
| PostgreSQL | `CREATE INDEX ON t ((expr))` — double parens for expressions |
| Oracle | `CREATE INDEX ON t (FUNCTION(col))` — native since Oracle 8i |
| MySQL 8+ | Functional indexes via `((expr))` syntax, or generated columns |
| SQL Server | Computed columns with `PERSISTED` and an index on them |

## Related Concepts

- [[Database Index]] — general index concepts
- [[Partial Index]] — indexes a subset of rows (orthogonal feature, can be combined)
- [[Covering Index]] — includes non-key columns to avoid table lookup
