---
title: "Private IP Address"
type: concept
tags: [ip-address, networking, private]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# Private IP Address

**Private IP addresses** are IP addresses reserved for use within private networks, not routable on the internet.

## RFC 1918 Ranges

| Range | Example | CIDR |
|-------|---------|-----|
| 10.0.0.0 - 10.255.255.255 | 10.x.x.x | 10.0.0.0/8 |
| 172.16.0.0 - 172.31.255.255 | 172.16.x.x - 172.31.x.x | 172.16.0.0/12 |
| 192.168.0.0 - 192.168.255.255 | 192.168.x.x | 192.168.0.0/16 |

## Characteristics

- Only valid within local network (LAN)
- Not routable on the internet
- Reusable in different networks
- Require NAT to communicate with internet

## Common Use Cases

- Home networks (typically 192.168.1.x)
- Enterprise networks (often 10.x.x.x)
- Data centers

## Related Concepts

- [[IP Address]] — Parent concept
- [[Public IP Address]] — Internet-routable
- [[NAT]] — Enables internet access from private IPs