---
title: "HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN"
type: source
tags:
  - cdn
  - caching
  - machine-learning
  - learned-cache
  - youtube
created: 2026-04-19
sources:
  - HALP - Youtube Heuristic CDNs.pdf
---

# HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN

**Authors:** Zhenyu Song, Kevin Chen, Nikhil Sarda, Deniz Altınbüken, Eugene Brevdo, Jimmy Coleman, Xiao Ju, Pawel Jurczyk, Richard Schooler, Ramki Gummadi (Google)

**Venue:** USENIX NSDI 2024

## Summary

This paper presents HALP, a cache eviction algorithm that augments a heuristic policy (LRU) with machine learning for YouTube's CDN. HALP addresses three challenges blocking ML deployment in large-scale production:

1. **Computation overhead** - HALP uses only 4 eviction candidates (vs 64 in prior work LRB), achieving 1.8% CPU overhead
2. **Robust byte miss ratio improvement** - Augmenting heuristics prevents regressions across diverse locations
3. **Measuring impact under production noise** - Novel "impact distribution analysis" denoises A/B test measurements

## Key Insights

### HALP Architecture
- Uses LRU to propose 4 eviction candidates
- Neural network ranks candidates via pairwise comparisons
- Online training generates labels from future re-accesses
- Binary classification: which object gets re-accessed first?

### Features Used
- Time between accesses (32-dim)
- Exponential decay counters (10-dim)
- Number of accesses
- Average time between accesses
- Time since last access
- End of chunk score (spatial locality)

### Impact Distribution Analysis
A novel method to measure algorithm impact in production by:
1. Estimating measurement distribution (experiment vs control)
2. Estimating noise distribution (no-op vs control)
3. Fitting impact distribution via deconvolution

## Results

- 9.1% average byte miss reduction during peak hours
- 3.8% reduction in disk first byte latency
- 1.22% reduction in join latency
- Deployed since early 2022 in YouTube CDN production

## Related Systems

- [[LRB]] — Prior learned cache using 64 candidates
- [[ARC]] — Adaptive Replacement Cache
- [[Adaptive-TinyLFU]] — Frequency-based heuristic
- [[B-LRU]] — LRU with Bloom filter admission

## External Links

- [Paper PDF](https://storage.googleapis.com/gweb-research2023-media/pubtools/7078.pdf)