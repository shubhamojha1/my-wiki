---
title: "Clustered Index"
type: concept
tags: [database, index, btree]
created: 2026-04-23
updated: 2026-05-20
---

# Clustered Index

A **clustered index** physically sorts the table rows on disk according to the index key. The leaf level of the index B-tree *is* the table — leaf pages hold the actual row data, not pointers to rows.

## Structure

```
B-Tree interior nodes  →  leaf pages (= table rows, sorted by key)

Interior:   [50]─────────[100]
            /      |        \
 [1..49]  [50..99] [100..199]  ← leaf pages contain full rows
```

Because rows are physically ordered, a range scan like `WHERE id BETWEEN 50 AND 99` reads one contiguous run of pages — no random I/O.

## Key Rules

- **One per table**: Data can only be sorted one way; SQL Server, MySQL (InnoDB) auto-cluster on the primary key.
- **PostgreSQL exception**: PostgreSQL heaps are not physically clustered; `CLUSTER` is a one-time sort, not maintained on writes. "Clustered index" in PG documentation means something different.
- **Secondary indexes store the PK**: Non-clustered indexes on a clustered table store the clustered key value (not a page pointer) as the row locator, so secondary lookup requires two B-tree traversals.

## Trade-offs

| Aspect | Clustered | Non-Clustered (Heap) |
|--------|-----------|---------------------|
| Range scan | Very fast (sequential I/O) | Random I/O per row |
| Point lookup on key | Fast | Fast |
| INSERT (random key) | Page splits, fragmentation | Append to heap |
| Secondary index lookup | Two B-tree traversals | One B-tree + heap fetch |
| Table size | PK stored once (in leaf) | PK + extra pointer |

## When Not to Cluster on PK

- **UUID primary keys**: Random UUIDs cause near-100% page split rate; use sequential UUIDs (`UUID v7`) or a surrogate auto-increment key instead.
- **Write-heavy hot spots**: Monotonically increasing keys concentrate inserts on the rightmost page ("hot page" contention).

## Related Concepts

- [[B+Tree]] — the underlying structure
- [[Primary Index]] — often implemented as the clustered index
- [[Secondary Index]] — stores clustered key as row locator
- [[Database Page]] — physical leaf pages hold the actual rows
- [[Index-Organized Table]] — Oracle term for clustered index table
