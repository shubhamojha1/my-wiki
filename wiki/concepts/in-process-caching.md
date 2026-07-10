---
title: "In-Process Caching"
type: concept
tags: [caching, performance]
created: 2026-07-10
sources: ["hellointerview-caching"]
---

# In-Process Caching

Caching data in local memory within an application process itself, rather than in a shared external store. Each server instance holds its own independent copy.

## Characteristics

- **Blazing fast** — no network hop at all; the data is in the same process's memory space.
- **Not shared** — each application server maintains its own cache, so the same key can hold different (or absent) values on different instances behind a load balancer.
- **Best suited to small, frequently accessed values** — configuration, feature flags, small lookup tables — where per-instance duplication is cheap and staleness is tolerable.

## vs. Other Cache Locations

| | In-Process | [[In-Memory Cache|External (Redis/Memcached)]] |
|---|---|---|
| Location | Inside the app process | Separate service/network hop |
| Sharing | Per-instance, not shared | Shared across all app servers |
| Speed | Fastest possible (no network) | Fast, but a network round trip |
| Consistency across instances | None by default | Consistent (single shared store) |
| Scaling | Scales with app instances (duplicated) | Scales independently |

In-process caching is the wrong choice for data that must be consistent across servers (e.g. session state, rate-limit counters) — see [[In-Memory Cache]] for the shared alternative used there.

## Related Concepts

- [[Caching]] — the broader set of cache locations this is one of
- [[In-Memory Cache]] — the shared, external alternative
- [[Application Caching]] — a separate axis (who manages cache logic), not to be confused with cache location
