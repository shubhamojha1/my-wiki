---
title: "Extendible Hashing"
type: concept
tags: [database, data-structure, hash]
created: 2026-04-23
---

# Extendible Hashing

**Extendible hashing** is a dynamic hash table that uses a directory and can grow incrementally by splitting buckets.

## How It Works

- **Directory**: Array of pointers to buckets
- **Global depth**: Number of bits used for directory index
- **Local depth**: Number of bits used for bucket
- Split: When bucket overflows, double directory, split bucket

## Split Process

1. Create new bucket
2. Redistribute entries based on next bit
3. Update directory pointers
4. Increment global depth if needed

## Properties

- **Incremental expansion**: Only split overflowing bucket
- **Directory doubles**: Grows by powers of 2
- **Local depth tracking**: Knows which buckets can split

## Trade-offs

- **Pros**: No full rehash, good for growing datasets
- **Cons**: Directory overhead, complexity

## Related

- [[Hash Table]] — General category
- [[Linear Hashing]] — Alternative dynamic scheme
- [[Chained Hashing]] — Simpler dynamic scheme