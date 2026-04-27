---
title: "Proxy vs Reverse Proxy"
type: source
tags: [system-design, networking, proxy]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# Proxy vs Reverse Proxy

A **proxy** acts on behalf of clients, while a **reverse proxy** acts on behalf of servers. Both sit between communicating parties but serve opposite purposes.

## Proxy (Forward Proxy)

Sits between client and internet, hiding client identity from servers.

- **Hides client IP** from destination servers
- Enables access control and content filtering
- Caches frequently accessed content
- Used for privacy and bypassing geo-restrictions

Client must be configured to use the proxy.

## Reverse Proxy

Sits in front of backend servers, hiding server infrastructure from clients.

- **Hides server IPs** from clients
- Load balancing across multiple servers
- SSL termination
- Caching static content
- DDoS protection, WAF

Client is typically unaware of the reverse proxy.

## Key Differences

| Aspect | Proxy | Reverse Proxy |
|--------|------|--------------|
| Acts on behalf of | Clients | Servers |
| Hides | Clients from servers | Servers from clients |
| Traffic direction | Outbound | Inbound |

## Common Tools

- **Nginx** — reverse proxy, load balancing
- **Cloudflare** — WAF, DDoS protection
- **HAProxy** — load balancer

## Related Concepts

- [[Load Balancing]] — distribute traffic
- [[SSL Termination]] — offload encryption
- [[WAF]] — Web Application Firewall

## Source

- AlgoMaster: [Proxy vs Reverse Proxy](https://blog.algomaster.io/p/proxy-vs-reverse-proxy-explained) (October 2024)