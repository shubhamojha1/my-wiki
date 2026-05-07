---
title: "Browser Caching"
type: concept
tags: [http, caching, browser, web-performance]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/"]
---

# Browser Caching

**Definition:** The HTTP cache implementation built into every web browser that stores web resources on the user's local filesystem, enabling instant delivery on subsequent requests.

## Performance Ideal

When a resource is served from browser cache:
- No DNS resolution
- No TCP connection
- No TLS handshake
- No network round-trips at all
- Zero latency, zero server load

This is the theoretical maximum for web performance.

## Key Limitations

### No Server-Initiated Invalidation
In a client/server architecture, the server cannot push cache invalidation to clients. Developers cannot force browsers to evict stale content — they must rely on cache headers and versioned URLs.

### Questionable Heuristics (Absent Headers)
When a response lacks explicit Cache-Control headers, browsers apply default heuristics that vary by implementation:
- Some cache resources for a "reasonable" period
- Heuristics are often undocumented and unpredictable
- This leads to serving stale content without understanding why

### User Control
Users can:
- Flush the browser cache entirely
- Disable caching (e.g., dev tools "Disable cache" option)
- Use private/incognito mode (limits cache duration to session)

### Multi-Layer Cache Complexity
Browsers implement multiple cache layers beyond just HTTP caching:
- Service Worker cache (Cache Storage API)
- HTTP disk cache
- Memory cache
- Push cache (HTTP/2 server push)

These layers interact in ways that are not always predictable.

### HTML Caching Danger
HTML files are the entry point for all other resources. Caching HTML aggressively means users see stale layouts and broken references. As a result, HTML is typically cached for minutes at most, or not at all.

## Common Server Configuration

Web servers often auto-generate caching headers based on file metadata:

- **ETag** — file hash or modification timestamp
- **Last-Modified** — file modification time

This works for static files but provides no benefit for dynamic API responses (JSON, XML) where there is no file to read metadata from. The server simply forwards the request without caching.

## Browser Cache Layers

| Layer | Scope | Speed |
|-------|-------|-------|
| Service Worker | Programmatic, app-controlled | Fastest (in-process) |
| Memory Cache | In-RAM, per-tab | Very fast |
| HTTP Disk Cache | On filesystem, persistent | Fast |
| Push Cache | HTTP/2 pushed resources | Fast |

These layers interact in priority order, with the fastest checked first.

## Best Practices

- Always set explicit Cache-Control headers — never rely on browser heuristics
- Use versioned URLs (fingerprinting) for long-lived assets (max-age=1 year)
- Cache HTML with short TTL or no-cache
- Use ETag for efficient revalidation of dynamic content
- Never assume you can invalidate browser caches remotely

## Related Pages

- [[HTTP Caching]], [[Proxy Cache]], [[CDN]], [[Web Caching]], [[Caching]], [[HTTP]], [[Cache Invalidation]], [[TLS]]
