---
title: "Latency"
type: concept
tags: [distributed-systems, performance, networking]
created: 2026-04-19
updated: 2026-05-20
sources: [mixu-distributed-systems-book, "algomaster-latency-throughput"]
---

# Latency

**Latency** is the time elapsed between initiating an operation and observing its effect — the delay before a result becomes visible.

## Why It Matters

Latency is bounded by physics, not just engineering. Unlike throughput, which can often be improved by throwing more hardware at a problem, latency has hard physical lower bounds:

- **Speed of light** — information cannot travel faster than ~300,000 km/s (in fiber: ~200,000 km/s)
- **Geographic distance** — New York to London is ~70ms round-trip at the speed of light in fiber; real RTT is ~80–100ms
- **Hardware floors** — L1 cache access: ~1ns; DRAM: ~100ns; NVMe SSD: ~100μs; HDD seek: ~10ms

## Common Latency Numbers

| Operation | Typical Latency |
|-----------|----------------|
| L1 cache read | ~1 ns |
| DRAM read | ~100 ns |
| SSD random read | ~100 μs |
| HDD seek | ~10 ms |
| Same datacenter round trip | ~0.5 ms |
| Cross-continent round trip | ~100–150 ms |

## Latency in Distributed Systems

For a data store, latency is typically measured as the time for a write to become visible to readers. This is coupled to the **consistency model**:

- **Strongly consistent** systems force all reads to see the latest write, which requires synchronization across nodes — adding latency
- **Eventually consistent** systems return local data immediately — low latency, but reads may be stale

The **latency-consistency trade-off**: lower latency often requires weaker consistency guarantees.

## Tail Latency

Average latency is misleading. The **tail** (p99, p999 percentiles) represents the worst-case experience for real users. In large systems, tail latency compounds:

> If a request fans out to 100 services, the response is limited by the slowest one. Even a 1% tail becomes almost certain to be hit.

This makes tail latency reduction critical in high-scale systems.

## Related Concepts

- [[Latency vs Throughput]] — the fundamental performance trade-off
- [[Consistency Model]] — consistency choices affect latency
- [[CAP Theorem]] — availability/consistency affect achievable latency
- [[CDN]] — reduces latency by serving from geographically close nodes
- [[Caching]] — primary tool for reducing read latency
