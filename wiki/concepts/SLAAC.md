---
title: "SLAAC"
type: concept
tags: [networking, ipv6, autoconfiguration]
created: 2026-05-10
updated: 2026-05-20
sources: ["algomaster-ip-address"]
---

# SLAAC (Stateless Address Autoconfiguration)

**SLAAC** lets IPv6 devices configure their own global unicast address without a DHCP server. The router provides only the network prefix; the device generates the host portion itself.

## How It Works

```
Device                        Router
  |                             |
  |── Router Solicitation ──→   |   (ICMPv6 type 133, multicast)
  |                             |
  |←── Router Advertisement ── |   (ICMPv6 type 134, prefix + lifetime)
  |                             |
  [Device constructs address]
  prefix (64 bits) + interface ID (64 bits)
  |
  [DAD: Neighbor Solicitation to tentative address]
  → if no reply after timeout → address is unique → use it
```

## Interface Identifier Generation

| Method | Description | Privacy |
|--------|-------------|---------|
| **EUI-64** | Derived from 48-bit MAC (insert `FF:FE` in middle, flip bit 6) | Low — stable, trackable |
| **RFC 7217 Stable** | Pseudo-random, host-specific, stable per network | Medium |
| **Temporary (RFC 4941)** | Random, rotated periodically | High — default on modern OSes |

## Duplicate Address Detection (DAD)

Before using the address, the device sends a Neighbor Solicitation for the tentative address. If another host replies (Neighbor Advertisement), there is a collision and the device must generate a new interface ID. DAD typically resolves within ~1 second.

## SLAAC vs. DHCPv6

| Feature | SLAAC | DHCPv6 |
|---------|-------|--------|
| Server required | No | Yes |
| Address assignment | Self-generated | Server-assigned |
| DNS configuration | Via RA (RDNSS option, RFC 8106) | Via DHCP options |
| Logging/tracking | Harder | Centralized |
| Control | Low | High |

Most networks use **SLAAC + RDNSS** for plug-and-play, or **Managed mode** (DHCPv6) when address control matters.

## Related Concepts

- [[IPv6]] — the address space SLAAC operates within
- [[MAC Address]] — basis for EUI-64 interface identifiers
- [[ICMPv6]] — the protocol carrying Router Solicitation/Advertisement
