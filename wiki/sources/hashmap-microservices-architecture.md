---
title: "Hashmap: The What, Why, and How of a Microservices Architecture"
type: source
tags: [microservices, architecture, hashmap, system-design]
created: 2026-05-11
sources: ["medium.com/hashmapinc/the-what-why-and-how-of-a-microservices-architecture-4179579423a9"]
author: "Jetinder Singh (Hashmap, an NTT DATA Company)"
---

# Hashmap: The What, Why, and How of a Microservices Architecture

**Author:** Jetinder Singh — Hashmap, an NTT DATA Company
**Source:** Medium / Hashmap Inc.
**Published:** June 7, 2018

## Summary

A practical guide to understanding, adopting, and implementing a microservices architecture. Covers the definition, benefits, challenges, and an 8-key framework for getting started with microservices in an organization.

## Key Content

### What is Microservices Architecture?

A microservices architecture structures an application as a collection of **loosely coupled services** that can be developed, deployed, and maintained independently. Each service is responsible for a discrete task and communicates with other services through simple APIs to solve a larger complex business problem.

### Key Benefits

- **Team Scalability** — small teams own service boundaries, making it easier to scale development effort
- **Independent Deployment** — services deploy independently; hot services scale without redeploying the whole app
- **Fault Isolation** — an error in one service doesn't crash the entire application
- **Polyglot Flexibility** — each service can use the best-suited tech stack (language, database, etc.)

### 8 Keys to Getting Started

1. **How to Decompose** — break down the monolith along domain boundaries (domain-driven design)
2. **Building and Deploying** — each service has its own build pipeline; choose different stacks per service (e.g., User Service in Java, Recommendation Service in Python)
3. **Design Individual Services Carefully** — well-defined APIs, bounded contexts, single responsibility
4. **Decentralize Things** — decentralized data management, governance, and decision-making
5. **Deploy** — one microservice per operating system (or container) for isolation
6. **Making Standards** — establish standards for service dependencies, API versioning, and communication protocols
7. **Failure** — design for failure: circuit breakers, retries, timeouts, bulkheads
8. **Monitoring and Logging** — centralized logging, distributed tracing, health checks

## Related Wiki Pages

- [[Microservices]] — core concept page
- [[N-Tier Architecture]] — precursor pattern
- [[Client-Server Architecture]] — foundational model
- [[Circuit Breaker Pattern]] — fault tolerance for microservices
- [[Service Discovery]] — runtime service location
- [[Distributed Tracing]] — end-to-end request tracking
- [[Martin Fowler]] — co-author of seminal microservices article
