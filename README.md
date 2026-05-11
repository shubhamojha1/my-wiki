# My Wiki

> A Git-backed, Obsidian-friendly, LLM-maintained knowledge base for computer
> science notes, papers, system design references, databases, distributed
> systems, GPU programming, caching, networking, and machine learning systems.

This repository is a personal knowledge base built around a simple rule:
source material lives in `raw/`, durable synthesized knowledge lives in
`wiki/`, and every meaningful change is committed to Git.

The wiki is designed to be maintained with an AI coding agent. The agent reads
immutable source documents, extracts the important ideas, creates linked
markdown pages, updates the index, records the activity log, and commits the
result. The output is still plain markdown, so it remains readable in Obsidian,
GitHub, a terminal, or any editor.

## What This Project Contains

```text
my-wiki/
|-- AGENTS.md              # Operating rules for AI agents
|-- README.md              # Project overview and usage guide
|-- setup.md               # Original setup notes for this wiki pattern
|-- raw/                   # Local-only source documents; never edit in-place
|-- wiki/                  # Maintained knowledge base
|   |-- index.md           # Master catalog of all wiki pages
|   |-- log.md             # Append-only activity log
|   |-- sources/           # Standalone summaries of source documents
|   |-- entities/          # People, papers, tools, systems, projects
|   |-- concepts/          # Ideas, patterns, mechanisms, frameworks
|   `-- queries/           # Saved synthesized answers
`-- .obsidian/             # Obsidian vault configuration
```

The current wiki already includes material across:

- distributed systems and consensus
- databases and storage engines
- caching, CDNs, and HTTP semantics
- system design fundamentals
- GPU programming and CUDA
- attention mechanisms and transformer optimization
- OOP, API design, networking, and reliability patterns

## Core Idea

Most note collections fail because raw notes, summaries, questions, and
concept definitions blur together. This repository keeps them separate.

`raw/` is the evidence layer. It contains clipped articles, PDFs, lecture
notes, transcripts, or extracted text. These files are treated as immutable and
are intentionally ignored by Git.

`wiki/sources/` is the source-summary layer. Each page summarizes one source
document thoroughly enough to stand alone even if the original raw file is not
available later.

`wiki/entities/` is the named-thing layer. It tracks systems, papers, people,
companies, hardware, protocols, projects, and tools.

`wiki/concepts/` is the reusable-idea layer. It captures mechanisms, patterns,
algorithms, principles, tradeoffs, and mental models.

`wiki/queries/` is the synthesis layer. It stores answers to questions that are
worth keeping after they have been synthesized from the wiki.

`wiki/index.md` ties everything together as the master catalog.

## Page Schema

Every wiki page uses YAML frontmatter:

```yaml
---
title: "Page Title"
type: entity | concept | source | query
tags: []
created: YYYY-MM-DD
sources: []
---
```

Pages use Obsidian-style wiki links:

```markdown
[[Apache Kafka]]
[[Distributed Commit Log]]
[[FlashAttention]]
```

Avoid bare filenames inside wiki prose. Link to concepts and entities by their
page titles so the graph stays navigable.

## Working With The Wiki

This repository is meant to be operated through a small set of repeatable
workflows.

### Ingest A New Source

Use this when a new article, paper, lecture, transcript, or note has been added
under `raw/`.

Expected workflow:

1. Read the raw source fully.
2. Discuss key takeaways before writing wiki pages.
3. Create one page in `wiki/sources/`.
4. Create or update related pages in `wiki/entities/`.
5. Create or update related pages in `wiki/concepts/`.
6. Update `wiki/index.md` with concise catalog entries.
7. Append an entry to `wiki/log.md`.
8. Commit the change.

A good ingest usually touches 5 to 15 wiki pages. The goal is not just to
summarize the source, but to integrate it into the existing knowledge graph.

Example request:

```text
Ingest raw/flash-attention-3.pdf into the wiki.
```

### Ask A Question

Use this when you want an answer grounded in the local wiki rather than a fresh
web search.

Expected workflow:

1. Read `wiki/index.md`.
2. Find the relevant source, entity, and concept pages.
3. Read those pages fully.
4. Synthesize an answer with citations to wiki pages.
5. Decide whether the answer is worth saving in `wiki/queries/`.

Example request:

```text
How does FlashAttention reduce memory traffic compared with standard attention?
```

### Lint The Wiki

Use this when the knowledge base needs maintenance.

Expected workflow:

1. Scan wiki pages for contradictions.
2. Find orphan pages with no inbound links.
3. Identify important mentioned concepts that lack pages.
4. Check for stale claims superseded by newer sources.
5. Suggest 3 to 5 high-value questions worth investigating.

Example request:

```text
Lint the wiki and suggest cleanup work.
```

## Git Workflow

The wiki is versioned deliberately. After every operation, stage and commit the
changes:

```powershell
git add -A
git commit -m "[YYYY-MM-DD] <operation>: <brief description>"
```

Examples:

```powershell
git commit -m "[2026-05-11] ingest: add FlashAttention-3 notes"
git commit -m "[2026-05-11] query: compare Kafka and RabbitMQ"
git commit -m "[2026-05-11] lint: identify stale cache pages"
```

Push when you are done with a session:

```powershell
git push
```

## Obsidian Usage

This repository can be opened directly as an Obsidian vault.

Recommended habits:

- Start from `wiki/index.md`.
- Use graph view to inspect concept and entity relationships.
- Keep new source captures under `raw/`.
- Keep durable notes under `wiki/`.
- Avoid editing generated wiki pages casually unless you also update related
  links, the index, and the log.

The vault is plain markdown, so Obsidian is helpful but not required.

## Agent Rules

The canonical operating rules live in `AGENTS.md`. Any AI agent working in this
repository should follow those instructions.

Important constraints:

- Only maintain files in `wiki/` during wiki operations unless asked otherwise.
- Never modify files in `raw/`.
- Keep `wiki/index.md` current.
- Keep `wiki/log.md` append-only.
- Use YAML frontmatter on every wiki page.
- Use `[[WikiLinks]]` for cross-references.
- Commit every completed operation.

This README is a project guide. `AGENTS.md` is the execution contract.

## Why This Structure Works

The structure keeps the knowledge base auditable:

- raw material remains unchanged
- source summaries preserve provenance
- entity pages collect facts about named things
- concept pages make ideas reusable across sources
- query pages preserve higher-level synthesis
- the log records what changed and when
- Git provides rollback, diffing, and history

The result is a wiki that can grow without becoming a pile of disconnected
notes.

## Quick Start

Clone or open the repository:

```powershell
cd C:\Users\subha\Projects\my-wiki
```

Open it in Obsidian, or browse directly from:

```text
wiki/index.md
```

Add source material to:

```text
raw/
```

Then ask an agent to ingest, query, or lint the wiki.

## Maintenance Checklist

Use this checklist after larger wiki sessions:

- `wiki/index.md` includes all new pages.
- `wiki/log.md` has a dated entry for the operation.
- New pages include valid YAML frontmatter.
- New pages use `[[WikiLinks]]` instead of bare filenames.
- Source summaries are detailed enough to stand alone.
- Related concept and entity pages are cross-linked.
- The operation has been committed to Git.

## Status

This is an active personal knowledge base. It is optimized for local use,
agent-assisted maintenance, and long-term retrieval, not for package publishing
or application deployment.
