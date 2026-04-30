---
title: "Idempotency"
type: concept
tags: [system-design, reliability, distributed-systems]
created: 2026-05-01
sources: [algomaster-idempotency.md]
---

# Idempotency

A property of operations where executing the same request multiple times produces the same result as executing it once.

## Why It Matters

In distributed systems, network failures are common. If a client times out waiting for a response, it retries. Without idempotency, retries cause duplicate effects (double charges, duplicate messages, data corruption).

## HTTP Methods

| Method | Idempotent? | Reason |
|--------|-------------|--------|
| GET | Yes | Read-only; no state change |
| PUT | Yes | Replaces resource with same state |
| DELETE | Yes | Deleting an already-deleted resource is a no-op |
| POST | No | Creates new resource each time |

## Implementation Strategies

1. **[[Idempotency Key]]** — Client sends unique ID; server tracks and deduplicates
2. **[[Upsert]]** — Database operation that updates if exists or inserts if new
3. **Unique Constraints** — DB-level prevention of duplicate entries
4. **Message Deduplication** — Log of processed message IDs in [[Message Queue]] systems

## Challenges

- **Performance**: Key storage and lookups add latency
- **Concurrency**: Race conditions between simultaneous duplicates
- **Distributed Systems**: Requires distributed locks or consensus
- **Time Window**: How long to keep idempotency keys (TTL)?

## Best Practices

- Design for idempotency from the start
- Use [[Exponential Backoff]] for retries
- Use locks or optimistic concurrency control for concurrent safety
- Document idempotent operations in API specs
- Test with simulated network failures and concurrent requests
