---
title: "OSI Layer 4: Transport"
type: concept
tags: [osi-model, networking, layer-4]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-osi-model"]
---

# OSI Layer 4: Transport

**Layer 4** (the Transport layer) is responsible for end-to-end delivery of data between applications on different hosts. It takes the network's best-effort packet delivery (Layer 3) and adds reliability, ordering, flow control, and multiplexing across applications on the same host.

## Core Responsibilities

| Responsibility | Description |
|---------------|-------------|
| **Multiplexing** | Ports identify which application on the host should receive each segment (src_ip:src_port → dst_ip:dst_port = 4-tuple) |
| **Segmentation / Reassembly** | Splits large application data into segments; receiver reassembles in order |
| **Flow control** | Prevents a fast sender from overwhelming a slow receiver (TCP sliding window) |
| **Congestion control** | Reduces send rate when the network is congested (TCP Reno, CUBIC, BBR) |
| **Error recovery** | Retransmits lost segments (TCP only) |
| **Connection management** | Establishes and tears down logical connections (TCP 3-way handshake, FIN) |

## TCP vs UDP

| Feature | TCP | UDP |
|---------|-----|-----|
| Connection | Yes (3-way handshake) | No |
| Reliability | Guaranteed (ACK + retransmit) | Best-effort |
| Order | Yes (sequence numbers) | Not guaranteed |
| Flow control | Yes (sliding window) | No |
| Overhead | ~20 byte header | ~8 byte header |
| Latency | Higher | Lower |
| Use cases | HTTP, SSH, databases | DNS, video streaming, gaming, VoIP |

## Port Numbers

```
Source:       192.168.1.5 : 54321  (ephemeral port, OS-assigned)
Destination:  93.184.216.34 : 443  (well-known HTTPS port)
```

Ports 0–1023: well-known (HTTPS=443, HTTP=80, SSH=22, DNS=53)  
Ports 1024–49151: registered applications  
Ports 49152–65535: ephemeral (client-side, OS-assigned per connection)

## How It Relates to Other Layers

```
Layer 7  Application  (HTTP, DNS, gRPC)
Layer 6  Presentation (TLS encryption)
Layer 5  Session
Layer 4  Transport    ← ports, reliability, flow control (TCP/UDP)
Layer 3  Network      (IP addressing, routing)
Layer 2  Data Link    (frames, MAC addresses)
Layer 1  Physical     (bits on wire)
```

## Related Concepts

- [[TCP]] — reliable, connection-oriented Layer 4 protocol
- [[UDP]] — fast, connectionless Layer 4 protocol
- [[Port (Network)]] — the Layer 4 application multiplexer
- [[OSI Model]] — full 7-layer framework
- [[OSI Layer 3: Network]] — delivers packets host-to-host (Layer 4 input)
- [[OSI Layer 5: Session]] — manages connection lifecycle above Layer 4
