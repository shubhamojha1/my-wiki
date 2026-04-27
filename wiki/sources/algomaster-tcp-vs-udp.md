---
title: "TCP vs UDP"
type: source
tags: [system-design, networking, tcp, udp]
created: 2026-04-28
sources: ["algomaster-tcp-vs-udp"]
---

# TCP vs UDP

**TCP** (Transmission Control Protocol) and **UDP** (User Datagram Protocol) are transport layer protocols.

## TCP

- **Connection-oriented**: Three-way handshake (SYN → SYN-ACK → ACK)
- **Reliable**: Guarantees delivery, in-order, error-checked
- **Flow control**: Prevents overwhelming receiver
- **Congestion control**: Adapts to network conditions
- **Slower**: More overhead for reliability

## UDP

- **Connectionless**: No handshake needed
- **Unreliable**: No delivery guarantee
- **No ordering**: Packets may arrive out of order
- **No flow/congestion control**: Application handles this
- **Faster**: Minimal overhead (8-byte header vs 20-60 bytes)

## Key Differences

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Handshake | None |
| Reliability | Guaranteed | None |
| Ordering | In-order | None |
| Speed | Slower | Faster |
| Header | 20-60 bytes | 8 bytes |
| Broadcast | No | Yes |

## Use Cases

**TCP**: Web (HTTP), email, file transfer, databases, SSH
**UDP**: DNS, VoIP, video streaming, gaming, DHCP

## QUIC

Google's QUIC runs on UDP but adds reliability - used in HTTP/3.

## Related Concepts

- [[OSI Layer 4: Transport]] — Layer using TCP/UDP
- [[HTTP/3]] — Uses QUIC (UDP)
- [[TCP]] — Detailed concept

## Source

- AlgoMaster.io: [TCP vs UDP](https://algomaster.io/learn/system-design/tcp-vs-udp) (November 2025)