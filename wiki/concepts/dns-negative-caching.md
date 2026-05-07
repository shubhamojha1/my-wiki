---
title: "DNS Negative Caching"
type: concept
tags: [dns, caching, nxdomain, nodata]
created: 2026-05-08
sources: ["https://www.rfc-editor.org/rfc/rfc2308"]
---

# DNS Negative Caching (NCACHE)

**Definition:** Caching of DNS responses that indicate the nonexistence of a domain name (NXDOMAIN) or the absence of a record type (NODATA), defined by RFC 2308.

Standard DNS caching stores positive answers (IP addresses, mail servers, etc.). Negative caching stores the knowledge that something does *not* exist, reducing unnecessary queries for nonexistent names.

## Why It Matters

A large proportion of DNS traffic consists of queries for nonexistent names (typos, misconfigurations, bots). Without negative caching, every such query traverses the full resolution chain — recursive resolver → root → TLD → authoritative. Negative caching eliminates this traffic for the duration of the cached TTL.

## Two Types of Negative Responses

| Type | Meaning | RCODE | Cache Key | Example |
|------|---------|-------|-----------|---------|
| NXDOMAIN | Domain name does not exist | NXDOMAIN | `<QNAME, QCLASS>` | `nonexistent.example.com` |
| NODATA | Name exists but no records of requested type | NOERROR (inferred) | `<QNAME, QTYPE, QCLASS>` | `example.com` has no AAAA record |

## TTL Derivation

The TTL for a cached negative response comes from the zone's SOA record:
```
negative TTL = min(SOA.MINIMUM, SOA.TTL)
```

The SOA MINIMUM field was historically overloaded (min TTL in zone, default TTL, negative TTL). RFC 2308 deprecated the first two meanings — MINIMUM now exclusively means **negative response TTL**.

**Recommended caching limits:** 1–3 hours default; values exceeding 1 day cause problems.

## How Caching Works

1. Authoritative server returns NXDOMAIN/NODATA with zone SOA in authority section
2. Resolver caches the negative answer, using SOA-derived TTL
3. TTL decrements normally while cached
4. When serving from cache, SOA record is included in authority section with decremented TTL
5. On TTL expiry, the negative cache entry is purged and the next query is forwarded normally

## Server Failure Caching (Optional)

DNS resolvers may also cache transient server failures:
- **SERVFAIL:** max 5 minutes, keyed by query tuple + server IP
- **Dead/unreachable server:** max 5 minutes, keyed by server IP (transport error) or query tuple

## Master File Format

RFC 2308 introduced the `$TTL` directive for specifying default TTL in zone files:
```
$TTL 86400
```

Resource records without explicit TTL values inherit from the most recent `$TTL` directive.

## Security

- Forged NXDOMAIN with long TTL = denial of service (DNS does not exist → service unreachable)
- More severe than bad A record: NXDOMAIN causes immediate bounce (SMTP), bad A allows queuing and retry
- Mitigations: TTL sanity checking, DNSSEC (NXT + SIG records verify negative responses)

## Related Pages

- [[DNS]], [[Cache-Control]], [[Caching]], [[DNSSEC]]
