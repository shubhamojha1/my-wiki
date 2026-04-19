---
title: "System Model"
type: concept
tags: [distributed-systems, abstraction]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

A system model is a set of assumptions about the environment and facilities on which a distributed system is implemented.

## Key Assumptions

### Node Properties
- Ability to execute programs
- Volatile vs stable storage
- Clock (accurate or not)

### Communication Link Properties
- Reliable or unreliable
- Message ordering (FIFO)
- Latency bounds

### Timing Properties
- Synchronous: known bounds on message delay
- Asynchronous: no bounds
- Partially synchronous: occasional bounds

## Robust System Models
Make weakest assumptions → most tolerant of different environments.

## Failure Models

### Crash-Recovery
Nodes fail by crashing, may recover later.

### Partition
Network fails between nodes.

### Byzantine
Arbitrary faults including malicious behavior.