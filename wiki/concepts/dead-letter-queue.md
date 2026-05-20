---
title: "Dead Letter Queue"
type: concept
tags: [system-design, reliability, messaging, fault-tolerance]
created: 2026-05-01
updated: 2026-05-20
sources: [algomaster-webhooks.md, algomaster-message-queues]
---

# Dead Letter Queue (DLQ)

A **dead letter queue** is a special queue that receives messages or events that have consistently failed processing and cannot be retried further. It acts as a safety net: instead of silently discarding failed messages or clogging the main queue, they are parked for investigation.

## Why DLQs Exist

Without a DLQ:
- A "poison message" (one that always fails) blocks the consumer indefinitely
- Retrying forever wastes compute and delays other messages
- Failed events vanish with no audit trail

## When Messages Go to DLQ

| Reason | Description |
|--------|-------------|
| **Max retries exceeded** | Consumer failed N times (e.g., 3 attempts) |
| **Malformed payload** | Message cannot be deserialized — will never succeed |
| **Validation failure** | Business rule violation that won't self-resolve |
| **Consumer timeout** | Processing took too long repeatedly |
| **Expired TTL** | Message too old to be worth processing |

## Workflow

```
[Producer] → [Main Queue]
                  ↓
           [Consumer] → success → done
                     → failure → retry
                     → retries exhausted → [Dead Letter Queue]
                                               ↓
                                         [Alert/Monitor]
                                               ↓
                                    [Fix root cause] → replay
```

## Implementations

| Platform | DLQ Mechanism |
|---------|--------------|
| **AWS SQS** | Configurable `redrive policy`: max receives → DLQ |
| **RabbitMQ** | Dead Letter Exchange (DLX) with routing key |
| **Apache Kafka** | No built-in DLQ; use separate topic + consumer group |
| **Azure Service Bus** | Built-in dead-letter subqueue |

## Operations

- **Monitoring**: Alert on DLQ depth; high DLQ rate indicates a systemic problem
- **Replay**: After fixing the root cause, messages can be moved back to the main queue for reprocessing
- **Inspection**: DLQ stores original message, metadata, and failure reason for debugging

## Related Concepts

- [[Message Queue]] — the main queue DLQ backs up
- [[Exponential Backoff]] — retry strategy before DLQ
- [[Idempotency]] — ensures replayed messages are safe to reprocess
- [[Dead Letter Queue]] — also applies to event-driven architectures
