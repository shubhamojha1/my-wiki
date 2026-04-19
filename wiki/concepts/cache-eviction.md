---
title: "Cache Eviction Policy"
type: concept
tags: [caching, systems, algorithms]
created: 2026-04-19
sources: []
---

# Cache Eviction Policy

Algorithms that determine which data to remove when a cache is full and new data needs to be inserted.

## Background

Caches store frequently accessed data closer to users to reduce latency and load on origin servers. YouTube's CDN uses multiple cache tiers: DRAM (fastest), SSDs, HDDs, and origin servers.

**Byte miss ratio** — the fraction of user-requested bytes not found in cache — is a key metric to optimize.

## Heuristic-Based Policies

### LRU (Least Recently Used)
Evicts the least recently accessed object. Works well when recently accessed items are likely to be re-accessed.

### FIFO (First In First Out)
Evicts oldest inserted object. Works for sequential workloads.

### ARC (Adaptive Replacement Cache)
Adaptively balances recency and frequency. Combines LRU and LFU.

### LFU (Least Frequently Used)
Evicts least frequently accessed object.

### GDSF (Greedy-Dual-Size-Frequency)
Considers object size and access frequency.

## Learned Policies

### LRB (Learning Relaxed Belady)
Uses regression to predict time to next access. Requires 64 eviction candidates (~19% CPU overhead).

### HALP (Heuristic Augmented Learned Preferences)
[[HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN]]

Augments LRU with ML using only 4 candidates:
- Lower CPU overhead (~1.8%)
- More robust to regression
- Online training via pairwise comparisons

### LeCaR (Learning Cache Agent)
Uses reinforcement learning for cache decisions.

## Key Challenges at Scale

1. **Computation overhead** — ML can be expensive per eviction
2. **Regression risk** — ML may hurt some locations
3. **Production noise** — Hard to measure impact via A/B testing

See also: [[Impact Distribution Analysis]]