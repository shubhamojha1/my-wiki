---
title: "Bitmap Index"
type: concept
tags: [database, index, bitmap, analytics]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Bitmap Index

A **bitmap index** represents the presence of each distinct key value as a separate bit-vector — one bit per row. Row i has bit=1 in the bitmap for value V if column[i] = V.

## Example

Table `orders` with `status` column (3 values: `pending`, `shipped`, `cancelled`):

```
Row:       1  2  3  4  5  6
status:    P  S  C  P  S  P

Bitmap for "pending":   1  0  0  1  0  1
Bitmap for "shipped":   0  1  0  0  1  0
Bitmap for "cancelled": 0  0  1  0  0  0
```

Query: `WHERE status = 'pending' OR status = 'shipped'`
→ OR the two bitmaps: `1 1 0 1 1 1` → rows 1, 2, 4, 5, 6

Multi-condition queries run as fast **bitwise AND/OR/NOT** operations — CPU-cache-friendly and SIMD-acceleratable.

## When to Use

| Factor | Bitmap is Good | B-Tree is Better |
|--------|---------------|-----------------|
| Cardinality | Low (< ~100 distinct values) | High (user IDs, emails) |
| Workload | Read-heavy OLAP | Write-heavy OLTP |
| Query pattern | Multi-column AND/OR | Point lookup, range scan |
| Concurrency | Low write concurrency | High write concurrency |

## Limitations

- **High write cost**: Inserting or updating a row requires modifying every bitmap for that column — poor for OLTP.
- **High-cardinality columns**: One bitmap per distinct value; 1M unique values = 1M bitmaps (use B-tree instead).
- **Locking**: Traditional bitmap index updates require coarse locks; concurrent writes serialize.

## Compression

Bitmaps are sparse (mostly 0s for high-cardinality). Run-length encoding (RLE) variants like **WAH** (Word-Aligned Hybrid) or **EWAH** keep them compact and still allow bitwise ops without decompression.

## Where Used

- Oracle Bitmap Indexes (primary use case: data warehouses)
- Apache Parquet / columnar stores (built-in RLE+bitpacking for low-cardinality columns)
- Roaring Bitmaps library (used in Lucene, Druid, Spark)

## Related Concepts

- [[Database Index]] — general index concepts
- [[B+Tree]] — preferred for high-cardinality or OLTP workloads
- [[Full-Text Index]] — uses bitmaps internally for posting lists
- [[Columnar Storage]] — natural home for bitmap indexes
