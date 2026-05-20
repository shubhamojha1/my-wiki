---
title: "Data Compression"
type: concept
tags: [database, storage, compression]
created: 2026-04-23
updated: 2026-05-20
---

# Data Compression (Databases)

**Data compression** in databases encodes data into a smaller representation to reduce storage, improve I/O throughput, and increase effective cache capacity. The trade-off is CPU time spent compressing and decompressing.

## Why It Helps

Modern CPUs are far faster than disks (and even fast SSDs). Reading 2 GB of compressed data and decompressing it in CPU is faster than reading 8 GB of raw data:

```
Uncompressed:  8 GB disk read  × 1 GB/s = 8 seconds
Compressed 4×: 2 GB disk read  × 1 GB/s = 2 seconds + ~0.2s decompress = 2.2 seconds
```

Benefits compound in the buffer pool: 8× compressed pages means 8× more data fits in RAM.

## Column Stores vs Row Stores

Column stores (Parquet, DuckDB, Redshift, BigQuery) compress far better because each column holds homogeneous data — many repeated values, small variance. Row stores store heterogeneous fields adjacently, defeating many compression algorithms.

## Compression Techniques

| Technique | How it works | Best for |
|-----------|-------------|---------|
| **Run-Length Encoding (RLE)** | Replace `AAABBBBA` with `3A4B1A` | Sorted columns with many repeats (status, date) |
| **Dictionary Encoding** | Map string values to integers; store compact integer codes | Low-cardinality strings (country, product name) |
| **Delta Encoding** | Store differences: `[100, 102, 105]` → `[100, +2, +3]` | Sorted numeric columns (timestamps, IDs) |
| **Bit-Packing** | Use only necessary bits: values 0–7 need 3 bits, not 64 | Integer columns with bounded range |
| **Frame-of-Reference (FOR)** | Store min value + small offsets | Monotone integer sequences |
| **LZ4 / Snappy / Zstd** | General-purpose byte-level compression | Row-store pages, Parquet pages, network |

## Compression Granularity

| Level | Scope | Used in |
|-------|-------|---------|
| **Column-segment** | One column of one row group | Parquet, Arrow, ORC |
| **Page-level** | One 4KB–16KB database page | PostgreSQL TOAST, InnoDB row compression |
| **Block/segment** | Multi-megabyte compressed segments | Redshift, BigQuery columnar storage |

## Lossless vs Lossy

All database compression is **lossless** — exact values must be recoverable. (Lossy compression is for media, not transactional or analytical data.)

## Late Materialization

Compressed columnar systems can operate directly on compressed data for filtering (e.g., RLE run can be filtered without decompressing every element) — this is called **operating on compressed data** or **late materialization**.

## Related Concepts

- [[Run-Length Encoding]] — consecutive identical values
- [[Column Store]] — natural fit for columnar compression
- [[Database Page]] — unit of page-level compression
- [[Buffer Pool]] — more data fits when pages are compressed
