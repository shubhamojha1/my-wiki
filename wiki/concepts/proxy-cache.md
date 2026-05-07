---
title: "Proxy Cache"
type: concept
tags: [http, caching, proxy, varnish, nginx, squid]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/"]
---

# Proxy Cache

**Definition:** A dedicated HTTP caching reverse proxy server (Varnish, Squid, Apache Traffic Server, Nginx) deployed between clients and origin servers to cache and serve responses.

Also referred to as a **private proxy cache** — distinct from shared CDN infrastructure.

## Overview

Proxy caches are the same software that powers most commercial CDNs. They sit in front of origin servers and cache HTTP responses, reducing load and latency. Unlike CDNs, they are deployed and managed by the application owner in their own infrastructure.

## Key Software

| Software | Language | Key Feature |
|----------|----------|-------------|
| [[Varnish Cache|Varnish]] | C | Purpose-built HTTP cache, VCL configuration language |
| Squid | C | Full-featured proxy with caching, supports HTTP/HTTPS |
| Apache Traffic Server | C++ | High-performance, used by large CDNs |
| [[Nginx]] | C | Web server with built-in caching (proxy_cache) |

## Advantages

### Free and Open Source
No licensing costs. All major proxy cache software is open source with permissive or GPL-style licenses.

### Mature and Battle-Tested
- Varnish, Squid, and Traffic Server have been developed over decades
- Backed by large companies (Yahoo! for Traffic Server, commercial Varnish Software)
- The software *is* the system for these products — not a side library — dramatically reducing abandonment risk

### Transferable Skills
Configuration knowledge transfers directly to CDN infrastructure, since most CDNs use the same underlying software. Learning VCL (Varnish Configuration Language) is applicable to many CDN platforms.

### Performance Local to Origin
Sitting adjacent to origin servers (often same datacenter), proxy caches can serve traffic with near-zero additional latency on cache hits, while still offloading the application servers.

## Should Be the First Solution

Before investing in CDN infrastructure, a private proxy cache should be the first caching layer considered:
- Cheaper (free software, runs on existing servers)
- Full control over configuration
- Same performance characteristics as CDN for users in the same region
- Complements CDN (CDN sits in front of proxy cache)

## How It Works

```
[Client] ←→ [CDN or Internet] ←→ [Proxy Cache] ←→ [Origin Server]
                                       ↓
                              (Cache hit: serves from RAM/disk
                               Cache miss: forwards to origin,
                               caches response, returns)
```

## Configuration Outside Codebase

One key advantage: caching policy lives in the proxy configuration (VCL, Nginx config), not in application code. This means:
- Non-developers can tune caching behavior
- Performance layer is factored out from application logic
- Changes don't require deployments

## Important Caveats

- Chaining multiple proxies can have subtle effects (e.g., Age header accumulation)
- Cache invalidation is not as instant as CDN claims — may require manual purging or restart
- Requires operational expertise to tune and maintain
- Adds a hop in the request path (though negligible for cache hits in the same datacenter)

## Related Pages

- [[HTTP Caching]], [[Browser Caching]], [[CDN]], [[Web Caching]], [[Caching]], [[Reverse Proxy]], [[Nginx]], [[Varnish Cache]]
