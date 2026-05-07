---
title: "An in-depth introduction to HTTP Caching: exploring the landscape"
type: source
tags: [http, caching, browser, cdn, proxy, performance, latency]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/"]
---

# An in-depth introduction to HTTP Caching: exploring the landscape

**Source:** freeCodeCamp article by Léo Jacquemin (Dec 2018)  
**Series:** Part 1 of a multi-part series on HTTP caching

This article covers the **where** and **why** of HTTP caching — the landscape of caching actors and the fundamental performance motivation.

## The Three HTTP Caching Actors

### Browsers
All browsers implement an HTTP cache that stores web resources on the user's filesystem. On a cache hit, the resource is delivered instantly — no network request, no round-trips, no database access. However:
- **No invalidation mechanism** — developers cannot push cache invalidation to clients in a client/server architecture
- **Questionable heuristics** — browsers guess caching behavior when no explicit Cache-Control headers are present
- **User-controlled** — users can flush or disable the cache at will
- **Multi-layer complexity** — browsers implement multiple cache layers whose interactions can be unpredictable
- **HTML files are dangerous to cache** — typically cached for minutes at most
- Web servers auto-generate ETag and Last-Modified headers from file metadata, but this doesn't work for dynamically generated API responses

### CDNs (Content Delivery Networks)
Globally distributed networks of HTTP proxy servers. Akamai alone has ~240,000 servers. Key properties:
- **All speak HTTP** — they are standard HTTP proxy servers, not proprietary protocols
- **Programmatic instant purging** — can invalidate cache entries on demand (solves one of the "two hard problems" of caching)
- **Configuration outside codebase** — non-developers can tune caching policy via web interfaces
- **Performance factored out** — entire performance layer can live at infrastructure level
- **Paid solutions** — caching millions of resources costs thousands of dollars
- Caveat: some differences between marketed capabilities and production reality

### Private Proxy Caches
Same software CDNs are built on: Varnish, Squid, Apache Traffic Server, Nginx. Key properties:
- **Free and open source**
- **Highly mature** — backed by decades of development and large-company usage
- **Transferable skills** — directly applicable to CDN configuration
- **Should be first solution** — simpler, cheaper, and still provides massive performance gains
- The software *is* the system for CDNs, reducing abandonment risk

## The Caching Abstraction

All caches speak HTTP and comply to the same specification (RFC 7234). Any chain of proxy caches is equivalent to a single caching proxy — simplifying reasoning about caching behavior. However, chaining proxies can have subtle consequences (e.g., Age header interactions).

## Why Latency is the Bottleneck

### The Anatomy of a Web Request
Each HTTP request requires:
1. **DNS resolution** — ~1 round trip (50-250ms), cached at various levels
2. **TCP handshake** — 1 RT (SYN, SYN-ACK)
3. **SSL/TLS handshake** — 2 RT (TLS 1.3: ~10 messages in minimum 2 TCP exchanges)
4. **Data download** — constrained by TCP slow-start and congestion control

### TCP Slow-Start
- Initial congestion window: historically 1 segment, now 10 (RFC 6928)
- MSS (Maximum Segment Size): 1460 bytes
- A 20kB resource = ~14 segments = 4 round trips
- Each round trip doubles the window until congestion detected

### The Arithmetic of a Slow Web
A modern web application:
- ~75 requests averaging ~20kB each
- ~1.5 MB total transfer
- Per request: ~8 round trips (DNS + TCP + TLS + data)
- Total: ~600 round trips
- At 50ms RTT (Europe ↔ US): **~30 seconds of latency**
- Amazon homepage: 6.3 MB, 339 requests → ~2 min 15 sec if sequential

### Why Bandwidth is Not the Problem
- Bandwidth stops being the bottleneck above ~5 Mb/s
- 3G maxes at 2 Mb/s (bandwidth is the bottleneck on 3G)
- 4G/5G: latency is the bottleneck (packet drops from interference increase latency)
- HTTP/2 (SPDY) was designed based on this observation
- Light in fiber travels at ~60% of theoretical max; even 99% wouldn't fix multi-second loads

### Mitigations (Existing)
- DNS caching at multiple levels
- TLS session resumption (reuse handshake results)
- Persistent TCP connections (HTTP keep-alive, RFC 2616)
- Increased initial congestion window (1 → 4 → 10)
- Browser parallel connections (typically 6 per origin)
- Browser predictive pre-fetching
- CDN TCP optimization (patented algorithms for congestion avoidance)
- HTTP/2 multiplexing

### The Only Real Solution
**Reduce the distance** between content and users — via browser caches and CDN edge servers. HTTP caching is the most effective way to accomplish this.

## Related Pages

- [[HTTP Caching]], [[Browser Caching]], [[Proxy Cache]], [[CDN]], [[Web Caching]], [[Caching]], [[DNS Caching]], [[HTTP]], [[HTTPS]], [[TLS]], [[TCP]]
