---
title: "HTTP/2"
type: concept
tags: [networking, http]
created: 2026-04-28
sources: ["algomaster-http-https"]
---

# HTTP/2

**HTTP/2** is the second major version of HTTP, introduced in 2015.

## Features

- **Binary framing**: More efficient parsing
- **Multiplexing**: Multiple concurrent requests over single TCP connection
- **Header compression**: HPACK algorithm
- **Server push**: Proactive resource sending

## vs HTTP/1.1

HTTP/1.1 requires multiple TCP connections for parallel requests (head-of-line blocking). HTTP/2 solves this.

## Related Concepts

- [[HTTP]] — Version 1.x
- [[HTTP/3]] — Next version over QUIC