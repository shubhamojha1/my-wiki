---
title: "Index Scan"
type: concept
tags: [database, execution, access-method]
created: 2026-04-23
---

# Index Scan

An **index scan** is a query execution access method that uses an index to find matching tuples.

## How It Works

1. Traverse index to find starting point
2. Either:
   - **Point query**: Single lookup
   - **Range scan**: Follow leaf links
3. Retrieve actual rows (if not covering)

## Types

- **Index-only scan**: All columns from index (covering)
- **Index scan**: Need to fetch from table
- **Index seek**: Using index to narrow to range
- **Index skip scan**: Skip leading index column

## Cost

- Number of I/Os = tree height + rows accessed
- Covering index eliminates table I/O

## Related

- [[B+Tree]] — Common index structure
- [[Clustered Index]] — Determines table access cost
- [[Secondary Index]] — Additional access paths