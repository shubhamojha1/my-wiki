---
title: "OSI Layer 1: Physical"
type: concept
tags: [osi-model, networking, layer-1]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-osi-model"]
---

# OSI Layer 1: Physical

**Layer 1** (the Physical layer) is the lowest layer of the OSI model. Its sole job is to transmit raw bits — 0s and 1s — across a physical medium between directly connected nodes. It has no concept of addresses, packets, or meaning; it only defines how bits are encoded as signals.

## Responsibilities

- **Signal encoding**: Convert binary bits into electrical voltage levels, light pulses (fiber), or radio waves (Wi-Fi).
- **Bit synchronization**: Sender and receiver must agree on when each bit starts and ends (clock synchronization, Manchester encoding, etc.).
- **Physical medium**: Define connector types, pin layouts, cable specs, and maximum segment lengths.
- **Bit rate / bandwidth**: Specify how fast bits can travel (e.g., 1 Gbps, 10 Gbps).
- **Topology**: Physical star, bus, ring — the actual wire layout.

## Signaling Types

| Medium | Signal | Example |
|--------|--------|---------|
| Copper (UTP/STP) | Electrical voltage | Ethernet (Cat5e/Cat6) |
| Fiber optic | Light pulses | SFP+, QSFP modules |
| Wireless | Radio waves | Wi-Fi (IEEE 802.11), Bluetooth |
| Coaxial | Electrical | Cable TV, older Ethernet |

## Devices at Layer 1

- **Hubs**: Repeat incoming bits to all ports — no intelligence, just amplification.
- **Repeaters**: Regenerate signal over longer distances.
- **Network Interface Cards (NICs)**: Convert computer's digital data to the physical signal type.
- **Cables, connectors, antennas**: The physical medium itself.

## Key Constraint

Layer 1 cannot fix errors — a flipped bit caused by noise is passed up unchanged. Error **detection** begins at Layer 2 (CRC in Ethernet frames).

## Position in OSI Stack

```
Layer 7  Application
Layer 6  Presentation
Layer 5  Session
Layer 4  Transport
Layer 3  Network
Layer 2  Data Link
Layer 1  Physical   ← here (bits over wire/air/fiber)
```

## Related Concepts

- [[OSI Model]] — the 7-layer framework
- [[OSI Layer 2: Data Link]] — adds framing and error detection above Layer 1
- [[Parity Bit]] — simple error detection scheme for physical transmission
- [[CRC]] — stronger error detection used in Ethernet frames
