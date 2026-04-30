---
title: "Polling"
type: concept
tags: [networking, real-time, pattern]
created: 2026-05-01
sources: [algomaster-websockets.md]
---

# Polling

A technique where the client repeatedly sends requests to the server at fixed intervals to check for updates.

## How It Works

Client sends HTTP requests on a schedule (e.g., every 2 seconds). Server responds with data if available, or empty response if not.

## Problems
- **Inefficient** — Many requests return no new data, wasting bandwidth
- **Latency** — Updates only arrive on next poll cycle
- **Server load** — High request volume from idle clients

## Alternatives
- [[Long-Polling]] — Server holds response until data available
- [[WebSockets]] — Persistent bidirectional connection (most efficient)
