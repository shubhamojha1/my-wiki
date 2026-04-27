---
title: "DNS Record"
type: concept
tags: [dns, networking]
created: 2026-04-28
sources: ["algomaster-dns"]
---

# DNS Record

**DNS records** are entries stored on authoritative name servers that map domain names to specific information.

## Record Types

### A Record
- Maps domain to **IPv4 address**
- Example: `google.com → 142.250.183.100`

### AAAA Record
- Maps domain to **IPv6 address**
- Example: `google.com → 2001:4860:4860::8844`

### CNAME Record
- **Canonical name** (alias)
- Maps one domain name to another
- Example: `www.google.com → google.com`

### MX Record
- **Mail Exchange**
- Specifies mail servers for email routing
- Example: `google.com → mx.google.com`

### TXT Record
- Text records for verification
- Used for SPF, DKIM, DMARC

## Related Concepts

- [[DNS]] — Parent concept
- [[Authoritative Name Server]] — Where DNS records are stored
- [[IP Address]] — What A/AAAA records map to