---
title: "HTTP 101"
type: concept
tags: [networking, http, protocol, websocket]
created: 2026-05-01
updated: 2026-05-20
sources: [algomaster-websockets.md]
---

# HTTP 101 (Switching Protocols)

**HTTP 101 Switching Protocols** is an informational status code indicating the server is agreeing to switch to a different protocol requested by the client via the `Upgrade` header.

## WebSocket Handshake

HTTP 101 is used during [[WebSockets]] connection establishment:

```http
-- Client Request --
GET /chat HTTP/1.1
Host: example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Sec-WebSocket-Version: 13

-- Server Response --
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
```

After the 101 response, the TCP connection is **repurposed**: HTTP communication ends and the [[WebSockets]] protocol begins over the same connection.

## Security

The `Sec-WebSocket-Key` / `Sec-WebSocket-Accept` exchange prevents caching proxies from mistakenly treating a WebSocket upgrade as a simple HTTP request. The accept value is a hash of the key concatenated with a fixed GUID, defined in RFC 6455.

## Related Concepts

- [[WebSockets]] — the protocol established after HTTP 101
- [[HTTP]] — the protocol that initiates the upgrade
- [[TCP]] — the underlying connection that is repurposed
- [[Frame (WebSocket)]] — the data unit used after the upgrade
