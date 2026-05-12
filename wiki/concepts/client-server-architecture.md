---
title: "Client-Server Architecture"
type: concept
tags: [architecture, networking, system-design]
created: 2026-05-11
sources: ["algomaster-client-server-architecture"]
---

# Client-Server Architecture

A computing model where multiple **clients** interact with a centralized **server** over a **network** to access data, resources, or services.

## Components

- **Client** — end-user application that initiates requests and presents responses (browser, mobile app, desktop app)
- **Server** — always-on machine that processes requests, runs business logic, and returns results (web server, app server, DB server)
- **Network** — communication medium (internet or LAN) using protocols like TCP/IP

## Communication Flow

1. Client performs an action → triggers a request (typically HTTP)
2. Request travels over the network to the server's IP address
3. Server receives, processes (runs logic, queries DB), prepares response
4. Server sends response back (HTML, JSON, image, error message)
5. Client processes response and presents it to the user

Key enabling technologies: [[HTTP]]/[[HTTPS]], [[DNS]], [[TCP]]/[[IP]], [[REST API]]/[[GraphQL]]

## Architectural Tiers

- [[One-Tier Architecture]] — everything in a single application
- [[Two-Tier Architecture]] — client (UI) + server (logic + data)
- [[Three-Tier Architecture]] — presentation + logic + data layers
- [[N-Tier Architecture]] — 3-tier + specialized layers (caching, auth, load balancing)

## Advantages

Centralized management, scalability (vertical/horizontal), data integrity, resource sharing across clients.

## Challenges

[[Single Point of Failure]] (server crash affects all), performance bottlenecks under load, operational complexity at scale.

## Scaling Techniques

- [[Load Balancing]] — distribute requests across server pools
- [[Caching]] — serve frequently accessed data faster (Redis, CDN)
- [[Horizontal Scalability]] — add more servers instead of bigger ones
- [[Microservices]] — decompose monolith into independent deployable services

## Contrast: Peer-to-Peer Architecture

In [[Peer-to-Peer Network|P2P architecture]], there is no central server. Each peer acts as both client and server, sharing resources directly. Client-server offers simpler management and predictable performance, while P2P provides better fault tolerance and horizontal scalability at the cost of coordination complexity.

## See Also

- [[Scalability]]
- [[Availability]]
- [[Reliability]]
- [[Peer-to-Peer Network]] — The decentralized alternative
