---
title: "Browser Caching"
type: concept
tags: [http, caching, browser, web-performance]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/http-caching-in-depth-part-1-a853c6af99db/", "https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
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

## Cache-Control Implications

Browser caches interpret [[Cache-Control]] directives:
- `max-age=3600` — resource is fresh for 1 hour; browser serves from disk without network
- `no-cache` — browser must always revalidate (shows spinner while waiting)
- `no-store` — browser must not store at all (always downloads)
- `private` — safe for user-specific content (default behavior)
- `public` — OK for shared assets; no difference from private for browser alone

### The Freshness Trap

Setting `max-age=86400` on an HTML file means the browser will not request it for 24 hours — even if the server has new content. There is no server-initiated way to invalidate this. This is why HTML should use `no-cache` and versioned URLs should be used for all other assets.

### The Vary Header in Browsers

Unlike public caches, each browser cache stores representations matching only its own user's preferences. The [[Vary Header]] has minimal impact on browser caches because there is naturally only one representation per URI per user in the private cache.

## Best Practices

- Always set explicit Cache-Control headers — never rely on browser heuristics
- Use versioned URLs (fingerprinting) for long-lived assets (`Cache-Control: public, max-age=31536000, immutable`)
- Cache HTML with `no-cache` (store but always revalidate)
- Use [[ETag]] for efficient revalidation of dynamic content
- Never assume you can invalidate browser caches remotely — freshness is time-bound
- Understand that `max-age` means the browser will not contact the server for that duration regardless of content changes

## Related Pages

- [[HTTP Caching]], [[Proxy Cache]], [[CDN]], [[Web Caching]], [[Caching]], [[Cache-Control]], [[Conditional Request]], [[ETag]], [[HTTP]], [[Cache Invalidation]], [[TLS]]
