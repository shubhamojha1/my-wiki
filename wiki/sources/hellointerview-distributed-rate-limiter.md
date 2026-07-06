---
title: "Design a Distributed Rate Limiter"
type: source
tags: [system-design, rate-limiting, api-gateway, redis]
created: 2026-07-07
sources: ["https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# Design a Distributed Rate Limiter

Source: [[Hello Interview]] system design problem breakdown, published/updated June 24, 2026.

## Problem Scope

The article designs a request-level [[Distributed Rate Limiter]] for a social media API. The limiter controls individual HTTP requests such as posting updates, fetching timelines, and uploading photos. It focuses on server-side enforcement because clients cannot be trusted to self-regulate; client-side throttling is useful only as a cooperative complement.

Functional requirements:

- Identify clients by user ID, IP address, or API key.
- Enforce configurable request rules such as 100 requests per minute per user.
- Reject excess requests with HTTP 429 and helpful headers such as `X-RateLimit-Remaining`, `X-RateLimit-Reset`, and optionally `Retry-After`.

Non-functional assumptions:

- Target load is roughly 1 million requests/second across 100 million daily active users.
- Each check should add less than 10 ms of latency.
- High availability matters, and eventual consistency is acceptable because small delays in enforcement across nodes are tolerable.
- Strong consistency across all nodes is out of scope.

Out of scope: complex analytics over rate-limit data and long-term persistence of rate-limit data.

## Core Model

The core entities are [[Rate Limit Rule]], clients, and requests. A rule defines the limit, window/refill policy, target client type, and endpoint scope. A client can be a user ID, IP address, API key, or a combination. A request supplies the context needed to identify the client and choose applicable rules.

The conceptual interface is:

```text
isRequestAllowed(clientId, ruleId) -> {
  passes: boolean,
  remaining: number,
  resetTime: timestamp
}
```

The return values are used for both the allow/deny decision and client-facing rate-limit response headers.

## Placement Options

The article compares three placements:

- In-process limiter: fastest because state is local memory, but each application server only sees its own traffic. Behind a load balancer, a global limit can be violated by a factor close to the server count.
- Dedicated rate-limiter service: centralizes state and can receive rich application context such as subscription tier, account status, endpoint, or special business rules. The trade-off is an extra network hop on every request, another critical service to operate, and explicit fail-open/fail-closed decisions during outages.
- [[API Gateway]] or load-balancer limiter: places enforcement at the edge before requests hit application servers. This is the recommended approach because blocked requests never consume backend capacity and no extra service hop is added after the gateway. The main limitation is that the limiter only sees request-visible data such as headers, path, IP address, API key, and JWT claims.

The chosen architecture is gateway-based rate limiting backed by shared state in [[Redis]] or [[Redis Cluster]].

## Client Identification

Because the gateway sees only the HTTP request, identification relies on request data:

- User ID from an `Authorization` header/JWT for authenticated APIs.
- IP address, often from `X-Forwarded-For`, for anonymous or public APIs.
- API key, usually from `X-API-Key`, for developer APIs.

Real systems layer several rules. A request may be constrained by per-user, per-IP, global, and endpoint-specific rules. The effective decision should enforce the most restrictive applicable rule.

## Algorithm Choice

The article reviews four production algorithms:

- [[Fixed Window Counter]]: simple counter per fixed time bucket, but window boundaries allow bursts such as 100 requests at 12:00:59 and another 100 at 12:01:00.
- [[Sliding Window Log]]: exact by storing every request timestamp, but memory and scanning costs grow with request volume.
- [[Sliding Window Counter]]: stores current and previous counters, weighting the previous window by overlap; more accurate than fixed windows but approximate.
- [[Token Bucket]]: stores current tokens and last refill timestamp, allowing bursts up to bucket capacity while enforcing an average refill rate.

The chosen algorithm is [[Token Bucket]] because it is simple, memory efficient, and fits bursty API traffic. Each client bucket stores only `tokens` and `last_refill`.

## Redis State And Atomicity

Gateway instances cannot keep token buckets in local memory because load-balanced requests for the same client would split state across gateways. Redis becomes the shared source of truth.

A naive Redis flow reads state with `HMGET client:bucket tokens last_refill`, calculates refills, then writes `tokens`, `last_refill`, and `EXPIRE` inside `MULTI/EXEC`. The article points out that this is still racy because the read happens outside the transaction. Two concurrent requests can read the same token count and both decide they are allowed.

The fix is to move the whole read-calculate-update decision into one Redis Lua script. Redis executes Lua scripts atomically, expanding the atomic boundary to the complete read-modify-write sequence. `EXPIRE` is used to delete inactive buckets and prevent unbounded memory growth.

## Rejection Behavior

The article recommends fail-fast rejection for interactive APIs. Queuing excess requests can consume memory, create unpredictable response times, and cause clients to retry anyway.

A complete rejection should return HTTP 429 with headers like:

```text
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1640995200
Retry-After: 60
```

These headers let well-behaved clients implement backoff instead of repeatedly hammering the API.

## Scaling To 1M Requests/Second

A single Redis instance cannot handle the target scale. The article estimates one Redis instance might handle roughly 100k-200k operations/second, and a rate-limit check requires at least a read and write if not wrapped in a script. At 1M requests/second, Redis state must be sharded.

The shard key must be the same identifier used for enforcement: user ID, IP address, or API key. All requests for a given client must route to the same shard; otherwise that client's bucket is split and the limit becomes meaningless.

The article describes two approaches:

- Consistent hashing in the gateways, using the client identifier to choose the Redis shard.
- [[Redis Cluster]], which divides keys into 16,384 hash slots and handles routing/failover for clients.

With 10 Redis shards, each handling about 100k checks/second, the design can reach the 1M requests/second target.

## Availability And Failure Mode

The article frames Redis outage behavior as a [[Rate Limiter Failure Mode]] decision:

- Fail-closed: reject requests when Redis cannot be reached. This preserves backend protection but can make a healthy API appear down.
- Fail-open: allow requests when Redis cannot be reached. This preserves availability but can remove protection exactly when traffic is already high.

For the social media platform, the article chooses fail-closed. Viral events and traffic spikes are precisely when rate limiting is most important; failing open could overload backend databases and turn a limiter outage into full platform collapse.

The better long-term answer is high availability for Redis: master-replica replication, automatic promotion, Redis Cluster failover, monitoring CPU/memory/network health, rate-limiter success rate, latency, and alerts when fallback behavior is triggered.

## Latency Optimization

Every gateway-to-Redis check adds network latency. Main mitigations:

- Connection pooling to avoid new TCP handshakes per request.
- Regional deployment so API gateways and Redis clusters sit close to users.
- Accepting eventual consistency across regions when the latency gain is worth it.
- Considering Redis pipelining, Lua scripts, or batching only when the simpler mitigations are not enough.

The article warns that local caching of rate-limit state is risky because stale cache entries can allow incorrect decisions.

## Hot Keys

[[Rate Limiter Hot Key]] scenarios can come from abusive clients or legitimate high-volume clients. A single user/IP/API key would need to generate tens of thousands of checks per second to overload one Redis shard, so many hot keys imply abuse, misconfigured clients, or unusual shared-IP scenarios.

Mitigations differ by cause:

- For legitimate high-volume clients: client-side rate limiting, batching, premium tiers, or dedicated infrastructure.
- For abuse: temporary blocklists, DDoS protection such as Cloudflare or AWS Shield, and upstream filtering before the limiter.

The article notes that IP-based rules should account for corporate NATs and public WiFi; authenticated user limits are often more precise.

## Dynamic Configuration

Production systems need [[Dynamic Rate Limit Configuration]] so limits can change without redeploying code.

Poll-based configuration stores rules in a database or config service and has gateways refresh on a schedule such as every 30 seconds. This is simple and often enough, but emergency changes are delayed.

Push-based configuration sends updates immediately to gateways. The article names [[ZooKeeper]], Redis pub/sub, and custom persistent config services as options. Push-based updates reduce propagation delay but add complexity around connection failures, partial updates, and fallback behavior.

## Interview Expectations

Mid-level candidates should identify gateway placement, one solid algorithm such as token bucket, Redis as shared state, and basic sharding needs.

Senior candidates should compare algorithms and placements, understand atomic Redis updates, discuss fail-open vs fail-closed, connection pooling, hot keys, Redis availability, and configuration management.

Staff+ candidates should move quickly through fundamentals and focus on production operations: multi-region behavior, observability, canaries, failure modes, gradual rollout, and real-world operational trade-offs.

## Related Pages

- [[Distributed Rate Limiter]]
- [[Rate Limiting]]
- [[Token Bucket]]
- [[API Gateway]]
- [[Redis]]
- [[Redis Cluster]]
- [[Consistent Hashing]]
- [[Rate Limiter Failure Mode]]
- [[Dynamic Rate Limit Configuration]]
- [[Rate Limiter Hot Key]]
