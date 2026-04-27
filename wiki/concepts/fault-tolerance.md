---
title: "Fault Tolerance"
type: concept
tags: [distributed-systems, properties]
created: 2026-04-19
sources: [mixu-distributed-systems-book, "cockroachlabs.com/blog/what-is-fault-tolerance"]
---

Fault tolerance is the ability of a system to handle errors/outages without loss of functionality.

## Core Principle
Define what faults to expect, design system to tolerate them.

## Types of Faults

| Type | Description |
|------|------------|
| Crash-Fail | Nodes stop executing |
| Partition | Network fails between nodes |
| Byzantine | Nodes behave arbitrarily (rare) |

## How It Works

1. **Replicate data** across multiple nodes
2. **Quorum commits** — majority required to write
3. **Automatic recovery** — re-replicate when nodes fail
4. **Rebalance** — redistribute when nodes recover

## Quorum Formula

`max failures = (replication factor - 1) / 2`

- 3 replicas → tolerate 1 failure
- 5 replicas → tolerate 2 failures

## Related

[[Redundancy]], [[Failover]], [[High Availability]], [[Quorum]]