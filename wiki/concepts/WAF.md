---
title: "WAF"
type: concept
tags: [security, networking, firewall, web]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# WAF

A **WAF (Web Application Firewall)** is a specialized reverse proxy that inspects HTTP/HTTPS traffic and blocks malicious requests before they reach backend servers. Unlike a network firewall (which operates at Layer 3–4), a WAF operates at Layer 7 and understands HTTP semantics.

## What It Blocks

| Attack Type | Description |
|-------------|-------------|
| SQL Injection | Malicious SQL in form inputs or query parameters |
| XSS (Cross-Site Scripting) | Script injection into web pages |
| CSRF (Cross-Site Request Forgery) | Forged requests from malicious sites |
| Path Traversal | `../../etc/passwd` style file access |
| Command Injection | OS commands embedded in input |
| DDoS / Bot Traffic | Rate-based rules, bot fingerprinting |
| OWASP Top 10 | Broad coverage of common web vulnerabilities |

## How It Works

```
[Internet] → [WAF] → [Web Server] → [App Server]
              ↑
         Inspect, filter, log HTTP requests
         Block based on rule sets
```

The WAF evaluates each request against a ruleset before forwarding. Matched rules can result in:
- **Block** — return 403 Forbidden
- **Challenge** — present CAPTCHA
- **Monitor** — log but allow (learning mode)
- **Rate limit** — throttle the source IP

## Rule Modes

| Mode | Behavior | Use Case |
|------|----------|---------|
| Detection | Log matches, allow traffic | Initial deployment / tuning |
| Prevention | Block matched requests | Production |
| Custom rules | User-defined logic | Business-specific protection |

## Placement

Deployed as a reverse proxy in front of web servers, either:
- **Cloud-based** (Cloudflare, AWS WAF, Akamai) — traffic routed through the provider's network
- **On-premises** (ModSecurity, NGINX with ModSecurity module) — runs on your infrastructure

## Limitations

- **False positives** — legitimate requests may match attack patterns; requires tuning
- **Encrypted payloads** — cannot inspect end-to-end encrypted content it does not terminate
- **Not a silver bullet** — WAF rules lag behind novel attack vectors; defense-in-depth still required

## Related Concepts

- [[Reverse Proxy]] — WAF is a specialized reverse proxy
- [[Rate Limiting]] — commonly integrated into WAF rule sets
- [[SSL Termination]] — WAF must terminate TLS to inspect HTTPS
- [[DDoS Protection]] — overlapping concern; WAFs often include DDoS mitigation
