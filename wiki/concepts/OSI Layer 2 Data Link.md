---
title: "OSI Layer 2: Data Link"
type: concept
tags: [osi-model, networking, layer-2]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-osi-model"]
---

# OSI Layer 2: Data Link

**Layer 2** (the Data Link layer) wraps raw bits (Layer 1) into structured **frames** and introduces local network addressing via MAC addresses. It manages delivery between directly connected nodes on the same network segment.

## Responsibilities

| Responsibility | Detail |
|---------------|--------|
| **Framing** | Delimits start/end of each frame so the receiver can parse boundaries |
| **Hardware addressing** | 48-bit MAC addresses identify source and destination on the local segment |
| **Error detection** | CRC/FCS at frame end; corrupted frames are dropped (not retransmitted — that's Layer 4/TCP) |
| **Flow control** | Prevents a fast sender from overwhelming a slow receiver at the link level |
| **Medium access** | CSMA/CD (Ethernet), CSMA/CA (Wi-Fi) — who gets to transmit and when |

## Sublayers

- **LLC (Logical Link Control)**: Error detection, flow control, multiplexing (identifies which Layer-3 protocol is encapsulated).
- **MAC (Media Access Control)**: Hardware addresses, framing, arbitrates access to the shared medium.

## Ethernet Frame Structure

```
┌──────────────┬───────────────┬──────┬──────────────────┬─────┐
│  Preamble    │  Dest MAC (6B)│ Src  │  Type/Length (2B)│ FCS │
│  7+1 bytes   │               │  MAC │  (EtherType)     │ CRC │
│  10101010... │ FF:FF:FF:FF…  │  (6B)│  0x0800 = IPv4   │ 4B  │
└──────────────┴───────────────┴──────┴──────────────────┴─────┘
         payload (46–1500 bytes of IP packet) ↑
```

## Key Devices

| Device | Layer | Behavior |
|--------|-------|---------|
| **Hub** | Layer 1 | Repeats bits to all ports; no MAC awareness |
| **Switch** | Layer 2 | Reads destination MAC; forwards only to correct port; learns MAC table |
| **Bridge** | Layer 2 | Connects two network segments; filters by MAC |

Switches maintain a **MAC address table** (CAM table): `{port → MAC}` learned by observing source MAC addresses on each port.

## Scope

Layer 2 only works within a single **broadcast domain** (one LAN/VLAN). To cross networks, Layer 3 (IP) takes over. A router separates Layer 2 domains.

## Related Concepts

- [[OSI Model]] — the 7-layer framework
- [[MAC Address]] — the 48-bit hardware identifier used at Layer 2
- [[OSI Layer 1: Physical]] — provides bits that Layer 2 frames
- [[OSI Layer 3: Network]] — adds IP addressing for inter-network routing
- [[CRC]] — the error-detection code in Ethernet frame FCS
