---
title: "Cache Stampede"
type: concept
tags: [caching, failure-mode, concurrency]
created: 2026-05-08
sources: ["https://medium.com/@shivanimutke2501/day-48-system-design-concept-cache-invalidation-strategies-de15e32020cf", "https://engineering.fb.com/2015/12/03/ios/under-the-hood-broadcasting-live-video-to-millions/"]
---

# Cache Stampede (Thundering Herd)

**Definition:** A failure mode where a cache entry expires or is invalidated, and multiple concurrent requests all miss the cache simultaneously, causing them all to query the backend database at once — potentially overwhelming it.

Also known as a **thundering herd** problem.

## How It Happens

```
1. [Cache entry expires/deleted]
2. [Request A arrives] → cache miss → query DB (expensive)
3. [Request B arrives] → cache miss → query DB (duplicate)
4. [Request C arrives] → cache miss → query DB (duplicate)
   ... [N more requests all hitting DB simultaneously]
```

Under normal traffic spikes, a single cache miss becomes N simultaneous database queries, each a full read.

## Consequences

- Database CPU/memory spikes (potentially causing downtime)
- Increased latency for all requests during the stampede
- Cascading failures — database slowdown causes more timeouts, more retries
- Particularly dangerous after cache node failures (all keys on the lost node must be repopulated)

## Mitigation Strategies

### 1. Mutex / Locking
Only one request recomputes the value; others wait:

```python
def get_expensive(key):
    data = cache.get(key)
    if data is None:
        if cache.lock(f"lock:{key}", ttl=5):  # acquire distributed lock
            data = db.query("...")
            cache.set(key, data, ttl=3600)
            cache.unlock(f"lock:{key}")
        else:
            # Wait for the first request to populate
            time.sleep(0.05)
            data = cache.get(key)
    return data
```

### 2. Probabilistic Early Expiration
Recompute before the TTL actually expires, with randomness to avoid synchronized recomputation:

```python
def get_with_probabilistic_expiry(key, ttl=3600):
    data = cache.get(key)
    if data is None:
        data = recompute(key)
        cache.set(key, data, ttl=ttl)
    elif data["age"] > ttl * 0.8:  # 80% of TTL elapsed
        if random.random() < 0.1:  # 10% of requests recompute early
            asyncio.ensure_future(recompute_async(key))
    return data
```

Known as **XFetch** or **early recomputation**.

### 3. Stale-While-Revalidate
Serve the stale value while refreshing in background (see [[Cache-Control]]):

```python
Cache-Control: max-age=3600, stale-while-revalidate=60
```

### 4. Read-Through / Refresh-Ahead Cache
The cache itself manages refreshing without exposing the miss to clients:

```python
# Using a read-through cache library
cache.get(key, ttl=3600, refresh_ahead=True)
```

### 5. Request Coalescing (Edge Cache)
A popular pattern for live/real-time content where multiple clients request the same uncached object simultaneously. The first request is forwarded to origin; subsequent requests are **queued at the edge** until the response arrives, then all are served from cache. See [[Edge Cache]] for Facebook's production implementation.

### 6. Global Cache Lock / Bulkhead
Limit concurrent recomputations with a semaphore:

```python
semaphore = Semaphore(max_concurrent_recomputations=5)
def get_with_bulkhead(key):
    data = cache.get(key)
    if data is None:
        with semaphore:
            data = cache.get(key)  # double-check
            if data is None:
                data = recompute(key)
                cache.set(key, data)
    return data
```

## Real-World Case Study: Facebook Live

When Facebook launched Live for Mentions (2015), public figures with millions of followers could trigger sudden traffic spikes. Their solution:

1. **Multi-layer edge cache** — 3-second HLS video segments cached at edge data centers worldwide
2. **98%+ edge hit rate** — only 1.8% of segment requests reached origin
3. **Request coalescing** at both edge and origin layers — queuing concurrent requests for the same uncached segment
4. **Result:** live stream servers received only a tiny fraction of the potential thundering herd

See [[Edge Cache]].

## Detection

Key metrics to monitor for stampede risk:
- **Cache miss rate spikes** — sudden increase indicates expiring/evicted keys
- **Database query rate correlation** — spikes that align with cache misses
- **Request latency increase** — higher p50/p95 during cache misses

## Related Pages

- [[Caching]], [[Cache Invalidation]], [[Cache Warming]], [[Read-Through Cache]], [[Refresh-Ahead Cache]], [[Cache-Control]], [[Edge Cache]]
