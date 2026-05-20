---
title: "Frame (WebSocket)"
type: concept
tags: [networking, websocket, protocol]
created: 2026-05-01
updated: 2026-05-20
sources: [algomaster-websockets.md]
---

# Frame (WebSocket)

A **WebSocket frame** is the basic unit of data transfer in the [[WebSockets]] protocol. After the HTTP upgrade handshake (HTTP 101), all communication between client and server consists of frames.

## Structure

A WebSocket frame has a compact binary header (2–14 bytes) followed by the payload:

| Field | Size | Description |
|-------|------|-------------|
| FIN | 1 bit | Indicates this is the last fragment of a message |
| RSV1–3 | 3 bits | Reserved for extensions |
| Opcode | 4 bits | Frame type (text, binary, close, ping, pong) |
| MASK | 1 bit | Whether payload is masked (client→server frames must be masked) |
| Payload length | 7–71 bits | Length of the payload data |
| Masking key | 0 or 4 bytes | Present only if MASK=1 |
| Payload | Variable | The actual data |

Minimum header is **2 bytes** — far smaller than the hundreds of bytes in a typical HTTP request header.

## Frame Types (Opcodes)

| Opcode | Type | Purpose |
|--------|------|---------|
| 0x0 | Continuation | Fragment of a multi-frame message |
| 0x1 | Text | UTF-8 text payload |
| 0x2 | Binary | Binary data |
| 0x8 | Close | Initiate graceful connection teardown |
| 0x9 | Ping | Keepalive/heartbeat |
| 0xA | Pong | Response to ping |

## Full-Duplex Communication

Both client and server can send frames **independently** at any time — no request/response pairing required. This enables true real-time bidirectional communication.

## Related Concepts

- [[WebSockets]] — the protocol these frames belong to
- [[HTTP 101]] — the upgrade that establishes the WebSocket connection
- [[TCP]] — the transport layer carrying WebSocket frames
