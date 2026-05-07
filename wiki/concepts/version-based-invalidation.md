---
title: "Version-Based Invalidation"
type: concept
tags: [caching, invalidation, pattern]
created: 2026-05-08
sources: ["https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf"]
---

# Version-Based Invalidation

**Definition:** A cache invalidation technique that uses monotonically increasing version counters or timestamps to determine whether cached data is stale, without requiring individual key-level purging.

## How It Works

Maintain a global or per-resource version counter:

```python
# On data update
current_version = cache.increment("version:product:123")
db.update("products", data, where={"id": 123})

# On cache read
cached = cache.get("product:123")
if cached and cached["version"] == cache.get("version:product:123"):
    return cached["data"]
else:
    fresh = db.query("SELECT * FROM products WHERE id = 123")
    cache.set("product:123", {"version": cache.get("version:product:123"), "data": fresh})
    return fresh
```

## Variations

### Global Version
A single counter for the entire dataset. Simplest but any change invalidates everything — poor hit rate.

### Per-Resource Version
Each resource has its own counter. Fine-grained, good hit rate, but more metadata to manage.

### Timestamp-Based
Use `updated_at` timestamps instead of counters. Works naturally with databases that track modification times. No separate counter store needed.

## Advantages

- **No explicit purge** — stale entries are detected on read and replaced
- **Natural consistency** — version check ensures cache never serves truly stale data
- **Works across distributed systems** — version counter can be a shared atomic counter (Redis INCR)
- **Fine-grained control** — per-resource versions minimize unnecessary invalidations

## Disadvantages

- **Extra lookup** — each cache read requires checking the current version (can be batched)
- **Version store overhead** — need a highly available version store (Redis, ZooKeeper)
- **Clock skew risk** — timestamp-based variants suffer from clock drift in distributed systems

## Use Cases

- **Distributed caches** where purge events are hard to propagate
- **Content-addressable caches** where the version is derived from content hash
- **Databases with `updated_at` columns** — natural fit for timestamp-based invalidation

## Comparison

| Strategy | Storage Overhead | Consistency | Cache Hit Impact |
|----------|-----------------|-------------|------------------|
| TTL | None | Eventual (time-bound) | Hit rate drops after TTL |
| [[Tag-Based Invalidation\|Tag-based]] | Tag index | Strong on invalidate | Minimal |
| Version-based | Version store | Strong on read | Minimal (if version checked efficiently) |
| Purge | None | Strong on invalidate | Miss on next read after purge |

## Related Pages

- [[Cache Invalidation]], [[Tag-Based Invalidation]], [[Caching]]
