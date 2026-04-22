---
title: "Query Plan"
type: concept
tags: [database, query, execution]
created: 2026-04-23
---

# Query Plan

A **query plan** (or **execution plan**) is a tree of operators that specifies how to execute a query.

## Structure

- **Root**: Returns final result to user
- **Leaves**: Access methods (scans)
- **Internal nodes**: Relational operators (joins, filters)
- **Data flow**: From leaves → root (pull model)

## Example

```
SELECT * FROM A WHERE x > 10
   ↓
Filter(x > 10)
   ↓
SeqScan(A)
```

## Plan Types

- **Logical plan**: Abstract operators (relational algebra)
- **Physical plan**: Implementation-specific operators

## Related

- [[Query Optimization]] — Creating good plans
- [[Iterator Model]] — Plan execution
- [[Sequential Scan]] — Leaf operator
- [[Index Scan]] — Leaf operator