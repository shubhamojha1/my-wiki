---
title: "Edge Cache"
type: concept
tags: [caching, cdn, edge-computing, live-video]
created: 2026-05-08
sources: ["https://engineering.fb.com/2015/12/03/ios/under-the-hood-broadcasting-live-video-to-millions/"]
---

# Edge Cache

**Definition:** A cache layer deployed at geographically distributed edge locations (edge data centers, CDN points of presence) to serve content to users from the nearest possible location, minimizing latency and reducing origin server load.

## Architecture

An edge cache sits between clients and the origin infrastructure:

```
[Client] → [Edge Cache (global PoPs)] → [Origin Cache] → [Origin Server]
```

Edge caches are typically HTTP proxy servers (Varnish, Nginx) deployed across dozens or hundreds of locations worldwide. They cache responses and serve them to nearby users, dramatically reducing round-trip time.

## Facebook's Live Video Edge Cache

In Facebook's live video architecture (2015):
- Live video split into **3-second HLS segments**
- Each segment request routed to the nearest edge cache
- **98%+ of segment requests** served from edge cache
- Only ~1.8% of requests leak through to origin

### Request Coalescing at the Edge

When a live video segment is not yet in cache (first request for a new segment), the edge cache uses **request coalescing** to prevent a [[Cache Stampede]]:

1. First request arrives → cache miss → forwarded to origin
2. Subsequent requests for same segment → **queued at edge**
3. Origin response arrives → segment stored in edge cache
4. All queued requests served as cache hits
5. Same mechanism repeats at the origin cache layer for multi-edge requests

## Edge Cache vs Browser Cache vs Proxy Cache

| Aspect | Edge Cache | [[Browser Caching\|Browser Cache]] | [[Proxy Cache]] |
|--------|-----------|-------------------|-----------------|
| Location | Edge data centers worldwide | User's device | Near origin servers |
| Serves | All users in a region | Single user | Local app servers |
| Control | CDN config / headers | Cache-Control headers | Full config (VCL) |
| Use case | CDN, live video, static assets | Browser filesystem | App server offload |

## Benefits

- **Reduced latency** — content served from nearest edge rather than origin
- **Origin offload** — absorbs the vast majority of traffic (98%+ in Facebook's case)
- **Thundering herd protection** — request coalescing at the edge prevents stampedes
- **Global scale** — hundreds of edge locations can absorb massive traffic spikes

## Challenges

- **Cache invalidation** — must propagate across all edge locations
- **Consistency** — different edges may have different cache states
- **Cost** — deploying and maintaining edge infrastructure is expensive (often uses CDN services)
- **Warm-up** — new edge locations start cold, requiring traffic ramping

## Related Pages

- [[CDN]], [[Cache Stampede]], [[Proxy Cache]], [[Browser Caching]], [[Caching]], [[Amazon CloudFront]]
