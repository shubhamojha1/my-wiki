---
title: "SSL Termination"
type: concept
tags: [networking, ssl, security]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# SSL Termination

**SSL termination** is the process of handling SSL/TLS encryption and decryption at a reverse proxy, instead of at the backend servers.

## How It Works

1. Client sends HTTPS request to reverse proxy
2. Proxy decrypts the request (terminates SSL)
3. Proxy forwards unencrypted request to backend
4. Backend processes request
5. Proxy encrypts response and sends back to client

## Benefits

- **Offloads work** from backend servers
- **Simplifies backend** code (no SSL needed)
- **Centralized** certificate management
- **Improved performance** for backends

## Related Concepts

- [[Reverse Proxy]] — Where termination happens
- [[TLS]] — Transport Layer Security
- [[HTTPS]] — HTTP over TLS