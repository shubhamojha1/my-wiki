---
title: "Exponential Backoff"
type: concept
tags: [system-design, reliability, retry]
created: 2026-05-01
sources: [webhooks-algomaster.md]
---

# Exponential Backoff

A retry strategy that increases the delay between retry attempts exponentially to avoid overwhelming a failing service.

## How It Works

After each failure, wait longer before retrying:
- Attempt 1: fail → wait 1s
- Attempt 2: fail → wait 2s
- Attempt 3: fail → wait 4s
- Attempt 4: fail → wait 8s
- ...up to max retries

## Jitter

Adding randomness to the backoff delay prevents the **thundering herd problem** where many clients retry simultaneously:
```
delay = base_delay * 2^attempt + random_jitter
```

## Alternatives

| Strategy | Pattern | Use Case |
|----------|---------|----------|
| Exponential | 1s, 2s, 4s, 8s... | General purpose (recommended) |
| Linear | 30s, 30s, 30s... | Fixed-rate retry scenarios |
| Exponential + Jitter | 1.3s, 2.7s, 3.1s... | High-concurrency systems |

## Use With

Always pair with a max retry limit and a [[Dead Letter Queue]] to handle permanently failing events.
