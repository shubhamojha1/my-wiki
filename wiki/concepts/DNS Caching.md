---
title: "DNS Caching"
type: concept
tags: [dns, networking, caching]
created: 2026-04-28
sources: ["algomaster-dns"]
---

# DNS Caching

**DNS caching** stores DNS query results at various levels to avoid repeated resolution lookups.

## Caching Levels

### Browser Cache
- Fastest access
- Short TTL (Time To Live)
- Stored in browser process

### Operating System Cache
- Shared across all applications
- System-wide cache

### Recursive Resolver Cache
- ISP or public DNS servers
- Reduces load on root/TLD/authoritative servers

## Time To Live (TTL)

- Determines how long to cache
- Set in DNS record
- Typical values: seconds to days

## Cache Invalidation

- TTL expiration
- DNS updates propagate naturally

## Related Concepts

- [[DNS]] — Parent concept
- [[Caching]] — General caching concept
- [[Recursive Resolver]] — Where caching occurs