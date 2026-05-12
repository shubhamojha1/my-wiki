---
title: "Event-Driven Architecture"
type: concept
tags: [architecture, events, distributed-systems, patterns]
created: 2026-05-12
sources: ["event-driven-architecture-intro"]
---

# Event-Driven Architecture

Event-Driven Architecture (EDA) is a software design pattern where systems detect, process, manage, and react to real-time events as they happen. Events are produced by sources, published to an event bus or message broker, and consumed by interested components asynchronously.

## How It Works

1. **Event Producers** generate events representing occurrences or state changes
2. Events are published to an **event broker** (e.g., [[Apache Kafka]])
3. The broker filters, augments, and distributes events to interested consumers
4. **Event Consumers** react asynchronously — processing, transforming, or triggering downstream actions

## Key Characteristics

- **Asynchronous Communication** — Producers and consumers are decoupled in time
- **Loose Coupling** — Components interact through events, not direct calls
- **Eventual Consistency** — Systems converge over time, not immediately
- **Real-Time Processing** — Events are acted upon as they occur

## Related Patterns

- [[Event Sourcing]] — Recording state changes as immutable event sequences
- [[CQRS]] — Separating read and write operations for scalability
- [[Pub/Sub Messaging]] — One-to-many asynchronous event distribution
- [[Event-Driven Microservices]] — Microservices communicating through events
- **Event-Driven Programming (EDP)** — Code-level paradigm for event response

## Advantages

- Independent scalability of loosely coupled components
- Real-time responsiveness and faster decision-making
- Fault tolerance via durable event stores and replay
- Seamless integration across heterogeneous systems

## Disadvantages

- Higher complexity than monolithic or request-response architectures
- Event ordering guarantees require careful design (partition keys, sequence IDs)
- Debugging and tracing across async event flows
- Eventual consistency adds data staleness considerations

## Common Technologies

- [[Apache Kafka]] — Distributed event streaming broker
- [[Apache Flink]] — Stream processing with event-time semantics
- [[Confluent]] — Managed EDA platform

## Use Cases

E-commerce order processing, IoT data collection, stock trading, real-time analytics, workflow automation, smart home systems, online gaming, notification systems, user registration pipelines.

## Cross-References

- [[Microservices]] — Independent service deployment (often combined with EDA)
- [[Distributed Commit Log]] — The append-only log underlying Kafka's implementation
