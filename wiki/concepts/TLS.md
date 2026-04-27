---
title: "TLS"
type: concept
tags: [security, networking, tls]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# TLS

**TLS** (Transport Layer Security) is a cryptographic protocol providing secure communication over a network.

## Versions

- TLS 1.2 — Current standard
- TLS 1.3 — Faster, simplified handshake

## TLS Handshake

1. Client Hello → Server Hello
2. Server sends certificate
3. Client verifies certificate
4. Key exchange
5. Establish secure session

## TLS 1.3 Features

- **0-RTT**: Repeat connections skip handshake
- **Simplified**: Fewer cipher suites
- **Forward secrecy**: Required

## Related Concepts

- [[HTTPS]] — HTTP over TLS
- [[SSL Termination]] — Termination at proxy
- [[Public Key Infrastructure]] — Certificate framework