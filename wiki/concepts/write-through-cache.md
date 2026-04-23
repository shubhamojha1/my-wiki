---
title: "Write-Through Cache"
type: concept
tags: [caching, pattern]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Write-Through Cache

**Definition:** Cache pattern where writes update both the cache and database synchronously, ensuring consistency.

## Flow

```
1. [Write request for key "user:123"]
       ↓
2. [Write to cache]
       ↓
3. [Write to database]
       ↓
4. [Return success]
```

## Example Implementation

```python
def update_user(user_id, data):
    key = "user.%s" % user_id
    
    # Step 1: Update cache first
    cache.set(key, json.dumps(data))
    
    # Step 2: Update database
    db.execute(
        "UPDATE users SET name=%s, email=%s WHERE user_id=%s",
        data['name'], data['email'], user_id
    )
    
    return data
```

## Characteristics

| Aspect | Description |
|--------|-------------|
| Consistency | Cache always matches database |
| Write latency | Slightly higher (two writes) |
| Read latency | Always fast (cache hit) |
| Stampede risk | Minimal |

## Advantages

- **Strong consistency** — Cache never goes stale
- **No stampede** — No cache invalidation = no rush to repopulate
- **Simple read path** — Reads always hit cache

## Disadvantages

- **Write overhead** — Every write touches cache
- **Write latency** — Slightly slower than single write
- **Cache pollution** — May cache data never read

## Comparison with Alternatives

| Pattern | Write Path | Read Path | Consistency |
|---------|------------|-----------|-------------|
| Write-through | Write cache + DB | Cache hit | Strong |
| Read-through | No-op | Cache miss → populate | Eventual |
| Write-behind | Write cache only | No-op | Weak (async flush) |

## When to Prefer

- Consistency is critical
- Same data written and read frequently
- Stampede risk must be minimized

## Related Concepts

[[Caching]], [[Read-Through Cache]], [[Cache Invalidation]]