---
title: "Apache Kafka"
type: entity
tags: [messaging, distributed-systems, streaming]
created: 2026-04-05
sources: [Kafka.pdf]
---

# Apache Kafka

An open-source distributed publish-subscribe messaging system originally developed at LinkedIn, based on the design described in the 2011 paper "[[Kafka: A Distributed Messaging System for Log Processing]]".

## Overview

Kafka provides a unified platform for handling real-time data feeds. It serves as the backbone for countless data pipelines at companies worldwide, enabling:

- Event streaming
- Log aggregation
- Real-time analytics
- Microservices communication

## Key Concepts

- **Topic**: A category to which messages are published
- **Partition**: subdivisions of topics for parallel processing
- **Producer**: Clients that publish messages to topics
- **Consumer**: Clients that subscribe to topics and process messages
- **Broker**: A Kafka server that stores messages
- **Consumer Group**: A group of consumers that share message processing

## Why It Matters

Kafka's commit log design enables:
- High throughput for data ingestion
- Horizontal scalability via partitioning
- Fault tolerance through replication
- Message retention independent of consumption
- Replay capability for debugging and reprocessing

## Role in Event-Driven Architecture

Kafka is the most widely adopted event broker for [[Event-Driven Architecture]]. It provides the foundational plumbing for EDA by acting as a highly scalable, fault-tolerant event storage and distribution layer:

- **Event Source of Truth** — Durable append-only log for event persistence
- **Asynchronous Decoupling** — Producers and consumers operate independently via topics
- **Ordered Delivery** — Partition-based ordering guarantees within event streams
- **Replay Capability** — Consumers can reprocess events from any point in the log

Paired with [[Apache Flink]] for stream processing and [[Confluent]] for managed operations, Kafka forms the backbone of modern EDA implementations.

## Related Concepts

- [[Distributed Commit Log]] — The architectural pattern
- [[Pub/Sub Messaging]] — The messaging paradigm
- [[Log Aggregation]] — Original use case at LinkedIn
- [[Event-Driven Architecture]] — The architectural pattern Kafka powers
- [[Event Sourcing]] — State management via immutable event logs
- [[CQRS]] — Read/write separation enabled by Kafka topics
- [[Event-Driven Microservices]] — Microservices communication via Kafka