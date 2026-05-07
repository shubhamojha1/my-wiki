---
title: "Caching"
type: concept
tags: [performance, architecture, optimization]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/", "https://aws.amazon.com/caching/", "https://github.com/donnemartin/system-design-primer#cache"]
---

# Caching

**Definition:** Storing copies of data or precomputed results in faster storage to reduce access latency and backend load.

## What Caching Solves

Caching enables:
1. **Better resource utilization** — More work from existing hardware
2. **Reduced latency** — Faster response times for cached data
3. **New product requirements** — Makes previously unattainable features feasible

## Three Caching Strategies

### 1. Precalculate Results
Compute expensive results in advance (e.g., daily analytics summaries)

### 2. Pre-generate Indexes
Create optimized access structures (e.g., "suggested users" based on click history)

### 3. Cache Frequently Accessed Data
Store copies in a faster backend (e.g., Memcached instead of PostgreSQL)

## Timing Considerations

Caching is important **earlier** in development than load balancing. Starting with a consistent caching strategy:
- Saves time later
- Ensures access patterns work with caching mechanisms
- Avoids optimizing patterns that become irrelevant with caching

## Caching Layers

```
[User Request]
    ↓
[CDN Cache] (static assets)
    ↓
[Application Cache] (computed data)
    ↓
[Database Cache] (query results)
    ↓
[Database] (source of truth)
```

## Cache Types by Location

| Location | Examples | Scope |
|----------|----------|-------|
| Client | Browser cache | Per-user |
| CDN | CloudFront, Fastly | Global |
| Application | Memcached, Redis | Shared |
| Database | Query cache | Per-DB |

## Challenges

- **Consistency** — Cache may drift from source of truth
- **Cold starts** — Cache misses after restart
- **Hot spots** — Popular items may overwhelm single cache server
- **Invalidation** — Knowing when to evict stale data

## Four Cache Update Strategies

| Strategy | Write Path | Read Path | Consistency | Use Case |
|----------|-----------|-----------|-------------|----------|
| [[Cache-Aside]] (lazy loading) | App writes to DB | Cache miss → load from DB → populate cache | Eventual | Read-heavy, Memcached pattern |
| [[Write-Through Cache\|Write-Through]] | Write cache + DB synchronously | Cache hit | Strong | Consistency-critical |
| [[Write-Behind Cache\|Write-Behind]] | Write cache only, async flush to DB | Cache hit | Weak (async) | Write-heavy, non-critical data |
| [[Refresh-Ahead Cache\|Refresh-Ahead]] | Configurable | Cache auto-refreshes before TTL expiry | Strong (if prediction accurate) | Predictable access patterns |

### Cache-Aside (Lazy Loading)

Most common pattern. App checks cache; on miss, loads from DB, populates cache, returns. Used by [[Memcached]]. Simple but has 3-trip penalty on misses and risk of stale data.

### Write-Through

Cache is main data store; synchronously writes to DB. Never stale, but write latency is higher.

### Write-Behind (Write-Back)

App updates cache; DB write happens asynchronously in background. Fast writes; risk of data loss on cache failure.

### Refresh-Ahead

Cache proactively refreshes hot entries nearing TTL expiration. Low latency if predictions are accurate; wastes resources if not.

## AWS 5-Layer Caching Stack

| Layer | Use Case | AWS Solution |
|-------|----------|-------------|
| Client-Side | Accelerate web content from browser | HTTP Cache Headers |
| DNS | Domain to IP resolution | [[Amazon Route 53]] |
| Web | Static asset delivery, session management | [[Amazon CloudFront]], [[Amazon ElastiCache\|ElastiCache]] |
| App | Application performance, data access | [[Amazon ElastiCache\|ElastiCache]] (Redis, Memcached) |
| Database | Reduce DB query latency | [[Amazon ElastiCache\|ElastiCache]] (Redis, Memcached) |

## AWS Distributed Caching Pattern

A dedicated caching layer with independent lifecycle allows app nodes to scale in/out without affecting the cache. Centralized caches benefit all consumers (vs local caches scoped to a single node). [[Amazon ElastiCache]] implements this pattern with managed Redis and Memcached.

## Benefits (per AWS)

1. **Improve Application Performance** — sub-millisecond reads from RAM
2. **Reduce Database Cost** — single cache replaces multiple DB instances
3. **Predictable Performance** — mitigates usage spikes (Super Bowl, Black Friday)
4. **Eliminate Hotspots** — cache popular keys (celebrity profiles, trending products)
5. **Increase Read Throughput** — hundreds of thousands of IOPS per instance

## Related Concepts

[[Application Caching]], [[Database Caching]], [[In-Memory Cache]], [[CDN]], [[Cache Invalidation]], [[Read-Through Cache]], [[Write-Through Cache]], [[Write-Behind Cache]], [[Cache-Aside]], [[Refresh-Ahead Cache]], [[LRU]], [[Web Caching]], [[Session Management]], [[Amazon ElastiCache]], [[Amazon CloudFront]], [[Amazon Route 53]]