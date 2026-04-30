---
title: "HTTP 101"
type: concept
tags: [networking, http, protocol]
created: 2026-05-01
sources: [algomaster-websockets.md]
---

# HTTP 101 (Switching Protocols)

HTTP status code indicating the server is switching from one protocol to another.

## WebSocket Handshake

Used during [[WebSockets]] connection establishment:
1. Client sends HTTP GET with `Upgrade: websocket` header
2. Server responds with `101 Switching Protocols`
3. Connection transitions from [[HTTP]] to WebSocket protocol

The 101 response signals the end of HTTP communication and the beginning of full-duplex WebSocket communication over the same [[TCP]] connection.
