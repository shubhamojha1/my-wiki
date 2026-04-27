---
title: "API"
type: source
tags: [system-design, api, networking]
created: 2026-04-28
sources: ["algomaster-api"]
---

# API

**API** (Application Programming Interface) is code that takes an input and gives predictable outputs. Acts as a middleman enabling applications to interact without direct access to each other's code.

## How It Works

1. Client makes request to API
2. API processes request, interacts with databases/services
3. API sends response (JSON/XML) back to client

## Request-Response Model

- Client request → API server processes → Response

## Types of APIs

### Web APIs
- REST, GraphQL, gRPC

### Library APIs
- Functions within a programming language/framework

### Operating System APIs
- System calls for OS interaction

## Core Components

- **Endpoint**: URL path
- **Method**: GET, POST, PUT, DELETE
- **Request/Response**: JSON or XML format

## Architecture

- **Backend**: APIs handle data processing, business logic
- **Frontend**: GUI that interacts with APIs

## Related Concepts

- [[REST API]] — Representational State Transfer
- [[GraphQL]] — Query language for APIs
- [[gRPC]] — High-performance RPC
- [[API Gateway]] — Central API management

## Source

- AlgoMaster.io: [What is an API?](https://algomaster.io/learn/system-design/what-is-an-api) (October 2025)