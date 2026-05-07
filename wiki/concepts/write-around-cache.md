---
title: "Write-Around Cache"
type: concept
tags: [caching, pattern, write-strategy]
created: 2026-05-08
sources: ["https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf"]
---

# Write-Around Cache

**Definition:** A caching strategy where write operations go directly to the database, bypassing the cache entirely. Only data that is subsequently read gets cached.

## Flow

```
[Write request]
    ↓
[Database (write directly)]
    ↓
[Return success]
    │
[Subsequent read]
    ↓
[Cache miss → load from DB → populate cache → return]
```

## Characteristics

| Aspect | Description |
|--------|-------------|
| Write path | Direct to database (cache bypassed) |
| Read path | Cache-aside: check cache, on miss load from DB |
| Cache churn | Low (only cached data that's read) |
| Consistency | Strong (cache never lags on writes) |

## Advantages

- **No cache pollution** — write-heavy workloads don't fill cache with data nobody reads
- **Lower write latency** — no cache write overhead
- **Reduced cache memory pressure** — fewer entries in cache
- **Simpler write path** — no cache update logic on writes

## Disadvantages

- **Higher read latency for recently written data** — first read after a write always misses
- **Cold start for new data** — every newly written item must be loaded into cache on first read
- **Not suitable for read-heavy workloads** — if the same data is read frequently after writing, write-through is better

## When to Use

- Write-heavy workloads where most written data is never read (logs, audit trails)
- Append-only datasets where historical data is rarely queried
- Temporary/batch data that is written once and consumed immediately

## Comparison

| Strategy | Write Path | Read Path | Cache Churn |
|----------|-----------|-----------|-------------|
| [[Write-Through Cache\|Write-Through]] | Cache + DB | Cache hit | High (all writes cached) |
| [[Write-Around Cache\|Write-Around]] | DB only | Cache miss → load from DB | Low (reads cached) |
| [[Write-Behind Cache\|Write-Behind]] | Cache (async DB) | Cache hit | High |

## Related Pages

- [[Caching]], [[Write-Through Cache]], [[Write-Behind Cache]], [[Cache-Aside]], [[Cache Invalidation]]
