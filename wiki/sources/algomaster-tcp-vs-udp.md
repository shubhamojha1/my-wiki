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

Google's **QUIC** (basis for HTTP/3) runs on UDP but adds TCP-like reliability. Key advantages:
- Avoids TCP handshake latency
- Built-in encryption (TLS 1.3 mandatory)
- Multiplexing: multiple streams without head-of-line blocking
- Custom reliability layers can be built over UDP (e.g., game uses UDP for movement, TCP-style ACKs for critical events)

## Decision Framework

| Requirement | Protocol |
|-------------|----------|
| Guaranteed/ordered delivery | TCP |
| Lowest possible latency | UDP or QUIC |
| Tolerates some packet loss | UDP |
| High accuracy/data integrity | TCP |
| Real-time communication | UDP |
| Built-in flow/congestion control | TCP |

Many large-scale systems use a **hybrid approach**: TCP for auth/API calls, UDP for telemetry, QUIC/HTTP/3 for web content and streaming.

## Security

- **TCP** is the foundation for **TLS** (HTTPS). Its reliable ordered stream is a prerequisite for TLS.
- **UDP** has no built-in security; applications use **DTLS** (Datagram TLS) for encryption.

## TCP Connection Termination (Four-Step)

1. FIN → 2. ACK → 3. FIN → 4. ACK — graceful shutdown ensures no data loss.

## Related Concepts

- [[OSI Layer 4: Transport]] — Layer using TCP/UDP
- [[HTTP/3]] — Uses QUIC (UDP)
- [[TCP]] — Detailed concept
- [[UDP]] — Detailed concept

## Source

- AlgoMaster.io: [TCP vs UDP](https://algomaster.io/learn/system-design/tcp-vs-udp) (November 2025)