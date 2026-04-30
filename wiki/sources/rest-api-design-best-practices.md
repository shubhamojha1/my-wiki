---
title: "REST API Design Best Practices"
type: source
tags: [api, rest, architecture, best-practices]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# REST API Design Best Practices

Source: [blog.wahab2.com/api-architecture-best-practices-for-designing-rest-apis](https://blog.wahab2.com/api-architecture-best-practices-for-designing-rest-apis-bf907025f5f) by Abdul Rafee Wahab (Oct 2021).

## Summary

A practical guide to REST API design based on real-world experience building and consuming APIs. Covers 13 best practices including HTTP fundamentals, URI design, status code usage, error handling, and framework selection.

## Key Takeaways

### HTTP Fundamentals
- **Learn HTTP basics**: Verbs (GET/POST/PUT/PATCH/DELETE), URIs, endpoints, status codes
- **Always set Content-Type**: Use `application/json`, never return plain text — programmatic clients rely on this header

### URI Design
- **No verbs in URIs**: HTTP verbs already describe the action. `POST /books/` not `POST /books/create/`
- **Use plural nouns**: `/books/` not `/book/` — avoids ambiguity between single and collection endpoints
- **No resource nesting**: Use query parameters instead. `/books?author=Cagan` not `/authors/Cagan/books/`
- **Handle trailing slashes gracefully**: Redirect clients if they use wrong convention; don't return 500 errors

### Status Codes
- **Use meaningful status codes**: Never return `200 OK` with error details in body — breaks trust between API and consumers
- **Be consistent**: Same method should return same status code across all endpoints
- **Standard pattern**: GET → 200, PUT → 200, POST → 201, PATCH → 200, DELETE → 204
- **[[HTTP 202 Accepted]]**: Useful when resource will be created asynchronously (e.g., after job completion)
- **401 vs 403**: 401 = not authenticated (missing/invalid credentials), 403 = authenticated but no permissions

### Error Handling
- **Return error details in body**: Include which fields were affected to help consumers debug
- **Format**: `{ "error": "message", "detail": { "field": "reason" } }`

### Filtering & Pagination
- **Use querystring**: `GET /books?published=true&page=2&page_size=10`
- **Page number pagination**: `page` + `page_size` parameters

### Implementation
- **Use REST-specific frameworks**: Falcon (Python), Django REST Framework, Restify (Node) rather than generic web frameworks
