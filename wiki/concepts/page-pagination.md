---
title: "Page Pagination"
type: concept
tags: [api, rest, pagination]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# Page Pagination

A pagination strategy where consumers retrieve data in numbered pages of fixed size.

## Parameters

- `page`: The page number (1-indexed)
- `page_size`: Number of items per page

## Usage

```
GET /books?page=1&page_size=10
```

Returns items 1–10. Next page: `page=2&page_size=10` returns items 11–20.

## Combined with [[Query String Filtering]]

```
GET /books?published=true&page=2&page_size=10
```

## Pros
- Simple to implement and understand
- Easy for consumers to navigate (next/previous page links)
- Works well with UI pagination components

## Cons
- Not ideal for very large datasets (deep pagination is slow)
- Items may shift between pages if data changes during pagination

## Alternatives
- **Cursor-based pagination**: Better for real-time data, no page shifting
- **Offset pagination**: `offset` + `limit` (similar but 0-indexed)
