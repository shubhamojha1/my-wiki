---
title: "IPv4"
type: concept
tags: [ip-address, networking, ipv4]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# IPv4

**IPv4** (Internet Protocol version 4) is the fourth version of the Internet Protocol and the first widely deployed version.

## Specifications

- **Address size**: 32 bits
- **Total addresses**: ~4.3 billion (2^32)
- **Notation**: Dotted-decimal (e.g., 192.168.1.1)

## Dotted-Decimal Notation

IPv4 addresses are written as four octets (8-bit groups), separated by dots:

```
192.168.1.1
|____| |____| |____| |____|
  octet1 octet2 octet3 octet4
   (0-255) (0-255) (0-255) (0-255)
```

Example binary: 11000000.10101000.00000001.00000001

## Classful Addressing (Historical)

| Class | First Octet | Default Mask | Networks |
|-------|-----------|------------|----------|
| A | 1-126 | /8 | 128 |
| B | 128-191 | /16 | 16,384 |
| C | 192-223 | /24 | ~2 million |

Class D (224-239): Multicast
Class E (240-255): Experimental

Replaced by CIDR in 1993 due to address exhaustion.

## Related Concepts

- [[IP Address]] — Parent concept
- [[IPv6]] — Successor
- [[CIDR Notation]] — Modern subnet notation
- [[Subnet Mask]] — Network/host division