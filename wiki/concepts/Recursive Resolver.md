---
title: "Recursive Resolver"
type: concept
tags: [dns, networking]
created: 2026-04-28
sources: ["algomaster-dns"]
---

# Recursive Resolver

A **recursive resolver** (also called DNS resolver) is a server that handles DNS queries on behalf of clients, traversing the DNS hierarchy to find the final IP address.

## How It Works

1. Client sends query to recursive resolver
2. Resolver checks its cache
3. If not cached, resolver queries:
   - Root server → TLD server → Authoritative server
4. Returns IP to client
5. Caches result for future queries

## Common Public Resolvers

| Provider | IP Address |
|----------|------------|
| Google | 8.8.8.8, 8.8.4.4 |
| Cloudflare | 1.1.1.1, 1.0.0.1 |
| OpenDNS | 208.67.222.222 |

## Caching

Recursive resolvers cache DNS responses to reduce latency and load on upstream servers.

## Related Concepts

- [[DNS]] — Parent concept
- [[Authoritative Name Server]] — Final DNS server
- [[DNS Caching]] — Cached DNS responses