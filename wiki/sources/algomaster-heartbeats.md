---
title: "AlgoMaster: Heartbeats in Distributed Systems"
type: source
tags: [distributed-systems, heartbeat, failure-detection]
created: 2026-05-11
sources: [algomaster-heartbeats]
---

# AlgoMaster: Heartbeats in Distributed Systems

**Author:** Ashish Pratap Singh
**URL:** https://blog.algomaster.io/p/heartbeats-in-distributed-systems
**Published:** April 20, 2024

## Summary

An introductory overview of heartbeats as a failure detection mechanism in distributed systems — how they work, types, challenges, and real-world examples from Kubernetes, Elasticsearch, and database replication.

## Key Concepts Covered

- **Definition**: Periodic signal from one component to another to monitor health ("I'm still here")
- **Purpose**: failure detection, triggering recovery, monitoring, load balancing
- **Protocol**: push vs pull heartbeats
- **Trade-offs**: frequency (bandwidth vs detection speed), timeout (false positives vs slow recovery)
- **Payload**: typically timestamp/sequence number, can include load metrics
- **Challenges**: network congestion, false positives, resource usage, split-brain scenarios
- **Real-world**: Kubernetes node → control plane heartbeats, Elasticsearch gossip network, DB primary-replica replication
