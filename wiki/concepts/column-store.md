---
title: "Column Store"
type: concept
tags: [database, storage, column-oriented]
created: 2026-04-23
---

# Column Store

A **column store** (or **decomposition storage**) stores each attribute in a separate file or region, rather than storing complete rows together.

## How It Works

- Each column stored in separate column file
- Column files may be partitioned by row groups or pages
- Must **reconstruct rows** for queries needing multiple columns

## Characteristics

- **Fast column aggregation**: Scan only needed columns
- **High compression ratio**: Homogeneous data compresses well
- **Slow row reconstruction**: Need to join columns for SELECT *
- **Good for OLAP**: Analytical workloads on few columns

## Optimizations

- **Late materialization**: Delay row reconstruction until needed
- **Vectorized execution**: Process column batches with SIMD
- **Columnar compression**: Better compression due to similar values
- **Run-length encoding**: Compress consecutive identical values

## Comparison with Row Store

| Aspect | Column Store | Row Store |
|--------|--------------|-----------|
| COUNT(col) | Fast (one column) | Slow (read all) |
| SELECT * | Slow (reconstruct) | Fast (one read) |
| Compression | Excellent | Poor |
| Write path | Complex | Simple |

## Examples

- ClickHouse
- Amazon Redshift
- Google BigQuery
- Apache Druid
- Apache Parquet (file format)

## Related

- [[Row Store]] — Alternative storage model
- [[OLAP]] — Workload suited for column stores
- [[Data Compression]] — Benefits from columnar storage
- [[Late Materialization]] — Optimization technique