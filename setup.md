# LLM Wiki — Setup Guide

A replicable setup for building a personal knowledge base using LLMs and Obsidian.
Based on the [LLM Wiki pattern](https://gist.github.com/tobi/e4f5b1a89e92e6c17ef36f2a4e9571bc).

---

## Prerequisites

- [Obsidian](https://obsidian.md) installed
- [OpenCode](https://opencode.ai) installed (or Claude Code — this setup works with both)
- A MiniMax API key (or any other LLM provider)
- Git installed

---

## Step 1: Create the Obsidian Vault

1. Open Obsidian → **Create new vault**
2. Name it (e.g. `my-wiki`) and choose a location: `~/projects/my-wiki`
3. Go to **Settings → Files and links**:
   - Default location for new notes → `wiki/`
   - Attachment folder path → `raw/assets/`

**Install community plugins** (Settings → Community plugins → Browse):
- **Dataview** — query page frontmatter as tables
- **Marp Slides** — generate slide decks from markdown

**Install in your browser** (not in-app):
- [Obsidian Web Clipper](https://obsidian.md/clipper) — clips web articles to markdown

---

## Step 2: Create the Directory Structure

```bash
cd ~/projects/my-wiki

mkdir -p raw/assets
mkdir -p wiki/entities
mkdir -p wiki/concepts
mkdir -p wiki/sources
mkdir -p wiki/queries

touch wiki/index.md
touch wiki/log.md
```

Final structure:

```
my-wiki/
├── raw/                   # your source docs — immutable, local-only
│   └── assets/            # downloaded images
├── wiki/                  # LLM owns this entirely
│   ├── index.md           # master content catalog
│   ├── log.md             # append-only activity log
│   ├── entities/          # people, papers, systems, projects
│   ├── concepts/          # ideas, patterns, mechanisms
│   ├── sources/           # one summary page per source doc
│   └── queries/           # saved answers worth keeping
├── AGENTS.md              # schema for OpenCode (and any agent)
└── CLAUDE.md              # schema for Claude Code (copy of AGENTS.md)
```

---

## Step 3: Create the Schema File

Create `AGENTS.md` at the vault root. This is the most important file — it turns the LLM into a disciplined wiki maintainer.

```markdown
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

## [YYYY-MM-DD] <operation> | <title>
<one paragraph summary of what changed>

## Style

- Write in clear, dense prose — not bullet soup
- Every claim should be traceable to a source page
- Prefer updating existing pages over creating new ones when content overlaps
- Flag contradictions explicitly: use a `> ⚠️ Contradiction:` blockquote

## After every operation
Run: `git add -A && git commit -m "[YYYY-MM-DD] <operation>: <brief description>"`
Remind the user to `git push` when the session wraps up.

## Note on raw sources
`raw/` is local-only and not in git. Write `wiki/sources/` summaries thorough
enough to stand alone — don't assume the raw file will always be accessible.
```

Then copy it for Claude Code:

```bash
cp AGENTS.md CLAUDE.md
```

---

## Step 4: Configure OpenCode with MiniMax

Edit `~/.config/opencode/config.json`:

```json
{
  "providers": {
    "minimax": {
      "apiKey": "YOUR_MINIMAX_API_KEY",
      "baseURL": "https://api.minimax.chat/v1"
    }
  },
  "model": "minimax/abab6.5s-chat"
}
```

To launch OpenCode inside your vault:

```bash
cd ~/projects/my-wiki
opencode
```

---

## Step 5: Set Up Git

```bash
cd ~/projects/my-wiki
git init
```

Create `.gitignore`:

```
raw/
.obsidian/workspace.json
.obsidian/workspace-mobile.json
.obsidian/cache
```

> **Why ignore `raw/`?** It contains PDFs, images, and local documents that are large and machine-specific. The `wiki/sources/` summaries are written to stand alone without them.

Commit the initial structure:

```bash
git add .
git commit -m "init: vault structure and schema"
```

Create a **private** repo on GitHub (empty — no README), then:

```bash
git remote add origin git@github.com:yourname/my-wiki.git
git push -u origin main
```

Push at natural breakpoints: after an ingest session, after a lint pass, after saving a good query.

---

## Step 6: Initialize the Wiki

Open OpenCode in your vault root and paste this as your first message:

```
Read AGENTS.md to understand how this wiki works.

Then initialize the wiki:
1. Write wiki/index.md with a header, a brief description of this knowledge base,
   and empty sections for: Sources, Entities, Concepts, Queries
2. Write wiki/log.md with a single entry:
   ## [today's date] init | Wiki initialized
   Brief note: empty wiki created, ready for first ingest.

This wiki is about: [YOUR TOPIC HERE]
```

---

## Step 7: First Ingest

Drop a source into `raw/` — clip an article with Obsidian Web Clipper, paste a paper as `.md`, or copy any text file. Then, tell OpenCode:

```
Ingest raw/my-first-source.md — follow the ingest workflow from AGENTS.md.
Start by telling me the 3–5 most important things in this source before writing anything.
```

Watch Obsidian's graph view fill in as pages get created and linked.

---

## Switching to Claude Code Later

The setup is model-agnostic. When you switch:

```bash
cd ~/projects/my-wiki
claude
```

Claude Code reads `CLAUDE.md` (same content as `AGENTS.md`) and picks up exactly where OpenCode left off. The wiki is the continuity — not the model.

---

## Quick Reference

| Operation | What to say |
|-----------|-------------|
| Ingest a source | `Ingest raw/<filename> — follow AGENTS.md` |
| Ask a question | Just ask — the LLM reads the index first |
| Save a good answer | `Save this to wiki/queries/<name>.md` |
| Health check | `Lint the wiki — follow AGENTS.md` |
| Commit progress | `git add -A && git commit -m "..."` |