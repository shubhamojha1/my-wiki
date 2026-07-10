---
title: "Cursor-Based Pagination"
type: concept
tags: [api, rest, pagination]
created: 2026-07-10
sources: ["hellointerview-api-design"]
---

# Cursor-Based Pagination

A pagination strategy where each response carries an opaque pointer (a **cursor**) to the next item, instead of a numeric offset. The client passes that cursor back to fetch the next page.

## Usage

First request:
```
GET /events?limit=10
```

Response:
```json
{
  "events": [ ... ],
  "next_cursor": "cmd9atj3p000007ky19w1dpy2"
}
```

Next request:
```
GET /events?cursor=cmd9atj3p000007ky19w1dpy2&limit=10
```

The cursor typically encodes a stable sort key (e.g. an ID or timestamp) rather than a row count, so it keeps pointing at the correct logical position even as rows are inserted or deleted elsewhere in the set.

## Why It Exists

[[Page Pagination]] (offset/page-number based) breaks under concurrent writes: if a row is inserted before the current offset while a client is paging through results, later pages can skip a record or repeat one, because "page 3" is defined by position, not identity.

## Trade-offs

**Pros**
- Stable under real-time/high-write data — no duplicate or skipped records as the underlying set changes.
- Cursor can be indexed directly (e.g. `WHERE id > :cursor ORDER BY id LIMIT :n`), which tends to perform better than large-offset `OFFSET`/`LIMIT` queries on big tables.

**Cons**
- No "jump to page 5" — cursors only support sequential forward/backward traversal from a known position.
- Cursor encoding/decoding adds implementation complexity absent from a plain integer offset.

## When to Use

Default to [[Page Pagination]] for most interview and CRUD scenarios — it's simpler and sufficient. Reach for cursor-based pagination specifically for high-volume or real-time-write datasets (activity feeds, event streams, chat history) where offset instability would be a real, not theoretical, problem.

## Related Concepts

- [[Page Pagination]] — the offset/page-number alternative this pattern replaces under high-write conditions
- [[REST API]] — the context this pagination style is usually applied in
- [[Query String Filtering]] — often combined with pagination parameters
