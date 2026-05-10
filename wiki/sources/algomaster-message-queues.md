---
title: "Message Queues"
type: source
tags: [system-design, messaging, async]
created: 2026-05-10
sources: ["algomaster-message-queues"]
---

# Message Queues

A **message queue** is a communication mechanism for asynchronous message exchange. It acts as an intermediary that temporarily holds messages from producers and delivers them to consumers, enabling decoupled architectures.

## Core Components

- **Producer/Publisher**: Sends messages to the queue
- **Consumer/Subscriber**: Reads and processes messages
- **Queue**: Data structure that stores messages until consumed
- **Broker/Queue Manager**: Manages the queue, handles delivery, and routes messages
- **Message**: Unit of data (payload + metadata)

## How It Works

1. **Message Creation**: Producer generates message with payload and metadata
2. **Enqueue**: Producer sends message to the queue
3. **Storage**: Queue stores message (persistent or transient)
4. **Dequeue**: Consumer retrieves message (in order, by priority, or parallel)
5. **Acknowledgment**: Consumer sends ack back to broker
6. **Deletion**: Broker removes message after acknowledgment

## Queue Types

- **Point-to-Point (P2P)**: One producer, one consumer — task processing
- **Pub/Sub**: One publisher, multiple consumers — notifications
- **Priority Queue**: Higher-priority messages processed first
- **Dead Letter Queue (DLQ)**: Holds messages that fail after max retries

## Advantages

Decoupling, async processing, load balancing, fault tolerance (persistence + retries), scalability (horizontal consumers), throttling.

## When to Use

- Microservices communication (async, decoupled)
- Task scheduling and background processing (image resizing, emails)
- Event-driven architectures (broadcasting events)
- Load leveling (smoothing burst traffic)
- Reliable communication (persistent queues, retry on failure)

## Best Practices

Idempotent consumers, message durability choices, error handling with retries/DLQ, encryption and auth, monitoring (throughput, queue length, consumer lag), plan for horizontal scaling.

## Popular Systems

RabbitMQ (AMQP, flexible routing), Apache Kafka (high-throughput streaming), Amazon SQS (managed, AWS-integrated), Google Cloud Pub/Sub (managed, event-driven), Redis Streams (lightweight, in-memory), ActiveMQ (enterprise, multi-protocol).

## Related Concepts

- [[Message Queue]] — Core pattern
- [[Pub/Sub Messaging]] — Fan-out variant
- [[Dead Letter Queue]] — Failed message handling
- [[Apache Kafka]] — Log-based implementation

## Source

- AlgoMaster.io: [Message Queues](https://algomaster.io/learn/system-design/message-queues) (October 2025)
