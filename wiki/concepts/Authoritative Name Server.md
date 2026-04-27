---
title: "Authoritative Name Server"
type: concept
tags: [dns, networking]
created: 2026-04-28
sources: ["algomaster-dns"]
---

# Authoritative Name Server

An **authoritative name server** is the DNS server that holds the official DNS records for a domain and provides the final answer to DNS queries.

## Characteristics

- Has the **source of truth** for a domain
- Returns actual IP addresses (A/AAAA records)
- Can return multiple IPs for load balancing
- Usually multiple servers for redundancy

## Types

- **Primary (Master)** — zone file is edited directly
- **Secondary (Slave)** — receives transfers from primary

## High Availability

- Domains typically have multiple authoritative servers
- Spread across different regions
- If one fails, another responds

## Related Concepts

- [[DNS]] — Parent concept
- [[DNS Record]] — Records stored on this server
- [[Recursive Resolver]] — Queries this server