---
title: "Publish-Subscribe (Pub/Sub)"
type: source
tags: [system-design, messaging, pub-sub]
created: 2026-05-10
sources: ["algomaster-pub-sub"]
---

# Publish-Subscribe (Pub/Sub)

**Pub/Sub** is an architectural pattern for asynchronous communication between components in a distributed system. Publishers send messages to topics without knowing the subscribers, and subscribers receive messages without knowing the publishers.

## Components

- **Publishers**: Components that send messages to a topic (e.g., order service publishes "Order Placed")
- **Subscribers**: Components that express interest in topics and process messages
- **Message Broker**: Core intermediary that manages topics, receives messages, and distributes to all subscribers

Popular brokers: Apache Kafka, RabbitMQ, Google Cloud Pub/Sub, Amazon SNS/SQS.

## How It Works

1. Publisher sends message to a topic on the broker
2. Broker receives and stores the message (optionally persisted to disk)
3. Subscribers receive the message (real-time push or polling)
4. Subscribers process and optionally send acknowledgment back to broker

## Benefits

- **Loose Coupling**: Publishers and subscribers unaware of each other
- **High Throughput**: Broker efficiently routes large message volumes
- **Asynchronous Processing**: Components process at their own pace
- **Easy Integration**: New subscribers added without modifying publishers
- **Real-Time Communication**: Live data dissemination
- **Message Durability**: Brokers persist messages to prevent loss
- **Fault Tolerance**: Decoupled nature isolates failures

## Use Cases

- Real-time notifications (social media likes, comments)
- Event logging and analytics (Apache Kafka for stream logs)
- Microservices communication (async, scalable workflows)
- IoT data aggregation (sensor data published to topics)

## Related Concepts

- [[Pub/Sub Messaging]] — Core pattern concept
- [[Apache Kafka]] — Popular pub/sub implementation
- [[Message Queue]] — Point-to-point alternative

## Source

- AlgoMaster.io: [Pub/Sub](https://algomaster.io/learn/system-design/pub-sub) (January 2026)
