---
title: "Inverted Index"
type: concept
tags: [database, index, search]
created: 2026-04-23
---

# Inverted Index

An **inverted index** maps content (words, terms) to document or record IDs where they appear.

## How It Works

- **Term dictionary**: List of all unique terms
- **Postings list**: For each term, list of documents containing it
- Like a book index: term → page numbers

## Use Cases

- **Full-text search**: Find documents containing query words
- **Text retrieval**: ElasticSearch, Solr use inverted indexes
- **Keyword search**: Efficient keyword lookups

## Variations

- **Document-level**: Map to document IDs
- **Position-level**: Include term positions in document
- **Frequency-weighted**: Store term frequency for ranking

## Trade-offs

- **Pros**: Fast term lookup, supports complex queries
- **Cons**: Building can be expensive, storage overhead

## Related

- [[B+Tree]] — Not ideal for text search
- [[Full-Text Search]] — Use case for inverted index