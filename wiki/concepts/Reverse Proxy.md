---
title: "Reverse Proxy"
type: concept
tags: [networking, proxy]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# Reverse Proxy

A **reverse proxy** sits in front of backend servers and regulates incoming traffic. Think of it as a **gatekeeper** that hides server infrastructure from clients and creates a single controlled entry point.

## How It Works

1. Client sends request to website
2. Reverse proxy receives request first
3. Proxy forwards to appropriate backend server
4. Backend processes and returns to proxy
5. Proxy relays response to client

## Benefits

- **Security**: Hides server IPs and infrastructure — mitigates risks from hackers and DDoS attacks
- **Load Balancing**: Distributes across multiple servers (round-robin, ip_hash, least_conn)
- **SSL Termination**: Handles encryption, offloading backend servers
- **Caching**: Static content (images, CSS, JS) at the edge
- **DDoS Protection**: Filters malicious traffic before it reaches origin

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

### Load Balancing

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

Round-robin is the default. Other algorithms include `ip_hash` (session stickiness) and `least_conn`.

## Common Tools

- **Nginx**: Popular reverse proxy
- **Cloudflare**: WAF, DDoS protection
- **HAProxy**: Load balancer

## Related Concepts

- [[Proxy vs Reverse Proxy]] — Parent concept
- [[Proxy]] — Forward proxy (opposite)
- [[Load Balancing]] — Distributes traffic
- [[SSL Termination]] — Offloads encryption