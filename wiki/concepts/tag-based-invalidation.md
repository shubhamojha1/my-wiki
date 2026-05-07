---
title: "Tag-Based Invalidation"
type: concept
tags: [caching, invalidation, pattern]
created: 2026-05-08
sources: ["https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf"]
---

# Tag-Based Invalidation

**Definition:** A cache invalidation technique where entries are assigned descriptive tags, allowing related entries to be invalidated as a group when underlying data changes.

## How It Works

When storing a cache entry, attach one or more tags representing logical groupings:

```
cache.set("product:123", product_data, tags=["category:electronics", "brand:apple", "region:us"])
```

When data changes, invalidate by tag rather than by individual key:

```
cache.invalidate_by_tag("category:electronics")
```

This removes all cached entries tagged with `category:electronics` — products, category pages, search results, etc.

## Advantages

- **Bulk invalidation** — one operation clears all related entries
- **Consistency** — reduces risk of stale cross-referencing data
- **Decoupled** — writers don't need to know every cached query that depends on the data
- **Granularity control** — fine-grained tags (brand:apple) or coarse (category:electronics)

## Challenges

- **Tag explosion** — too many unique tags defeats the purpose
- **Tag management** — must be consistent across all cache writes
- **Storage overhead** — tags must be indexed for efficient lookup
- **Platform support** — requires cache software with tag capability (Redis with RediSearch, custom implementation)

## Use Cases

- **E-commerce** — invalidate all product pages when a category changes
- **CMS** — invalidate all pages referencing an updated article
- **Multi-tenant systems** — invalidate all entries for a specific tenant

## Related Pages

- [[Cache Invalidation]], [[Version-Based Invalidation]], [[Caching]]
