---
title: "UDP"
type: concept
tags: [networking, udp]
created: 2026-04-28
sources: ["algomaster-tcp-vs-udp"]
---

# UDP

**UDP** (User Datagram Protocol) is a connectionless transport layer protocol operating on a "fire-and-forget" principle. Each **datagram** is an independent message routed individually through the network.

## Characteristics

- **Connectionless**: No handshake — data sent immediately
- **Unreliable**: No delivery guarantee (best-effort)
- **No ordering**: Packets may arrive out of order
- **No retransmission**: Lost packets not resent
- **No flow/congestion control**: Application handles
- **Lightweight**: 8-byte header
- **Supports broadcast/multicast**

## How UDP Works

- Application creates a datagram with destination IP and port
- Sent directly to network — no setup phase, no sequence number exchange
- Receiving application processes incoming data if listening on that port

## Security

UDP has no built-in security mechanism. Applications use **DTLS** (Datagram TLS) to add encryption.

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