---
title: "Proxy"
type: concept
tags: [networking, proxy]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# Proxy

A **proxy** (or forward proxy) is a server that acts on behalf of clients, sitting between a private network and the public internet.

## How It Works

1. Client sends request
2. Proxy intercepts the request
3. Proxy decides to forward, deny, or serve cached
4. Forwarded request goes to target server
5. Server sees only proxy's IP, not client's
6. Proxy relays response back to client

## Use Cases

- **Privacy**: Hide client's real IP address
- **Access Control**: Content filtering and restrictions
- **Caching**: Store frequently accessed content
- **Geo-bypassing**: Access region-locked content

## VPN vs Proxy

- VPN encrypts all traffic
- Proxy forwards specific requests without encryption

## Related Concepts

- [[Proxy vs Reverse Proxy]] — Parent concept
- [[Reverse Proxy]] — Opposite direction