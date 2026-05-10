---
title: "Proxy vs Reverse Proxy"
type: source
tags: [system-design, networking, proxy]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# Proxy vs Reverse Proxy

A **proxy** acts on behalf of clients (a "middleman" between private network and internet), while a **reverse proxy** acts on behalf of servers (a "gatekeeper" in front of backend infrastructure). Both sit between communicating parties but serve opposite purposes.

## Proxy (Forward Proxy)

Sits between client and internet, hiding client identity from servers.

- **Hides client IP** from destination servers
- Enables access control and content filtering
- Caches frequently accessed content with **TTL-based expiration** — stale content auto-expires
- Used for privacy and bypassing geo-restrictions (e.g., accessing US Netflix from another country)
- **VPN vs Proxy**: VPN encrypts all traffic; proxy forwards specific requests without encryption

Client must be configured to use the proxy.

## Reverse Proxy

Sits in front of backend servers, hiding server infrastructure from clients.

- **Hides server IPs** from clients — mitigates risks from hackers and DDoS attacks
- Load balancing across multiple servers (round-robin, ip_hash, least connections)
- SSL termination — offloads encryption from backend servers
- Caching static content (images, CSS, JS) at the edge
- DDoS protection, WAF — filters malicious traffic before it reaches origin

Client is typically unaware of the reverse proxy.

## Nginx Configuration

### Basic Reverse Proxy

```nginx
server {
    listen 80;
    location / {
        proxy_pass http://backend_server_ip;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Load Balancing (Upstream)

```nginx
upstream backend_servers {
    ip_hash;
    server backend1.example.com;
    server backend2.example.com;
    server backend3.example.com;
}

server {
    listen 80;
    server_name example.com;
    location / {
        proxy_pass http://backend_servers;
    }
}
```

Round-robin is the default. Other algorithms include `ip_hash`, `least_conn`.

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