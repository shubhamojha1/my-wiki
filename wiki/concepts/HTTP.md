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

| Method | Use Case | Idempotent? |
|--------|---------|-------------|
| `GET` | Retrieve resource | Yes |
| `POST` | Submit new data, create resources | No |
| `PUT` | Update/replace existing resource | Yes |
| `DELETE` | Remove a resource | Yes |
| `PATCH` | Apply partial modifications | No |
| `HEAD` | Get headers only (no body) | Yes |

**Idempotency**: An operation safe to retry multiple times without side effects beyond the first. Critical for retry logic in distributed systems — `POST` and `PATCH` need idempotency keys.

## Status Codes

- **1xx (Informational)**: Request received, continuing
- **2xx (Success)**:
  - `200 OK` — Success
  - `201 Created` — Resource created
- **3xx (Redirection)**:
  - `301 Moved Permanently`
  - `302 Found` — Temporary redirect
- **4xx (Client Error)**:
  - `400 Bad Request` — Invalid syntax
  - `401 Unauthorized` — Authentication required
  - `403 Forbidden` — Server refuses to authorize
  - `404 Not Found`
- **5xx (Server Error)**:
  - `500 Internal Server Error` — Generic server failure
  - `502 Bad Gateway` — Invalid upstream
  - `503 Service Unavailable` — Temporary unavailability

## Statelessness Tradeoffs

- **Pro**: Easy to scale — any server can handle any request
- **Con**: State management requires cookies, session IDs, or JWTs at the application level

## Security Risks (Plain HTTP)

- **Eavesdropping**: Passwords, credit cards stolen on insecure networks
- **Man-in-the-Middle (MITM)**: Attacker intercepts, impersonates, alters communication
- **Injection Attacks**: Malicious code injected into unencrypted traffic

## Evolution

- HTTP/1.1: Keep-Alive connection reuse
- HTTP/2: Multiplexing, header compression, server push
- HTTP/3: QUIC (UDP-based)

## Related Concepts

- [[HTTP and HTTPS]] — Parent concept
- [[HTTPS]] — HTTP over TLS
- [[TCP]] — Transport protocol