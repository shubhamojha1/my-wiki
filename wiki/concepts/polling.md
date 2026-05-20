---
title: "Polling"
type: concept
tags: [networking, real-time, pattern, http]
created: 2026-05-01
updated: 2026-05-20
sources: [algomaster-websockets.md, long-polling-vs-websockets]
---

# Polling

**Polling** is a technique where the client repeatedly sends HTTP requests to the server at fixed intervals to check for new data or state changes. It is the simplest approach to real-time communication but the least efficient.

## How It Works

```
Client          Server
  |--GET /updates-->|
  |<--200 (empty)---|
  | (wait 2s)       |
  |--GET /updates-->|
  |<--200 (data)----|
  | (wait 2s)       |
  |--GET /updates-->|
  ...
```

The client sends requests on a schedule (e.g., every 2 seconds) regardless of whether new data exists.

## Problems

- **Inefficiency** — Most requests return no new data, wasting bandwidth and server CPU
- **Latency** — Updates are delayed until the next poll cycle (up to the full interval)
- **Server load** — Many idle clients still generate continuous request volume
- **Not truly real-time** — There is always a gap between when data changes and when the client learns about it

## When to Use

Polling is acceptable when:
- Updates are infrequent and delay is tolerable
- Infrastructure doesn't support [[WebSockets]] or [[Long-Polling]]
- Simplicity matters more than efficiency

## Alternatives (in order of efficiency)

| Technique | How | Trade-off |
|-----------|-----|---------|
| Polling | Client requests at fixed intervals | Simple, but wasteful |
| [[Long-Polling]] | Server holds request until data is ready | Fewer empty responses; more complex |
| [[WebSockets]] | Persistent bidirectional TCP connection | Most efficient; requires upgrade |
| Server-Sent Events (SSE) | Server pushes over HTTP | One-directional; simpler than WebSockets |

## Related Concepts

- [[Long-Polling]] — server-side improvement to polling
- [[WebSockets]] — the preferred real-time alternative
- [[HTTP]] — polling uses standard HTTP requests
