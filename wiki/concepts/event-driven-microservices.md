---
title: "Event-Driven Microservices"
type: concept
tags: [microservices, events, architecture, patterns]
created: 2026-05-12
sources: ["event-driven-architecture-intro"]
---

# Event-Driven Microservices

A combination of [[Microservices]] and [[Event-Driven Architecture]] where services communicate asynchronously through events rather than synchronous HTTP calls. Services react autonomously to events, promoting loose coupling, scalability, and extensibility.

## Characteristics

- **Event-Driven Communication** — Services emit and consume events through a message broker (e.g., [[Apache Kafka]])
- **Autonomous Services** — Each service reacts to events independently without waiting for responses
- **Choreographed Workflows** — Services coordinate through event propagation rather than a central orchestrator
- **Decoupled Lifecycles** — Services can be deployed, scaled, and modified independently

## Benefits

- Reduced coupling compared to synchronous request-response patterns
- Improved fault tolerance — failure in one service doesn't cascade
- Natural fit for domain-driven bounded contexts
- Easier addition of new services — they just subscribe to relevant events

## Common Patterns

- **Event Choreography** — Services react to events and emit new ones; no single point of control
- **Event Orchestration** — A central coordinator service manages workflow state
- **Event Sourcing** — Service state derived from replayed event streams
- **Saga Pattern** — Distributed transactions managed through compensating events

## Communication

Services typically deploy containers or lightweight VMs and communicate via lightweight protocols (HTTP, messaging queues, [[Event-Driven Architecture|event streams]]). The event broker (Kafka) ensures reliable delivery, ordering within partitions, and persistence.

## Related

- [[Microservices]] — The service decomposition paradigm
- [[Event-Driven Architecture]] — The architectural pattern powering the communication
- [[Apache Kafka]] — Most common event broker for microservices
- [[Event Sourcing]] — State management pattern for event-driven services
- [[CQRS]] — Query model optimization alongside event-driven writes
- [[Pub/Sub Messaging]] — The messaging model enabling event distribution
