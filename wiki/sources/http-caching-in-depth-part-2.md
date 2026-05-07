---
title: "An In-depth Introduction to HTTP Caching: Cache-Control & Vary"
type: source
tags: [http, caching, cache-control, vary, content-negotiation]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
---

# An In-depth Introduction to HTTP Caching: Cache-Control & Vary

**Source:** freeCodeCamp article by Léo Jacquemin (Oct 2019)  
**Series:** Part 2 of a multi-part series on HTTP caching

This article covers the **how** of HTTP caching — Cache-Control directives, the Vary header for content negotiation, and the 4-outcome decision tree.

## The 4-Outcome Decision Tree

Every cacheable request has four possible outcomes:
1. **Cache hit** — fresh matching resource found, served immediately
2. **Cache miss (empty)** — no matching resource stored; forwarded to origin
3. **Cache miss (stale + successful validation)** — stale resource, origin returns 304 Not Modified; cache updates headers and serves local copy
4. **Cache miss (stale + failed validation)** — stale resource, origin returns 200 OK with updated body; cache stores new version

## Cache-Control Directives

| Directive | Meaning |
|-----------|---------|
| `max-age=<seconds>` | Lifetime of a representation |
| `no-store` | Never store anything, delete existing copies |
| `no-cache` | Never serve from cache without revalidation (cache hit forbidden) |
| `must-revalidate` | Never serve stale (fresh is OK, stale must revalidate) |
| `public` | Cacheable by any cache (browser + shared proxy + CDN) |
| `private` | Cacheable only by browser cache (default) |
| `s-maxage=<seconds>` | Like max-age, but only for shared/public caches; overrides max-age |
| `stale-while-revalidate=<seconds>` | Serve stale immediately while revalidating in background |
| `stale-if-error=<seconds>` | Serve stale if origin returns 5xx |

### Common Misconception: no-cache ≠ no-store
- `no-store`: never store
- `no-cache`: store but never cache-hit (always revalidate)
- `must-revalidate`: store and cache-hit when fresh, but never serve stale

Mnemonic: **no-store = never store; no-cache = never cache hit; must-revalidate = never serve stale**

## The Vary Header

Caches construct cache keys primarily from URIs. However, content negotiation means the same URI can have multiple representations. The Vary header tells caches which request headers were used to generate the response, so the cache key can be extended.

Example: `Vary: Accept-Language` → cache key becomes `https://example.net/home.html_fr-FR`

### Challenges
- **Multiple Vary headers** → combinatorial explosion of cache entries
- **Normalization required** — `fr, fr-FR, fr_FR` must be grouped as `FR`
- **Accept-Encoding** — found in 44 different forms in the wild
- **User-Agent** — 8000+ variations sampled by Fastly; extremely dangerous to Vary on

### Best Practice: Browser caches don't need Vary
Each browser cache only stores representations matching its own user's preferences, making Vary unnecessary for private caches.

## Freshness vs Validation

Two distinct mechanisms:
- **Freshness control** — happens in the cache; based solely on time (max-age, s-maxage)
- **Validation** — happens at the origin server; based on ETags and Last-Modified timestamps

Fresh ≠ most recent version. A cached resource may be fresh (within TTL) but stale in content — the cache won't revalidate until the TTL expires.

## Conditional Requests

When a resource is stale, the cache sends a conditional request:
- `If-None-Match: <etag>` — matches ETag
- `If-Modified-Since: <date>` — matches Last-Modified

Responses:
- **304 Not Modified** — resource unchanged, cache updates headers, serves local copy (body empty)
- **200 OK** — resource changed, full response with updated ETag/Last-Modified

## Related Pages

- [[Cache-Control]], [[Vary Header]], [[Conditional Request]], [[ETag]], [[HTTP Caching]], [[Browser Caching]], [[Proxy Cache]], [[CDN]]
