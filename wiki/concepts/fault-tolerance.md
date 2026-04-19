---
title: "Fault Tolerance"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Fault tolerance is the ability of a system to behave in a well-defined manner when faults occur.

## Core Principle
Define what faults you expect, then design a system or algorithm tolerant of them. You can't tolerate faults you haven't considered.

## Types

### Crash-Fail
Nodes stop executing. Most common assumption.

### Partition
Network fails between nodes. Nodes remain operational but can't communicate.

### Byzantine
Nodes behave arbitrarily/maliciously. Rare in commercial systems due to complexity and cost.

## Redundancy Levels
- Component redundancy
- Server redundancy  
- Datacenter redundancy

## Tradeoffs
More redundancy = higher availability but also higher probability of some component failing (increasing with number of components).