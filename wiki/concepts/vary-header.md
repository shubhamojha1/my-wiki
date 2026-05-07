---
title: "Vary Header"
type: concept
tags: [http, caching, content-negotiation, headers]
created: 2026-05-08
sources: ["https://www.freecodecamp.org/news/an-in-depth-introduction-to-http-caching-cache-control-and-vary/"]
---

# Vary Header

**Definition:** An HTTP response header that tells caches which request headers were used by the origin server to generate the response, enabling caches to distinguish between different representations of the same URI.

## Why Vary Matters

URIs alone do not fully identify a resource. Content negotiation means the same URI can produce different responses depending on request headers:

- `Accept` — MIME type (HTML vs JSON vs XML)
- `Accept-Language` — language (`fr`, `en-US`, `zh`)
- `Accept-Encoding` — compression (gzip, brotli, deflate)
- `Accept-Charset` — character encoding
- `User-Agent` — browser/device type (rarely used — dangerous)

Without `Vary`, a cache could serve a French-language page to an English-speaking user, or a brotli-compressed response to a browser that doesn't support brotli.

## How It Works

The origin server includes:
```
Vary: Accept-Language
```

The cache extends its cache key to include the value of `Accept-Language`:
```
https://example.net/home.html_fr-FR
https://example.net/home.html_en-US
```

With multiple headers:
```
Vary: Accept-Language, Accept-Encoding
```
The cache key incorporates both values:
```
https://example.net/home.html_fr-FR_gzip
https://example.net/home.html_en-US_br
```

## The Normalization Problem

HTTP's robustness principle means clients send header values in many inconsistent formats. Caches must normalize values to avoid cache key explosion.

### Real-World Data (Fastly sampling of 100,000 requests)

| Header | Distinct Values | Impact |
|--------|-----------------|--------|
| Accept-Encoding | 44 | Manageable with normalization |
| User-Agent | ~8,000 | Catastrophic — never Vary on this |

### Examples of normalization

Language variations for French:
```
fr, fr-FR, fr_FR, fr-FR, fr-Latn-FR, Fr, FR
```
All should normalize to `FR`.

Without normalization, distinct values create distinct cache entries with identical content — wasting storage and reducing hit rates.

## Storage Implications

Vary introduces a tradeoff:
- **Vary on everything** → perfect representation matching, large storage, low hit rate
- **Vary on nothing** → small storage, high hit rate, wrong representations served
- **Partial Vary** → select the minimum headers needed to differentiate content

## Private vs Public Caches

Private caches (browsers) store only representations matching a single user's preferences. The Vary header is much less impactful because there's naturally only one representation per user per resource in the cache.

Public caches (CDNs, proxies) serve multiple users with different preferences. Vary on popular headers like Accept-Encoding and Accept-Language can significantly increase storage requirements and reduce hit rates.

## Best Practices

- Never Vary on `User-Agent` (8000+ variations destroys cache efficiency)
- Normalize header values at the cache layer (VCL, configuration scripts)
- Vary only on headers that genuinely produce different representations
- Consider whether public caching is needed — if not, use `Cache-Control: private` to skip Vary entirely
- For public caches, `Vary: Accept-Encoding` is generally safe with proper normalization

## Related Pages

- [[Cache-Control]], [[HTTP Caching]], [[Conditional Request]], [[ETag]], [[Browser Caching]], [[CDN]], [[Proxy Cache]]
