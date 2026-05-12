---
title: "System Design Trade-Offs"
type: concept
tags: [system-design, architecture, trade-offs]
created: 2026-05-12
sources: ["system-design-top-15-trade-offs"]
---

# System Design Trade-Offs

Rule No. 1 of system design: everything is a trade-off. There is no perfect architecture — only informed choices that optimize for specific requirements while accepting unavoidable downsides.

## 1. Scalability vs Performance

**Scalability** is the ability to handle more work by adding resources. **Performance** is how fast a single unit of work completes. Adding machines improves scalability but introduces coordination overhead that can degrade per-request latency.

See [[Scalability]], [[Latency vs Throughput]].

## 2. Vertical vs Horizontal Scaling

**Vertical scaling** (scale up): add CPU/RAM to an existing machine — simple but has a physical ceiling and creates a [[Single Point of Failure]]. **Horizontal scaling** (scale out): add more machines — near-limitless but brings distributed system complexity (coordination, consistency, networking).

See [[Horizontal Scalability]].

## 3. Latency vs Throughput

**Latency** is delay per unit of data. **Throughput** is total data processed per unit time. Low latency is critical for real-time apps (online gaming, video calls). High throughput matters for data-intensive batch workloads (analytics pipelines).

See [[Latency vs Throughput]], [[Latency]].

## 4. SQL vs NoSQL

**SQL** (relational): structured schema, [[ACID Transactions]], powerful joins, harder to [[Horizontal Scalability|scale horizontally]]. Best for financial systems, inventory management. **[[NoSQL]]**: flexible schema, easy horizontal scaling, weaker consistency guarantees. Best for real-time recommendations, IoT, high-velocity data.

See [[SQL vs NoSQL|SQL vs NoSQL]].

## 5. Consistency vs Availability (CAP)

The [[CAP Theorem]] states a distributed system can guarantee only two of: Consistency, Availability, Partition Tolerance. Network partitions are inevitable, so the real choice is **CP vs AP**. CP for banking (can't show wrong balance). AP for messaging (better to show stale data than none).

See [[Consistency Model]], [[Eventual Consistency]].

## 6. Strong vs Eventual Consistency

**Strong consistency**: all reads return the latest write — critical for banking, booking systems. **[[Eventual Consistency]]**: replicas converge over time — acceptable for social feeds, DNS, CDNs. The trade-off is correctness guarantees vs availability and latency.

## 7. Read-Through vs Write-Through Cache

**Read-through cache**: load data into cache on cache miss. Ideal for read-heavy, infrequently updated data (product catalog). **Write-through cache**: write to both cache and primary storage simultaneously. Prevents data loss and keeps cache fresh, useful for write-heavy workloads (booking systems). Both are [[Cache-Aside|cache strategies]].

See [[Write-Through Cache]], [[Read-Through Cache]].

## 8. Batch vs Stream Processing

**[[Offline Processing|Batch processing]]**: collect data over a time window, process all at once. Simple, cost-effective for periodic tasks (daily billing, payroll). **Stream processing**: process each event as it arrives. Real-time, stateful — essential for fraud detection, monitoring dashboards.

## 9. Synchronous vs Asynchronous Processing

**Synchronous**: caller blocks until response. Simple to reason about, natural for payments and auth. **Asynchronous**: caller fires and forgets. Decouples components, enables background work (photo uploads, notifications). Async adds [[Message Queue]] complexity and eventual response handling.

## 10. Stateful vs Stateless Architecture

**Stateful**: server remembers session context across requests (shopping cart). Simpler client logic, but harder to [[Horizontal Scalability|scale horizontally]] (sticky sessions required). **Stateless**: each request is independent with all context provided ([[REST API]]). Easy to scale and route to any server, but shifts state management to the client or external store ([[Redis]], DB).

See [[Stateful Architecture]], [[Stateless Architecture]], [[Session Management]].

## 11. Long Polling vs WebSockets

**[[Long-Polling|Long polling]]**: client requests, server holds the connection open until data arrives. HTTP-compatible, simpler to implement but higher overhead per message. **[[WebSockets]]**: persistent full-duplex TCP connection. Low latency, efficient for real-time bidirectional communication (chat, gaming). Trade-off: infrastructure complexity vs polling overhead.

## 12. Normalization vs Denormalization

**Normalization**: split data into related tables, minimize redundancy, maximize integrity. More joins at read time. **[[Data Denormalization|Denormalization]]**: combine data into fewer tables, duplicate fields. Faster reads at the cost of write complexity and storage overhead. Normalized for transactional systems; denormalized for read-heavy analytics.

## 13. Monolithic vs Microservices

**Monolithic**: single deployable unit. Simple development, deployment, and testing. Becomes a bottleneck as teams and features grow. **[[Microservices]]**: independently deployable services per bounded context. Scales teams and technology independently, but introduces operational complexity, [[Service Discovery]], [[Distributed Tracing]], and data consistency challenges.

## 14. REST vs GraphQL

**[[REST API|REST]]**: resource-oriented endpoints, well-understood, cacheable, but suffers from [[Over-fetching]] and [[Under-fetching]]. **[[GraphQL]]**: single endpoint, client-specified queries, eliminates over/under-fetching. Trade-off: steep learning curve, complex caching, and server-side query cost analysis.

## 15. TCP vs UDP

**[[TCP]]**: connection-oriented, reliable delivery, ordered, congestion control. Higher overhead but guarantees delivery — essential for email, file transfer, web. **[[UDP]]**: connectionless, fire-and-forget, no ordering guarantees. Lower latency, loss-tolerant — ideal for streaming, gaming, VoIP. The choice is reliability vs speed.
