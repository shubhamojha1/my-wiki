---
title: "URI Naming Conventions"
type: concept
tags: [api, rest, design]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# URI Naming Conventions

Standards for naming resource endpoints in [[REST API]] design.

## Rules

### 1. No Verbs in URIs
HTTP verbs already describe the action. The URI should only identify the resource.

| Bad | Good |
|-----|------|
| `POST /books/create/` | `POST /books/` |
| `GET /books/generateBookCover/` | `GET /books/:slug/bookCover/` |

### 2. Use Plural Nouns
Use plural form for all resource endpoints to avoid ambiguity.

| Bad | Good |
|-----|------|
| `/book/:id/` | `/books/:id/` |
| `/book/` (single? all?) | `/books/` (collection) |

### 3. No Nesting
Avoid representing relationships through URI hierarchy. Use query parameters instead.

| Bad | Good |
|-----|------|
| `/authors/Cagan/books/` | `/books?author=Cagan` |

### 4. Trailing Slashes
Choose one convention (with or without) and gracefully redirect the other. Never return 500 errors for missing trailing slashes.

## Rationale

- **Consistency**: Predictable patterns make APIs easier to learn
- **Clarity**: Plural nouns remove ambiguity about what resource is being accessed
- **Flat over nested**: Clearer resource identification, simpler routing
