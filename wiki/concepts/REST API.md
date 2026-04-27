---
title: "REST API"
type: concept
tags: [api, rest]
created: 2026-04-28
sources: ["algomaster-api"]
---

# REST API

**REST** (Representational State Transfer) is an architectural style for web APIs.

## Principles

- Client-server architecture
- Stateless (no client state stored)
- Cacheable responses
- Uniform interface (resources via URLs)

## HTTP Methods

- **GET**: Retrieve resource
- **POST**: Create new resource
- **PUT**: Update existing resource
- **DELETE**: Remove resource

## Example Endpoints

- `GET /users` — List users
- `GET /users/{id}` — Get user
- `POST /users` — Create user
- `PUT /users/{id}` — Update user
- `DELETE /users/{id}` — Delete user

## Related Concepts

- [[API]] — Parent concept
- [[GraphQL]] — Alternative API style
- [[gRPC]] — High-performance RPC