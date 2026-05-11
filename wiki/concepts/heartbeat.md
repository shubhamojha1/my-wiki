---
title: "Heartbeat"
type: concept
tags: [distributed-systems, failure-detection, monitoring]
created: 2026-05-11
sources: [algomaster-heartbeats]
---

# Heartbeat

A **heartbeat** is a periodic signal sent from one component to another in a distributed system to monitor health and availability. Its purpose is to communicate: "I'm still here and working."

## Protocol

### Push Heartbeats
Nodes actively send heartbeat signals to a monitor at regular intervals.
- **Pro**: Immediate failure signal (missing heartbeat = likely failure)
- **Con**: Network overhead from continuous sending

### Pull Heartbeats
The monitor periodically queries nodes for their status.
- **Pro**: Monitor controls polling rate
- **Con**: Node may be dead but monitor hasn't polled yet

## Design Trade-offs

| Parameter | Too Aggressive | Too Conservative |
|-----------|---------------|-----------------|
| **Frequency** | Network congestion | Slow failure detection |
| **Timeout** | False positives (slow but alive = dead) | Long recovery delay |

## Payload

Heartbeats typically carry:
- Timestamp or sequence number
- Node identity
- Optional: load metrics, health status, version info

## Challenges

- **Network congestion**: High-frequency heartbeats at scale consume bandwidth
- **False positives**: Aggressive timeouts mark healthy-but-slow nodes as dead
- **Split-brain**: Network partition causes both sides to declare each other dead (requires quorum or lease mechanisms)
- **Resource usage**: Continuous monitoring consumes CPU and network

## Real-World Uses

- **Kubernetes**: Each node sends heartbeats to the control plane (kube-controller-manager) for node health tracking and scheduling decisions
- **Elasticsearch**: Nodes exchange heartbeats in a gossip network for cluster membership and state dissemination
- **Database replication**: Primary and replica exchange heartbeats to detect failures and trigger failover

## Related

- [[Failure Detector]] — Abstraction using timeouts and heartbeats
- [[Gossip Protocol]] — Heartbeats as part of gossip-based membership
- [[Split-Brain]] — Network partition scenario heartbeats can't resolve alone
- [[Sloppy Quorum]] — Handling failures without strict consistency
