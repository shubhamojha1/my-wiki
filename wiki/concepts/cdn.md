---
title: "CDN"
type: concept
tags: [infrastructure, caching, distribution]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# CDN (Content Distribution Network)

**Definition:** A distributed network of servers that caches and delivers static content (images, CSS, JavaScript) from edge locations closer to users.

## What CDNs Do

1. **Reduce application server load** — Static assets served from CDN, not app servers
2. **Improve geographic distribution** — Cache at edge locations near users
3. **Faster asset loading** — Lower latency for static content
4. **Handle traffic spikes** — Absorb bursts for popular assets

## How It Works

```
[User Request for image.jpg]
    ↓
[CDN Edge Server]
    ↓ (cache miss)
[Origin Server (your infrastructure)]
    ↓
[CDN caches and serves content]
```

### On Cache Hit
- CDN serves content immediately
- Sub-millisecond response times
- Zero load on origin servers

### On Cache Miss
- CDN fetches from origin
- Caches locally
- Serves to user
- Subsequent requests served from cache

## CDN as Read-Through Cache

CDNs act as read-through caches:
1. Request comes for static asset
2. CDN checks local cache
3. If found (hit): serve immediately
4. If not found (miss): fetch from origin, cache, serve

## Configuration

HTTP headers control CDN caching:
```
Cache-Control: public, max-age=31536000
```
Defines how long CDN should cache content.

## Preparing for CDN Migration

If your site isn't large enough for CDN yet, prepare by:
1. Serving static media from a separate subdomain (e.g., `static.example.com`)
2. Using lightweight HTTP server (e.g., Nginx)
3. Pointing DNS to CDN when ready

## Benefits Summary

| Benefit | Impact |
|---------|--------|
| Reduced latency | Users download from nearby edge |
| Reduced server load | App servers handle fewer requests |
| DDoS protection | CDN absorbs attack traffic |
| Reliability | Geographic redundancy |

## Related Concepts

[[Caching]], [[Cache Invalidation]], [[Read-Through Cache]], [[Load Balancing]]