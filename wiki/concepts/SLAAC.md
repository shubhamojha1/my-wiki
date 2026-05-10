---
title: "SLAAC"
type: concept
tags: [networking, ipv6, autoconfiguration]
created: 2026-05-10
sources: ["algomaster-ip-address"]
---

# SLAAC

**SLAAC** (Stateless Address Autoconfiguration) allows IPv6 devices to generate their own IP address without needing a DHCP server.

## How It Works

1. Device sends a **Router Solicitation** (RS) message
2. Router responds with a **Router Advertisement** (RA) containing the network prefix (e.g., `/64`)
3. Device combines the prefix with a self-generated interface identifier (typically derived from its MAC address via EUI-64, or randomly generated for privacy)
4. Device performs **Duplicate Address Detection** (DAD) to ensure the address is unique

## Key Benefits

- Zero configuration required — plug-and-play networking
- No DHCP server needed for address assignment
- Each device generates a globally unique address

## Related Concepts

- [[IPv6]] — Where SLAAC operates
- [[Static vs Dynamic IP]] — SLAAC as an alternative to DHCP
- [[MAC Address]] — Often used as basis for the interface identifier
