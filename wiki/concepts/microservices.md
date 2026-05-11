---
title: "Microservices"
type: concept
tags: [architecture, distributed-systems, microservices]
created: 2026-05-11
sources: ["hashmap-microservices-architecture"]
aliases: ["Microservices Architecture"]
---

# Microservices

An architectural style that structures an application as a collection of **loosely coupled, independently deployable services**, each responsible for a discrete business capability and communicating via lightweight APIs.

## Characteristics

- **Single Responsibility** — each service owns one bounded context or business capability
- **Independent Deployment** — services can be built, tested, and deployed separately
- **Decentralized Governance** — teams choose their own tech stacks (polyglot programming and persistence)
- **Fault Isolation** — failure in one service does not cascade to others
- **Autonomous Teams** — small teams own full lifecycle of their service(s)

## Benefits

- Scalable development (teams work in parallel)
- Independent scaling of hot services
- Easier technology upgrades (replace one service at a time)
- Faster release cycles with CI/CD

## Challenges

- Operational complexity (many services to monitor, deploy, and coordinate)
- Distributed system complexity (network latency, service discovery, data consistency)
- Testing across service boundaries
- Eventual consistency instead of ACID transactions

## Key Practices

- **Domain-Driven Design** — decompose along domain boundaries
- **Smart Endpoints, Dumb Pipes** — services are intelligent; communication channels are simple (HTTP/REST or async messaging)
- **CI/CD** — continuous integration and delivery for each service
- **Observability** — centralized logging, [[Distributed Tracing]], metrics, health checks
- **Design for Failure** — [[Circuit Breaker Pattern]], retries, timeouts, bulkheads
- **Service Discovery** — dynamic location of services at runtime ([Service Discovery]])

## Relationship to Other Patterns

Microservices extend the [[N-Tier Architecture]] concept by fully decomposing the application layer into independently deployable units. They contrast with monolithic architecture where all functionality is deployed as a single unit.

## See Also

- [[Serverless Architecture]] — serverless as a deployment model for microservices
- [[Client-Server Architecture]]
- [[N-Tier Architecture]]
- [[Service Discovery]]
- [[Circuit Breaker Pattern]]
- [[Distributed Tracing]]
- [[API Gateway]]
- [[Message Queue]]
- [[Martin Fowler]]
