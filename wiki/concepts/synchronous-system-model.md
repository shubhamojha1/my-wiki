---
title: "Synchronous System Model"
type: concept
tags: [distributed-systems, timing]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Synchronous system model assumes processes execute in lock-step with known bounds on message transmission delay and accurate clocks.

## Characteristics
- Known upper bound on message delay
- Processes execute at known rates
- Accurate clocks available
- Nodes have same "experience"

## Advantages
- Easier to solve problems
- Can make inferences about timing
- Can rule out inconvenient failure scenarios

## Disadvantages
- Unrealistic for most settings
- Real-world networks have unbounded delays
- Not practical for production systems

## Usage
- Academic analysis
- Embedded systems with guarantees
- Simulations