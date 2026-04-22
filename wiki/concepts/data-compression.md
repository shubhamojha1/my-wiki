---
title: "Data Compression"
type: concept
tags: [database, storage, compression]
created: 2026-04-23
---

# Data Compression

**Data compression** in databases reduces storage size by encoding data more efficiently, enabling faster I/O and better cache utilization.

## Why Compress in Databases?

- **Reduce I/O**: Smaller data = less disk read/write
- **Improve cache**: More data fits in memory
- **Reduce storage cost**: Less disk space needed
- **Sequential access**: Compressed data often stays compressed during scans

## Database-Specific Considerations

- **CPU vs I/O tradeoff**: Decompression costs CPU
- **Columnar vs Row**: Column stores compress better (homogeneous data)
- **Page-level**: Compress individual pages for random access
- **Segment-level**: Compress large segments for batch operations

## Related Techniques

- [[Run-Length Encoding]] — Consecutive identical values
- [[Dictionary Encoding]] — Map values to codes
- [[Delta Encoding]] — Store differences
- [[Bit-Vector Encoding]] — Bitmap per distinct value

## Related

- [[Column Store]] — Benefits from compression
- [[Database Page]] — Unit of compression
- [[Storage Manager]] — Handles compression/decompression