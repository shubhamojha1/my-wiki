---
title: "Time-Series Database"
type: concept
tags: [database, time-series, observability]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Time-Series Database

A **time-series database (TSDB)** specializes in storing, retrieving, and managing time-stamped data points collected over time intervals.

## Characteristics

- **Append-heavy**: New data points arrive continuously
- **Time-ordered**: Data naturally sorted by timestamp
- **Downsampling**: Automatic aggregation of old data
- **Retention policies**: Automatic expiration of stale data
- **Range queries**: Optimized for time-window scans

## Use Cases

- **Infrastructure monitoring**: CPU, memory, network metrics
- **IoT and sensors**: Temperature, vibration, location readings
- **Financial markets**: Stock prices, trade volumes over time
- **Application performance**: APM traces and request latencies

## Examples

- InfluxDB — Open-source, purpose-built TSDB
- TimescaleDB — PostgreSQL-based with time-series extensions
- [[Prometheus]] — Metrics and alerting, pull-based model

## Related

- [[Wide-Column Store]] — Often used for time-series at scale
- [[OLAP]] — Analytical workloads overlapping with TSDB
