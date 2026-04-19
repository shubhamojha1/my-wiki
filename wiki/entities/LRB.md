---
title: "LRB (Learning Relaxed Belady)"
type: entity
tags: [caching, machine-learning, learned-cache]
created: 2026-04-19
sources: [HALP - Youtube Heuristic CDNs.pdf]
---

# LRB (Learning Relaxed Belady)

A learned cache eviction algorithm that uses regression to predict time to next access.

## Overview

LRB approximates the Belady (MIN) algorithm — which evicts the object accessed furthest in the future — by learning access patterns from traces.

## Algorithm

- Maintains features for objects currently and historically in cache
- Trains a regression model to predict time to next access
- At eviction: randomly samples 64 objects, predicts, evicts the one predicted furthest in future

## Performance

- Better than heuristic algorithms on many workloads
- BUT requires 64 candidates → ~19% CPU overhead (prohibitive at scale)
- Sensitive to memory window hyperparameter

## Comparison with HALP

| Aspect | LRB | HALP |
|--------|-----|------|
| Candidates | 64 | 4 |
| CPU overhead | ~19% | ~1.8% |
| Byte miss | Baseline | Similar |
| Training | Offline | Online |

See: [[HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN]]