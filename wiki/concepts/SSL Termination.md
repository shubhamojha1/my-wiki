---
title: "SSL Termination"
type: concept
tags: [networking, ssl, security]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# SSL Termination

**SSL termination** (more precisely TLS termination) decrypts HTTPS traffic at the edge — a load balancer, reverse proxy, or API gateway — so backend servers communicate over plain HTTP within the trusted internal network.

## Traffic Flow

```
Client ──[HTTPS]──→ Reverse Proxy ──[HTTP]──→ Backend
           ↑ TLS handshake + decrypt             ↑ plain TCP
           certificates live here                no certs needed
```

## Benefits

| Benefit | Detail |
|---------|--------|
| **CPU offload** | TLS handshakes are expensive; dedicated hardware (SSL accelerator cards) or load balancers handle them |
| **Centralized certs** | One certificate renewal point instead of every backend server |
| **Simplified backends** | Services written without TLS boilerplate; easier local testing |
| **Inspection** | WAF, rate limiting, logging see plaintext before forwarding |

## Security Consideration: mTLS Re-encryption

Terminating at the proxy means the backend leg is unencrypted. In high-security environments the proxy **re-encrypts** the request before forwarding to the backend (**SSL bridging** or **end-to-end TLS**). Alternatively, backends use **mutual TLS (mTLS)** with the proxy.

| Mode | Backend Link | Use Case |
|------|-------------|---------|
| **Termination** | Plain HTTP | Trusted internal network |
| **Bridging** | Re-encrypted HTTPS | Compliance, zero-trust |
| **Pass-through** | Encrypted (proxy is transparent) | End-to-end encryption required |

## Session Persistence

Because TLS session state (session tickets, session IDs) is maintained at the terminating proxy, sticky sessions are easier to manage — the same proxy node handles session resumption without coordination.

## Related Concepts

- [[TLS]] — the protocol being terminated
- [[HTTPS]] — HTTP over TLS
- [[Reverse Proxy]] — where termination typically occurs
- [[API Gateway]] — another common termination point
- [[mTLS]] — mutual authentication alternative
