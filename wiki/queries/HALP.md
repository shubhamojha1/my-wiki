---
title: "How does YouTube HALP work?"
type: query
tags: [cache-eviction, machine-learning, cdn, youtube]
created: 2026-04-21
sources: []
---

**HALP** (Heuristic Aided Learned Preference Eviction Policy) is YouTube's ML-based cache eviction system for their CDN's DRAM cache, presented at NSDI 2023.

## Problem

YouTube's CDN uses multi-tier caching. When DRAM cache is full and a new item arrives, an eviction policy must decide what to remove. Traditional policies (LRU, LFU) are simple but suboptimal. Pure ML approaches fail in production due to high CPU overhead, sensitivity to distribution shift, and poor handling of cold items.

## Solution

HALP is a **hybrid** that combines:
1. **Heuristic baseline** — lightweight LRU-variant eviction rule
2. **Learned reward model** — lightweight neural network (one hidden layer) predicting which of two cached items will be re-accessed first

The algorithm uses **randomized blending** between heuristic and ML predictions, plus **preference learning with automated feedback** — trained on pairs to predict re-access order.

## Architecture

- **Feature extraction**: cache metadata (recency, frequency, size, freshness)
- **Reward model**: binary classifier trained on pairwise comparisons (cross-entropy loss)
- **Inference**: ~720ns per pairwise prediction
- **Blending**: randomness merges heuristic + ML recommendations

## Results (production)

- **9.1%** byte miss reduction during peak traffic
- **12%** improvement in egress/ingress ratio  
- **6%** improvement in memory hit rate
- **1.8%** CPU overhead
- Running since early 2022

See also: [[LRB]], [[Cache Eviction Policy]], [[Pairwise Learning to Rank]], [[Impact Distribution Analysis]]