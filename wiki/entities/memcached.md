---
title: "Memcached"
type: entity
tags: [tool, infrastructure, cache]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Memcached

**Type:** In-memory key-value cache  
**Website:** [memcached.org](http://memcached.org/)

## Overview

Memcached is a distributed, high-performance, in-memory caching system used to accelerate dynamic web applications by reducing database load. It stores data in RAM using a simple key-value format.

## Key Characteristics

- **Pure in-memory** — all data stored in RAM
- **Distributed** — clients hash keys to distribute across servers
- **LRU eviction** — Least Recently Used policy when memory fills
- **Simple protocol** — ASCII-based protocol for easy integration

## Read-Through Cache Pattern

```python
key = "user.%s" % user_id
user_blob = memcache.get(key)
if user_blob is None:
    user = mysql.query("SELECT * FROM users WHERE user_id=...", user_id)
    if user:
        memcache.set(key, json.dumps(user))
    return user
else:
    return json.loads(user_blob)
```

## Why RAM is Faster

Memory access is orders of magnitude faster than disk access. A typical Memcached setup can handle hundreds of thousands of requests per second per server, compared to hundreds for database queries.

## Limitations

- **No persistence** — data lost on restart
- **Fixed memory** — requires sizing planning
- **Simple data** — key-value only, no complex data structures
- **No replication** — single-server reliability concerns

## Comparison with Redis

| Feature | Memcached | Redis |
|---------|-----------|-------|
| Data types | Key-value | Multiple (strings, lists, sets, sorted sets) |
| Persistence | No | Optional (RDB/AOF) |
| Eviction policies | LRU | Multiple (LRU, LFU, TTL, etc.) |
| Performance | Very high | High |
| Memory efficiency | Higher for simple data | Slightly lower |

## Related Concepts

[[In-Memory Cache]], [[Caching]], [[LRU]], [[Cache Invalidation]], [[Application Caching]], [[Read-Through Cache]]