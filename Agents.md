# Wiki Schema

This is a persistent, LLM-maintained knowledge base. You write and maintain
all files in `wiki/`. Files in `raw/` are immutable source documents — never
modify them.

## Directory layout

- `wiki/index.md` — master catalog; update on every ingest
- `wiki/log.md` — append-only activity log
- `wiki/sources/` — one summary page per source document
- `wiki/entities/` — pages for people, papers, systems, projects
- `wiki/concepts/` — pages for ideas, patterns, mechanisms, frameworks
- `wiki/queries/` — saved answers to questions worth keeping

## Page format

Every wiki page should include YAML frontmatter:

---
title: "Page Title"
type: entity | concept | source | query
tags: []
created: YYYY-MM-DD
sources: []          # list of raw source filenames that informed this page
---

Use `[[WikiLinks]]` for all cross-references. Never use bare filenames.

## Operations

### Ingest
When asked to ingest a source from `raw/`:
1. Read the source document fully
2. Discuss key takeaways with me before writing anything
3. Create a summary page in `wiki/sources/`
4. Create or update entity pages for any named things (systems, papers, people)
5. Create or update concept pages for any key ideas
6. Update `wiki/index.md` — add the new pages with a one-line description
7. Append to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <source title>`

A single ingest should touch 5–15 wiki pages. Don't be conservative.

### Query
When I ask a question:
1. Read `wiki/index.md` to find relevant pages
2. Read those pages fully
3. Synthesize and answer with citations to wiki pages
4. Ask me: "Worth saving this answer to `wiki/queries/`?"

### Lint
When asked to lint the wiki:
1. Scan all pages for contradictions with other pages
2. Find orphan pages (no inbound links)
3. Find concepts mentioned but lacking their own page
4. Check for stale claims superseded by newer sources
5. Suggest 3–5 new questions worth investigating

## Log format

Each log entry:
```
## [YYYY-MM-DD] <operation> | <title>

<one paragraph summary of what changed> 
```

## Note on raw sources
`raw/` is local-only and not in git. Write `wiki/sources/` summaries thorough
enough to stand alone — don't assume the raw file will always be accessible.

### After every operation
Run: `git add -A && git commit -m "[YYYY-MM-DD] <operation>: <brief description>"`
Remind the user to `git push` when the session wraps up.