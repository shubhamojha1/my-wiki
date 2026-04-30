---
title: "AlgoMaster: WebSockets"
type: source
tags: [networking, real-time, system-design]
created: 2026-05-01
sources: [websockets-algomaster.md]
---

# AlgoMaster: WebSockets

Source: [blog.algomaster.io/p/websockets](https://blog.algomaster.io/p/websockets) by Ashish Pratap Singh (Aug 2024).

## Summary

WebSockets are a communication protocol enabling full-duplex, bidirectional real-time communication between client and server over a single [[TCP]] connection. Unlike [[HTTP]]'s request-response model, WebSockets maintain a persistent connection allowing both parties to send messages independently.

## Key Takeaways

### Connection Lifecycle
1. **Handshake** — Client sends HTTP GET with `Upgrade: websocket` header; server responds with [[HTTP 101]] status code switching protocols
2. **Connection** — Persistent connection stays open until explicitly closed
3. **Data Transfer** — Messages sent in small frames with minimal overhead (as small as 2-byte headers)
4. **Closure** — Either party can close with a "close" frame indicating reason

### Advantages over Alternatives
- **vs HTTP**: Eliminates stateless request-response latency; enables bidirectional communication
- **vs Polling**: No repeated requests wasting bandwidth when no data available
- **vs Long-Polling**: Server holds response until data ready, but still requires reconnection after each response; WebSockets maintain single persistent connection

### Use Cases
- Real-time chat (Slack)
- Live notifications (social media)
- Multiplayer online games
- Financial market data feeds (stock prices, crypto)
- Real-time collaboration (Google Docs)
- IoT device communication
- Live streaming interactive features

### Challenges
- **Proxy/firewall compatibility** — Some proxies don't support WebSocket connections
- **Scalability** — Large numbers of persistent connections require load balancers and distributed WebSocket servers
- **Network reliability** — Need reconnection strategies and heartbeat (ping/pong) mechanisms
- **Security** — Vulnerable to Cross-Site WebSocket Hijacking and DDoS; use `wss://`, authenticate users, validate input
- **Fallback** — Implement long-polling fallback for incompatible clients/networks

### Implementation
Basic Node.js server using `ws` library; client-side uses native JavaScript `WebSocket` API with `onopen`, `onmessage`, `onclose`, `onerror` event handlers.
