---
title: "Dead Letter Queue"
type: concept
tags: [system-design, reliability, messaging]
created: 2026-05-01
sources: [webhooks-algomaster.md]
---

# Dead Letter Queue (DLQ)

A special holding queue for messages or events that consistently fail processing after multiple retry attempts.

## Purpose

Prevents bad events from clogging the main processing pipeline and ensures no event is silently lost.

## When Events Go to DLQ

- Persistent downstream service unavailability
- Malformed payloads that cannot be parsed
- Data validation failures that won't resolve on retry

## Workflow

1. Worker attempts to process event
2. Processing fails; retry counter increments
3. After exceeding max retries, event is moved to DLQ
4. DLQ triggers alerts for investigation
5. Events can be manually retried after root cause is fixed

## Common Implementations

- AWS SQS Dead Letter Queues
- RabbitMQ DLX (Dead Letter Exchange)
- Kafka topic for failed events (with separate consumer group)
