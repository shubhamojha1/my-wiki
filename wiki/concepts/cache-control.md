---
title: "Cache-Control"
type: concept
tags: [http, caching, headers, web-performance]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
---

# Cache-Control

**Definition:** The primary HTTP/1.1 response header origin servers use to communicate caching instructions to browsers, proxies, and CDNs.

Replaces the deprecated `Pragma` header (which was never a true standard).

## Freshness Directives

### max-age
`Cache-Control: max-age=3600`

Specifies the lifetime of a representation in seconds. During this period the resource is considered **fresh** and cache hits occur. After expiry the resource becomes **stale** and validation takes over.

Maximum value: 31536000 seconds (1 year).

### s-maxage
`Cache-Control: s-maxage=3600`

Like max-age but applies only to **shared/public caches** (proxies, CDNs). Ignored by private (browser) caches. If both are present, s-maxage takes precedence for shared caches.

**Best practice:** s-maxage should always be less than max-age. The reasoning: caches closer to the origin should check freshness more frequently. If a proxy caches for 1 day, browsers might as well cache for 1 day too — if not longer.

## Storage Directives

### no-store
`Cache-Control: no-store`

The most restrictive directive. A compliant cache:
- Must not store the response anywhere (memory or disk)
- Must delete any existing copy it might hold

Use for: sensitive data (bank balances, medical records), dynamic real-time data.

### no-cache
`Cache-Control: no-cache`

**Counter-intuitive name.** This directive does not forbid caching — it forbids cache hits. A cache may store the response but must always revalidate with the origin server before serving it.

Use for: HTML entry points, content that changes frequently but benefits from validation bandwidth savings.

### must-revalidate
`Cache-Control: must-revalidate, max-age=3600`

Forbids serving stale content. Fresh resources (within max-age) may be served without revalidation. Once stale, the cache must revalidate — it cannot serve a stale copy under any circumstances.

## Access Control Directives

### public
`Cache-Control: public, max-age=86400`

The resource may be cached by any cache: browser, intermediate proxy, CDN. Use for static assets (images, CSS, JS) with versioned URLs.

### private
`Cache-Control: private, max-age=3600`

The resource may only be cached by the browser cache (private to a single user). Shared/proxy caches must not store it. This is the **default** behavior if no directive is specified.

**Why private matters:**
- `/users/me` returns different content for each user based on Authorization header
- Public caches don't inspect headers by default — only URIs
- Without `private`, one user's profile could be served to another

## Extension Directives (RFC 5861)

### stale-while-revalidate
`Cache-Control: max-age=3600, stale-while-revalidate=60`

Allows the cache to immediately return a stale response while revalidating in the background. The client doesn't wait for the revalidation. Particularly useful for images and media where outdated content for a few seconds is better than a loading delay.

### stale-if-error
`Cache-Control: max-age=3600, stale-if-error=86400`

Allows the cache to serve a stale response if the origin server returns a 5xx error. Provides a grace period during which clients are shielded from error pages. Use for third-party content (weather widgets, ads) where a stale result is better than a broken page.

## Classification Table

| Directive | Stores? | Cache Hits? | Serves Stale? | Primary Use |
|-----------|---------|-------------|---------------|-------------|
| `max-age` | Yes | Yes (while fresh) | No (unless extension) | Standard caching |
| `no-store` | No | N/A | N/A | Sensitive data |
| `no-cache` | Yes | No (always revalidate) | No | HTML, dynamic content |
| `must-revalidate` | Yes | Yes (while fresh) | No (forbidden) | Staleness-sensitive |
| `public` | Any cache | Yes | Depends on freshness | Static assets |
| `private` | Browser only | Yes | Depends on freshness | User-specific data |
| `s-maxage` | Shared only | Yes (while fresh) | No | CDN/proxy override |

## Common Combinations

```http
# Static asset with fingerprint (cache forever)
Cache-Control: public, max-age=31536000, immutable

# HTML page (always fresh from server)
Cache-Control: no-cache

# API response with short freshness
Cache-Control: private, max-age=60

# Conservative (belt-and-suspenders)
Cache-Control: no-cache, no-store, max-age=0, must-revalidate
```

The conservative combination shown above was historically common but is generally unnecessary today. Modern browsers correctly implement the spec — use only the directives you need.

## Related Pages

- [[HTTP Caching]], [[Vary Header]], [[Conditional Request]], [[ETag]], [[Browser Caching]], [[Proxy Cache]], [[CDN]], [[Web Caching]]
