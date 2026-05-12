---
title: "Confluent"
type: entity
tags: [kafka, streaming, managed-service, platform]
created: 2026-05-12
sources: ["event-driven-architecture-intro"]
---

# Confluent

A data streaming platform built around [[Apache Kafka]], offering both on-premise (Confluent Platform) and fully managed cloud (Confluent Cloud) deployments. Confluent provides a comprehensive set of tools for building, managing, and scaling [[Event-Driven Architecture]] systems.

## Key Offerings

### Deployment Options

- **Confluent Cloud** — Fully managed cloud-native Kafka service
- **Confluent Platform** — Self-managed on-premise deployment
- **Confluent Private Cloud** — Bridge between on-premise control and cloud automation
- **WarpStream** — Kafka-compatible streaming in private cloud

### Platform Components

- **Apache Kafka** — Distributed event streaming and broker
- **Apache Flink** — Managed stream processing with SQL capabilities
- **Kafka Streams** — Lightweight Java library for stream processing directly on Kafka topics
- **Schema Registry** — Centralized schema management with compatibility enforcement
- **Kafka Connect** — Framework for building and running connectors
- **Tableflow** — Topics to Iceberg/Delta Lake tables

### Management & Operations

- **Centralized Control Plane** — Manage and monitor Kafka clusters
- **Monitoring & Observability** — Event flow visibility, performance metrics, error tracking
- **Security & Encryption** — Data protection, access control, audit trails
- **Data Connectivity** — 200+ connectors (JDBC, Elasticsearch, S3, HDFS, Salesforce, MQTT)

## Role in EDA

Confluent addresses the key challenges of [[Event-Driven Architecture]] implementation: complexity management via a unified platform, schema evolution through Schema Registry, debugging through observability tools, and event ordering/consistency via Kafka's partitioned commit log.

## Related

- [[Apache Kafka]]
- [[Apache Flink]]
- [[Event-Driven Architecture]]
- [[Pub/Sub Messaging]]
