---
title: "REST API Design Best Practices"
type: concept
tags: [api, rest, best-practices, architecture]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# REST API Design Best Practices

Principles and conventions for designing clean, predictable, and consumer-friendly [[REST API]]s.

## Core Principles

### 1. Resource-Oriented URIs
- Resources represented by URIs, actions by HTTP verbs
- Use [[URI Naming Conventions]]: plural nouns, no verbs
- Avoid nesting — use [[Query String Filtering]] instead

### 2. Proper HTTP Usage
- Always set `Content-Type: application/json`
- Return meaningful [[HTTP Status Code]]s (never 200 with error body)
- Be consistent: same method → same status code everywhere
- Use [[HTTP 202 Accepted]] for async processing

### 3. Predictable Error Responses
- Use [[Error Response Format]] with field-level details
- Match status code to actual outcome (400, 401, 403, 404, 500)
- Never return `200 OK` with `"status": "failure"` in body

### 4. Query String Usage
- [[Query String Filtering]] for traits/conditions
- [[Page Pagination]] via `page` + `page_size` parameters
- Example: `GET /books?published=true&page=2&page_size=10`

### 5. Developer Experience
- Handle trailing slashes gracefully (redirect, don't error)
- Communicate rate limits via response headers
- Use REST-specific frameworks (Falcon, DRF, Restify)
