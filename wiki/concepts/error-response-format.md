---
title: "Error Response Format"
type: concept
tags: [api, error-handling, best-practices]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# Error Response Format

Standardized JSON structure for returning error details in [[REST API]] responses.

## Format

```json
{
    "error": "Human-readable error message.",
    "detail": {
        "field_name": "Specific reason for this field."
    }
}
```

## Principles

- **Include in body, not status code alone**: Status code tells consumers what happened; body explains why
- **Field-level details**: Specify which fields caused the error to aid debugging
- **Pair with correct status code**: Never return error details with `200 OK`

## Examples

### Validation Error (400 Bad Request)
```json
{
    "error": "Invalid payload.",
    "detail": {
        "name": "This field is required.",
        "email": "Invalid email format."
    }
}
```

### Not Found (404 Not Found)
```json
{
    "error": "Resource not found.",
    "detail": {
        "id": "No book exists with slug 'nonexistent'."
    }
}
```

## Anti-Pattern

Returning `200 OK` with a custom `"status": "failure"` field forces consumers to check both HTTP status code and response body — breaks the contract that status codes communicate.
