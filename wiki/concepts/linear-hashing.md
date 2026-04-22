---
title: "Linear Hashing"
type: concept
tags: [database, data-structure, hash]
created: 2026-04-23
---

# Linear Hashing

**Linear hashing** is a dynamic hash table that uses a split pointer to incrementally split buckets without directory doubling.

## How It Works

- **Split pointer**: Tracks next bucket to split
- **Round-robin splitting**: Split any overflowing bucket, not specific one
- **Multiple hash functions**: Use `h0`, `h1`, `h2` as table grows

## Split Process

1. Any bucket overflows (beyond threshold)
2. Split bucket at split pointer
3. Use hash function based on current round
4. Advance split pointer
5. When pointer reaches end, reset and increase hash function

## Properties

- **No directory**: Simpler than extendible hashing
- **Round-robin**: Splits buckets evenly over time
- **Eventually reshapes**: Pointer cycle completes full table

## Trade-offs

- **Pros**: Simple, no directory overhead, smooth growth
- **Cons**: May split non-overflowing buckets, less targeted

## Related

- [[Hash Table]] — General category
- [[Extendible Hashing]] — Alternative dynamic scheme
- [[Chained Hashing]] — Basis for implementation