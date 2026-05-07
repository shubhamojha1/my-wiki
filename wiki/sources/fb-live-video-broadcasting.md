---
title: "Under the hood: Broadcasting live video to millions"
type: source
tags: [facebook, caching, live-video, thundering-herd, edge-cache]
created: 2026-05-08
sources: ["https://engineering.fb.com/2015/12/03/ios/under-the-hood-broadcasting-live-video-to-millions/"]
---

# Under the hood: Broadcasting live video to millions

**Source:** Facebook Engineering blog by Federico Larumbe & Abhishek Mathur (Dec 2015)

Details Facebook's live video architecture for handling millions of concurrent viewers, with focus on thundering herd prevention and latency reduction.

## The Problem

Public figures on Facebook can have millions of followers. When they start a live broadcast, millions may try to watch simultaneously — a classic thundering herd problem.

## Solution: Multi-Layer Edge Cache Architecture

A live video is split into **3-second HLS segments**. The architecture has three tiers:

```
[Client] → [Edge Cache (global)] → [Origin Cache] → [Live Stream Server]
```

1. **Edge Cache** — HTTP proxies in edge data centers worldwide. 98%+ of segment requests served from edge cache.
2. **Origin Cache** — second cache layer with same architecture. Catches remaining requests from multiple edge locations.
3. **Live Stream Server** — only receives a tiny fraction of requests after both cache layers.

### Request Coalescing

Only ~1.8% of requests leak past the edge cache. Even this small percentage could overwhelm origin at Facebook scale. The fix: **request coalescing**:

- First request for a segment: edge cache forwards to origin (cache miss)
- Subsequent requests for the same segment (while first is in-flight): **queued at the edge**
- When the response arrives: segment stored in edge cache, all queued requests served as cache hits

This mechanism runs at both edge and origin cache layers independently.

### Key Numbers

- HLS segment size: 3 seconds
- Edge cache hit rate: >98%
- Requests leaking past edge: ~1.8%
- Requests reaching live stream server: << 1.8% (after coalescing + origin cache)

## Latency Reduction with RTMP

For lower-latency interactive broadcasts, Facebook implemented **RTMP**:
- Persistent TCP connection (push model, not pull)
- Video/audio split into **4KB chunks** (~64ms at 500Kbps)
- Chunks multiplexed over a single TCP connection
- Latency reduced 5× vs HLS (2–3 seconds end-to-end)
- Built by modifying the nginx-rtmp module

## Related Pages

- [[Cache Stampede]], [[Edge Cache]], [[CDN]], [[Caching]]
