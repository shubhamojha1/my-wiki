---
title: "Database Index"
type: concept
tags: [database, index, performance]
created: 2026-05-11
sources: [algomaster-indexing]
---

# Database Index

A **database index** is a lookup structure that enables fast data retrieval without scanning every row in a table. It holds indexed column values along with pointers to corresponding rows.

## Analogy

Like a book's index: sorted alphabetically with page numbers, it tells you exactly where to look rather than flipping through every page.

## How It Works

1. **Index creation**: DBA creates index on a column or set of columns
2. **Index building**: DBMS scans the table, stores indexed values + row pointers
3. **Query execution**: Engine checks if an index exists for the queried columns
4. **Index search**: Searches the index using the pointer to locate data
5. **Data retrieval**: Fetches the requested data via the pointer

## Benefits

- Faster query performance (especially on large datasets)
- Reduced CPU usage (fewer rows scanned)
- Rapid data retrieval for equality and range conditions
- Efficient sorting without expensive sort operations

## Trade-offs

- Extra disk space (additional data structures alongside tables)
- Slower writes (INSERT/UPDATE/DELETE must update the index)
- Over-indexing hurts write performance

## Related

- [[Primary Index]] — Index on the primary key
- [[Clustered Index]] — Data physically ordered by index key
- [[Secondary Index]] — Non-clustered alternate access path
- [[Dense Index]] — Entry for every search key
- [[Sparse Index]] — Entry for some search keys
- [[B+Tree]] — Most common underlying structure
- [[Hash Index]] — For exact-match lookups
- [[Bitmap Index]] — For low-cardinality columns
