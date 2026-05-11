---
title: "AlgoMaster: Client-Server Architecture"
type: source
tags: [algomaster, system-design, architecture]
created: 2026-05-11
sources: ["algomaster.io/learn/system-design/client-server-architecture"]
author: "Ashish Pratap Singh"
---

# Client-Server Architecture

**Author:** [[Ashish Pratap Singh]]
**Source:** AlgoMaster.io — System Design
**Last Updated:** October 5, 2025

## Summary

A comprehensive overview of the client-server model, the fundamental computing architecture underpinning modern internet applications. Covers how clients and servers communicate, the evolution from 1-tier to N-tier architectures, and real-world scaling techniques.

## Key Content

### What It Is

Client-server architecture is a computing model where multiple clients interact with a centralized server to access data, resources, or services. The client initiates requests; the server processes them and returns results.

Three fundamental components:
- **Client** — end-user application (browser, mobile app, desktop app)
- **Server** — always-on machine processing requests (web server, app server, DB server)
- **Network** — communication medium (internet or LAN)

### Communication Flow

1. Client initiates a request (e.g., clicking a link)
2. Request travels over the network (typically HTTP to a server IP)
3. Server receives, processes (runs logic, queries DB), prepares response
4. Server sends back response (HTML, JSON, image, error)
5. Client processes and presents response to user

Key technologies: HTTP/HTTPS, DNS, TCP/IP, REST/GraphQL.

### Architectural Tiers

| Tier | Architecture | Pros | Cons |
|------|-------------|------|------|
| **1-Tier** | Everything in one app (Excel) | Simple, no network overhead | Not scalable, no separation |
| **2-Tier** | Client (UI) + Server (logic + data) | Centralized data, simpler than 3-tier | Poor scalability, server bottleneck |
| **3-Tier** | Presentation + Logic + Data layers | Scalable, maintainable, centralized logic | More complex, network latency |
| **N-Tier** | 3-tier + specialized layers (cache, auth, LB) | Highly scalable, modular, fault-tolerant | High complexity, ops overhead |

### Advantages

- Centralized management (updates, security)
- Scalability (vertical/horizontal)
- Data integrity (central storage)
- Resource sharing across clients

### Challenges

- Single point of failure (server crash affects all)
- Performance bottlenecks under load
- Operational complexity at scale

### Scaling Techniques

- Load balancers (distribute requests across server pool)
- Caching (Redis, CDN — serve frequently accessed data faster)
- Horizontal scaling (add more servers instead of bigger ones)
- Microservices (decompose monolith into independent deployable services)

## Related Wiki Pages

- [[Scalability]] — vertical vs horizontal scaling
- [[Load Balancing]] — request distribution
- [[Horizontal Scalability]] — adding more servers
- [[Caching]] — storing copies for faster access
- [[Single Point of Failure]] — eliminating SPOFs
- [[Microservices]] — independent deployable services
- [[Client-Server Architecture]] — core concept page
