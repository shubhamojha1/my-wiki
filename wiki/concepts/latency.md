---
title: "Latency"
type: concept
tags: [distributed-systems, performance]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Latency is the time between the initiation of something and its occurrence - the delay before impact becomes visible.

## Etymology
From Latin "latens" (lying hidden). The period during which something that has already happened is concealed from view.

## Why It Matters
Low latency is interesting because it's connected to physical (not financial) limitations. It's harder to address latency using money than other performance aspects.

## Minimum Latency Constraints
- Speed of light limits information travel
- Hardware components have minimum latency (RAM, disk, CPU)
- Geographic distance directly impacts achievable latency

## Distributed Systems View
For a data store, latency could be measured as time for a write to become visible to readers. If data doesn't change, latency isn't a concern.

## Tradeoffs
Achieving lower latency often requires weaker consistency guarantees (more communication between nodes).