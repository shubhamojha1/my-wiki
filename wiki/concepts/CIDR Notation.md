---
title: "CIDR Notation"
type: concept
tags: [ip-address, networking, cidr]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# CIDR Notation

**CIDR** (Classless Inter-Domain Routing) notation is a method of representing IP addresses and their associated network prefix.

## Format

```
IP address/prefix length
192.168.1.0/24
```

The prefix length = number of bits for the network portion.

## Common Prefixes

| CIDR | Subnet Mask | Total | Usable Hosts |
|------|-------------|-------|---------------|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 2 |

## Formula

Usable hosts = 2^(32 - prefix) - 2

The minus 2 accounts for:
- **Network address**: all host bits = 0
- **Broadcast address**: all host bits = 1

## Why CIDR?

Replaced classful addressing (A/B/C) in 1993 to:
- Allocate address space more efficiently
- Enable variable-length subnet masking (VLSM)
- Reduce routing table size via route aggregation

## Related Concepts

- [[IP Address]] — Parent concept
- [[Subnet Mask]] — Binary mask for network/host
- [[IPv4]] — Where CIDR is commonly used