---
title: "Proxy"
type: concept
tags: [networking, proxy]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# Proxy (Forward Proxy)

A **forward proxy** (usually just called a "proxy") is a server that sits between clients and the internet, making requests on clients' behalf. The destination server sees the proxy's IP address, not the client's.

## Traffic Flow

```
Client ──→ Forward Proxy ──→ Internet / Target Server
  (private network)    ↑
                       Intercepts, filters, caches,
                       or anonymizes outbound requests
```

Compare with a [[Reverse Proxy]], which sits in front of servers and handles inbound traffic on their behalf.

## Use Cases

| Use Case | How Proxy Helps |
|----------|----------------|
| **Privacy / Anonymity** | Server sees proxy IP, not client IP |
| **Content filtering** | Corporate proxy blocks social media, malware domains |
| **Caching** | Frequently requested resources served from proxy cache, saving bandwidth |
| **Geo-bypassing** | Exit through a proxy in a different region |
| **Access control** | Enforce allowlist/denylist of external URLs |
| **Logging / DLP** | Inspect all outbound HTTP requests for data exfiltration |

## Explicit vs Transparent Proxy

| Type | Client configured? | Example |
|------|-------------------|---------|
| **Explicit** | Client configured with proxy address | Corporate HTTPS proxy; browser setting |
| **Transparent** | Client unaware; traffic intercepted at network level | ISP/school firewall interception |

## Forward Proxy vs VPN

| Feature | Forward Proxy | VPN |
|---------|--------------|-----|
| Scope | Usually application-level (HTTP/S) | All traffic (OS-level tunnel) |
| Encryption | Optional (CONNECT tunnel for HTTPS) | Always (tunnel encrypted) |
| Setup | Browser/app config | OS network setting |
| Latency | Lower | Higher (encryption overhead) |
| Use case | Corporate filtering, caching | Privacy, remote access |

## CONNECT Tunneling (HTTPS Proxies)

For HTTPS traffic, the client sends a `CONNECT` request to the proxy:
```
Client → Proxy: CONNECT example.com:443 HTTP/1.1
Proxy:          200 Connection Established
Client ←→ Proxy ←→ example.com  (encrypted tunnel; proxy can't inspect content)
```
The proxy acts as a raw TCP tunnel — it cannot decrypt or cache HTTPS content (without SSL inspection / MitM certificate).

## Related Concepts

- [[Reverse Proxy]] — handles inbound traffic for servers
- [[SSL Termination]] — reverse proxy variant that decrypts HTTPS
- [[API Gateway]] — a specialized reverse proxy for APIs
- [[CDN]] — a globally distributed forward+reverse caching proxy
