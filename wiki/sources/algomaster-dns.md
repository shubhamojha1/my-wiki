---
title: "DNS"
type: source
tags: [system-design, networking, dns]
created: 2026-04-28
sources: ["algomaster-dns"]
---

# DNS

**DNS (Domain Name System)** is a distributed directory system that translates human-readable domain names to machine-friendly IP addresses. Often called the "phonebook of the internet."

## How Resolution Works

1. **Browser Cache** — Check local cache first
2. **OS Cache** — Check operating system cache
3. **Recursive Resolver** — ISP DNS (8.8.8.8 Google, 1.1.1.1 Cloudflare)
4. **Root Server** — Directs to TLD server
5. **TLD Server** — Manages .com, .org, etc.
6. **Authoritative Name Server** — Returns final IP

The process happens in milliseconds.

## DNS Hierarchy

- **Root Servers** — 13 sets globally, direct to TLD
- **TLD Servers** — Manage extensions (.com, .org)
- **Authoritative Name Servers** — Source of truth for domains

## Record Types

- **A** — Domain to IPv4
- **AAAA** — Domain to IPv6
- **CNAME** — Alias to another domain
- **MX** — Email routing
- **TXT** — Verification

## Caching

Cached at multiple levels: browser, OS, and recursive resolver.

## Related Concepts

- [[DNS Record]] — Individual DNS record types
- [[Recursive Resolver]] — DNS query resolver
- [[Authoritative Name Server]] — Domain's official DNS server

## Source

- AlgoMaster: [How DNS Actually Works](https://blog.algomaster.io/p/how-dns-actually-works) (September 2025)