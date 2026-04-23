---
title: "Offline Processing"
type: concept
tags: [architecture, scalability, async]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Offline Processing

**Definition:** Computation that cannot or should not be performed within the user's request-response timeline, either due to latency requirements or periodic nature.

## Why Offline?

Some processing is unsuitable for inline execution:
- **Too slow** — Would cause unacceptable latency (e.g., updating social graph)
- **Periodic** — Must happen at specific times (e.g., daily reports)
- **Expensive** — Consumes significant resources
- **Batch-oriented** — Works best with large datasets

## Processing Categories

### Latency-Driven
Processing that *could* be inline but is too slow:
- Social graph propagation
- Recommendation updates
- Search index updates
- Notification sending

### Schedule-Driven
Processing that must occur periodically:
- Daily analytics rollups
- Cleanup jobs
- Report generation
- Data aggregation

## Enabling Technologies

- [[Message Queue]] — Decouples producers from consumers
- [[Scheduling Periodic Tasks]] — Cron + queue workers
- [[Map-Reduce]] — Large-scale batch processing

## Related Concepts

[[Message Queue]], [[Scheduling Periodic Tasks]], [[Map-Reduce]], [[Scalability]]