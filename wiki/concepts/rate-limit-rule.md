---
title: "Rate Limit Rule"
type: concept
tags: [rate-limiting, api, configuration]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Rate Limit Rule

A **rate limit rule** is the policy object that defines how much traffic a particular client or endpoint is allowed to send.

## Fields

Common fields include:

- Client scope: user ID, IP address, API key, tenant, or global.
- Endpoint scope: all API requests or a narrower path such as search, timeline reads, or profile updates.
- Limit: request count, refill rate, or token bucket capacity.
- Time basis: fixed window, sliding window, or token refill interval.
- Priority: how to resolve overlapping rules.

## Layering

Production systems often apply multiple rules to the same request:

- Per-user limits such as "Alice can make 1000 requests/hour".
- Per-IP limits such as "this IP can make 100 requests/minute".
- Global limits such as "the API can handle 50,000 requests/second".
- Endpoint-specific limits such as "search is 10 requests/minute".

The request should be denied if any applicable rule is exhausted. In practice, the most restrictive active rule controls the decision.

## Related Concepts

- [[Rate Limiting]]
- [[Distributed Rate Limiter]]
- [[Dynamic Rate Limit Configuration]]
