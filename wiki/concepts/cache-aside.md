---
title: "Cache-Aside"
type: concept
tags: [caching, pattern, lazy-loading]
created: 2026-05-08
sources: ["https://github.com/donnemartin/system-design-primer#cache"]
---

# Cache-Aside (Lazy Loading)

**Definition:** A caching pattern where the application is responsible for reading and writing from both cache and database — the cache does not directly interact with storage.

Also known as **lazy loading** because data is only loaded into cache when actually requested.

## Flow

```
1. [App requests key]
       ↓
2. [Cache lookup]
       ↓ (miss)
3. [Read from database]
       ↓
4. [Store in cache]
       ↓
5. [Return to app]
```

Subsequent reads for the same key hit the cache directly.

## Example

```python
def get_user(user_id):
    user = cache.get("user.{0}", user_id)
    if user is None:
        user = db.query("SELECT * FROM users WHERE user_id = {0}", user_id)
        if user is not None:
            key = "user.{0}".format(user_id)
            cache.set(key, json.dumps(user))
    return user
```

Used by [[Memcached]].

## Characteristics

| Aspect | Description |
|--------|-------------|
| Cache population | On demand (lazy) |
| Write path | App writes directly to DB |
| Consistency | Eventual (data can be stale) |
| Cache fill risk | Only requested data cached |

## Advantages

- **Efficient storage** — only requested data occupies cache
- **Simple to implement** — minimal code changes
- **Resilient** — cache failure doesn't crash the app (falls back to DB)

## Disadvantages

- **Cache miss penalty** — 3 trips (cache miss → DB read → cache write → return)
- **Stale data** — cached data can become outdated if DB is updated directly
- **Cold node** — new/replacement node starts empty, increasing latency until cache warms up

## Mitigations

- Set **TTL** (time-to-live) to force periodic refresh
- Combine with **write-through** for data that's both read and written frequently

## Related Pages

- [[Caching]], [[Write-Through Cache]], [[Write-Behind Cache]], [[Refresh-Ahead Cache]], [[Read-Through Cache]], [[Application Caching]], [[Memcached]]
