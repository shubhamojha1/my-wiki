---
title: "In-Memory Database"
type: concept
tags: [database, in-memory, performance]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# In-Memory Database

An **in-memory database** stores data primarily in main memory (RAM) rather than on disk, providing extremely fast data access and low latency by eliminating disk I/O.

## Characteristics

- **RAM-resident**: Primary storage is memory (disk used for persistence)
- **Microsecond latency**: Orders of magnitude faster than disk-based DBs
- **Volatile by nature**: Data lost on power failure unless persisted
- **Limited by RAM**: Dataset size constrained by available memory

## Persistence Options

- **Snapshotting** (RDB): Periodic full dumps to disk
- **Append-only log** (AOF): Log every write operation
- **Replication**: Keep replica nodes for failover

## Use Cases

- **Caching**: Hot data in memory ([[Redis]], [[Memcached]])
- **High-frequency trading**: Sub-millisecond transaction processing
- **Online gaming**: Real-time game state and session management
- **Real-time analytics**: Aggregations on streaming data

## Examples

- [[Redis]] — In-memory with optional persistence, rich data structures
- [[Memcached]] — Simple distributed cache, no persistence
- SAP HANA, VoltDB — Enterprise in-memory databases

## Related

- [[Key-Value Store]] — Many in-memory DBs use key-value model
- [[In-Memory Cache]] — Same principle, focused on caching
- [[Redis]] — Leading in-memory data structure store
