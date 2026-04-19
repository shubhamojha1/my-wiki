---
title: "Impact Distribution Analysis"
type: concept
tags: [experimentation, production, statistics]
created: 2026-04-19
sources: [HALP - Youtube Heuristic CDNs.pdf]
---

# Impact Distribution Analysis

A method for measuring the impact of a new algorithm in a noisy production environment, developed for deploying HALP at YouTube CDN.

## Problem

In large-scale systems, A/B testing is challenging because:
- Machines on the same rack show different byte miss ratios over time
- Noise can cause up to 10% difference in measurements
- Mean-shift estimates miss distribution of impacts

## Approach

1. **Model measurements**: M = I + N
   - M = observed measurement
   - I = actual impact
   - N = production noise

2. **Split machines into three groups**:
   - **Experiment machines**: Run new algorithm
   - **No-op machines**: Run baseline (measure noise)
   - **Control machines**: Baseline for comparison

3. **Fit distributions**:
   - Fit noise distribution using t-distribution (no-op vs control)
   - Fit measurement distribution (experiment vs control)
   - Deconvolve to get impact distribution

## Results

Without denoising: 1.5% of racks show negative impact (up to 4% increase)
With denoising: 9.1% average byte miss reduction with negligible regression

This enables accurate measurement of ML algorithm impact in production.

See: [[HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN]]