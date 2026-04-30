---
title: "Webhooks"
type: concept
tags: [event-driven, system-design, real-time]
created: 2026-05-01
sources: [webhooks-algomaster.md]
---

# Webhooks

An event-driven pattern where a provider system pushes data to a receiver system via HTTP POST when an event occurs.

## How It Works

1. **Registration** — Receiver provides a webhook URL and selects events to subscribe to
2. **Triggering** — Provider monitors for matching events
3. **Delivery** — Provider sends HTTP POST with JSON payload to the webhook URL
4. **Acknowledgment** — Receiver validates, processes, returns `200 OK`

## Request Anatomy

| Component | Description |
|-----------|-------------|
| Method | POST (de facto standard) |
| Content-Type | application/json |
| User-Agent | Identifies sender (e.g., GitHub-Hookshot, Stripe/1.0) |
| X-Event-Type | Event type identifier |
| X-Signature | HMAC signature for verification |
| X-Request-ID | Unique event ID for deduplication |
| Body | JSON with event details, timestamps, resource metadata |

## Receiver Requirements

- **Dedicated HTTPS endpoint** — Accept only POST + JSON
- **[[Event Idempotency]]** — Track processed event IDs to prevent duplicate side effects
- **Signature verification** — Validate HMAC using shared secret
- **Proper status codes** — 200 OK on success, 400 on invalid payload, avoid 5xx

## vs Other Real-Time Patterns

| Pattern | Direction | Initiated By | Connection |
|---------|-----------|--------------|------------|
| [[Webhooks]] | Provider → Receiver | Provider | Per-event HTTP request |
| [[Polling]] | Client → Server | Client | Repeated HTTP requests |
| [[Long-Polling]] | Server → Client | Client (holds) | Reconnect after response |
| [[WebSockets]] | Bidirectional | Either | Persistent TCP connection |

## Scalable Architecture

Production webhook systems use: queue → store → async workers → retry with backoff → [[Dead Letter Queue]] → observability.

## Examples

- GitHub webhooks for CI/CD triggers, Slack notifications
- Stripe payment events (payment_intent.succeeded, customer.subscription.deleted)
- E-commerce order status updates from payment processors
