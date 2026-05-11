---
title: "Filtered Index"
type: concept
tags: [database, index, optimization]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Filtered Index

A **filtered index** indexes only a subset of rows in a table based on a filter condition. It is a specialized type of [[Database Index]].

## Characteristics

- **Partial coverage**: Only rows matching the WHERE predicate are indexed
- **Smaller size**: Less storage than a full-table index
- **Faster writes**: Fewer index entries to maintain
- **Best for**: Queries that frequently filter on a common condition

## Example

```sql
CREATE INDEX idx_active_orders
ON orders (order_date)
WHERE status = 'active';
```

## Use Cases

- Soft-delete patterns (index only non-deleted rows)
- Status-based queries (index only active records)
- Partitioned data access patterns

## Related

- [[Partial Index]] — Similar but PostgreSQL terminology
- [[Database Index]] — General concept
