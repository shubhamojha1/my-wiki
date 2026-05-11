---
title: "Key-Value Store"
type: concept
tags: [database, nosql, key-value]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Key-Value Store

A **key-value store** is a NoSQL database that stores data as key-value pairs, providing fast retrieval of values based on unique keys.

## Characteristics

- **Simple model**: Every value accessed by its unique key
- **High throughput**: Optimized for fast reads and writes
- **Schemaless**: Values can be any data type (strings, JSON, blobs)
- **Horizontal scaling**: Easy to partition by key range or hash

## Use Cases

- **Session storage**: User preferences, shopping carts, auth tokens
- **Caching**: Frequently accessed data in memory
- **Real-time data**: Event processing, message queues
- **Leaderboards**: Sorted sets for gaming scores

## Examples

- [[Redis]] — In-memory with optional persistence, rich data types
- [[DynamoDB]] — Fully managed, auto-scaling (from Amazon)
- [[Memcached]] — Simple distributed memory cache

## Related

- [[Document Database]] — Stores documents (keyed by ID)
- [[In-Memory Database]] — Often key-value based
- [[NoSQL]] — Broader non-relational category
