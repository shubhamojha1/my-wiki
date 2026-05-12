---
title: "Stream Processing"
type: concept
tags: [data-processing, real-time, streaming, architecture]
created: 2026-05-12
sources: ["batch-vs-stream-processing"]
---

# Stream Processing

A data processing approach where data is processed in real-time or near-real-time as it arrives. Contrasted with [[Batch Processing]], stream processing is event-driven and designed for continuous, unbounded data flows.

## Key Characteristics

- **Real-time** — Data processed immediately on arrival (milliseconds to seconds)
- **Event-driven** — Processing triggered by each event as it occurs
- **Low latency** — Designed for minimal delay between arrival and output
- **Infinite streams** — Works on continuous flows, not finite datasets

## Workflow

1. **Data Ingestion** — Continuous flow from sources: message brokers ([[Apache Kafka]], AWS Kinesis), IoT sensors, server logs, financial transactions
2. **Processing / Transformation** — Per-event operations: filtering, aggregation, windowing (time-based tumbling/sliding windows), enrichment via external data joins
3. **State Management** — Maintaining and updating state across events (e.g., running totals per user). Modern frameworks provide fault-tolerant distributed state.
4. **Output** — Results sent to databases, real-time dashboards, alerts/notifications, or external APIs

## Challenges

- **Complexity** — Continuous operation requires real-time monitoring, scaling, and fault tolerance
- **Data consistency** — Maintaining consistency across distributed real-time processing
- **Error handling** — Recovering from failures while preserving result accuracy is difficult in stateful streaming

## Frameworks

- **[[Apache Kafka]]** — Distributed messaging system for high-throughput data ingestion as a buffer between producers and stream processors
- **[[Apache Flink]]** — Stream processing framework with low-latency, stateful computations, event-time processing, and exactly-once semantics
- **AWS Kinesis** — Managed stream processing service with Lambda, S3, and Redshift integration

## Hybrid: Micro-Batch Processing

Apache Spark Streaming bridges batch and stream by processing small data chunks over short intervals, achieving near-real-time latency with the simplicity of batch processing semantics.

## Related

- [[Batch Processing]] — The scheduled, bulk alternative
- [[Apache Kafka]] — Commonly used as the ingestion layer
- [[Apache Flink]] — Leading stream processing engine
- [[Event-Driven Architecture]] — Stream processing as a component of EDA
