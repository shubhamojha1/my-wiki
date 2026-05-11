---
title: "Circuit Breaker Pattern (Design Patterns for Microservices)"
type: source
tags: [microservices, circuit-breaker, fault-tolerance]
created: 2026-05-11
sources: [medium-circuit-breaker]
---

# Circuit Breaker Pattern (Design Patterns for Microservices)

**Author:** Hasitha Subhashana
**URL:** https://medium.com/geekculture/design-patterns-for-microservices-circuit-breaker-pattern-276249ffab33
**Published:** June 12, 2021

## Summary

An introduction to the Circuit Breaker pattern for microservices — 3 states (closed, open, half-open), cascading failure prevention, threshold-based tripping, and background health probing.

## Key Concepts Covered

- **Problem**: Cascading failures when a downstream service slows or fails, causing thread pool exhaustion and queue buildup
- **3 states**: Closed (normal, requests pass through), Open (fail fast, no requests forwarded), Half-Open (limited test requests allowed)
- **Trip mechanism**: When failure rate exceeds threshold (e.g., 75% of requests > threshold latency or absolute timeout)
- **Recovery**: Background ping/probe requests; on success, circuit resets to closed
- **Fallback**: Requests return error immediately during open state (no queuing)
- **Result**: Service protected from overload, can recover, no cascading failures
