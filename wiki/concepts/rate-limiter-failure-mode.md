---
title: "Rate Limiter Failure Mode"
type: concept
tags: [rate-limiting, availability, fault-tolerance]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Rate Limiter Failure Mode

A **rate limiter failure mode** defines what the system does when the limiter cannot reach its backing state store or cannot confidently evaluate a request.

## Fail-Open

Fail-open allows requests through when the limiter cannot make a decision.

Benefits:

- Preserves API availability.
- Avoids rejecting legitimate user traffic during limiter outages.

Risks:

- Temporarily removes abuse protection.
- Can cause cascading failure if the outage coincides with a traffic spike.
- Sends all traffic downstream, possibly overwhelming databases or application services.

## Fail-Closed

Fail-closed rejects requests when the limiter cannot make a decision, commonly with HTTP 503 or 429.

Benefits:

- Protects downstream services.
- Prevents unverified traffic from bypassing controls.

Risks:

- Can make a healthy backend appear unavailable.
- May trigger client retry storms if clients handle failures poorly.

## Choosing

The Hello Interview social-media design chooses fail-closed. Its reasoning is that rate-limit failures often happen during high traffic, when protection is most important. For payment or high-security systems, fail-closed can also be the safer default. For low-risk public APIs, fail-open may be acceptable if backend capacity is resilient.

The better answer is to reduce the likelihood of this choice through [[Redis Cluster]] failover, replication, monitoring, and clear alerts.

## Related Concepts

- [[Distributed Rate Limiter]]
- [[Availability]]
- [[Fault Tolerance]]
- [[Circuit Breaker Pattern]]
