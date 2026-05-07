---
title: "Cache Invalidation"
type: concept
tags: [caching, consistency, architecture]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/", "https://martinfowler.com/bliki/TwoHardThings.html", "https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf"]
---

# Cache Invalidation

> *"There are only two hard things in Computer Science: cache invalidation and naming things."* — Phil Karlton (~1996), popularized by [[Martin Fowler]]

**Definition:** The process of removing or updating cached data when the source of truth changes, maintaining consistency between cache and database.

## The Problem

Cached data can drift from reality. Without invalidation:
- Users see stale data
- Application behavior becomes bizarre
- Data integrity suffers

## Invalidation Strategies

### 1. Write-Through Cache
Update cache when writing to database:
```python
def update_user(user_id, data):
    # Write to database
    db.update("UPDATE users SET ... WHERE user_id=%s", user_id, data)
    # Immediately update cache
    cache.set("user.%s" % user_id, json.dumps(data))
```

### 2. Delete and Repopulate (Read-Through)
Delete from cache, let next read repopulate:
```python
def update_user(user_id, data):
    # Write to database
    db.update("UPDATE users SET ... WHERE user_id=%s", user_id, data)
    # Delete from cache (next read will repopulate)
    cache.delete("user.%s" % user_id)
```

### Strategy Comparison

| Strategy | Pros | Cons |
|----------|------|------|
| Write-through | No stampede risk, always consistent | Extra write latency, more cache writes |
| Delete + repopulate | Simpler logic, fewer cache writes | Cache miss on next read, potential stampede |

## Stampede Risk

When cache is deleted, multiple concurrent requests might all:
1. Find cache empty
2. All query database simultaneously
3. Overwhelm the database

**Mitigation**: Write-through caches reduce this risk.

## Core Invalidation Methods

### Purge
Immediately removes cached content for a specific object or URL. The next request fetches fresh data from the origin. Simple and precise — best for known individual keys.

### Ban
Invalidates based on criteria such as URL patterns or headers. Any cached content matching the pattern is removed. Useful for bulk invalidation when you don't know every affected key:
```
BAN /products/* HTTP/1.1
Host: example.com
```

## Invalidation Strategies

### TTL (Time-Based)
Simplest and most widely used. Each cache entry has a [[Cache-Control|max-age]] or TTL after which it automatically expires. No explicit invalidation logic needed. Tradeoff: data may be stale within the TTL window.

### Event-Driven Invalidation
Trigger cache updates in response to specific system events using pub/sub or message queues:

```python
# Publisher (on data update)
publish("user.updated", {"user_id": 123})

# Subscriber (cache listener)
subscribe("user.updated", lambda event: cache.delete(f"user:{event['user_id']}"))
```

Provides near real-time consistency. Requires additional infrastructure (message broker).

### Write-Through
Write to cache and database synchronously. See [[Write-Through Cache]].

### Write-Around
Write directly to database, bypassing cache. See [[Write-Around Cache]].

### Write-Behind
Write to cache, asynchronously flush to database. See [[Write-Behind Cache]].

### Lazy Loading (Cache-Aside)
Check cache first; on miss, load from database and populate cache. See [[Cache-Aside]].

## Advanced Invalidation Patterns

### Tag-Based Invalidation
Group related cache entries under descriptive tags for bulk invalidation (e.g., "category:electronics"). When data changes, invalidate all entries matching the tag. See [[Tag-Based Invalidation]].

### Dependency-Based Invalidation
Track data dependencies explicitly. If resource A depends on resource B, any change to B triggers invalidation of all cache entries derived from B. Requires a dependency graph.

### Version-Based Invalidation
Use monotonically increasing version counters per resource. Cache entries include the version; on read, compare against the current version. No explicit purge needed. See [[Version-Based Invalidation]].

## Cache Stampede

When a popular cache entry expires, multiple concurrent requests may all miss and query the database simultaneously — overwhelming it. See [[Cache Stampede]] for mitigations (locking, probabilistic early expiration, stale-while-revalidate).

## Multi-Datacenter Challenges

Invalidation becomes complex with:
- Multiple data centers
- Replication lag
- Multiple code paths writing to database

Single datacenter: straightforward
Multiple datacenters: significant engineering effort required — often solved with global invalidation buses or version-based approaches.

## Related Concepts

[[Caching]], [[Write-Through Cache]], [[Write-Around Cache]], [[Write-Behind Cache]], [[Read-Through Cache]], [[Cache-Aside]], [[Tag-Based Invalidation]], [[Version-Based Invalidation]], [[Cache Stampede]], [[Cache Warming]], [[Eventual Consistency]], [[Martin Fowler]]