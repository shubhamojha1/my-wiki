---
title: "Partial Index"
type: concept
tags: [database, index, optimization]
created: 2026-04-23
---

# Partial Index

A **partial index** is an index created on a subset of a table, defined by a WHERE clause.

## How It Works

- `CREATE INDEX idx ON table(col) WHERE condition`
- Only indexes rows matching condition
- Smaller than full table index

## Benefits

- **Smaller size**: Less data to index
- **Faster writes**: Less to maintain on insert/update
- **Targeted queries**: Optimizes specific query patterns

## Use Cases

- Index recent data (time-based)
- Index frequently accessed rows
- Index specific categories

## Related

- [[Index Scan]] — Access method
- [[B+Tree]] — Common index structure