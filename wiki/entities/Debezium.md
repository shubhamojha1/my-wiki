---
title: "Debezium"
type: entity
tags: [cdc, kafka, open-source, streaming]
created: 2026-05-10
sources: ["algomaster-cdc"]
---

# Debezium

**Debezium** is an open-source distributed platform for log-based Change Data Capture (CDC). It streams database changes from MySQL, PostgreSQL, MongoDB, and other databases into Apache Kafka topics in near real time.

## How It Works

Debezium connects to a database via Kafka Connect, reads the database's transaction log (WAL or binlog), and converts each change into a structured event published to a Kafka topic. Downstream applications consume these events to stay synchronized.

## Key Features

- **Log-based CDC**: Reads directly from database transaction logs — minimal impact on the source database
- **Kafka integration**: Uses Kafka Connect framework for scalable, fault-tolerant streaming
- **Schema evolution handling**: Tracks schema changes alongside data changes
- **Exactly-once semantics**: Reliable delivery of change events

## Typical Architecture

```
Database → Debezium Connector → Kafka Topic → Downstream Consumers
                                                    ↓
                                         (Search, Cache, Data Warehouse, Microservices)
```

## Related Concepts

- [[Change Data Capture (CDC)]] — The pattern Debezium implements
- [[Apache Kafka]] — Streaming backbone for Debezium events
- [[Kafka Connect]] — Framework Debezium runs on
