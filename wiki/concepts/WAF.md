---
title: "WAF"
type: concept
tags: [security, networking]
created: 2026-04-28
sources: ["algomaster-proxy-vs-reverse-proxy"]
---

# WAF

A **WAF (Web Application Firewall)** inspects incoming HTTP/HTTPS traffic and blocks malicious requests before they reach backend servers.

## What It Blocks

- SQL injection
- Cross-site scripting (XSS)
- Cross-site request forgery (CSRF)
- DDoS attacks
- OtherOWASP Top 10 vulnerabilities

## Placement

Typically deployed as a reverse proxy in front of web servers.

## Examples

- **Cloudflare WAF**
- **AWS WAF**
- **ModSecurity**

## Related Concepts

- [[Reverse Proxy]] — WAF often sits behind
- [[DDoS Protection]] — Related security concept