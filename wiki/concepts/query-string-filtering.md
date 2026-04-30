---
title: "Query String Filtering"
type: concept
tags: [api, rest, design]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# Query String Filtering

Using URL query parameters to filter resource collections in [[REST API]] responses.

## Purpose

Allows consumers to retrieve subsets of data based on specific conditions without creating dedicated endpoints for every filter combination.

## Usage

Filter traits/conditions should be query parameters, not URI path segments.

| Bad | Good |
|-----|------|
| `GET /books/published/` | `GET /books?published=true` |
| `GET /authors/Cagan/books/` | `GET /books?author=Cagan` |

## Examples

```
GET /books?published=true
GET /books?author=Cagan&genre=fiction
GET /books?min_price=10&max_price=50
```

## Combined with [[Page Pagination]]

```
GET /books?published=true&page=2&page_size=10
```

## Benefits

- No endpoint proliferation for every filter combination
- Composable: multiple filters can be combined
- Clear separation between resource identification (URI) and filtering (query string)
