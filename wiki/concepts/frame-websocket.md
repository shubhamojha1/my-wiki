---
title: "Frame (WebSocket)"
type: concept
tags: [networking, websocket, protocol]
created: 2026-05-01
sources: [algomaster-websockets.md]
---

# Frame (WebSocket)

The unit of data transfer in the [[WebSockets]] protocol.

## Properties

- Sent as small packets over the established WebSocket connection
- Minimal header overhead — as small as 2 bytes
- Much smaller than [[HTTP]] request headers

## Role

After the initial HTTP handshake and [[HTTP 101]] response, all communication between client and server occurs via WebSocket frames. Both parties can send frames independently in a full-duplex manner.

A "close" frame is used to terminate the connection, optionally including a reason code.
