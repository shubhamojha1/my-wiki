---
title: "IP Address"
type: source
tags: [system-design, networking, ip-address]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# IP Address

An **IP address** (Internet Protocol address) is a numerical label assigned to each device connected to a computer network. It serves two functions: identification and location addressing.

## IPv4

- **32-bit** number (~4.3 billion addresses)
- **Dotted-decimal notation**: four octets 0-255 (e.g., 192.168.1.1)
- **Classful addressing** (historical): Class A (/8), B (/16), C (/24)

## Subnetting & CIDR

- **Subnet mask**: separates network/host portions
- **CIDR notation**: `address/prefix` (e.g., 192.168.1.0/24)
- **Usable hosts**: 2^(32-prefix) - 2 (network + broadcast addresses)

## Public vs Private

**Private** (RFC 1918):
- 10.0.0.0/8
- 172.16.0.0/12
- 192.168.0.0/16

**Public**: Globally routable, assigned by ISP

NAT maps private to public IPs for internet access.

## IPv6

- **128-bit** address space (~340 undecillion)
- **Hexadecimal** notation (e.g., 2001:db8::1)
- No NAT needed

## Special Addresses

- 127.0.0.1 — localhost/loopback
- 0.0.0.0 — default route/unspecified
- 169.254.0.0/16 — link-local (APIPA)
- ::1 — IPv6 loopback

## Routing

Device checks if destination is on local subnet via AND operation. If yes, sends directly; if not, forwards to default gateway (router).

## Related Concepts

- [[OSI Layer 3: Network]] — Layer using IP addresses
- [[CIDR Notation]] — Classless subnet notation
- [[NAT]] — Network Address Translation
- [[Subnet Mask]] — Network/host division

## Source

- AlgoMaster.io: [IP Address](https://algomaster.io/learn/system-design/ip-address) (March 15, 2026)