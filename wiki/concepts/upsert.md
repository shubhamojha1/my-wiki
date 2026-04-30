---
title: "Upsert"
type: concept
tags: [database, system-design, pattern]
created: 2026-05-01
sources: [algomaster-idempotency.md]
---

# Upsert

A database operation that updates an existing record if it exists, or inserts a new record if it doesn't.

## Purpose

Achieves idempotency at the database level by ensuring that repeated insertions of the same logical record result in a single, correct state.

## SQL Implementation

```sql
INSERT INTO items (item_id, stock)
VALUES ('item_1', 10)
ON CONFLICT (item_id) 
DO UPDATE SET stock = stock + EXCLUDED.stock;
```

- If `item_1` doesn't exist: inserts new row with stock=10
- If `item_1` exists: adds 10 to existing stock

## Benefits

- Eliminates duplicate records
- Simplifies application logic (no need to check-then-insert)
- Atomic at database level (no race conditions)

## Use Cases

- Inventory management
- Counter increments
- Merging data from external sources
- [[Event Idempotency]] in [[Message Queue]] consumers
