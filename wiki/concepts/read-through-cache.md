---
title: "Read-Through Cache"
type: concept
tags: [caching, pattern]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Read-Through Cache

**Definition:** Cache pattern where reads check the cache first; on cache miss, the cache fetches from the backend and populates itself before returning.

## Flow

```
1. [Request for key "user:123"]
       ↓
2. [Cache lookup] → MISS
       ↓
3. [Fetch from database]
       ↓
4. [Store in cache]
       ↓
5. [Return result]
```

## Example Implementation

```python
def get_user(user_id):
    key = "user.%s" % user_id
    
    # Step 1: Check cache
    user_blob = cache.get(key)
    if user_blob is not None:
        return json.loads(user_blob)
    
    # Step 2: Cache miss - query database
    user = db.query(
        "SELECT * FROM users WHERE user_id = %s",
        user_id
    )
    
    # Step 3: Populate cache for future requests
    if user:
        cache.set(key, json.dumps(user))
    
    return user
```

## Characteristics

| Aspect | Description |
|--------|-------------|
| Trigger | Lazy population on first access |
| Simplicity | Application code handles fallback |
| Latency | First access slower (cache miss) |
| Subsequent | All reads fast (cache hit) |

## Advantages

- **Simple application logic** — Cache handles miss transparently
- **Self-populating** — Cache fills as needed
- **Reduced cache pollution** — Only accessed data is cached

## Disadvantages

- **Cold start penalty** — First access always misses
- **Potential stampede** — Multiple concurrent misses hit database

## Related Concepts

[[Caching]], [[Write-Through Cache]], [[Cache Invalidation]], [[Application Caching]]