---
title: "Web Caching"
type: concept
tags: [caching, web, performance, cdn]
created: 2026-05-08
sources: ["https://aws.amazon.com/caching/", "https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/"]
---

# Web Caching

**Definition:** Caching web artifacts (HTML, JavaScript, images, video) to reduce latency, server load, and bandwidth — applied on both client side and server side.

## Server-Side Web Caching

- Uses a **web proxy** or reverse proxy that retains web responses from servers it sits in front of
- Reduces server load and response latency
- Common implementations: CDNs, reverse proxies (Nginx, HAProxy), [[Amazon CloudFront]]

## Client-Side Web Caching

- **Browser caching** — retains cached versions of previously visited web content
- Controlled via HTTP cache headers:
  ```
  Cache-Control: public, max-age=31536000
  ```
- Reduces repeat requests for the same assets

## The Web Caching Stack

| Level | Mechanism | Example |
|-------|-----------|---------|
| Browser | Local cache on device | Chrome disk cache |
| CDN Edge | Global edge servers | [[Amazon CloudFront]] |
| Reverse Proxy | Caching proxy before app servers | Nginx, Varnish |
| Web Server | Application-level cache | Redis session store |

## Browser Caching Specifics

Browser HTTP cache stores resources on the user's filesystem. On a cache hit, there is zero network activity — no DNS, no TCP, no TLS. However:
- **No server-initiated invalidation** — developers cannot force browsers to evict content
- **Browsers apply heuristics** when Cache-Control headers are absent — often unpredictable
- **Users can disable/flush** the cache at will
- **Multiple cache layers** (Service Worker, Memory Cache, Disk Cache, Push Cache) interact in complex ways
- **HTML cached cautiously** — typically minutes at most, since it's the entry point for all other resources

See [[Browser Caching]] for the full treatment.

## Key Benefits

- Eliminates disk reads for cached assets
- Reduces server CPU/memory load
- Dramatically faster page loads for end users
- Bandwidth savings

## Related Pages

- [[Caching]], [[CDN]], [[Amazon CloudFront]], [[Reverse Proxy]], [[HTTP]], [[HTTP Caching]], [[Browser Caching]], [[Proxy Cache]]
