---
title: "Public IP Address"
type: concept
tags: [ip-address, networking, public]
created: 2026-04-28
sources: ["algomaster-ip-address"]
---

# Public IP Address

**Public IP addresses** are globally unique IP addresses that are routable on the internet.

## Characteristics

- Assigned by ISP or Regional Internet Registry (RIR)
- Globally unique
- Routable on the internet
- Costs money

## Examples

- 8.8.8.8 (Google DNS)
- 203.0.113.1 (TEST-NET-3, documentation)
- 1.1.1.1 (Cloudflare DNS)

## Getting a Public IP

1. **From ISP**: Most common for home/business users
2. **From cloud provider**: AWS, GCP, Azure allocate public IPs
3. **From RIR**: ARIN, RIPE, APNIC (rare for end users)

## Related Concepts

- [[IP Address]] — Parent concept
- [[Private IP Address]] — Not internet-routable
- [[NAT]] — Maps private to public IPs