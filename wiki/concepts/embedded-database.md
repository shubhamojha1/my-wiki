---
title: "Embedded Database"
type: concept
tags: [database, embedded, lightweight]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Embedded Database

An **embedded database** is tightly integrated into a software application, running as part of the application process rather than as a separate server.

## Characteristics

- **No separate process**: Runs in-process with the application
- **Zero configuration**: No installation, no admin
- **Small footprint**: Minimal memory and disk usage
- **Fast data access**: No network or IPC overhead
- **Simplified deployment**: Single binary including the database

## Use Cases

- **Mobile apps**: Local storage on device (Android/iOS)
- **Desktop applications**: Configuration, user preferences, local data
- **Gaming**: Save states, player progress, settings
- **IoT devices**: Resource-constrained embedded environments
- **Browser storage**: IndexedDB in web browsers

## Examples

- [[SQLite]] — Most widely deployed database engine
- RocksDB — Embedded key-value store from Facebook
- Berkeley DB — Embedded database from Oracle
- DuckDB — Embedded analytical (OLAP) database

## Related

- [[SQLite]] — Leading embedded relational database
- [[Key-Value Store]] — RocksDB is an embedded KV store
