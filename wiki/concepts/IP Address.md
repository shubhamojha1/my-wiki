---
title: "IP Address"
type: concept
tags: [networking, ip-address]
created: 2026-05-10
sources: ["algomaster-ip-address"]
---

# IP Address

An **IP address** (Internet Protocol address) is a unique numerical label assigned to each device connected to a network using IP for communication.

## Two Functions

1. **Identification**: Uniquely identifies a network interface on the network
2. **Location Addressing**: Specifies the device's location in the network, providing a path for data delivery

## Address Structure

Every IP address splits into two parts:

- **Network ID**: Identifies the specific network the device is on. All devices on the same local network share the same Network ID.
- **Host ID**: Identifies a specific device within that network.

Example (`192.168.1.10` with subnet mask `255.255.255.0`):
- Network ID: `192.168.1`
- Host ID: `10`

Routers primarily use the Network ID to forward packets, avoiding the need to know every device in the world.

## Analogy: Postal System

An IP address is like a home address. The street and city identify the neighborhood (network), while the house number identifies the specific home (device). Routers act as mail carriers, delivering data packets to the correct location.

## Two Versions

- [[IPv4]] — 32-bit, ~4.3 billion addresses, dotted-decimal notation
- [[IPv6]] — 128-bit, ~340 undecillion addresses, hexadecimal notation

## Related Concepts

- [[OSI Layer 3: Network]] — The layer where IP operates
- [[IPv4]] — Current dominant version
- [[IPv6]] — Successor addressing scheme
- [[CIDR Notation]] — Modern subnet notation
- [[Subnet Mask]] — Separates network/host portions
- [[NAT]] — Maps private addresses to public
- [[Public IP Address]] — Globally routable
- [[Private IP Address]] — Local-only, non-routable
