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

## Comparison

| Protocol | Latency | Bidirectional | Connection |
|----------|---------|---------------|------------|
| [[HTTP]] | High | No | Per-request |
| [[Polling]] | Medium | No | Repeated requests |
| [[Long-Polling]] | Medium | No | Reconnect after each response |
| WebSockets | Low | Yes | Persistent |

## See Also
- [[Frame (WebSocket)]]
- [[HTTP 101]]
- [[Polling]]
- [[Long-Polling]]
