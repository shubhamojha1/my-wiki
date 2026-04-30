---
title: "Event Idempotency"
type: concept
tags: [system-design, reliability, pattern]
created: 2026-05-01
sources: [algomaster-webhooks.md]
---

# Event Idempotency

Ensuring that processing the same event multiple times has no additional side effects beyond the first processing.

## Why It Matters

Event sources (like [[Webhooks]]) may deliver the same event multiple times due to:
- Network retries
- Provider re-delivery after timeout
- Manual replay by operators

Without idempotency, duplicate events cause incorrect state (e.g., double-charging, duplicate notifications).

## Implementation

1. Each event includes a **unique identifier** (e.g., Stripe `evt_1234`, GitHub `delivery_id`)
2. Store processed IDs in a database or cache
3. Before processing, check if the ID was already handled:
   ```
   if (eventAlreadyProcessed(eventId)) {
       return 200 OK;  // Acknowledge without reprocessing
   }
   ```
4. Process and persist the event atomically

## Result

Provides **exactly-once processing semantics** even over at-least-once delivery systems.
