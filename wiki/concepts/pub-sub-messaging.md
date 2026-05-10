---
title: "Pub/Sub Messaging"
type: concept
tags: [messaging, distributed-systems, patterns]
created: 2026-04-05
sources: [Kafka.pdf]
---

# Pub/Sub Messaging

Publish-Subscribe is a messaging pattern where senders (publishers) categorize messages into topics, and receivers (subscribers) subscribe to topics they're interested in. A **message broker** acts as the intermediary that manages topics, receives messages, and distributes them to all subscribers.

## Core Concepts

- **Publisher**: Produces messages to a topic without knowing subscribers
- **Subscriber**: Consumes messages from topics it subscribed to
- **Topic**: Logical channel that categorizes messages
- **Broker**: Intermediary that routes messages from publishers to subscribers

## Message Flow

1. Publisher sends message to a topic on the broker
2. Broker receives and stores the message (optionally persisted to disk)
3. Subscribers receive the message (real-time push or polling)
4. Subscribers process and optionally send **acknowledgment** back to broker

## Benefits

- **Loose Coupling**: Publishers and subscribers unaware of each other
- **High Throughput**: Broker efficiently routes large message volumes
- **Asynchronous Processing**: Components process at their own pace
- **Easy Integration**: New subscribers added without modifying publishers
- **Real-Time Communication**: Live data dissemination
- **Message Durability**: Brokers persisting messages prevent loss
- **Fault Tolerance**: Decoupled nature isolates and contains failures

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
- Real-time notifications (social media likes, comments)
- Data pipeline integration
- Microservices communication
- Activity monitoring
- IoT data aggregation (sensor data published to topics)

## Related

- [[Apache Kafka]]
- [[Distributed Commit Log]]