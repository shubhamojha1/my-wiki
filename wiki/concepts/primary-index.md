---
title: "Primary Index"
type: concept
tags: [database, index, primary-key]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Primary Index

A **primary index** is automatically created when a primary key constraint is defined on a table. It ensures uniqueness and enables fast lookups via the primary key.

## Characteristics

- **Automatic**: Created implicitly with PRIMARY KEY constraint
- **Unique**: Enforces uniqueness of key values
- **Fast lookups**: Optimized for point queries on the primary key
- **Often clustered**: Many DBMS default to making the primary key the clustered index

## Related

- [[Primary Key]] — The column(s) the index is built on
- [[Clustered Index]] — Primary index is often implemented as clustered
- [[Database Index]] — General concept of database indexes
