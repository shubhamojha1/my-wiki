---
title: "Long-Polling"
type: concept
tags: [networking, real-time, pattern]
created: 2026-05-01
sources: [algomaster-websockets.md, long-polling-vs-websockets]
---

# Long-Polling

A technique where the client sends a request and the server holds the connection open until data is available or a timeout occurs. An enhancement over traditional [[Polling]] that eliminates wasted periodic requests.

## How It Works

1. Client sends HTTP request
2. Server holds connection open — doesn't respond immediately
3. When data is available (or timeout reached), server responds and closes connection
4. Client **immediately** sends a new request to maintain the loop

## Advantages over [[Polling]]
- No wasted requests — every response contains data (or timeout)
- Lower latency — server responds as soon as data is ready
- Universally supported — uses standard HTTP, works through firewalls and proxies

## Disadvantages
- Higher latency per update compared to [[WebSockets]] (must re-establish connection after each response)
- Resource-heavy on servers — many concurrent open connections consume memory/threads
- Not suitable for high-frequency or bidirectional communication

## When to Use

- Simple chat or comment systems where near-real-time is acceptable
- Notification systems with infrequent updates (e.g., email alerts)
- Legacy environments where WebSockets aren't feasible
- Projects requiring minimal implementation complexity

## Alternative Solutions

- **[[WebSockets]]** — Full-duplex persistent connection, lower latency, bidirectional
- **Server-Sent Events (SSE)** — Server push over HTTP, one-way, simpler than WebSockets
- **MQTT** — Lightweight pub/sub protocol for IoT
- **Socket.io** — WebSocket abstraction with automatic long polling fallback

## Related

- [[WebSockets]] — The lower-latency alternative
- [[Polling]] — The simpler but wasteful predecessor
