---
title: "HTTP and HTTPS"
type: source
tags: [system-design, networking, http, https]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# HTTP and HTTPS

**HTTP** (HyperText Transfer Protocol) is a stateless, text-based application-layer protocol (OSI Layer 7).

## HTTP Basics

- **Port**: 80
- **Transport**: TCP (reliable, ordered)
- **Stateless**: Each request is independent — easy scaling but requires cookies/JWTs for state

### Methods

| Method | Use Case | Idempotent |
|--------|---------|------------|
| GET | Retrieve resource | Yes |
| POST | Submit data, create | No |
| PUT | Update/replace | Yes |
| DELETE | Remove | Yes |
| PATCH | Partial modify | No |
| HEAD | Headers only | Yes |

### Status Codes

- **1xx**: Informational
- **2xx**: 200 OK, 201 Created
- **3xx**: 301 Moved Permanently, 302 Found
- **4xx**: 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found
- **5xx**: 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable

## HTTP Evolution

- **HTTP/1.1** (1997): Keep-Alive for connection reuse; still suffered from head-of-line blocking (sequential requests per connection)
- **HTTP/2** (2015): Binary framing, multiplexing (eliminates HoL), header compression (HPACK), server push. Major impact on API and microservice design.
- **HTTP/3** (2018): Runs over UDP (QUIC), eliminates TCP-level HoL blocking, 0-RTT repeat connections, connection migration (Wi-Fi → cellular). Adopted by Google, YouTube, Cloudflare.

## HTTP Limitations (Unencrypted)

Data sent in plain text. Specific attack vectors:
- **Eavesdropping**: Passwords, credit cards visible on insecure networks
- **Man-in-the-Middle (MITM)**: Attacker intercepts and alters communication
- **Injection Attacks**: Malicious code injected into traffic

## HTTPS

HTTP layered on **SSL/TLS**, default **port 443**.

### Guarantees

- **Encryption**: All data encrypted
- **Authentication**: Server identity verified via CA certificates (PKI)
- **Integrity**: Tamper detection

### TLS Handshake

1. Client Hello: sends TLS versions, cipher suites, random number
2. Server Hello: selected cipher, certificate, random number
3. Certificate Verification: validate CA-issued certificate
4. Key Exchange: derive symmetric session keys
5. Secure Communication: encrypted with session keys

TLS 1.3 enables **0-RTT** for repeat connections.

### HTTP vs HTTPS

| Feature | HTTP | HTTPS |
|---------|------|-------|
| Security | Plain text | Encrypted |
| Port | 80 | 443 |
| Authentication | None | CA certificates |
| Integrity | None | Tamper-proof |
| SEO | Lower rank, "Not Secure" | Preferred, padlock |
| Use case | Local dev | Production

## Related Concepts

- [[TLS]] — Encryption protocol
- [[HTTPS]] — HTTP over TLS
- [[HTTP/2]] — HTTP version 2
- [[HTTP/3]] — HTTP version 3 over QUIC

## Source

- AlgoMaster.io: [HTTP and HTTPS](https://algomaster.io/learn/system-design/http-https) (October 6, 2025)