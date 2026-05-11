---
title: "Dynatrace: What Is Distributed Tracing?"
type: source
tags: [observability, tracing, distributed-systems, monitoring]
created: 2026-05-11
sources: [dynatrace-distributed-tracing]
---

# Dynatrace: What Is Distributed Tracing?

**URL:** https://www.dynatrace.com/knowledge-base/distributed-tracing/
**Last updated:** April 23, 2026

## Summary

An introductory guide to distributed tracing in cloud-native environments — what it is, how it works, benefits, challenges, and how it differs from traditional logging.

## Key Concepts Covered

- **Definition**: Method of observing requests as they propagate through distributed cloud environments using unique identifiers (trace IDs)
- **Spans**: Individual units of work (segments); each has name, timestamps, metadata; parent-child hierarchy
- **Trace**: Complete record of a single request's journey across all services
- **Benefits**: reduced MTTD/MTTR, SLA compliance, faster time to market, improved collaboration
- **Challenges**: manual instrumentation (some tools), limited backend coverage, head-based sampling misses traces
- **Three pillars of observability**: Logs, Metrics, Traces
- **Logging vs tracing**: Centralized logging (aggregate logs to single location) vs distributed logging (logs across locations)
- **Head-based vs tail-based sampling**: Head-based samples at start of request (may miss important traces); tail-based samples after completion (captures priority traces)
