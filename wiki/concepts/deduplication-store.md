---
title: "Deduplication Store"
type: concept
tags: [system-design, data-structures, reliability]
created: 2026-05-01
updated: 2026-05-20
sources: [algomaster-idempotency.md]
---

# Deduplication Store

A **deduplication store** is a shared, persistent data structure that records which operations have already been processed, so that duplicate requests (retries, replayed messages, network duplicates) can be detected and suppressed.

It is the implementation mechanism behind [[Idempotency Key]] patterns.

## Problem It Solves

In distributed systems, retries are unavoidable — network timeouts, load balancer retries, and client-side retry loops all cause the same request to arrive multiple times. Without a deduplication store, a payment might be charged twice, an email sent twice, or an order created twice.

## Record Schema

```
idempotency_key (PK, indexed)
status          ENUM(IN_PROGRESS, COMPLETED, FAILED)
result_payload  JSON / blob (cached response to return on duplicate)
created_at      timestamp
expires_at      timestamp (TTL)
```

## Two-Phase Insert Pattern

Atomic operations prevent race conditions when two identical requests arrive simultaneously:

```
Request arrives with key K:

1. RESERVATION (atomic INSERT or equivalent):
   INSERT INTO dedup_store (key, status, created_at)
   VALUES (K, 'IN_PROGRESS', now())
   ON CONFLICT DO NOTHING   ← if duplicate, this fails

   If conflict → return cached result for K (or wait if IN_PROGRESS)

2. PROCESS the actual operation

3. COMPLETION:
   UPDATE dedup_store SET status='COMPLETED', result=<resp> WHERE key=K

4. Return result to caller
```

## Implementation Options

| Backend | Pros | Cons |
|---------|------|------|
| **Redis** (with `SET NX PX`) | O(1) lookup, TTL built-in, high throughput | Memory-only (configure persistence); no rich queries |
| **Relational DB** (unique index on key) | Durable, ACID, result caching | Higher latency (~1–5 ms) |
| **AWS SQS** | Built-in 5-minute dedup window for FIFO queues | Fixed TTL, queue-specific |
| **Apache Kafka** | Idempotent producers (sequence numbers per partition) | Producer-side only, within session |

## Key Design Decisions

| Decision | Guidance |
|----------|---------|
| **TTL** | Match to your maximum retry window + buffer (e.g., 24 hours for payment retries) |
| **Scope** | Per-user, per-resource, or global? Narrow scope = less storage, more granular |
| **Atomicity** | Always use `INSERT ... ON CONFLICT` or `SET NX` — never read-then-write |
| **Cleanup** | Schedule TTL-based expiry; do not grow unbounded |
| **Result caching** | Store the full response so duplicates get identical replies (not re-processed results) |

## Related Concepts

- [[Idempotency Key]] — the unique identifier tracked by the dedup store
- [[Idempotency]] — the broader property the store helps enforce
- [[Event Idempotency]] — dedup at the message/event consumer level
- [[Dead Letter Queue]] — handles messages that fail repeatedly despite dedup
