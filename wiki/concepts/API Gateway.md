---
title: "API Gateway"
type: concept
tags: [api, gateway]
created: 2026-04-28
sources: ["algomaster-api"]
---

# API Gateway

An **API Gateway** is a central server that sits between clients and backend services.

## Responsibilities

- Request routing
- Authentication
- Rate limiting
- Load balancing
- Request/response transformation

## How It Works

1. Client sends request to API Gateway
2. Gateway authenticates, rate limits
3. Gateway routes to appropriate service
4. Service responds, gateway returns to client

## Benefits

- Single entry point for all clients
- Simplified client code
- Centralized security

## Examples

- AWS API Gateway
- NGINX
- Kong

## Related Concepts

- [[API]] — Parent concept
- [[Load Balancing]] —/distributes traffic
- [[Authentication]] — Identity verification