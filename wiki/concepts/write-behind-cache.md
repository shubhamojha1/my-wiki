---
title: "Write-Behind Cache"
type: concept
tags: [caching, pattern, async]
created: 2026-05-08
sources: ["https://github.com/donnemartin/system-design-primer#cache"]
---

# Write-Behind Cache (Write-Back)

**Definition:** A caching pattern where the application writes data to the cache and the cache asynchronously writes it to the database, optimizing write performance.

## Flow

```
1. [App writes key]
       ↓
2. [Write to cache (fast)]
       ↓
3. [Return success immediately]
       ↓
4. [Background: cache flushes to DB]
```

## Characteristics

| Aspect | Description |
|--------|-------------|
| Write latency | Very low (cache-only write) |
| Read latency | Fast (cache hit) |
| Consistency | Weak (async flush to DB) |
| Durability | Risk of loss on cache failure |

## Advantages

- **Fast writes** — no waiting for DB I/O
- **Write absorption** — can batch/coalesce writes to DB
- **Reduced DB load** — fewer write operations

## Disadvantages

- **Data loss risk** — if cache fails before flush, unflushed writes are lost
- **Complexity** — harder to implement than cache-aside or write-through
- **Stale reads** — DB may lag behind cache temporarily

## When to Use

- Write-heavy workloads where throughput matters more than durability
- Non-critical data that can tolerate some loss
- High-volume logging, analytics, counters

## Related Pages

- [[Caching]], [[Cache-Aside]], [[Write-Through Cache]], [[Refresh-Ahead Cache]], [[Application Caching]]
