---
title: "NoSQL"
type: concept
tags: [database, nosql, distributed, scalability]
created: 2026-05-08
sources: ["https://algomaster.io/learn/system-design/sql-vs-nosql"]
---

# NoSQL

**Definition:** A broad class of database management systems that diverge from the traditional relational (SQL) model, designed for flexible schemas, horizontal scalability, and high-throughput workloads.

## The Four NoSQL Models

### Key-Value Store
- Data stored as key-value pairs
- Simple GET, PUT, DELETE operations by key
- Excellent horizontal scaling
- Examples: [[Redis]], DynamoDB, [[Memcached]]
- Use cases: caching, sessions, simple lookups

### Document Store
- Data stored as documents (JSON, BSON)
- Flexible schema — documents can have varying attributes
- Rich query language on document fields
- Examples: MongoDB, Couchbase, Firestore
- Use cases: content management, catalogs, rapid prototyping

### Column-Family Store
- Data organized into rows with variable columns per row
- Optimized for large-scale distributed storage
- High write throughput, tunable consistency
- Examples: Cassandra, HBase
- Use cases: time-series, IoT, analytics, high-write workloads

### Graph Database
- Data stored as nodes and edges with properties
- Optimized for relationship traversal
- Examples: Neo4j, Amazon Neptune
- Use cases: social networks, recommendation engines, fraud detection

## Key Characteristics

| Aspect | Property |
|--------|----------|
| Schema | Flexible, schema-less, dynamic |
| Scalability | Horizontal (scale-out by adding nodes) |
| Transactions | BASE (Basically Available, Soft state, Eventual consistency) |
| Query | Proprietary APIs per database type |
| Consistency | Often eventual, tunable in some systems |

## BASE vs ACID

NoSQL databases typically follow the **BASE** model:
- **Basically Available** — the system guarantees availability
- **Soft state** — the system state may change over time (even without input)
- **Eventual consistency** — the system will become consistent over time

This is the inverse trade-off from [[ACID Transactions]]: availability and partition tolerance over strong consistency.

## When to Choose NoSQL

- Rapid iteration with evolving data models
- Massive horizontal scale requirements
- Unstructured or semi-structured data
- High-throughput read/write workloads
- Eventual consistency is acceptable

## Related Pages

- [[SQL]], [[ACID Transactions]], [[CAP Theorem]], [[Document Database]], [[Vector Database]], [[Redis]], [[Memcached]]
