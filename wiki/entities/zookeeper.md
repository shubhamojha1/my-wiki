---
title: "ZooKeeper"
type: entity
tags: [distributed-systems, coordination, configuration]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter", "kleppmann-distributed-locking"]
---

# ZooKeeper

ZooKeeper is a distributed coordination service used for configuration management, service coordination, leader election, and lock-like patterns. In [[Dynamic Rate Limit Configuration]], it is useful because clients can watch configuration znodes and receive notifications when rules change.

## Rate Limiter Use

For a [[Distributed Rate Limiter]], ZooKeeper can hold rate-limit rules and push updates to API gateways quickly. This avoids waiting for the next polling interval when operators need to reduce or raise limits during incidents, launches, or traffic spikes.

The trade-off is operational complexity: gateways must handle session loss, missed notifications, partial rollout, and fallback to a cached configuration.

## Related Concepts

- [[Dynamic Rate Limit Configuration]]
- [[Distributed Lock]]
- [[Fencing Token]]
- [[ZAB]]
