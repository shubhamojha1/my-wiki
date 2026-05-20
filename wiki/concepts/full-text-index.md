---
title: "Full-Text Index"
type: concept
tags: [database, index, search, text, nlp]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Full-Text Index

A **full-text index** is a specialized database index designed for efficient text search — finding documents that contain specific words, phrases, or patterns rather than exact column value matches.

## How It Works

Full-text indexing pre-processes text at write time:

1. **Tokenization** — split text into individual words (tokens)
2. **Normalization** — lowercase, strip punctuation
3. **Stop word removal** — filter common words ("the", "a", "is") that add noise
4. **Stemming / Lemmatization** — reduce words to their root form (running → run; runs → run)
5. **Build [[Inverted Index]]** — map each token to the list of document IDs that contain it

At query time, the query terms are similarly processed and looked up in the inverted index.

## Capabilities

| Feature | Description |
|---------|-------------|
| **Keyword search** | Match documents containing a word |
| **Phrase search** | Match exact multi-word phrases |
| **Fuzzy matching** | Handle typos and spelling variants |
| **Proximity search** | Words within N tokens of each other |
| **Relevance ranking** | TF-IDF or BM25 scoring to order results |
| **Boolean operators** | AND, OR, NOT between terms |

## Use Cases

- Blog / article search
- E-commerce product search
- Log search and analysis
- Document management systems
- Any `LIKE '%keyword%'` replacement (LIKE cannot use B-tree indexes; full-text can)

## Database Support

| Database | Full-Text Support |
|---------|-----------------|
| PostgreSQL | `tsvector` / `tsquery`; GIN index |
| MySQL | `FULLTEXT` index; InnoDB and MyISAM |
| Elasticsearch | Purpose-built; distributed full-text |
| SQLite | FTS5 extension |

## Related Concepts

- [[Inverted Index]] — the underlying data structure
- [[Database Index]] — general index concepts
- [[Vector Index]] — semantic search alternative (embeddings)
