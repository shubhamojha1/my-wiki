---
title: "AlgoMaster: Rate Limiting Algorithms"
type: source
tags: [system-design, rate-limiting, algorithms]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md]
---

# AlgoMaster: Rate Limiting Algorithms

Source: [blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code](https://blog.algomaster.io/p/rate-limiting-algorithms-explained-with-code) by Ashish Pratap Singh (Jul 2024).

## Summary

Covers 5 common rate limiting algorithms with code implementations (Python/Java): [[Token Bucket]], [[Leaky Bucket]], [[Fixed Window Counter]], [[Sliding Window Log]], and [[Sliding Window Counter]]. Each has trade-offs in accuracy, memory usage, and burst handling.

## Algorithms Covered

### 1. [[Token Bucket]]
- Bucket holds tokens, refilled at fixed rate
- Requests consume tokens; denied if insufficient
- **Pros**: Simple, allows bursts up to bucket capacity
- **Cons**: Memory scales with users, doesn't guarantee smooth rate

### 2. [[Leaky Bucket]]
- Queue-based; requests leak out at constant rate
- **Pros**: Smooth, predictable processing rate; prevents bursts
- **Cons**: Drops excess requests immediately; slightly complex

### 3. [[Fixed Window Counter]]
- Time divided into fixed windows (e.g., 1 min); counter resets each window
- **Pros**: Easy to implement, clear limits
- **Cons**: Boundary problem — allows 2x rate at window edges

### 4. [[Sliding Window Log]]
- Stores timestamp log per request; removes expired entries
- **Pros**: Very accurate, no window boundary issues
- **Cons**: Memory-intensive for high-volume APIs

### 5. [[Sliding Window Counter]]
- Hybrid: weighted sum of current + previous window counts
- Formula: `weight = (100 - overlap%) * lastWindowRequests + currentWindowRequests`
- **Pros**: More accurate than Fixed Window, more memory-efficient than Sliding Window Log
- **Cons**: Slightly more complex

## Best Practice

Always communicate rate limits via response headers so clients can implement retry and [[Exponential Backoff]] strategies.
