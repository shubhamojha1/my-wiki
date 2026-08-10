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
- `wiki/problems/` — one page per solved LeetCode/interview problem; `wiki/problems/index.md` is the master table (all solved problems, one row each)

## Page format

Every wiki page should include YAML frontmatter:

---
title: "Page Title"
type: entity | concept | source | query | problem
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

### Ingest a book (chapter-wise)
For books too large to read in one pass (1000+ pages). Each chapter gets a
full ingest, not a shallow bullet summary. No pre-split of the PDF needed —
Read the raw file's `pages` param directly (max 20 pages/request, batch as
needed).

**Setup (once per book, before any chapter):**
1. Read the table of contents / front matter to get the full chapter list
   with page ranges.
2. Create `wiki/entities/<book-slug>.md` — the book's entity page:
   title, author, full chapter list with page ranges, and a status column
   (`pending` / `done`) per chapter. This is the progress tracker across
   sessions — a 1000-page book won't finish in one sitting.
3. Add one line for this entity page to `wiki/index.md`.

**Per chapter (repeat for each):**
1. Read the chapter's full page range in ≤20-page batches. Track pages
   read vs. the chapter's total range — don't move on until the count
   matches. Don't skip figures, footnotes, or appendix material within
   the range.
2. Discuss key takeaways with me before writing anything.
3. Create `wiki/sources/<book-slug>-ch<NN>-<chapter-slug>.md` with
   frontmatter:
   ```
   title: "<Book Title> — Ch<NN>: <Chapter Name>"
   type: source
   tags: []
   created: YYYY-MM-DD
   sources: ["<raw filename>, pp. <start>-<end>"]
   book: "[[<Book Entity Page>]]"
   chapter: <NN>
   ```
   Body requirement: this page must stand in for the chapter — someone
   reading only this page should come away with what the chapter argued,
   not just its topic list. Mirror the chapter's own section/subsection
   headings, and under each cover every key definition, argument, example,
   formula, and named system/technique — not just a title bullet. Close
   with a "Key Takeaways" list.
4. Create or update entity pages for named things (systems, people,
   papers) introduced in the chapter.
5. Create or update concept pages for key ideas introduced in the chapter.
6. Update the book entity page: mark this chapter `done`, link the new
   source page. Do NOT add a separate `wiki/index.md` row per chapter —
   only add rows for new entity/concept pages (the book's single index
   row already covers all its chapters via the entity page).
7. Append to `wiki/log.md`:
   `## [YYYY-MM-DD] ingest | <Book Title> Ch<NN>: <Chapter Name>`
8. Commit: `git add -A && git commit -m "[YYYY-MM-DD] ingest: <Book Title> Ch<NN> <Chapter Name>"`

A single chapter ingest should touch 3–8 wiki pages (source page + entity/
concept pages). When the last chapter is done, update the book entity
page's status to `complete` and append a final log entry summarizing the
whole book.

### Log a problem
When I give a solved problem (LeetCode/interview):
1. Create `wiki/problems/<slug>.md` with frontmatter (`type: problem`) plus:
   `difficulty`, `pattern` (list of `[[Concept]]` links, e.g. `[[Sliding Window]]`)
2. Body: one-line problem statement, optimal approach + why it's optimal, time/space complexity, the gotcha/insight that would trip a naive solution
3. Add one row to `wiki/problems/index.md`: `| [[Problem Name]] | difficulty | pattern | optimal approach one-liner |`
4. If the pattern doesn't have a concept page yet, create one in `wiki/concepts/`
5. Append to `wiki/log.md`

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