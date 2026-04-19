---
title: "ARC (Adaptive Replacement Cache)"
type: entity
tags: [caching, algorithms]
created: 2026-04-19
sources: [HALP - Youtube Heuristic CDNs.pdf]
---

# ARC (Adaptive Replacement Cache)

A self-tuning cache algorithm that dynamically balances recency and frequency.

## Overview

ARC maintains four lists:
- T1: recently used (recency)
- T2: frequently used (frequency)  
- B1: ghost entries for T1
- B2: ghost entries for T2

The cache adapts based on workload: more recency for sequential workloads, more frequency for repeating workloads.

## Performance

- Better than LRU or LFU alone across diverse workloads
- But still heuristic-based, not learning patterns

See: [[Cache Eviction Policy]]