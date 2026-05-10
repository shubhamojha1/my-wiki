---
title: "Change Data Capture (CDC)"
type: source
tags: [system-design, databases, streaming]
created: 2026-05-10
sources: ["algomaster-cdc"]
---

# Change Data Capture (CDC)

**CDC** is a design pattern that tracks and captures database changes (inserts, updates, deletes) and streams them in real time to downstream systems. Ensures synchronization without expensive batch ETL jobs.

## How CDC Works

1. **Monitor**: Detect changes from source database
2. **Capture**: Extract change details (before/after values, timestamp, table)
3. **Deliver**: Transmit change event to consumers (message queues, data pipelines, analytics)

## Implementation Approaches

### Timestamp-Based
- `last_updated` column queried periodically
- Simple but misses deletes, performance overhead at scale

### Trigger-Based
- Database triggers log changes to an audit table
- Real-time capture with detailed audit trail
- Performance impact on writes; maintenance burden with schema changes

### Log-Based (Preferred)
- Reads from database write-ahead log (WAL) or binary log (binlog)
- Tools: Debezium, Kafka Connect, AWS DMS
- Minimal DB impact, comprehensive capture, near real-time
- Preferred for high-transaction environments

## Use Cases

- **Microservices communication**: Keep services in sync without direct calls
- **Event sourcing**: Record every state change as an event sequence
- **Data warehousing**: Push changes to warehouses in near real-time
- **Cache invalidation**: Trigger cache updates when underlying data changes

## Debezium + Kafka

Debezium is an open-source log-based CDC platform. Integrated with Apache Kafka, it streams database changes to Kafka topics for consumption by downstream systems.

## Challenges

Schema evolution, high throughput handling, ordering guarantees, security and compliance.

## Related Concepts

- [[Change Data Capture (CDC)]] — Core pattern
- [[Event Sourcing]] — Recording state changes as events
- [[Apache Kafka]] — Streaming platform for CDC events
- [[Debezium]] — Open-source CDC tool

## Source

- AlgoMaster.io: [Change Data Capture (CDC)](https://algomaster.io/learn/system-design/change-data-capture-cdc) (October 2025)
