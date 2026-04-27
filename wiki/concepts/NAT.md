---
title: "NAT"
type: concept
tags: [networking, nat]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# NAT

**NAT** (Network Address Translation) is a method of mapping private IP addresses to public IPs, enabling multiple devices to share a single public IP.

## Problem Solved

IPv4 has only ~4.3 billion addresses. Private networks use non-routable addresses (RFC 1918) that cannot communicate directly with the internet.

## How NAT Works

1. Device with private IP (e.g., 192.168.1.10) sends packet to internet
2. NAT device (router) replaces private source IP with public IP
3. NAT tracks the mapping in a table
4. Response comes back to public IP
5. NAT looks up mapping and forwards to original private IP

## NAT Types

- **Static NAT**: One-to-one mapping (expensive, requires public IPs for each device)
- **Dynamic NAT**: Pool of public IPs assigned as needed
- **PAT** (Port Address Translation): Many-to-one using ports (most common)

## NAT and IPv6

IPv6's massive address space (~340 undecillion) eliminates the need for NAT. Each device can have a unique global IP.

## Related Concepts

- [[IP Address]] — Parent concept
- [[Private IP Address]] — Addresses that require NAT
- [[Public IP Address]] — Internet-routable addresses
- [[IPv6]] — Makes NAT unnecessary