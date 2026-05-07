---
title: "System Design Primer: Cache"
type: source
tags: [system-design, caching, patterns]
created: 2026-05-08
sources: ["https://github.com/donnemartin/system-design-primer#cache"]
---

# System Design Primer: Cache

**Source:** [System Design Primer - Cache](https://github.com/donnemartin/system-design-primer#cache)

Caching section of the popular system-design-primer repo by Donne Martin. Covers cache locations, levels, update strategies, and tradeoffs.

## Cache Locations

- **Client caching** — OS or browser level
- **CDN caching** — globally distributed proxy servers
- **Web server caching** — reverse proxies (Varnish), serving static/dynamic content without contacting app servers
- **Database caching** — DB default configuration optimization
- **Application caching** — in-memory key-value stores (Memcached, Redis)

## Caching Levels

| Level | Approach | Challenge |
|-------|----------|-----------|
| Database Query | Hash query as key, store result | Hard to invalidate; one cell change may invalidate many cached queries |
| Object | Assemble data into objects/class instances | Must track data dependencies for invalidation |

## Four Cache Update Strategies

### 1. Cache-Aside (Lazy Loading)
- App reads from cache; on miss, loads from DB, stores in cache, returns
- Used by Memcached
- **Downsides:** 3 trips on miss, stale data, empty node on failure

### 2. Write-Through
- Cache is main data store; synchronously writes to DB
- Data never stale; slow writes; new nodes empty after failure

### 3. Write-Behind (Write-Back)
- App updates cache; async write to DB
- Fast writes; risk of data loss on cache failure

### 4. Refresh-Ahead
- Cache auto-refreshes recently accessed entries before TTL expiry
- Reduced latency if predictions accurate; wasteful if not

## Suggestions for Object-Level Caching

- User sessions
- Fully rendered web pages
- Activity streams
- User graph data

## Related Pages

- [[Caching]], [[Cache-Aside]], [[Write-Through Cache]], [[Write-Behind Cache]], [[Refresh-Ahead Cache]], [[Application Caching]], [[In-Memory Cache]]
