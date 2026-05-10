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
- **Retransmission**: Automatically resends lost packets on timeout
- **Flow control**: Sliding window prevents overwhelming receiver
- **Congestion control**: Adapts to network conditions (slows on congestion)
- **Error detection**: Checksum in each segment; corrupted packets discarded and resent
- **Header**: 20-60 bytes

## Three-Way Handshake

1. **SYN**: Client requests connection, shares initial sequence number (ISN)
2. **SYN-ACK**: Server acknowledges, reserves resources, shares its ISN
3. **ACK**: Connection established, both sides synchronized

## Data Transfer

TCP segments application data and transmits with:
- **Sliding window**: Multiple packets in flight before requiring ACK, improving throughput
- **Sequence numbers**: Enable ordered reassembly and duplicate detection
- **Retransmission**: Lost packets resent after timeout

## Connection Termination (Four-Step)

1. **FIN**: Client signals no more data to send
2. **ACK**: Server acknowledges, processes remaining data
3. **FIN**: Server closes its side
4. **ACK**: Client confirms, both release resources

This graceful shutdown ensures no data loss.

## Security

TCP is the foundation for **TLS** (Transport Layer Security), which powers HTTPS. The reliable, ordered stream is a prerequisite for how TLS operates.

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