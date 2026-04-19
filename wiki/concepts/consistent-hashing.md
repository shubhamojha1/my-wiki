---
title: "Consistent Hashing"
type: concept
tags: [distributed-systems, partitioning]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Consistent hashing maps keys to nodes in a way that minimizes remapping when nodes are added or removed.

## How It Works
- Keys mapped to points on circle
- Nodes responsible for arc of circle
- Adding node only affects segment

## Advantages
- Reduces data movement on changes
- Improves availability
- Used in [[Dynamo]]

## Tradeoffs
- Non-uniform distribution possible
- Virtual nodes help balance