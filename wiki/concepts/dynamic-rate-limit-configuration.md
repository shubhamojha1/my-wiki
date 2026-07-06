---
title: "Dynamic Rate Limit Configuration"
type: concept
tags: [rate-limiting, configuration, distributed-systems]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Dynamic Rate Limit Configuration

**Dynamic rate limit configuration** lets operators change rate-limit rules without redeploying gateway or application code.

## Why It Matters

Production systems need to:

- Raise limits during launches or known traffic events.
- Lower limits during abuse or unexpected overload.
- Give premium customers higher quotas.
- Tune endpoint-specific limits as backend capacity changes.

## Poll-Based Configuration

Gateways periodically read rules from a database or configuration service and cache them locally. A polling interval such as 30 seconds is simple and operationally robust.

Trade-off: rules do not propagate instantly. Emergency reductions may take one polling interval to reach all gateways.

## Push-Based Configuration

A configuration service pushes changes to gateways immediately. [[ZooKeeper]], Redis pub/sub, or a custom service with persistent connections can implement this pattern.

Trade-off: lower propagation delay but more operational complexity. The system must handle connection loss, partial updates, gateways that miss notifications, and fallback behavior when the push channel is down.

## Related Concepts

- [[Rate Limit Rule]]
- [[Distributed Rate Limiter]]
- [[ZooKeeper]]
- [[Pub/Sub Messaging]]
