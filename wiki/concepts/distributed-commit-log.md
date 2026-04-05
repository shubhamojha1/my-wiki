---
title: "Distributed Commit Log"
type: concept
tags: [distributed-systems, architecture, persistence]
created: 2026-04-05
sources: [Kafka.pdf]
---

# Distributed Commit Log

An append-only, ordered data structure that serves as the foundation for Kafka's architecture. Unlike traditional message queues that delete messages after consumption, a commit log retains messages for a configurable duration.

## Key Properties

1. **Append-only** — Messages can only be written at the end
2. **Ordered** — Strict ordering within each partition
3. **Durable** — Messages are persisted to disk before acknowledgment
4. **Immutable** — Messages cannot be modified once written

## Benefits

- **Replayability** — Consumers can re-read old messages for debugging or reprocessing
- **Decoupling** — Producers and consumers are temporally decoupled
- **Performance** — Sequential disk writes achieve high throughput
- **Simplicity** — Single data structure avoids complex in-memory structures

## Related Systems

Kafka popularized this pattern in messaging, but the concept appears in other systems:
- Amazon Kinesis
- Google Cloud Pub/Sub
- Apache Pulsar
- Various database transaction logs

## In Kafka

Kafka implements this via:
- Partitioned logs across brokers
- Configurable retention (time or size-based)
- Replicated log for fault tolerance
- Sequential consistency within partitions

## See Also

- [[Apache Kafka]]
- [[Log Processing]]