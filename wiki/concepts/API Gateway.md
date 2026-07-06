---
title: "API Gateway"
type: concept
tags: [api, gateway, microservices, architecture]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-api", "algomaster-api-gateway", "https://www.hellointerview.com/learn/system-design/problem-breakdowns/distributed-rate-limiter"]
---

# API Gateway

An **API Gateway** is a server that acts as the single entry point for all client requests to backend services. It handles cross-cutting concerns so individual services don't have to.

## Responsibilities

- **Request routing** — directs requests to the appropriate downstream service
- **Authentication & authorization** — validates tokens (JWT, OAuth) before forwarding
- **Rate limiting** — enforces per-client or per-endpoint request quotas
- **Load balancing** — distributes traffic across service instances
- **Request/response transformation** — translates formats (e.g., REST to gRPC, JSON to XML)
- **SSL termination** — decrypts HTTPS so backends receive plain HTTP
- **Caching** — serves cached responses for repeated requests
- **Logging & observability** — central place to capture request traces and metrics

## How It Works

```
[Client]
   ↓ HTTPS
[API Gateway]  ← Auth, Rate Limit, Route
   ↓ HTTP / gRPC
[Service A]  [Service B]  [Service C]
```

1. Client sends request to the gateway
2. Gateway authenticates the caller and enforces rate limits
3. Gateway routes the request to the correct backend service
4. Service responds; gateway applies any response transforms
5. Gateway returns the response to the client

## Benefits

| Benefit | Without Gateway | With Gateway |
|---------|----------------|-------------|
| Client complexity | Each client calls many services | One endpoint for everything |
| Security | Each service enforces auth independently | Centralized |
| Cross-cutting concerns | Duplicated per service | Implemented once |
| Protocol translation | Client must speak service protocol | Gateway adapts |

## Drawbacks

- **Single point of failure** — must be highly available (deploy in active-active or with health checks)
- **Added latency** — one extra network hop per request
- **Bottleneck risk** — all traffic flows through one component

## Rate Limiting Placement

For a [[Distributed Rate Limiter]], the gateway is a strong placement because it rejects excess traffic before requests consume application-server capacity. It also avoids the extra per-request hop that a dedicated rate-limiter service would add after the request reaches an application server.

The trade-off is context. Gateway rate limiting can use request-visible data such as:

- URL/path and query parameters
- `Authorization` headers or JWT claims
- `X-API-Key`
- `X-Forwarded-For` or client IP
- user-agent and other headers

Rules that depend on deeper application state, such as premium tier or account status, need that state encoded in the request token/header or require an external lookup that adds latency.

## Examples

| Product | Notes |
|---------|-------|
| AWS API Gateway | Fully managed, integrates with Lambda |
| Kong | Open-source, plugin ecosystem |
| NGINX | Widely used as both proxy and gateway |
| Envoy | High-performance, used in service meshes |
| Apigee | Enterprise-grade, Google Cloud |

## Related Concepts

- [[Rate Limiting]] — enforces request quotas
- [[Load Balancing]] — distributes traffic across instances
- [[Reverse Proxy]] — shares many responsibilities with an API gateway
- [[SSL Termination]] — often handled at the gateway
- [[Microservices]] — API gateways are essential in microservice architectures
- [[Service Discovery]] — gateway needs to locate services dynamically
- [[Circuit Breaker Pattern]] — protects backends from overload
