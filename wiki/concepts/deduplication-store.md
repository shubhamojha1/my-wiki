---
title: "Deduplication Store"
type: concept
tags: [system-design, data-structures, reliability]
created: 2026-05-01
sources: [algomaster-idempotency.md]
---

# Deduplication Store

A data store used to track processed operation identifiers (like [[Idempotency Key]]s or message IDs) to prevent duplicate processing.

## Purpose

Enables idempotency by providing a centralized, authoritative record of which operations have already been completed.

## Implementation

- **Redis**: Fast in-memory lookups with TTL support; good for high-throughput systems
- **Database table**: Persistent storage with unique constraints; reliable but slower
- **Message Queue metadata**: Built-in deduplication in systems like AWS SQS or [[Apache Kafka]]

## Key Design Decisions

| Decision | Consideration |
|----------|---------------|
| TTL | How long to keep keys? Match to retry window |
| Atomicity | Use atomic "insert if not exists" to prevent race conditions |
| Storage format | Key → status (PENDING/COMPLETED/FAILED) + result payload |

## Two-Phase Pattern

For correctness under concurrency:
1. **Reservation**: Atomically insert key with status `IN_PROGRESS`
2. **Completion**: After processing, update status to `COMPLETED` and store result
