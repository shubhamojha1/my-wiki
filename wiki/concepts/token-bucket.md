---
title: "Token Bucket"
type: concept
tags: [rate-limiting, algorithm, system-design]
created: 2026-05-01
sources: [algomaster-rate-limiting-algorithms.md, "https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
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

## Distributed Implementation

In a [[Distributed Rate Limiter]], every gateway must see the same bucket state for a client. If each gateway stores buckets locally, load-balanced requests can split a client's usage across gateways and allow more traffic than intended.

A Redis-backed token bucket stores two fields per client:

- `tokens`: current token count
- `last_refill`: timestamp used to calculate elapsed refill

The full read-refill-decrement-write sequence must be atomic. Wrapping only the writes in Redis `MULTI/EXEC` is not enough if `HMGET` happens before the transaction, because two concurrent gateways can read the same token count. A Redis Lua script is the stronger pattern because it executes the whole read-modify-write decision atomically.

`EXPIRE` can be set on inactive buckets so idle clients do not leave state in Redis forever.

## Related Concepts

- [[Rate Limiting]]
- [[Distributed Rate Limiter]]
- [[Redis]]
