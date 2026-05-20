---
title: "gRPC"
type: concept
tags: [api, grpc, rpc, microservices]
created: 2026-04-28
updated: 2026-05-20
sources: ["algomaster-api"]
---

# gRPC

**gRPC** (Google Remote Procedure Call) is an open-source, high-performance RPC framework that uses **HTTP/2** for transport and **Protocol Buffers** (protobuf) for serialization. Callers invoke methods on remote services as if they were local function calls.

## How It Works

1. Define the service and message types in a `.proto` file
2. Use the protobuf compiler to generate client and server stubs in your language
3. Server implements the service; client calls stubs directly

```protobuf
service UserService {
  rpc GetUser (UserRequest) returns (UserResponse);
  rpc ListUsers (ListRequest) returns (stream UserResponse);
}

message UserRequest { string id = 1; }
message UserResponse { string id = 1; string name = 2; string email = 3; }
```

## Communication Patterns

| Pattern | Description | Use Case |
|---------|-------------|---------|
| Unary | One request → one response | Standard CRUD |
| Server streaming | One request → stream of responses | Live feeds, large result sets |
| Client streaming | Stream of requests → one response | File upload, aggregation |
| Bidirectional streaming | Both sides stream simultaneously | Chat, real-time collaboration |

## Key Features

- **Protocol Buffers** — binary encoding; typically 5–10× smaller and faster to parse than JSON
- **HTTP/2** — multiplexed streams over one connection; header compression; no head-of-line blocking per stream
- **Code generation** — stubs auto-generated for Go, Java, Python, C++, Node.js, and more
- **Deadlines & cancellation** — built-in timeout propagation across service calls
- **Interceptors** — middleware for auth, logging, retries (equivalent to REST middleware)

## vs REST

| Aspect | REST | gRPC |
|--------|------|------|
| Protocol | HTTP/1.1 or HTTP/2 | HTTP/2 |
| Serialization | JSON (text) | Protocol Buffers (binary) |
| Contract | OpenAPI (optional) | `.proto` file (required) |
| Streaming | Requires SSE or WebSocket | First-class bidirectional |
| Browser support | Native | Requires gRPC-Web proxy |
| Readability | Human-readable | Binary (not directly inspectable) |
| Ecosystem | Massive | Strong, but smaller |

## When to Use

- **Internal microservice communication** where performance matters
- Polyglot environments (auto-generated stubs for any language)
- Real-time bidirectional streaming needs
- **Avoid** when browser clients must call directly (use REST or gRPC-Web)

## Related Concepts

- [[REST API]] — Human-readable alternative
- [[HTTP 2]] — Transport protocol gRPC is built on
- [[Microservices]] — Primary use case for gRPC
- [[API Gateway]] — Can translate REST → gRPC for external clients
