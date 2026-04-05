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

## Related Concepts

- [[Distributed Commit Log]] — The architectural pattern
- [[Pub/Sub Messaging]] — The messaging paradigm
- [[Log Aggregation]] — Original use case at LinkedIn