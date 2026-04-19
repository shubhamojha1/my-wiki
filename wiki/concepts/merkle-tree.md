---
title: "Merkle Tree"
type: concept
tags: [distributed-systems, synchronization]
created: 2026-04-19
sources: [mixu-distributed-systems-book]
---

Merkle trees enable efficient comparison of data across replicas through hierarchical hashing.

## Structure
Multiple levels of hashes:
- Hash of entire content
- Hash of half the keys
- Hash of quarter
- etc.

## Comparison Process
1. Compare root hashes
2. If different, compare next level
3. Identify specific keys that differ

## Advantages
- Efficient narrow differences
- Only transfer necessary updates
- Used in [[Dynamo]] replica sync

## Alternative Names
- Hash tree
- Merkle hash tree