---
title: "Cache Invalidation"
type: concept
tags: [caching, consistency, architecture]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Cache Invalidation

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

## Complex Invalidation Scenarios

### Fuzzy Queries
Hard to invalidate caches for complex searches (e.g., "all users near Seattle"):
- Option 1: Rely on database caching
- Option 2: Aggressive TTL expiration
- Option 3: Rework query to be cache-key friendly

### Bulk Deletes
"Delete all objects created more than a week ago":
```python
# Bad: Don't do this
db.execute("DELETE FROM logs WHERE created < :cutoff")

# Better: Explicit invalidation
items = db.query("SELECT * FROM logs WHERE created < :cutoff")
for item in items:
    cache.delete("log.%s" % item.id)
db.execute("DELETE FROM logs WHERE id IN (:ids)", [item.id])
```

## Multi-Datacenter Challenges

Invalidation becomes complex with:
- Multiple data centers
- Replication lag
- Multiple code paths writing to database

Single datacenter: straightforward
Multiple datacenters: significant engineering effort required

## Related Concepts

[[Caching]], [[Write-Through Cache]], [[Read-Through Cache]], [[Eventual Consistency]]