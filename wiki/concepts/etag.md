---
title: "ETag"
type: concept
tags: [http, caching, validation, headers]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
---

# ETag (Entity Tag)

**Definition:** An HTTP response header providing an opaque identifier representing a specific version of a resource. Used by [[Conditional Request]] headers (`If-None-Match`) to determine if a cached copy is still valid.

## Format

```
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```

Typically a hash of the resource content or a version identifier.

## Strong vs Weak ETags

### Strong ETag
```
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
```
Changes whenever any byte of the resource changes. Required for byte-range requests. Use for static assets and API responses where byte-level accuracy matters.

### Weak ETag
```
ETag: W/"33a64df551425fcc55e4d42a148795d9f25f89d4"
```
Prefixed with `W/`. Tolerates semantically equivalent changes (e.g., whitespace differences, identical data from different serializers). Cannot be used for byte-range requests.

## How Validation Works

1. Server generates response with `ETag: "abc123"`
2. Cache stores response along with the ETag
3. Resource becomes stale; cache sends `If-None-Match: "abc123"`
4. Server compares: same ETag → 304 Not Modified; different → 200 OK

## Relationship with Last-Modified

Servers commonly send both headers:

```
ETag: "33a64df551425fcc55e4d42a148795d9f25f89d4"
Last-Modified: Wed, 21 Oct 2015 07:28:00 GMT
```

ETag is more precise (not limited to 1-second resolution). When both are present, ETag takes precedence for validation (HTTP requires strong comparison).

## Auto-Generation by Web Servers

Many web servers auto-generate ETags from file metadata (inode, size, modification time). This works for static files but has subtle consequences:
- Doesn't work for dynamically generated API responses (no file to read)
- Can cause false mismatches in load-balanced environments where files are served from different servers with different inodes

## Best Practices

- Always pair ETag with Cache-Control for complete caching policy
- Use strong ETags for API responses (JSON/XML) where content accuracy is critical
- Use weak ETags when serving semantically identical content from different sources
- Generate ETags from content hashes (MD5/SHA) for deterministic validation
- Consider disabling ETags in multi-server deployments if auto-generated from metadata

## Related Pages

- [[Conditional Request]], [[Cache-Control]], [[HTTP Caching]], [[Vary Header]]
