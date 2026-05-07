---
title: "Conditional Request"
type: concept
tags: [http, caching, validation, etag]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
---

# Conditional Request

**Definition:** An HTTP request that includes validation headers (ETag or Last-Modified) so the server can respond with 304 Not Modified if the resource hasn't changed, avoiding retransmission of the full response body.

## The Problem

Caches need to know if a stored (stale) response is still valid. Rather than re-downloading the entire resource, a conditional request allows the server to say "you already have the latest version" with a lightweight response (304, empty body).

## Validation Headers

### ETag (Entity Tag)
```
If-None-Match: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```
An opaque identifier representing a specific version of the resource. Strong ETags (with quotes) change when any byte changes. Weak ETags (`W/"33a64df551425fcc55e4d42a148795d9f25f89d4"`) tolerate semantically equivalent changes.

### Last-Modified
```
If-Modified-Since: Wed, 21 Oct 2015 07:28:00 GMT
```
A timestamp of when the resource was last modified. Less precise than ETags (1-second resolution, may miss changes within the same second).

## The Two Outcomes

### 304 Not Modified (Successful Validation)

```
HTTP/1.1 304 Not Modified
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Cache-Control: max-age=3600
```
- Body is empty (saves bandwidth)
- Cache updates its headers (new max-age, potentially new ETag)
- Cache serves its local stored copy to the client
- Latency is not eliminated (round-trip still happens) but bandwidth is saved

### 200 OK (Failed Validation)

```
HTTP/1.1 200 OK
ETag: "3f64df551425fcc55e4d42a148795d9f25f89e8a"
Cache-Control: max-age=3600
Content-Length: 45234
```
- Resource has changed
- Full response body sent
- Cache stores the new version
- Effectively identical to an empty-cache miss

## Flow Diagram

```
[Client] → [Cache has stale resource]
    ↓
[Cache sends GET with If-None-Match: "old-etag"]
    ↓
[Origin Server]
    ├── Same ETag → 304 Not Modified (empty body)
    │   └── Cache updates headers, serves local copy
    └── New ETag → 200 OK (full body)
        └── Cache stores new version, serves to client
```

## Freshness vs Validation

**Critical distinction from the article:**
- **Freshness control** happens in the cache; based solely on time (max-age)
- **Validation** happens at the origin server; based on ETags/Last-Modified

A resource can be fresh (within TTL) but outdated in content — the cache will not revalidate until the timer expires.

## Performance Characteristics

| Outcome | Latency | Bandwidth | Server Load |
|---------|---------|-----------|-------------|
| Cache hit (fresh) | None (zero) | None | None |
| 304 (validated) | Round-trip latency | Headers only (~200 bytes) | Minimal (no body generation) |
| 200 (changed) | Round-trip latency | Full response | Full request processing |
| Cache miss (empty) | Round-trip latency | Full response | Full request processing |

## Related Pages

- [[ETag]], [[Cache-Control]], [[HTTP Caching]], [[Vary Header]], [[Browser Caching]], [[Proxy Cache]]
