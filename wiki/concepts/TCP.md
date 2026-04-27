---
title: "TCP"
type: concept
tags: [networking, tcp]
created: 2026-04-28
sources: ["algomaster-tcp-vs-udp"]
---

# TCP

**TCP** (Transmission Control Protocol) is a connection-oriented transport layer protocol.

## Characteristics

- **Connection-oriented**: Three-way handshake before data transfer
- **Reliable**: Guarantees delivery and in-order arrival
- **Acknowledgments**: Confirms packet receipt
- **Retransmission**: Automatically resends lost packets
- **Flow control**: Prevents overwhelming receiver
- **Congestion control**: Adapts to network conditions
- **Header**: 20-60 bytes

## Three-Way Handshake

1. **SYN**: Client requests connection
2. **SYN-ACK**: Server acknowledges
3. **ACK**: Connection established

## Use Cases

- HTTP/HTTPS (web)
- Email (SMTP, IMAP)
- File transfer (FTP)
- SSH
- Databases

## Related Concepts

- [[TCP vs UDP]] — Parent concept
- [[UDP]] — Alternative protocol
- [[OSI Layer 4: Transport]] — Layer