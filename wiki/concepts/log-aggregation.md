---
title: "Log Aggregation"
type: concept
tags: [data-engineering, logging, infrastructure]
created: 2026-04-05
sources: [Kafka.pdf]
---

# Log Aggregation

The process of collecting, centralizing, and processing log data from multiple sources across a distributed system. This was Kafka's original motivation at LinkedIn.

## Traditional Approach

- Files copied from servers to a central location
- Periodic batch processing
- High latency between log generation and availability

## Kafka's Solution

Kafka replaced this with:
1. Applications push logs directly to Kafka topics
2. Multiple consumers can process the same logs simultaneously
3. Real-time streaming instead of batch
4. Durable storage enables both real-time and batch consumption

## Benefits

- **Low Latency**: Logs available in near real-time
- **Multiple Consumers**: Same logs feed multiple systems (Hadoop, monitoring, analytics)
- **Scalability**: Handles massive log volumes
- **Replay**: Debug by re-reading historical logs

## Evolution

Log aggregation with Kafka enabled:
- [[Real-time Analytics]]
- Monitoring and alerting
- Change data capture
- Event sourcing patterns

## Related

- [[Apache Kafka]]
- [[Log Processing]]