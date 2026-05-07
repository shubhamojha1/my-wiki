---
title: "HTTP Caching"
type: concept
tags: [http, caching, protocol, web-performance]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/"]
---

# HTTP Caching

**Definition:** Caching performed at the HTTP protocol level, where responses are stored by intermediaries (browsers, proxies, CDNs) and reused for future requests without contacting the origin server.

## The Three Cache Actors

HTTP caching operates at three tiers:

| Tier | Examples | Location | Control |
|------|----------|----------|---------|
| [[Browser Caching]] | Chrome, Firefox disk cache | Client device | Cache-Control headers |
| [[Proxy Cache]] | Varnish, Squid, Nginx | Between client and origin | Cache-Control + config |
| [[CDN]] | CloudFront, Akamai, Fastly | Edge servers globally | Cache-Control + management UI |

## Universal HTTP Semantics

All three actors speak HTTP and comply with RFC 7234. From a modeling perspective, any chain of caching proxies is equivalent to a single logical proxy between client and origin. This simplification helps reason about caching behavior, though chaining can produce subtle edge cases (e.g., Age header accumulation).

## The Latency Problem

HTTP caching exists because of a fundamental observation: **bandwidth is no longer the bottleneck — latency is**.

- A 20kB resource needs ~8 round trips (DNS + TCP + TLS + TCP slow-start)
- A typical SPA makes 75 such requests → ~600 round trips → ~30 seconds at 50ms RTT
- Bandwidth stops being the bottleneck above ~5 Mb/s
- Light speed in fiber is limited; reducing distance is the only solution
- HTTP caching "reduces distance" by serving from browser disk or CDN edge

## Cache-Control and the Specification

HTTP caching behavior is governed by:
- **Cache-Control** headers (max-age, s-maxage, private, public, no-cache, no-store, must-revalidate)
- **ETag** — entity tag for cache validation
- **Last-Modified / If-Modified-Since** — timestamp-based freshness
- **Expires** — legacy absolute expiration (superseded by Cache-Control: max-age)
- **Age** — how long the response has been in a proxy cache

Detailed mechanics of freshness, revalidation, and representations are covered in Part 2 of this series.

## The Caching Abstraction

Any multi-proxy setup can be simplified to a single caching proxy for reasoning:

```
[Client] ←→ [Cache (single logical proxy)] ←→ [Origin Server]
```

This holds because all proxies implement the same HTTP caching specification transparently — they appear as servers to clients and as clients to servers.

## Related Pages

- [[Browser Caching]], [[Proxy Cache]], [[CDN]], [[Web Caching]], [[Caching]], [[HTTP]], [[Cache Invalidation]], [[DNS Caching]], [[TLS]]
