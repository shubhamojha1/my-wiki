---
title: "CDN"
type: concept
tags: [infrastructure, caching, distribution]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/", "https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/"]
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

## CDN as HTTP Proxy

CDNs are fundamentally HTTP proxy servers. They speak standard HTTP (RFC 7234) — no proprietary application protocols. This means any knowledge of HTTP caching is directly applicable to CDN configuration.

### Programmatic Instant Purging
Most modern CDNs advertise the ability to programmatically purge resources from the entire network instantly. This effectively solves one of the "two hard problems" of caching (invalidation). However, experience shows some CDNs have gaps between marketed capabilities and production reality — supplemental cache-busting techniques may still be needed.

### Configuration Outside Codebase
CDNs provide web interfaces to set caching rules that can override or supplement origin Cache-Control headers. This allows:
- Non-developers to tune caching policy
- Performance configuration factored out of application code
- Quick policy changes without deployments

### Performance at Infrastructure Level
With well-configured caching headers and CDN settings, poorly optimized server code can still deliver most responses in under 300ms by serving cached, still-fresh versions. The entire performance layer can live at the infrastructure level.

## AWS CloudFront

[[Amazon CloudFront]] is AWS's global CDN service:
- Edge locations worldwide for low-latency delivery
- Caches static assets (videos, images, HTML, JS, CSS)
- Configurable for dynamic content (fetches from origin)
- Integrates with other AWS services
- No minimum usage commitments

## Benefits Summary

| Benefit | Impact |
|---------|--------|
| Reduced latency | Users download from nearby edge |
| Reduced server load | App servers handle fewer requests |
| DDoS protection | CDN absorbs attack traffic |
| Reliability | Geographic redundancy |

## Related Concepts

[[Caching]], [[Cache Invalidation]], [[Read-Through Cache]], [[Load Balancing]], [[Amazon CloudFront]], [[HTTP Caching]], [[Proxy Cache]], [[Browser Caching]]