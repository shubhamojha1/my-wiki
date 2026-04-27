---
title: "HTTP/3"
type: concept
tags: [networking, http]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# HTTP/3

**HTTP/3** is the third major version of HTTP (RFC 9114), introduced in 2018.

## Key Change

Runs over **UDP** via the **QUIC** protocol instead of TCP.

## Benefits

- **No head-of-line blocking**: Lost packets don't stall other streams
- **0-RTT**: Fast repeat connections
- **Connection migration**: Seamless network switching (Wi-Fi to cellular)

## QUIC

Quick UDP Internet Connections combines TLS and transport in one protocol.

## Related Concepts

- [[HTTP]] — Previous versions
- [[HTTP/2]] — Version over TCP
- [[UDP]] — Transport protocol