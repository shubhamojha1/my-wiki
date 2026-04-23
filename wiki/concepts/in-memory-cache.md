---
title: "In-Memory Cache"
type: concept
tags: [caching, memory, performance]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# In-Memory Cache

**Definition:** Cache system that stores all data in RAM, providing orders-of-magnitude faster access than disk-based storage.

## Why RAM is Faster

Memory access is orders of magnitude faster than disk access:
- RAM: ~100 nanoseconds access time
- SSD: ~100 microseconds access time
- HDD: ~10 milliseconds access time

This is a **~100x to 100,000x** difference depending on storage type.

## Examples

- **Memcached** — Pure in-memory, key-value store
- **Redis** — In-memory with optional persistence

## LRU (Least Recently Used)

Most in-memory caches use LRU eviction:
- When memory fills, least recently accessed items are evicted
- Keeps "hot" (frequently accessed) data in cache
- Appropriate for almost all caching scenarios

## Tradeoff: RAM vs Disk

| Aspect | In-Memory | Disk |
|--------|-----------|------|
| Speed | Extremely fast | Slow |
| Capacity | Limited by RAM | Large (TB+) |
| Persistence | None (data lost on restart) | Durable |
| Cost | Expensive per GB | Cheap per GB |

## Strategy for Limited RAM

Since RAM is limited compared to disk space, you need a strategy for keeping only the "hot" subset of data:

1. **LRU** — Evict least recently used (used by Memcached)
2. **TTL** — Expire data after time period
3. **Size limits** — Cap total cache size per item or overall
4. **Sampling** — Cache only statistically frequent items

## Use Cases

In-memory caching excels when:
- Same data accessed repeatedly
- Computation is expensive (CPU or I/O)
- Latency requirements are strict
- Working set fits in available RAM

## Related Concepts

[[Caching]], [[LRU]], [[Memcached]], [[Redis]], [[Cache Eviction Policy]]