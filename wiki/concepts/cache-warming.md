---
title: "Cache Warming"
type: concept
tags: [caching, performance, startup]
created: 2026-05-08
sources: ["https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf"]
---

# Cache Warming

**Definition:** The practice of pre-populating a cache with frequently accessed data before it is requested by users, avoiding the performance penalty of cold-start cache misses.

## The Problem

A cold cache (empty or recently flushed) causes:
- High miss rate for early requests
- Increased latency for users who hit the cache just after startup
- Database load spikes as requests cascade through uncached data
- Potential [[Cache Stampede]] if many requests hit simultaneously

## Warming Strategies

### Scheduled Warming
Pre-load cache at fixed intervals using cron or scheduled jobs:

```python
# Daily at 2 AM
@schedule(cron="0 2 * * *")
def warm_product_cache():
    products = db.query("SELECT * FROM products WHERE active = 1")
    for product in products:
        cache.set(f"product:{product.id}", product, ttl=86400)
```

Best for: predictable access patterns, daily data refreshes.

### Event-Driven Warming
Populate cache as a side effect of data-change events:

```python
def on_product_updated(product_id):
    product = db.query("SELECT * FROM products WHERE id = ?", product_id)
    cache.set(f"product:{product_id}", product, ttl=86400)
```

Best for: data that changes infrequently but is read immediately after updates.

### Just-in-Time (JIT) Warming
On first access, proactively fetch and cache related data beyond what was requested:

```python
def get_product(product_id):
    product = cache.get(f"product:{product_id}")
    if product is None:
        product = db.query("SELECT * FROM products WHERE id = ?", product_id)
        # Warm related data too
        related = db.query("SELECT * FROM products WHERE category_id = ?", product.category_id)
        for r in related:
            cache.set(f"product:{r.id}", r, ttl=3600)
        cache.set(f"product:{product_id}", product, ttl=3600)
    return product
```

Best for: applications with strong data locality (if one product is requested, related ones likely will be too).

## Anti-Patterns

- **Warming everything** — loading the entire database into cache wastes memory on rarely accessed data
- **Stale warming data** — warming with data that's already outdated before users see it
- **Warming at the wrong time** — running warming jobs during peak traffic adds load pressure

## Best Practices

- Warm only the most frequently accessed data (based on access logs or analytics)
- Use gradual warming to avoid write spikes
- Pair warm with appropriate TTLs so data is refreshed naturally
- Monitor hit rate after warming to validate effectiveness
- Consider distributing warming across multiple workers for large datasets

## Related Pages

- [[Caching]], [[Cache Stampede]], [[Cache Invalidation]], [[Cache-Aside]], [[Read-Through Cache]]
