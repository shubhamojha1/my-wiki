---
title: "Reverse Proxy"
type: concept
tags: [networking, proxy]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# Reverse Proxy

A **reverse proxy** sits in front of backend servers and regulates incoming traffic, hiding server infrastructure from clients.

## How It Works

1. Client sends request to website
2. Reverse proxy receives request first
3. Proxy forwards to appropriate backend server
4. Backend processes and returns to proxy
5. Proxy relays response to client

## Benefits

- **Security**: Hides server IPs and infrastructure
- **Load Balancing**: Distributes across multiple servers
- **SSL Termination**: Handles encryption
- **Caching**: Static content at the edge
- **DDoS Protection**: Filters malicious traffic

## Common Tools

- **Nginx**: Popular reverse proxy
- **Cloudflare**: WAF, DDoS protection
- **HAProxy**: Load balancer

## Related Concepts

- [[Proxy vs Reverse Proxy]] — Parent concept
- [[Proxy]] — Forward proxy (opposite)
- [[Load Balancing]] — Distributes traffic
- [[SSL Termination]] — Offloads encryption