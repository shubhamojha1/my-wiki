---
title: "Hadoop"
type: entity
tags: [tool, infrastructure, map-reduce]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Hadoop

**Type:** Distributed data processing framework  
**Website:** [hadoop.apache.org](http://hadoop.apache.org/)

## Overview

Hadoop is an open-source framework for distributed storage and processing of large datasets using clusters of commodity hardware. It implements the MapReduce programming model for batch processing.

## Components

### HDFS (Hadoop Distributed File System)
- Stores data across multiple nodes
- Replicates data for fault tolerance
- Optimized for sequential reads/writes

### MapReduce
- Batch processing model
- **Map phase**: process data in parallel, emit key-value pairs
- **Reduce phase**: aggregate results by key

### Hive
- SQL-like interface (HiveQL) on top of MapReduce
- Good for data analysts who know SQL

### HBase
- NoSQL database on Hadoop
- Random read/write access
- Useful for real-time queries on large data

## Use Cases

- **Social graph calculations** — "suggested users" based on connections
- **Analytics reports** — daily/weekly/monthly aggregations
- **Log processing** — click streams, server logs, events
- **Data warehousing** — ETL at scale

## When to Use

Ad-hoc SQL queries may suffice for smaller systems, but MapReduce becomes necessary when:
- Data volume requires database sharding
- Write load is too high for analytical queries
- You need dedicated query infrastructure

## Related Concepts

[[Map-Reduce]], [[Offline Processing]], [[Scalability]], [[Horizontal Scalability]]