---
title: "HTTP"
type: concept
tags: [networking, http]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# HTTP

**HTTP** (HyperText Transfer Protocol) is a stateless, text-based application-layer protocol (OSI Layer 7).

## Characteristics

- **Port**: 80 (default)
- **Transport**: TCP
- **Stateless**: Each request independent
- **Client-Server**: Clients initiate requests

## Methods

- `GET` — Retrieve resource
- `POST` — Submit data
- `HEAD` — Headers only, no body

## Status Codes

- `200 OK` — Success
- `500 Internal Server Error` — Server failure
- `502 Bad Gateway` — Invalid upstream
- `503 Service Unavailable` — Temporary unavailability

## Evolution

- HTTP/1.1: Keep-Alive connection reuse
- HTTP/2: Multiplexing, header compression, server push
- HTTP/3: QUIC (UDP-based)

## Limitations

- No encryption (plain text)
- No server authentication
- No tamper detection

## Related Concepts

- [[HTTP and HTTPS]] — Parent concept
- [[HTTPS]] — HTTP over TLS
- [[TCP]] — Transport protocol