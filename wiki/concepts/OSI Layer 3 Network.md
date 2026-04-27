---
title: "OSI Layer 3: Network"
type: concept
tags: [osi-model, networking, layer-3]
created: 2026-04-28
sources: ["algomaster-osi-model"]
---

# OSI Layer 3: Network

**Layer 3** of the OSI model routes data across multiple networks to reach destinations.

## Responsibility

- Route data across multiple networks
- Assign logical IP addresses
- Fragment oversized packets
- Select optimal paths

## Key Details

- Uses **IP addresses** (logical, can change) for cross-network routing
- Critical distinction: MAC addresses are permanent hardware (Layer 2, local); IP addresses are logical (Layer 3, cross-network)
- Both MAC and IP are required for end-to-end communication

## Key Device

- **Router**: Reads destination IP address and forwards packets hop-by-hop toward the destination

## Protocols

- IP (IPv4/IPv6)
- ICMP (error reporting, ping)
- ARP (maps IP addresses to MAC addresses)
- OSPF, BGP (routing protocols)

## Related Concepts

- [[OSI Model]] — The 7-layer framework this layer belongs to
- [[IP Address]] — Layer 3 logical address
- [[OSI Layer 2: Data Link]] — The layer below
- [[OSI Layer 4: Transport]] — The layer above