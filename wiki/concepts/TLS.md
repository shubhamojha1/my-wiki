---
title: "TLS"
type: concept
tags: [security, networking, tls]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-http-https"]
---

# TLS (Transport Layer Security)

**TLS** is a cryptographic protocol that provides confidentiality, integrity, and authentication for data in transit. It is the successor to SSL (Secure Sockets Layer) and the foundation of HTTPS, gRPC, SMTP with STARTTLS, and many other protocols.

## What TLS Provides

| Property | Mechanism | Guarantee |
|----------|-----------|-----------|
| **Confidentiality** | Symmetric encryption (AES-GCM, ChaCha20) | Data cannot be read in transit |
| **Integrity** | HMAC / AEAD (Authenticated Encryption) | Tampering detected |
| **Authentication** | X.509 certificates + PKI | Server (and optionally client) identity verified |
| **Forward Secrecy** | Ephemeral key exchange (ECDHE) | Past sessions safe if long-term key is compromised |

## TLS 1.2 Handshake (2 RTT)

```
Client                                Server
  │──── ClientHello (cipher suites) ──→│
  │←─── ServerHello + Certificate ─────│
  │←─── ServerHelloDone ───────────────│
  │── ClientKeyExchange (pre-master) →─│
  │── ChangeCipherSpec + Finished ────→│
  │←── ChangeCipherSpec + Finished ────│
  │═══════ Encrypted data ════════════│
```

Total: 2 round trips before data can flow.

## TLS 1.3 Handshake (1 RTT, or 0-RTT resumption)

TLS 1.3 (RFC 8446, 2018) removed obsolete features and streamlined the handshake:

```
Client                                Server
  │── ClientHello + KeyShare ─────────→│   (includes ephemeral public key)
  │←─ ServerHello + KeyShare ──────────│   (server computes shared secret)
  │←─ Certificate + Finished ──────────│   (encrypted immediately)
  │── Finished ────────────────────────→│
  │═══════ Encrypted data ════════════│   (1 RTT total)
```

**0-RTT (Session Resumption)**: Client sends application data with the first flight using a pre-shared session ticket. Risk: replay attacks (no forward secrecy for 0-RTT data). Used only for idempotent operations.

## TLS 1.2 vs TLS 1.3

| Feature | TLS 1.2 | TLS 1.3 |
|---------|---------|---------|
| Handshake RTT | 2 | 1 (or 0-RTT) |
| Cipher suites | Many (including weak ones: RC4, 3DES, RSA key exchange) | 5 strong suites only |
| Forward secrecy | Optional | Required (ECDHE always) |
| RSA key exchange | Supported | Removed |
| Encrypted handshake | Partial | Certificate encrypted |
| Adoption | ~30% of TLS traffic | ~70%+ (growing) |

## Certificate Verification

1. Server presents its X.509 certificate.
2. Client checks: cert signed by a trusted CA (Certificate Authority) in its trust store.
3. Client checks: hostname matches cert's Common Name or Subject Alternative Name (SAN).
4. Client checks: cert not expired and not on a CRL / OCSP revocation list.

## mTLS (Mutual TLS)

In standard TLS, only the server is authenticated. **mTLS** requires the client to also present a certificate — used for service-to-service authentication (zero-trust networks, API clients).

## Related Concepts

- [[HTTPS]] — HTTP layered over TLS
- [[SSL Termination]] — ending TLS at a reverse proxy
- [[Public Key Infrastructure]] — the CA trust chain system
- [[Certificate]] — the X.509 document TLS uses for authentication
- [[mTLS]] — mutual certificate authentication
