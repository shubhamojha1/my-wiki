---
title: "AlgoMaster: Webhooks"
type: source
tags: [system-design, event-driven, real-time]
created: 2026-05-01
sources: [webhooks-algomaster.md]
---

# AlgoMaster: Webhooks

Source: [blog.algomaster.io/p/what-are-webhooks](https://blog.algomaster.io/p/what-are-webhooks) by Ashish Pratap Singh (Apr 2025).

## Summary

Webhooks are an event-driven mechanism where one system (provider) pushes data to another system (receiver) in real time when an event occurs, using an HTTP request. Unlike [[Polling]], the provider initiates communication only when something happens, eliminating wasted requests.

## Key Takeaways

### How Webhooks Work
1. **Registration** — Receiver registers a webhook URL with the provider (e.g., GitHub, Stripe) and selects which events to subscribe to
2. **Triggering** — Provider monitors internal events for the subscribed actions
3. **Delivery** — Provider sends an HTTP POST request with a JSON payload to the registered URL
4. **Acknowledgment** — Receiver processes the payload and returns HTTP `200 OK`

### Anatomy of a Webhook Request
- **HTTP method**: POST (de facto standard)
- **Headers**: Content-Type (application/json), User-Agent, X-Event-Type, X-Signature (HMAC), X-Request-ID
- **Body**: JSON containing event details, timestamps, and resource metadata

### Setting Up a Receiver
- **Dedicated endpoint**: Accept only POST + JSON over HTTPS
- **[[Event Idempotency]]**: Store processed event IDs to prevent duplicate processing — ensures exactly-once semantics
- **Status codes**: 200 OK for success, 400 for invalid payloads, avoid 5xx (triggers provider retries)
- **Security**: Verify HMAC signature using shared secret; optional IP whitelisting; never log full payloads in plaintext

### Scalable Webhook Infrastructure
Production-grade pipeline with six components:
1. **Queue incoming requests** — Parse, validate, enqueue immediately (Kafka, RabbitMQ, AWS SQS); return fast 200 OK
2. **Store events for audit & replay** — Persist raw payload, event ID, type, status, timestamps (PostgreSQL, MongoDB, DynamoDB)
3. **Async workers** — Background worker pools pull from queue, deduplicate, validate, execute business logic
4. **Retry with backoff** — Exponential backoff with jitter; limit retries and log failures
5. **[[Dead Letter Queue]]** — Events that exceed retry limits go to DLQ for investigation and manual retry
6. **Observability** — Track event volume, success/failure rate, processing latency, queue length, DLQ count; alert on spikes in failures or growing queue sizes (Prometheus + Grafana, Datadog, ELK Stack)
