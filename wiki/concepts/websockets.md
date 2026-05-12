---
title: "WebSockets"
type: concept
tags: [networking, real-time, protocol]
created: 2026-05-01
sources: [algomaster-websockets.md]
---

# WebSockets

A communication protocol for full-duplex, bidirectional communication over a single [[TCP]] connection.

## Protocol

WebSocket connection begins with an [[HTTP]] handshake:
1. Client sends HTTP GET request with `Upgrade: websocket` header
2. Server responds with [[HTTP 101]] (Switching Protocols)
3. Connection upgrades to WebSocket protocol; both parties send [[Frame (WebSocket)]] messages

## Advantages
- **Persistent connection** — No reconnection overhead per message
- **Low latency** — Frames have minimal header overhead (2 bytes minimum)
- **Bidirectional** — Both client and server initiate communication
- **Resource efficient** — Superior to [[Polling]] and [[Long-Polling]]

## Challenges
- **Scalability** — Many persistent connections require distributed architecture
- **Network reliability** — Requires heartbeat (ping/pong) and reconnection logic
- **Proxy compatibility** — Some firewalls/proxies block WebSocket traffic
- **Security** — Use `wss://` (TLS), authenticate users, validate input

## Use Cases
- Real-time chat and messaging (Slack)
- Live notifications
- Multiplayer gaming
- Financial data streaming
- Collaborative editing (Google Docs)
- IoT device communication

## Choosing WebSockets vs Long Polling

| Factor | WebSockets | [[Long-Polling]] |
|--------|------------|------------------|
| Setup complexity | Higher (needs capable proxy: Nginx, HAProxy) | Simple (standard HTTP) |
| Scalability | Better for high-frequency, many concurrent users | Resource-intensive at scale |
| Data frequency | High-frequency, bidirectional | Infrequent, one-way preferred |
| Network constraints | May face firewall/proxy issues | Works universally |
| Latency | Ultra-low (persistent connection) | Higher (reconnect per message) |

## Comparison

| Protocol | Latency | Bidirectional | Connection |
|----------|---------|---------------|------------|
| [[HTTP]] | High | No | Per-request |
| [[Polling]] | Medium | No | Repeated requests |
| [[Long-Polling]] | Medium | No | Reconnect after each response |
| WebSockets | Low | Yes | Persistent |

## Alternative Real-Time Protocols

- **Server-Sent Events (SSE)** — Server push over HTTP, one-way, simpler than WebSockets. Good for news feeds, notifications.
- **MQTT** — Lightweight pub/sub optimized for IoT with minimal bandwidth overhead.
- **Socket.io** — Library abstracting WebSockets with automatic fallback to long polling for cross-browser compatibility.

## See Also
- [[Frame (WebSocket)]]
- [[HTTP 101]]
- [[Polling]]
- [[Long-Polling]]
