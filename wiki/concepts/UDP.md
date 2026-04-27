---
title: "UDP"
type: concept
tags: [networking, udp]
created: 2026-04-28
sources: ["algomaster-tcp-vs-udp"]
---

# UDP

**UDP** (User Datagram Protocol) is a connectionless transport layer protocol.

## Characteristics

- **Connectionless**: No handshake
- **Unreliable**: No delivery guarantee
- **No ordering**: Packets may arrive out of order
- **No retransmission**: Lost packets not resent
- **No flow/congestion control**: Application handles
- **Lightweight**: 8-byte header
- **Supports broadcast/multicast**

## Use Cases

- DNS queries
- VoIP (real-time voice)
- Video streaming
- Online gaming
- DHCP
- QUIC/HTTP/3

## When to Use

- Low latency > reliability
- Application can tolerate loss
- Real-time communication needed

## Related Concepts

- [[TCP vs UDP]] — Parent concept
- [[TCP]] — Alternative protocol
- [[QUIC]] — Runs on UDP
- [[OSI Layer 4: Transport]] — Layer