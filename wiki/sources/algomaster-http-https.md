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
- **Stateless**: Each request is independent

### Methods

- `GET` — Retrieve resource
- `POST` — Submit data
- `HEAD` — Headers only

### Status Codes

- `200 OK` — Success
- `500 Internal Server Error` — Server failure
- `502 Bad Gateway` — Invalid upstream
- `503 Service Unavailable` — Temporary unavailability

## HTTP Evolution

- **HTTP/1.1** (1997): Keep-Alive for connection reuse
- **HTTP/2** (2015): Binary framing, multiplexing, header compression, server push
- **HTTP/3** (2018): Runs over UDP (QUIC), eliminates head-of-line blocking

## HTTPS

HTTP layered on **SSL/TLS**, default **port 443**.

### Guarantees

- **Encryption**: All data encrypted
- **Authentication**: Server identity verified via CA certificates
- **Integrity**: Tamper detection

### TLS Handshake

1. Client Hello: sends TLS versions, cipher suites, random number
2. Server Hello: selected cipher, certificate, random number
3. Certificate Verification: validate CA-issued certificate
4. Key Exchange: derive symmetric session keys
5. Secure Communication: encrypted with session keys

## Related Concepts

- [[TLS]] — Encryption protocol
- [[HTTPS]] — HTTP over TLS
- [[HTTP/2]] — HTTP version 2
- [[HTTP/3]] — HTTP version 3 over QUIC

## Source

- AlgoMaster.io: [HTTP and HTTPS](https://algomaster.io/learn/system-design/http-https) (October 6, 2025)