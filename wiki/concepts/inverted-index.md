---
title: "Inverted Index"
type: concept
tags: [database, index, search]
created: 2026-04-23
updated: 2026-05-20
---

# Inverted Index

An **inverted index** maps each unique term to the list of documents (or positions within documents) where it appears. It is the core data structure behind every full-text search engine.

The name "inverted" contrasts with a "forward" index (document → words it contains). An inverted index goes the other direction: word → documents containing it.

## Structure

```
Term Dictionary          Postings List
─────────────────        ─────────────────────────────────
"apple"          →       [doc1, doc3, doc7, doc12]
"database"       →       [doc2, doc3, doc8, doc9, doc15]
"fast"           →       [doc1, doc4, doc9]
```

### Postings List Variants

| Level | Stored data | Used for |
|-------|------------|---------|
| **Document-level** | doc_id only | Boolean retrieval (does document contain term?) |
| **Frequency-level** | (doc_id, tf) | TF-IDF ranking |
| **Position-level** | (doc_id, [pos1, pos2, …]) | Phrase queries ("hello world"), proximity search |
| **Payload-level** | (doc_id, arbitrary payload) | Custom scoring signals |

## Building an Inverted Index

```
1. Tokenize: "The quick brown fox" → ["quick", "brown", "fox"]
2. Normalize: lowercase, remove stop words ("the"), stem ("running" → "run")
3. For each (term, doc_id): append doc_id to term's postings list
4. Sort and compress postings lists (delta encoding: [3,7,12] → [3, +4, +5])
```

## Query Execution

```
Query: "database AND fast"

1. Look up "database" → postings [2,3,8,9,15]
2. Look up "fast"     → postings [1,4,9]
3. Intersect sorted lists → [9]   (doc 9 contains both terms)
```

Postings lists are kept sorted by doc_id so intersection is O(n+m) — a merge of two sorted lists.

## Compression

Postings lists can be huge (the word "the" may appear in every document). Compression techniques:
- **Delta/gap encoding**: store differences between consecutive IDs (small gaps → small numbers)
- **Variable-byte encoding**: encode small integers in fewer bytes
- **Roaring bitmaps**: hybrid bitmap/array for fast set operations

## Where It's Used

| System | Implementation |
|--------|---------------|
| **Elasticsearch / Lucene** | FST (Finite State Transducer) term dictionary; compressed posting lists |
| **PostgreSQL** | `tsvector` + `tsquery`; GIN index on tsvector |
| **Solr** | Lucene-based |
| **Meilisearch, Typesense** | In-memory inverted index optimized for typo-tolerance |

## Related Concepts

- [[Full-Text Index]] — the database-level concept backed by an inverted index
- [[TF-IDF]] — the classic ranking algorithm that uses term frequency from postings
- [[Bloom Filter]] — often used to test if a term exists before hitting the index
