---
title: "Run-Length Encoding"
type: concept
tags: [database, compression, encoding]
created: 2026-04-23
---

# Run-Length Encoding (RLE)

**Run-length encoding** is a compression technique that stores consecutive identical values as a single value-count pair.

## How It Works

Instead of: `AAAAABBBCC`
Encoded as: `A5B3C2`

## Benefits

- **Simple**: Easy to encode/decode
- **Effective for**: Sorted data, low-cardinality columns
- **Database use**: Column stores with sorted data

## Limitations

- **Poor for**: High-cardinality, random data
- **Worse than nothing**: If no runs exist

## Database Applications

- Column store sorted columns
- Time-series data
- Bitmap compression (run-length encoded bitmaps)

## Related

- [[Data Compression]] — General category
- [[Dictionary Encoding]] — Alternative compression
- [[Column Store]] — Where RLE is commonly used