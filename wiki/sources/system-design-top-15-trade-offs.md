---
title: "System Design: Top 15 Trade-Offs"
type: source
tags: [system-design, trade-offs, architecture, algomaster]
created: 2026-05-12
sources: []
---

# System Design: Top 15 Trade-Offs

An AlgoMaster article by Ashish Pratap Singh (Mar 2024) cataloging 15 fundamental trade-offs in system design with examples.

## The 15 Trade-Offs

1. [[System Design Trade-Offs|Scalability vs Performance]] — Adding machines helps scale but adds coordination overhead that can hurt latency
2. [[System Design Trade-Offs|Vertical vs Horizontal Scaling]] — Vertical: simpler, limited ceiling, SPOF. Horizontal: near-limitless, complex distributed mgmt
3. [[System Design Trade-Offs|Latency vs Throughput]] — Low latency for real-time (gaming); high throughput for data-intensive (analytics)
4. [[System Design Trade-Offs|SQL vs NoSQL]] — SQL: strong schema, ACID, hard to scale horizontally. NoSQL: flexible, scales easy, weaker consistency
5. [[System Design Trade-Offs|Consistency vs Availability]] — CAP Theorem: choose 2 of 3 (C, A, P). CP: bank transactions. AP: messaging service
6. [[System Design Trade-Offs|Strong vs Eventual Consistency]] — Strong: immediate consistency (banking). Eventual: short delay tolerated (Instagram feed)
7. [[System Design Trade-Offs|Read-Through vs Write-Through Cache]] — Read-through: lazy population, good for read-heavy. Write-through: sync write to cache+DB, prevents loss
8. [[System Design Trade-Offs|Batch vs Stream Processing]] — Batch: periodic, full dataset (billing). Stream: real-time, per-event (fraud detection)
9. [[System Design Trade-Offs|Synchronous vs Asynchronous Processing]] — Sync: wait, simple (payment). Async: background, decoupled (photo upload)
10. [[System Design Trade-Offs|Stateful vs Stateless Architecture]] — Stateful: remembers context (shopping cart). Stateless: no session memory (REST API)
11. [[System Design Trade-Offs|Long Polling vs WebSockets]] — Long polling: hold request open, HTTP compatible. WebSockets: full-duplex persistent connection
12. [[System Design Trade-Offs|Normalization vs Denormalization]] — Normalization: less redundancy, more joins. Denormalization: faster reads, data duplication
13. [[System Design Trade-Offs|Monolithic vs Microservices]] — Monolith: simple, hard to scale. Microservices: scalable, operationally complex
14. [[System Design Trade-Offs|REST vs GraphQL]] — REST: multiple endpoints, well-known. GraphQL: single endpoint, flexible queries, steeper learning curve
15. [[System Design Trade-Offs|TCP vs UDP]] — TCP: reliable, ordered, connection-based. UDP: fast, loss-tolerant, connectionless

## Key Insight

Every system design decision is a trade-off. Understanding these 15 pairs helps designers make intentional, informed choices based on the specific requirements and constraints of each system.

## Source

- AlgoMaster: [System Design: Top 15 Trade-Offs](https://blog.algomaster.io/p/system-design-top-15-trade-offs) (Mar 2024)
