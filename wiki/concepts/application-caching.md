---
title: "Application Caching"
type: concept
tags: [caching, application-layer]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Application Caching

**Definition:** Caching implemented explicitly in application code, where the application manages cache reads, writes, and invalidation.

## Pattern

Application code explicitly integrates with cache:

```
Check cache
    ↓ (miss)
Query database
    ↓
Store in cache
    ↓
Return result
```

## Read-Through Cache Example

```python
def get_user(user_id):
    key = "user.%s" % user_id
    
    # Check cache first
    user_blob = memcache.get(key)
    if user_blob is None:
        # Cache miss: get from database
        user = mysql.query(
            "SELECT * FROM users WHERE user_id=%s", 
            user_id
        )
        if user:
            # Store in cache for next time
            memcache.set(key, json.dumps(user))
        return user
    else:
        # Cache hit: deserialize cached data
        return json.loads(user_blob)
```

## Characteristics

| Aspect | Description |
|--------|-------------|
| Control | Full control over caching logic |
| Integration | Requires explicit code changes |
| Flexibility | Can implement complex invalidation |
| Maintenance | Must be kept in sync with database |

## When to Use

- Complex access patterns not handled by database cache
- Need fine-grained control over what gets cached
- Custom invalidation logic required
- Non-standard data structures

## Advantages

- **Precise control** — Cache exactly what you need
- **Custom logic** — Implement business-specific caching rules
- **Optimization** — Can cache preprocessed results

## Disadvantages

- **Code complexity** — Requires integration in every access path
- **Risk of inconsistency** — Must manually maintain cache coherence
- **Maintenance burden** — Easy to introduce bugs

## Related Concepts

[[Caching]], [[Read-Through Cache]], [[Cache Invalidation]], [[In-Memory Cache]], [[Memcached]]