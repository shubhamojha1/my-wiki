---
title: "Index-Organized Table"
type: concept
tags: [database, storage, index, btree]
created: 2026-04-23
---

# Index-Organized Table (IOT)

An **Index-Organized Table** (IOT) is a storage organization where the table data is stored directly in the leaf nodes of a B+Tree index, using the primary key as the index key.

## How It Works

- **Primary key** is the B+Tree key
- **Leaf nodes** contain the full tuple data (not just pointers)
- Internal nodes contain index keys and child pointers

## Benefits

- **Fast point queries**: Data and index are together (one I/O)
- **Fast range scans**: Leaf nodes are linked, sequential access
- **Space efficient**: No separate heap or index structure

## Trade-offs

- **Slower writes**: Must maintain sort order in B+Tree
- **Large tuples**: Can cause page splits and larger index height
- **Secondary indexes**: Require additional structure (physical row ID)

## Used In

- Oracle
- MySQL (InnoDB)
- SQL Server
- PostgreSQL (BRIN indexes)

## Related

- [[B+Tree]] — The underlying data structure
- [[Heap File]] — Traditional alternative (separate data/index)
- [[Database Page]] — Where leaf nodes store data
- [[Primary Key]] — The index key