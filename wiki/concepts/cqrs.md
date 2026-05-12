---
title: "CQRS"
type: concept
tags: [architecture, patterns, cqrs, events]
created: 2026-05-12
sources: ["event-driven-architecture-intro"]
aliases: ["Command Query Responsibility Segregation"]
---

# CQRS

Command Query Responsibility Segregation (CQRS) is a pattern that separates read and update operations for a data store. Reads use one model/interface (queries), while writes use another (commands), enabling independent optimization of each.

## How It Works

- **Commands** — Mutate state (inserts, updates, deletes). Do not return data.
- **Queries** — Read state. Do not mutate data.
- Models can use different storage technologies (e.g., normalized write store + denormalized read views)

## Relationship to Event-Driven Architecture

CQRS is commonly paired with [[Event Sourcing]] in [[Event-Driven Architecture]] systems. Events captured by event sourcing feed into CQRS, where the write model processes commands and produces events, while read models consume those events to build optimized query projections.

## Benefits

- Independent scaling of read and write workloads
- Optimized data models per operation type (e.g., column store for reads, row store for writes)
- Improved security — commands and queries have separate authorization boundaries
- Enables event-driven projections for real-time read model updates

## Challenges

- Eventual consistency between write and read models
- Increased system complexity
- Requires careful handling of stale read data

## Related

- [[Event Sourcing]] — Often used together with CQRS
- [[Event-Driven Architecture]] — The architectural context for CQRS usage
- [[Apache Kafka]] — Commonly used as the event bus bridging commands and queries
