---
title: "Multicast Address"
type: concept
tags: [networking, ip-address, multicast]
created: 2026-05-10
sources: ["algomaster-ip-address"]
---

# Multicast Address

**Multicast** is a one-to-many communication pattern where a single packet is sent to a "group" of interested receivers, rather than to all devices (broadcast) or one device (unicast).

## IPv4 Multicast

- **Class D** addresses: `224.0.0.0` to `239.255.255.255`
- Devices join a multicast group to receive traffic
- Examples: `224.0.0.1` (all hosts on subnet), `224.0.0.9` (RIP routers)

## IPv6 Multicast

IPv6 uses multicast **instead of broadcast**, making it more efficient:
- `ff00::/8` — multicast prefix
- Only devices that have joined the group process the message
- Used for neighbor discovery, router advertisements, and more

## Comparison

| Method | Receivers | Efficiency |
|--------|-----------|------------|
| Unicast | One | Point-to-point |
| Multicast | Group | Targeted group delivery |
| Broadcast | All on subnet | Wastes resources on uninterested devices |

## Related Concepts

- [[IP Address]] — Parent concept
- [[Broadcast Address]] — Less efficient alternative
- [[IPv6]] — Relies on multicast instead of broadcast
