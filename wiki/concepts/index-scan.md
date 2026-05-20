---
title: "Index Scan"
type: concept
tags: [database, execution, access-method]
created: 2026-04-23
updated: 2026-05-20
---

# Index Scan

An **index scan** is a query access method that uses an index structure to locate matching rows rather than scanning every row in the table. The planner chooses between index scan and sequential scan based on estimated selectivity, index coverage, and row count.

## How It Works (B+Tree)

```
Query: WHERE age = 30

1. Traverse B+Tree from root to leaf:
   root → interior node(s) → leaf containing key 30

2. From the leaf:
   - Point query: retrieve one or a few matching row pointers
   - Range query: follow sibling pointers along the leaf level until key > upper bound

3. For each row pointer:
   - Clustered index: row is in the leaf — no extra I/O
   - Non-clustered index: follow heap pointer to fetch row (random I/O)
```

## Access Method Variants

| Variant | Description | When Used |
|---------|-------------|-----------|
| **Index Scan** | Traverse B+Tree; fetch each row from heap | Selective filter; non-covering index |
| **Index-Only Scan** | All needed columns in the index; no heap access | [[Covering Index]] |
| **Index Range Scan** | Traverse leaf pages for a key range | `BETWEEN`, `>=`, `<` predicates |
| **Index Skip Scan** | Skip the leading index column; enumerate distinct leading values | Query on non-leading column (MySQL 8+, Oracle) |
| **Bitmap Index Scan** | Build bitmap of row IDs from index, then fetch heap pages | Multiple indexes combined (PostgreSQL) |

## Cost Model

```
Cost ≈ (tree height × random I/O cost) + (matching rows × row fetch cost)

For a non-covering secondary index:
  I/Os ≈ log_b(N)   [tree traversal]
       + K           [K matching rows × random heap I/O each]

For a covering index:
  I/Os ≈ log_b(N) + leaf pages spanned   [no heap I/O]
```

The planner switches from index scan to sequential scan when K is large (many matching rows make random I/O more expensive than a full sequential pass).

## When Index Scans Are Chosen

| Condition | Likely plan |
|-----------|-------------|
| High selectivity (< ~5% rows match) | Index scan |
| Low selectivity (> ~20% rows match) | Sequential scan |
| Covering index available | Index-only scan |
| Range predicate on indexed column | Index range scan |
| ORDER BY matches index order | Index scan (avoids sort) |

## Related Concepts

- [[B+Tree]] — the standard index structure traversed
- [[Sequential Scan]] — alternative access method (no index)
- [[Covering Index]] — enables index-only scan
- [[Clustered Index]] — determines if heap fetch is needed
- [[Secondary Index]] — typically requires heap fetch after index traversal
