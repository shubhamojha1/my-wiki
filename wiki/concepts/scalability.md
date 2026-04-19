---
title: "Scalability"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Scalability is the ability of a system to handle growing amounts of work without degrading performance.

## Dimensions

### Size Scalability
Adding more nodes should make the system linearly faster; growing dataset should not increase latency.

### Geographic Scalability
Using multiple data centers to reduce response time while handling cross-data center latency.

### Administrative Scalability
Adding more nodes should not increase administrative costs (e.g., admin-to-machine ratio).

## Ideal Case
Linear scaling: 2x nodes → 2x performance. In practice, coordination overhead prevents perfect scaling.

## Key Challenge
Tradeoffs between size, geographic distribution, and administrative complexity.