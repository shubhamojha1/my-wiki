---
title: "Long-Polling"
type: concept
tags: [networking, real-time, pattern]
created: 2026-05-01
sources: [websockets-algomaster.md]
---

# Long-Polling

A technique where the client sends a request and the server holds the connection open until data is available or a timeout occurs.

## How It Works

1. Client sends HTTP request
2. Server holds connection open (doesn't respond immediately)
3. When data is available, server responds and closes connection
4. Client immediately sends a new request

## Advantages over [[Polling]]
- No wasted requests — every response contains data (or timeout)
- Lower latency — server responds as soon as data is ready

## Disadvantages
- Still requires repeated reconnections after each response
- Server resource exhaustion from managing many open connections
- Higher latency than [[WebSockets]]
