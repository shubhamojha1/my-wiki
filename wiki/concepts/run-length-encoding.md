---
title: "Run-Length Encoding"
type: concept
tags: [database, compression, encoding]
created: 2026-04-23
updated: 2026-05-20
---

# Run-Length Encoding (RLE)

**Run-length encoding** compresses a sequence of values by replacing consecutive identical values (a "run") with a single `(value, count)` pair. It achieves excellent compression when runs are long and poor compression on random data.

## Basic Encoding

```
Input:     AAAAABBBCC        (10 symbols)
Encoded:   (A,5)(B,3)(C,2)   (3 pairs = 6 symbols → 40% smaller)

Numeric:   [100,100,100,200,200]
Encoded:   [(100,3),(200,2)]
```

## Database Application: Column Stores

RLE shines in **column-oriented storage** when the column is sorted (or has locality). Example: a `status` column with millions of rows, sorted so all `pending` rows come first:

```
Raw column (status):
pending, pending, pending, ..., active, active, ..., closed, closed, ...
1M rows of "pending"           500K "active"         2M "closed"

RLE-encoded:
(pending, 1000000), (active, 500000), (closed, 2000000)
→ 3 entries instead of 3.5 million
```

This enables **late materialization** — filter and aggregate directly on the compressed data without decompressing every row.

## Operating on Compressed Data

With RLE, a `WHERE status = 'active'` query can:
1. Find the `(active, 500000)` run — O(1) with a binary search on the run dictionary.
2. Derive the row range [1M, 1.5M) — no row-by-row scan.
3. Apply aggregations on the run metadata (COUNT = 500000 directly).

## When RLE Is Effective

| Situation | Compression | Example |
|-----------|-------------|---------|
| Sorted low-cardinality column | Excellent | `status`, `country`, `department` |
| Time-series with repeated values | Good | Temperature sensor with stable readings |
| Boolean/flag columns | Good | `is_deleted`, `is_active` |
| Unsorted, high-cardinality | Poor / negative | User IDs, timestamps (each unique) |

## RLE Variants

| Variant | Description |
|---------|-------------|
| **Byte-aligned RLE** | Each (value, count) pair has fixed-width fields |
| **Run-length limited** | Cap run length at a max (to fit in N bits) |
| **WAH (Word-Aligned Hybrid)** | RLE applied to bitmap words; used in bitmap indexes |
| **Oracle RLE** | Column-level RLE in Oracle In-Memory column store |

## Related Concepts

- [[Data Compression]] — the broader compression category
- [[Dictionary Encoding]] — alternative compression for low-cardinality string columns
- [[Column Store]] — the storage format where RLE is most effective
- [[Bitmap Index]] — uses WAH (run-length encoded bitmaps) internally
