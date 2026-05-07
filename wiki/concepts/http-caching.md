---
title: "HTTP Caching"
type: concept
tags: [http, caching, protocol, web-performance]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/", "https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
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

## The 4-Outcome Decision Tree

Every cacheable request has exactly four possible outcomes:

```
                    ┌─ Cache hit (fresh) → serve immediately
                    │
[Request] → [Cache] ── Cache miss (empty) → forward to origin → store → serve
                    │
                    └─ Cache miss (stale) ──┬─ 304 (revalidated) → update headers, serve local
                                           │
                                           └─ 200 (changed) → store new, serve
```

| Outcome | Latency | Bandwidth | Server Impact |
|---------|---------|-----------|---------------|
| Cache hit (fresh) | Zero | Zero | None |
| 304 (validated) | One round-trip | Headers only (~200B) | Minimal body generation |
| 200 (changed/empty) | One round-trip | Full response | Full processing |

## Cache-Control Directives

The [[Cache-Control]] header is the primary mechanism for origin servers to communicate caching policy. Key directives:

| Directive | Meaning |
|-----------|---------|
| `max-age=<sec>` | Freshness lifetime in seconds |
| `no-store` | Never store anything |
| `no-cache` | Store but always revalidate (never cache hit) |
| `must-revalidate` | Never serve stale content |
| `public` | Cacheable by any cache (browser + shared) |
| `private` | Cacheable only by browser cache (default) |
| `s-maxage=<sec>` | Shared-cache-only max-age (overrides max-age) |
| `stale-while-revalidate=<sec>` | Serve stale while revalidating in background |
| `stale-if-error=<sec>` | Serve stale if origin returns 5xx |

See [[Cache-Control]] for full details on each directive.

## Freshness vs Validation

**Two distinct mechanisms that serve different purposes:**

- **Freshness control** — happens entirely in the cache; based solely on time (`max-age`, `s-maxage`)
- **Validation** — happens at the origin server; based on [[ETag]] and `Last-Modified` timestamps via [[Conditional Request]]

A resource can be **fresh** (within its TTL) but **outdated in content** — the cache will not contact the origin until the timer expires. Setting `max-age=86400` on an HTML page means users may see stale content for up to 24 hours with no way to force a refresh.

## The Vary Header

The [[Vary Header]] tells caches which request headers were used to generate different representations of the same URI:

```
Vary: Accept-Language, Accept-Encoding
```

Without Vary, a cache could serve a brotli-compressed French page to a user who speaks English on a browser that doesn't support brotli.

Key challenges:
- **Combinatorial explosion** — varying on multiple headers multiplies cache entries
- **Normalization needed** — `fr, fr-FR, fr_FR` must all map to the same cache key
- **Never Vary on User-Agent** — Fastly found 8,000+ distinct values in 100K requests

## The Caching Abstraction

Any multi-proxy setup can be simplified to a single caching proxy for reasoning:

```
[Client] ←→ [Cache (single logical proxy)] ←→ [Origin Server]
```

This holds because all proxies implement the same HTTP caching specification transparently — they appear as servers to clients and as clients to servers.

## Related Pages

- [[Browser Caching]], [[Proxy Cache]], [[CDN]], [[Cache-Control]], [[Vary Header]], [[Conditional Request]], [[ETag]], [[Web Caching]], [[Caching]], [[HTTP]], [[Cache Invalidation]], [[DNS Caching]], [[TLS]]
