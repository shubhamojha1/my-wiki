---
title: "Time-Series Database"
type: concept
tags: [database, time-series, observability]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-15-db-types]
---

# Time-Series Database (TSDB)

A **time-series database** is optimized for storing and querying sequences of values indexed by time. Its storage engine and query language are designed around the assumption that data arrives in timestamp order and is queried primarily over time windows.

## Data Model

```
metric: cpu_usage
  tags:  host=web01, region=us-east
  points:
    2026-05-20T10:00:00Z  →  42.3%
    2026-05-20T10:00:10Z  →  43.1%
    2026-05-20T10:00:20Z  →  41.8%
```

A time series is identified by a **metric name** + **tag set** (dimensions). Within that series, each data point is a (timestamp, value) pair.

## Workload Characteristics

| Property | Implication |
|----------|-------------|
| **Append-only** | No UPDATEs; new points always added at the end → sequential I/O |
| **High ingest rate** | Thousands to millions of points/sec; needs efficient batch writes |
| **Time-range queries** | `SELECT avg(cpu) FROM metrics WHERE time > now()-1h` |
| **Downsampling** | Recent data at 10s resolution; old data at 1h resolution (automatic rollup) |
| **Retention** | Old data expires automatically (no manual deletes needed) |
| **Compression** | Timestamps often stored as delta; values often delta-of-delta → 10–100× compression |

## Storage Techniques

- **Gorilla compression** (Facebook): Delta-of-delta encoding for timestamps; XOR compression for floating-point values.
- **Columnar storage**: Timestamps in one column, values in another — compresses much better than row storage.
- **Chunk-based**: Data partitioned into fixed time chunks (e.g., 2-hour blocks); old chunks are sealed and compressed.

## Query Patterns

```sql
-- InfluxDB / PromQL style:
SELECT mean(value) FROM cpu WHERE time > now() - 1h GROUP BY time(5m), host

-- TimescaleDB (SQL):
SELECT time_bucket('5 minutes', time) as bucket, avg(value)
FROM cpu_metrics WHERE time > NOW() - INTERVAL '1 hour'
GROUP BY bucket, host ORDER BY bucket;
```

## Popular TSDBs

| System | Engine | Best For |
|--------|--------|---------|
| **Prometheus** | Custom (chunks in memory + WAL) | Kubernetes/ops metrics; pull-based scraping |
| **InfluxDB** | Purpose-built (TSM storage engine) | General time-series; IoT |
| **TimescaleDB** | PostgreSQL extension (hypertable) | SQL familiarity; relational + time-series |
| **OpenTSDB** | HBase-backed | High cardinality at scale |
| **Victoria Metrics** | Custom Go engine | Very high cardinality; Prometheus-compatible |
| **Apache Cassandra** | Wide-column (time as clustering key) | Extremely high write throughput |

## TSDB vs Relational DB

| Aspect | TSDB | Relational DB |
|--------|------|--------------|
| Time-range queries | Optimized (chunk pruning) | Requires index on timestamp |
| Ingest throughput | Very high | Moderate |
| Downsampling / rollup | Built-in | Requires materialized views |
| Retention policies | Automatic | Manual |
| Cardinality explosion | Handled carefully | Challenging |
| Ad-hoc queries | Limited | Flexible SQL |

## Related Concepts

- [[Wide-Column Store]] — Cassandra used at scale for time-series data
- [[OLAP]] — analytical workloads share window-query patterns with TSDB
- [[Data Compression]] — essential for TSDB efficiency (Gorilla, delta-of-delta)
