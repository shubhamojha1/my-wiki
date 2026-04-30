---
title: "Leaky Bucket"
type: concept
tags: [rate-limiting, algorithm, system-design]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md]
---

# Leaky Bucket

A rate limiting algorithm that processes requests at a constant rate, smoothing out bursty traffic.

## How It Works

1. Requests enter a queue (the "bucket")
2. Requests "leak" out at a fixed, constant rate
3. If the bucket is full, new requests are discarded/dropped

## Properties

| Aspect | Behavior |
|--------|----------|
| Burst handling | Drops excess requests; no bursts allowed |
| Rate enforcement | Strictly constant rate |
| Memory | O(n) where n = queue size |
| Smoothness | Guaranteed smooth output |

## vs [[Token Bucket]]

| Token Bucket | Leaky Bucket |
|--------------|--------------|
| Allows bursts | Smooths bursts |
| Token-based | Queue-based |
| Flexible rate | Strict constant rate |

## Pros
- Predictable, steady processing rate
- Prevents system overload from traffic spikes

## Cons
- Does not handle bursts well (drops excess)
- Slightly more complex than Token Bucket
- Can starve requests if time gap between arrivals is large (leaks only on new requests without timer-based implementation)
