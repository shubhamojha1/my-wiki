---
title: "Pub/Sub Messaging"
type: concept
tags: [messaging, distributed-systems, patterns]
created: 2026-04-05
sources: [Kafka.pdf]
---

# Pub/Sub Messaging

Publish-Subscribe is a messaging pattern where senders (publishers) categorize messages into topics, and receivers (subscribers) subscribe to topics they're interested in. Kafka implements this pattern with some unique twists.

## Core Concepts

- **Publisher**: Produces messages to a topic without knowing subscribers
- **Subscriber**: Consumes messages from topics it subscribed to
- **Topic**: Logical channel that categorizes messages
- **Broker**: Intermediary that routes messages from publishers to subscribers

## Kafka's Implementation

Unlike traditional pub/sub, Kafka adds:
- **Consumer Groups**: Multiple consumers can form a group to share work
- **Partitioning**: Topics split across partitions for parallel processing
- **Offset Management**: Consumers track their position, enabling precise control
- **Persistent Subscriptions**: Messages retained beyond subscription lifetime

## Comparison with Queue

| Aspect | Message Queue | Pub/Sub |
|--------|--------------|---------|
| Consumption | Exclusive (one consumer) | Shared (all subscribers) |
| Message lifecycle | Delete on consumption | Retained for duration |
| Coupling | Point-to-point | Topic-based |

## Use Cases

- Event-driven architectures
- Real-time notifications
- Data pipeline integration
- Microservices communication
- Activity monitoring

## Related

- [[Apache Kafka]]
- [[Distributed Commit Log]]