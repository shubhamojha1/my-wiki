---
title: "HTTPS"
type: concept
tags: [networking, https, security]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# HTTPS

**HTTPS** (HTTP Secure) is HTTP layered on top of SSL/TLS, defaulting to port 443.

## Guarantees

- **Encryption**: All data unreadable to interceptors
- **Authentication**: Server identity verified via CA certificates
- **Integrity**: Data cannot be modified without detection

## TLS Handshake

1. **Client Hello**: TLS versions, cipher suites, random number
2. **Server Hello**: Selected cipher, certificate, random number
3. **Certificate Verification**: Validate CA-issued certificate
4. **Key Exchange**: Derive symmetric session keys
5. **Secure Communication**: Encrypted with session keys

## TLS 1.3 Optimization

0-RTT (Zero Round Trip Time) for repeat connections eliminates handshake latency.

## PKI

**Public Key Infrastructure (PKI)** is the foundation of HTTPS. It uses public/private key pairs along with digital certificates issued by trusted **Certificate Authorities (CAs)** to establish secure connections.

## HTTP vs HTTPS Comparison

| Feature | HTTP | HTTPS |
|---------|------|-------|
| Security | Unencrypted, plain text | Encrypted via SSL/TLS |
| Port | 80 | 443 |
| Performance | Slightly faster | Negligible overhead (TLS 1.3) |
| Authentication | None | Server via CA certificates |
| Data Integrity | No guarantee | Tamper-proof |
| SEO & Trust | Lower ranking, "Not Secure" warning | Preferred, padlock icon |
| Use Case | Local dev, internal | All production traffic |

## Related Concepts

- [[HTTP]] — Plaintext version
- [[TLS]] — Encryption protocol
- [[SSL Termination]] — Offloading encryption