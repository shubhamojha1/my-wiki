---
title: "Clustered Index"
type: concept
tags: [database, index, btree]
created: 2026-04-23
---

# Clustered Index

A **clustered index** determines the physical order of data in a table. The table is stored sorted by the index key.

## Characteristics

- **One per table**: Only one clustered index (data can only be in one order)
- **Table is the index**: Leaf nodes contain actual row data
- **Usually on primary key**: Unless specified otherwise
- **Range scans efficient**: Data sorted on disk

## Trade-offs

- **Pros**: Fast range scans, point queries on PK
- **Cons**: INSERT/UPDATE slower (must maintain order), secondary indexes slower

## Related

- [[B+Tree]] — Usually the underlying structure
- [[Secondary Index]] — Additional indexes point to clustered index
- [[Index-Organized Table]] — Extreme form of clustering