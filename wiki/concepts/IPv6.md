---
title: "IPv6"
type: concept
tags: [ip-address, networking, ipv6]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# IPv6

**IPv6** (Internet Protocol version 6) is the successor to IPv4, developed to address IPv4 address exhaustion.

## Specifications

- **Address size**: 128 bits
- **Address space**: ~340 undecillion (2^128)
- **Notation**: Hexadecimal with colons

## Address Format

Eight groups of 4 hex digits separated by colons:

```
2001:0db8:85a3:0000:0000:8a2e:0370:7334
```

## Shortened Forms

- Leading zeros can be dropped: `2001:db8:85a3:0:0:8a2e:370:7334`
- Consecutive zeros replaced with `::`: `2001:db8:85a3::8a2e:370:7334`

## Key Differences from IPv4

- Larger address space (no NAT needed)
- No broadcast (multicast instead)
- Simplified header
- Built-in security (IPsec)

## Special Addresses

- `::1` — loopback (equivalent to 127.0.0.1)
- `::` — unspecified (equivalent to 0.0.0.0)
- `fe80::/10` — link-local
- `2001:db8::/32` — documentation prefix

## CIDR Notation

- `/48` — typically organizations
- `/64` — standard for subnets (SLAAC)
- `/128` — single host

## Related Concepts

- [[IP Address]] — Parent concept
- [[IPv4]] — Predecessor
- [[NAT]] — Not needed with IPv6