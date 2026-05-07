---
title: "System Design Concept: Cache Invalidation Strategies"
type: source
tags: [caching, invalidation, system-design]
created: 2026-05-08
sources: ["https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf"]
---

# System Design Concept: Cache Invalidation Strategies

**Source:** Medium article by CoVaib DeepLearn (Sep 2025)
**Series:** Day 48 of a system design series

Comprehensive guide covering cache invalidation from fundamentals to advanced patterns.

## Core Invalidation Methods

- **Purge** — immediately remove cached content for a specific object/URL. Next request fetches from origin.
- **Ban** — invalidate based on criteria (URL patterns, headers). Any matching content is removed immediately.

## Invalidation Strategies

- **TTL (Time-based)** — automatic expiry after a duration. Simplest, most widely used.
- **Event-driven** — trigger invalidation on data-change events via pub/sub or message queues
- **Write-through** — write to cache + DB synchronously
- **Write-around** — write directly to DB, bypass cache
- **Write-behind** — write to cache, async flush to DB
- **Lazy loading (cache-aside)** — check cache first, on miss load from DB

## Eviction Policies

LRU, LFU, FIFO, Random Replacement

## Advanced Invalidation Patterns

- **Tag-based** — group entries under tags for bulk invalidation
- **Dependency-based** — track data dependencies; invalidate all dependent entries when source changes
- **Version-based** — use monotonically increasing version counters

## Cache Warming

Pre-populating cache before expected load:
- Scheduled warming (cron-based)
- Event-driven warming (triggered by data changes)
- JIT (Just-in-Time) warming (on first access, proactively fetch related data)

## Cache Stampede (Thundering Herd)

Many concurrent requests miss cache simultaneously and overload the database. Mitigations: locking/mutex, early recomputation, probabilistic expiration.

## Multi-Layer Invalidation

Strategies for CDN, database, and microservices cache layers — with performance monitoring and metrics (hit rate, eviction rate).

## Related Pages

- [[Cache Invalidation]], [[Write-Through Cache]], [[Write-Behind Cache]], [[Write-Around Cache]], [[Cache-Aside]], [[Cache Stampede]], [[Cache Warming]], [[Tag-Based Invalidation]], [[Version-Based Invalidation]], [[Cache Eviction Policy]]
