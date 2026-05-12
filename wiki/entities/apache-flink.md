---
title: "Apache Flink"
type: entity
tags: [stream-processing, real-time, flink, apache]
created: 2026-05-12
sources: ["event-driven-architecture-intro"]
---

# Apache Flink

An open-source stream processing framework that provides advanced capabilities for event-time processing, stateful computations, fault tolerance, and batch processing in event-driven architectures.

## Role in EDA

Flink brings SQL-capable stream processing to the [[Event-Driven Architecture]] pattern. It processes, filters, and augments event streams from [[Apache Kafka]] before delivering results to downstream consumers and microservices.

## Key Features

- **Event-Time Processing**: Handles out-of-order events with watermarks and timers
- **Stateful Computations**: Maintains state across streaming operations with exactly-once semantics
- **Fault Tolerance**: Checkpoint-based recovery, consistent state snapshots
- **Batch Processing**: Unified batch and stream processing in a single engine
- **SQL Interface**: Declarative stream processing via Flink SQL

## Integration

In the Confluent managed platform, Flink is offered as a fully managed service alongside Kafka, enabling SQL-based stream processing on Kafka topics without infrastructure management.

## Related Concepts

- [[Apache Kafka]] — Primary event source/sink for Flink pipelines
- [[Confluent]] — Managed platform offering Flink-as-a-service
- [[Event-Driven Architecture]] — The architectural pattern Flink enables at scale
