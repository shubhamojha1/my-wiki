---
title: "HTTP/2"
type: concept
tags: [networking, http]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-http-https"]
---

# HTTP/2

**HTTP/2** (RFC 7540, 2015) is the second major version of HTTP. It keeps HTTP's familiar request/response semantics but replaces the text-based wire format with a binary framing layer, enabling multiplexing, header compression, and server push over a single TCP connection.

## Problems with HTTP/1.1

| Problem | Description |
|---------|-------------|
| **Head-of-line blocking** | Requests on a connection are serialized; one slow response stalls all later ones |
| **Connection overhead** | Browsers open 6–8 parallel TCP connections per host to work around HoL blocking |
| **Verbose headers** | Headers (cookies, user-agent) repeat on every request with no compression |
| **No server initiative** | Server can only respond; can't push resources the client will obviously need |

## Key Features

### Binary Framing

HTTP/2 breaks messages into **frames** (the smallest unit) — typed binary envelopes. Frame types: HEADERS, DATA, SETTINGS, PING, WINDOW_UPDATE, PUSH_PROMISE, etc.

### Multiplexing

Multiple **streams** (request/response pairs) share one TCP connection. Each stream is identified by a stream ID. Frames from different streams are **interleaved** on the wire:

```
Connection:
  ← [Stream 1: HEADERS] [Stream 3: DATA] [Stream 1: DATA] [Stream 5: HEADERS] →
```

This eliminates application-level HoL blocking (TCP-level HoL blocking remains — addressed by HTTP/3).

### HPACK Header Compression

HPACK maintains a shared compression table of previously seen headers. Repeated headers (e.g., `content-type`, cookies) are sent as a 1-byte index instead of full text. Typical compression ratio: 85–95% for header bytes.

### Server Push

Server can proactively send resources (e.g., CSS, JS) by sending a `PUSH_PROMISE` frame before the client requests them. Eliminated in HTTP/3 (misused in practice; early hints replaced it).

### Stream Prioritization

Clients can assign weights and dependencies to streams, letting servers prioritize which responses to send first (e.g., critical CSS over images). In practice, prioritization was poorly implemented by servers.

## HTTP/1.1 vs HTTP/2 vs HTTP/3

| Feature | HTTP/1.1 | HTTP/2 | HTTP/3 |
|---------|---------|--------|--------|
| Transport | TCP | TCP | QUIC (UDP) |
| Multiplexing | No (workaround: parallel connections) | Yes | Yes |
| Header compression | None | HPACK | QPACK |
| HoL blocking | App + TCP | TCP only | Eliminated |
| Connection setup | TCP + TLS (2 RTT) | TCP + TLS (2 RTT) | 0-RTT / 1-RTT |
| Server push | No | Yes (mostly unused) | No |

## Adoption

Broadly supported by major browsers since 2015. Requires TLS in practice (browsers enforce HTTPS). ~65% of web traffic as of 2024.

## Related Concepts

- [[HTTP]] — HTTP/1.1 foundation
- [[HTTP/3]] — QUIC-based successor that eliminates TCP HoL blocking
- [[TLS]] — required by all major browsers for HTTP/2
- [[gRPC]] — uses HTTP/2 for multiplexed RPC streams
