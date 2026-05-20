---
title: "Key-Value Store"
type: concept
tags: [database, nosql, key-value]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-15-db-types]
---

# Key-Value Store

A **key-value store** is the simplest database model: data is stored as a collection of (key, value) pairs. The key is a unique identifier; the value is an opaque blob (string, JSON, binary, etc.). Reads and writes are O(1) by key.

## Data Model

```
SET user:1001 → {"name":"Alice","email":"alice@example.com","tier":"pro"}
GET user:1001 → {"name":"Alice", ...}

SET session:abc123 → {"user_id":1001,"expires":1716400000}
GET session:abc123 → {"user_id":1001, ...}
```

No schema. No joins. No WHERE clauses across keys (unless the system supports secondary indexes). The key is everything.

## Characteristics

| Property | Detail |
|----------|--------|
| **Access pattern** | Primary key lookup only (by default) |
| **Schema** | None — value is opaque bytes |
| **Throughput** | Very high — often millions of ops/sec per node |
| **Horizontal scaling** | Partition by key hash or range; no cross-partition joins to worry about |
| **Complexity** | Simplest possible database API |

## When to Use (and Not)

| Good for | Poor for |
|---------|---------|
| Caching (set + expire) | Ad-hoc queries across keys |
| Session storage | Relational queries (JOINs) |
| Rate limiting counters | Complex aggregations |
| Feature flags | Secondary index lookups |
| Distributed locks | Strict schema enforcement |
| Pub/Sub / message queue | Multi-key transactions across partitions |

## Implementations

| System | Type | Strengths |
|--------|------|-----------|
| **Redis** | In-memory + optional disk | Rich data types (sorted sets, streams, HLL), Lua scripting, Pub/Sub |
| **Memcached** | In-memory only | Simplest; pure cache; no persistence |
| **DynamoDB** | Managed cloud | Auto-scaling, global tables, integrated with AWS |
| **etcd** | Strongly consistent | Watch notifications; used for distributed coordination |
| **RocksDB** | Embedded, on-disk | LSM-tree; powers many larger systems |
| **Riak KV** | Distributed | High availability; CRDTs; eventual consistency |

## Storage Internals

Most on-disk key-value stores use an **LSM tree** (Log-Structured Merge-tree): writes go to an in-memory buffer (memtable), flush to immutable disk segments (SSTables), and merge in the background. This gives excellent write throughput. B-trees are used by some (LMDB, BoltDB) for better point read performance.

## Related Concepts

- [[Document Database]] — values are structured documents with queryable fields
- [[Hash Table]] — the in-memory data structure key-value stores resemble
- [[LSM Tree]] — common storage engine for on-disk key-value stores
- [[Consistent Hashing]] — used to shard keys across nodes
- [[Redis]] — the most popular key-value store, with extended data types
