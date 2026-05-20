---
title: "Primary Index"
type: concept
tags: [database, index, primary-key, storage]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Primary Index

A **primary index** is the index automatically created on a table's primary key column(s). It enforces uniqueness and provides the fastest path to retrieve rows by their primary key.

## Characteristics

- **Automatic** — created implicitly when a `PRIMARY KEY` constraint is defined
- **Unique** — rejects duplicate key values; each row must have a distinct primary key
- **Fast point lookups** — the DBMS uses the primary index for `WHERE id = ?` queries
- **Often clustered** — many DBMSs (InnoDB/MySQL, SQL Server) physically sort table rows by the primary key, making the primary index a [[Clustered Index]]

## Primary Index vs Clustered Index

These terms are often used interchangeably but are distinct:

| | Primary Index | Clustered Index |
|--|--------------|----------------|
| Definition | Index on the primary key column(s) | Index that determines physical row order |
| Count per table | 1 | 1 |
| Relationship | Usually implemented as clustered | May or may not be on primary key |
| In InnoDB | Yes, always clustered | Always exists (defaults to PK if defined) |
| In PostgreSQL | Primary key creates a B-tree index | Heap tables; CLUSTER command for physical sort |

## Impact on Secondary Indexes

In clustered primary index implementations (e.g., InnoDB), [[Secondary Index]] leaf nodes store the **primary key value** (not the physical row location). This means a secondary index lookup first finds the primary key, then does a second lookup in the primary index — called a **double lookup** or **bookmark lookup**.

## Related Concepts

- [[Primary Key]] — the column(s) the primary index is built on
- [[Clustered Index]] — the physical row ordering index; often the same as primary index
- [[Secondary Index]] — additional indexes; reference primary index in clustered implementations
- [[Database Index]] — general concept of database indexes
- [[B-Tree]] — the data structure typically used for primary indexes
