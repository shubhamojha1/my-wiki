---
title: "Token Bucket"
type: concept
tags: [rate-limiting, algorithm, system-design]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md]
---

# Token Bucket

A rate limiting algorithm where tokens are added to a bucket at a fixed rate and requests consume tokens to proceed.

## How It Works

1. Bucket has a maximum token capacity
2. Tokens are added at a fixed rate (e.g., 10 tokens/second)
3. Each request must consume a token to be allowed
4. If bucket is empty, request is denied
5. Bucket never exceeds maximum capacity

## Properties

| Aspect | Behavior |
|--------|----------|
| Burst handling | Allows bursts up to bucket capacity |
| Rate enforcement | Average rate = token refill rate |
| Memory | O(n) where n = number of users |
| Smoothness | Not guaranteed; bursty |

## Pros
- Simple to implement and understand
- Allows short-term bursts (good for UX)

## Cons
- Memory scales with number of users
- Doesn't guarantee smooth request rate

## Example
Bucket capacity: 10 tokens, refill: 1 token/second
- After 10s idle: bucket full (10 tokens)
- User can burst 10 requests instantly
- Then limited to 1 request/second
