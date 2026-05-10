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

## Why UDP

TCP's head-of-line blocking persists even in HTTP/2: a single lost TCP packet stalls *all* streams on that connection. HTTP/3 moves to UDP via QUIC to eliminate this.

## Benefits

- **No head-of-line blocking**: Lost packets only affect the affected stream, not all streams
- **0-RTT**: Fast repeat connections — send data in the first packet
- **Connection migration**: Identified by connection ID, not IP/port — seamless Wi-Fi to cellular switching

## System Design Impact

Ideal for real-time applications, faster connection setup, improved performance on unreliable networks. Major adopters: Google, YouTube, Cloudflare.

## QUIC

Quick UDP Internet Connections combines TLS and transport in one protocol.

## Related Concepts

- [[HTTP]] — Previous versions
- [[HTTP/2]] — Version over TCP
- [[UDP]] — Transport protocol