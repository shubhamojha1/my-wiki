---
title: "Failure Detector"
type: concept
tags: [distributed-systems, failure]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Failure detectors abstract the problem of detecting crashed nodes using timeouts and heartbeats.

## Implementation
- Exchange heartbeat messages
- If no response before timeout, suspect failure

## Properties (Chandra & Toueg)

### Completeness
- **Strong**: Every crashed process eventually suspected by every correct process
- **Weak**: Every crashed process eventually suspected by some correct process

### Accuracy
- **Strong**: No correct process ever suspected
- **Weak**: Some correct process never suspected

## Tradeoffs
- Overly aggressive: incorrectly suspects working nodes
- Overly conservative: takes long to detect failures

## Accrual Failure Detectors
- Output suspicion level (0-1) rather than binary
- Application can decide tradeoff
- Used in Cassandra

## Connection to Consensus
Even weak failure detector (⋄W) can solve consensus in async systems.