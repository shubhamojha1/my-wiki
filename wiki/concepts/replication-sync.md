---
title: "Synchronous Replication"
type: concept
tags: [distributed-systems, replication]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Synchronous replication (also: eager, active, push, pessimistic) waits for all replicas before responding to client.

## Communication Pattern
1. Client sends request
2. Server contacts all N-1 other servers
3. Waits for all acknowledgments
4. Returns response to client

## Properties

### Write Pattern
- N-of-N approach (all nodes must respond)
- Slowest server determines speed
- Sensitive to network latency

### Fault Tolerance
- Cannot tolerate loss of any server
- If any node fails, writes block

### Durability
- Strong guarantees
- Client certain all N servers received/stored

## Use Cases
- When data cannot be lost
- Financial systems
- Critical metadata