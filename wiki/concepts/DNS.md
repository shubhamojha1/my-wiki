---
title: "DNS"
type: concept
tags: [networking, dns]
created: 2026-05-10
sources: ["algomaster-dns"]
---

# DNS

The **Domain Name System (DNS)** translates human-readable domain names into machine-friendly IP addresses. Often called the "phonebook of the internet."

## Resolution Hierarchy

DNS queries traverse a hierarchy of servers to resolve a domain:

1. **Browser Cache** — Fastest check; browser stores recent lookups
2. **OS Cache** — System-wide cache shared across applications
3. **Recursive Resolver** — ISP or public resolver (8.8.8.8, 1.1.1.1) that does the hunting
4. **Root Server** — 13 sets globally; directs to the correct TLD server
5. **TLD Server** — Manages .com, .org, .gov, etc.; points to authoritative server
6. **Authoritative Name Server** — Source of truth; returns final IP address

All this happens in milliseconds.

## Key Components

- [[Recursive Resolver]] — Client-facing server that traverses the hierarchy
- [[Root Server]] — Top of the DNS hierarchy
- [[TLD Server]] — Manages domain extensions
- [[Authoritative Name Server]] — Official record-keeper for a domain
- [[DNS Record]] — Individual records (A, AAAA, CNAME, MX, TXT)

## Performance Mechanisms

- [[DNS Caching]] — Multi-level caching (browser, OS, resolver)
- [[Anycast]] — Global routing to nearest server
- [[GeoDNS]] — Geographic-based responses for latency reduction
- [[CDN]] — DNS resolves to edge servers near the user

## Related Concepts

- [[IP Address]] — What DNS resolves domain names to
- [[OSI Layer 7: Application]] — DNS operates at the application layer
