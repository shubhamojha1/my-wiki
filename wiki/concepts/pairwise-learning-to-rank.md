---
title: "Pairwise Learning to Rank"
type: concept
tags: [machine-learning, ranking, online-learning]
created: 2026-04-19
sources: [HALP - Youtube Heuristic CDNs.pdf]
---

# Pairwise Learning to Rank

A framework for learning ranking functions by comparing pairs of items, used in HALP for cache eviction decisions.

## Core Idea

Instead of assigning absolute scores, learn to compare pairs:
- "Is item A better than item B?"
- Binary classification: which item will be re-accessed first?

## Application to Cache Eviction

HALP uses pairwise comparisons to select eviction candidates:

1. **Candidate selection**: LRU proposes 4 eviction candidates
2. **Pairwise ranking**: Tournament-style comparisons (3 comparisons for 4 candidates)
3. **Training data**: Labels resolved from future re-accesses

## Key Benefits

- **Robust**: Error on one comparison doesn't dominate
- **Efficient**: O(n log n) comparisons for n candidates
- **Online**: Labels become available as requests arrive
- **Flexible**: Works with any binary classifier

## Technical Details

- Uses neural network with one hidden layer (~20 neurons)
- Pairwise prediction: 720 ns
- Training: ~ms per mini-batch
- Retrain interval: every 1024 training samples

See: [[HALP: Heuristic Aided Learned Preference Eviction Policy for YouTube CDN]]