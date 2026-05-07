---
title: "Negative Caching of DNS Queries (DNS NCACHE)"
type: source
tags: [dns, caching, rfc, standards-track]
created: 2026-05-08
sources: ["https://www.rfc-editor.org/rfc/rfc2308"]
---

# Negative Caching of DNS Queries (DNS NCACHE)

**Source:** RFC 2308 by Mark Andrews (CSIRO), March 1998 — Standards Track  
**Updates:** RFC 1034, RFC 1035  
**Updated by:** RFC 4035, RFC 4033, RFC 4034, RFC 6604, RFC 8020, RFC 8499, RFC 9499, RFC 9520

Defines the mechanism for caching negative DNS responses — the knowledge that a domain name or record type does not exist.

## Negative Response Types

### NXDOMAIN (Name Error)
Indicated by RCODE=NXDOMAIN. The queried domain name (QNAME) does not exist. Cached against the tuple `<QNAME, QCLASS>`.

### NODATA
Indicated by RCODE=NOERROR with no relevant answers. The name exists but has no records of the requested type. Must be inferred algorithmically from the response. Cached against the tuple `<QNAME, QTYPE, QCLASS>`.

## TTL for Negative Responses

Derived from the SOA record in the authority section:
```
negative TTL = min(SOA.MINIMUM field, SOA's own TTL)
```

The SOA MINIMUM field was historically overloaded with three meanings. This RFC deprecated two of them and redefined MINIMUM to mean "TTL for negative responses."

**Recommended caching limits:** 1–3 hours default; exceeding 1 day is problematic.

## Caching Rules

- Negative responses **without SOA records** must NOT be cached (prevents infinite forwarding loops)
- Authoritative servers MUST include the zone SOA in authority section for NXDOMAIN/NODATA responses
- Cached negative answers must include the SOA record with TTL decremented by cache time
- Implicit referral (NS records) should be included for resolvers to locate authoritative sources
- NXT and SIG records (DNSSEC) must be cached alongside negative answers when present

## Server Failure Caching (OPTIONAL)

| Failure Type | Max TTL | Cache Key |
|-------------|---------|-----------|
| Server Failure (SERVFAIL) | 5 minutes | `<QNAME, QTYPE, QCLASS, server IP>` |
| Dead/Unreachable Server | 5 minutes | Per-IP (transport error) or per-query |

## Security Considerations

- An injected NXDOMAIN with high TTL can act as a denial of service attack
- Without negative caching, spreading a bad A record had similar practical effect
- NXDOMAIN attack causes immediate bounce (e.g., SMTP mail); bad A would queue for retry
- DNSSEC (NXT + SIG records) provides verification of negative responses
- TTL sanity checking reduces attack effectiveness

## Changes from RFC 1034

- Negative caching in resolvers is **no longer optional** — if a resolver caches anything, it must cache negative answers too
- Non-authoritative negative answers MAY be cached
- SOA record from authority section MUST be cached
- $TTL directive added to master file format

## Related Pages

- [[DNS Negative Caching]], [[DNS]], [[DNSSEC]]
