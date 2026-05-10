---
title: "Change Data Capture (CDC)"
type: concept
tags: [databases, streaming, data-integration]
created: 2026-05-10
sources: ["algomaster-cdc"]
---

# Change Data Capture (CDC)

**CDC** (Change Data Capture) is a pattern that tracks database changes (inserts, updates, deletes) and streams them in real time to downstream systems. It replaces slow batch ETL with continuous, low-latency data synchronization.

## How It Works

1. **Monitor**: Continuously watch the source database for changes
2. **Capture**: Extract before/after values, metadata (timestamp, table name, operation type)
3. **Deliver**: Transmit change events to consumers via message brokers or data pipelines

## Three Implementation Approaches

### Timestamp-Based CDC

Uses a `last_updated` column. Applications query for rows newer than the last sync time.

```sql
SELECT * FROM orders WHERE last_updated > '2024-02-15 12:00:00';
```

- **Pros**: Simple, no external dependencies
- **Cons**: Misses deletes, performance overhead at scale, clock skew risks

### Trigger-Based CDC

Database triggers log each change to a separate audit table.

- **Pros**: Real-time capture, detailed before/after values, flexible schema targeting
- **Cons**: Slows write operations, requires trigger maintenance on schema changes, resource-intensive at high volume

### Log-Based CDC (Preferred)

Reads changes directly from the database's write-ahead log (WAL) or binary log (binlog). Intercepts low-level operations without impacting application workflow.

- **Pros**: Minimal DB impact, captures all operations (including deletes), near real-time, scales to high transaction volumes
- **Cons**: Complex setup, depends on database log format, often requires additional tooling (Debezium, Kafka Connect)

## Use Cases

- **Microservices communication**: Propagate state changes across services without direct HTTP calls
- **Event sourcing**: Build a complete log of all state changes for audit and replay
- **Data warehousing**: Feed near real-time data into analytics systems
- **Cache invalidation**: Update caches automatically when source data changes

## Challenges

- **Schema evolution**: Pipeline must adapt gracefully to column additions and type changes
- **High throughput**: Must keep up with rapid change volume without overwhelming consumers
- **Ordering guarantees**: Events must be processed in the correct sequence for data integrity
- **Security**: Captured changes can expose sensitive data — need encryption, masking, access controls

## Related Concepts

- [[Event Sourcing]] — Pattern for recording state changes as event sequences
- [[Apache Kafka]] — Streaming platform commonly used with CDC
- [[Debezium]] — Open-source log-based CDC tool
- [[Message Queue]] — Delivering change events to consumers
