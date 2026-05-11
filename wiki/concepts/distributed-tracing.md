---
title: "Distributed Tracing"
type: concept
tags: [observability, tracing, monitoring, microservices]
created: 2026-05-11
sources: [dynatrace-distributed-tracing]
---

# Distributed Tracing

**Distributed tracing** is a method of observing requests as they propagate through distributed cloud environments. Each request is tagged with a unique **trace ID** that follows it across every service it touches.

## Core Concepts

### Trace
A complete record of a single request's end-to-end journey across all services and components.

### Span
An individual unit of work within a trace. Each span has:
- Name (operation being performed)
- Start and end timestamps
- Metadata (service name, error codes, etc.)
- Parent-child relationship (hierarchical ordering)

```
Trace: GET /checkout
├── Span: API Gateway (parent)
│   ├── Span: Auth Service
│   ├── Span: Cart Service
│   │   └── Span: Redis Lookup
│   └── Span: Payment Service
│       └── Span: DB Write
└── Span: Response
```

## Benefits

- **Reduced MTTD/MTTR** — quickly find root cause across services
- **SLA compliance** — understand end-to-end latency per request
- **Improved collaboration** — pinpoint exact service and owning team
- **Bottleneck detection** — identify slow spans in the chain

## Challenges

| Challenge | Issue |
|-----------|-------|
| Manual instrumentation | Some tools require code changes for each service |
| Backend-only coverage | Trace ID starts at first backend service, misses frontend |
| Head-based sampling | Random sampling at request start may miss high-value traces |

## Sampling Strategies

- **Head-based**: Sample decided at request start (random; may miss important traces)
- **Tail-based**: Sample decided after request completes (can prioritize by tags like customer tier or error status)

## Relation to Observability

Distributed tracing is one of the **three pillars of observability** alongside [[Log Aggregation|logs]] and [[Metrics|metrics]]. It provides the contextual linkage that logs alone cannot — showing how a single request flows across services.

## Related

- [[Log Aggregation]] — Combines logs across services; tracing adds cross-service context
- [[OpenTelemetry]] — Open standard for traces, metrics, and logs
- [[Service Discovery]] — Services must find each other before tracing can instrument calls
- [[Microservices]] — Tracing is essential for microservice observability
