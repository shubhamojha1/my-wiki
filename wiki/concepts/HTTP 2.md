---
title: "HTTP/2"
type: concept
tags: [networking, http]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# HTTP/2

**HTTP/2** is the second major version of HTTP, introduced in 2015.

## Problems Solved

HTTP/1.1 allowed one outstanding request per TCP connection. Workarounds (multiple connections, pipelining) were partial fixes. A slow request still blocked subsequent ones on the same connection — **head-of-line blocking**.

## Features

- **Binary framing**: Data in binary format, more efficient to parse than text
- **Multiplexing**: Multiple concurrent requests over a single TCP connection — eliminates head-of-line blocking
- **Header compression (HPACK)**: Reduces redundant header data, saves bandwidth
- **Server push**: Servers proactively send anticipated resources (e.g., CSS before HTML is requested)

## System Design Impact

Reduced latency significantly for complex pages with many assets. Modern APIs and microservices often build on HTTP/2 for multiplexing benefits.

## vs HTTP/1.1

HTTP/1.1 requires multiple TCP connections for parallel requests (head-of-line blocking). HTTP/2 solves this.

## Related Concepts

- [[HTTP]] — Version 1.x
- [[HTTP/3]] — Next version over QUIC