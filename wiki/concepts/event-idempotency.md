---
title: "Event Idempotency"
type: concept
tags: [system-design, reliability, pattern]
created: 2026-05-01
updated: 2026-05-20
sources: [algomaster-webhooks.md]
---

# Event Idempotency

**Event idempotency** is the property where processing the same event multiple times produces the same outcome as processing it once. It converts **at-least-once** delivery (the norm in distributed systems) into **effectively exactly-once** semantics.

## Why Duplicates Happen

| Cause | Example |
|-------|---------|
| **Network retry** | Client didn't receive ACK; resends the event |
| **Provider re-delivery** | Webhook provider retries after timeout (Stripe retries up to 72 hours) |
| **Consumer restart** | Consumer crashes mid-processing; redelivers from queue offset |
| **Manual replay** | Operator replays events for debugging or backfill |

Without idempotency: a `payment.charged` event arriving twice charges the customer twice.

## Implementation Pattern

```
Receive event with ID "evt_1234":

1. CHECK: Is "evt_1234" in the processed-events store?
   YES → return 200 OK immediately (idempotent response)
   NO  → continue

2. RESERVE: Atomically insert "evt_1234" with status IN_PROGRESS
   (prevents parallel duplicates from racing)

3. PROCESS: Apply business logic (charge payment, send email, etc.)

4. COMMIT: Update "evt_1234" status to COMPLETED + store result

5. RESPOND: Return 200 OK to the event source
```

## Storage for Processed IDs

| Option | Pros | Cons |
|--------|------|------|
| **Redis SET NX** | Fast, built-in TTL | Memory-only unless persisted |
| **DB unique index** | Durable, ACID | Slower (~1–5ms write) |
| **SQS FIFO dedup** | Built-in 5-min window | Only within 5 minutes |
| **Kafka consumer offset** | Natural ordering | Per-partition; requires careful offset commit |

## Consumer-Side Idempotency

For business logic that is inherently non-idempotent (e.g., `INSERT INTO orders`), use:
- **Idempotency key as unique constraint**: `INSERT INTO orders (idempotency_key, ...) ON CONFLICT DO NOTHING`
- **Conditional update**: `UPDATE balances SET amount = amount - 10 WHERE txn_id NOT IN (processed_txns)`

## Exactly-Once vs Effectively Exactly-Once

True exactly-once delivery (the message system guarantees it arrives exactly once) requires distributed transactions between the message broker and the consumer's state store — expensive and brittle. **Effectively exactly-once** via idempotent consumers is the practical approach: deliver at-least-once, deduplicate at the consumer.

## Related Concepts

- [[Idempotency]] — the general property
- [[Idempotency Key]] — the unique identifier tracked per operation
- [[Deduplication Store]] — the data structure holding processed IDs
- [[Dead Letter Queue]] — handles events that fail even after dedup/retry
- [[Webhooks]] — a common source of at-least-once event delivery
