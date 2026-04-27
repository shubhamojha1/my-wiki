---
title: "CAP Theorem"
type: concept
tags: [distributed-systems, consistency, tradeoff]
created: 2026-04-19
sources: [mixu-distributed-systems-book, "algomaster.io/learn/system-design/cap-theorem"]
---

CAP theorem states that a distributed system can only provide two of: Consistency, Availability, Partition Tolerance.

## Three Properties

| Property | Meaning |
|----------|---------|
| Consistency (C) | Every read sees most recent write or error |
| Availability (A) | Every request gets non-error response |
| Partition Tolerance (P) | System works despite network failures |

## The Trade-Off

During a **network partition**, must choose:

- **CP**: Consistency over availability (MongoDB, ZooKeeper)
- **AP**: Availability over consistency (Cassandra, DynamoDB)

## System Types

| Type | Behavior |
|------|----------|
| CP | Sacrifice availability during partition |
| AP | Always respond, may return stale data |
| CA | Only when no partitions (theoretical) |