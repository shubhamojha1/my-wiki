---
title: "Log-Structured Storage"
type: concept
tags: [database, storage, write-optimized]
created: 2026-04-23
---

# Log-Structured Storage

**Log-structured storage** is an append-only storage model where the DBMS never overwrites data in place. Instead, it writes updates as log records and periodically compacts logs into new data files.

## How It Works

1. **Write log records**: INSERT, DELETE, UPDATE appended to log
2. **No in-place updates**: Never modify existing pages
3. **Periodic compaction**: Merge old logs, remove stale updates
4. **Read reconstruction**: Replay logs or use compacted files

## Benefits

- **Fast writes**: Sequential append only (no random I/O)
- **Crash consistency**: Log can be replayed for recovery
- **No fragmentation**: Compaction eliminates dead space
- **Write amplification**: Downside — compaction rewrites data

## Use Cases

- **Write-heavy workloads**: Logging, analytics, time-series
- **Append-only data**: Event streams, audit logs
- **LSM-Trees**: Log-Structured Merge-Tree (LevelDB, RocksDB)

## Comparison

| Aspect | Page-Oriented | Log-Structured |
|--------|---------------|----------------|
| Write pattern | Random (in-place) | Sequential (append) |
| Read pattern | Direct + scan | Scan + replay |
| Compaction | None needed | Required |
| Latency | Consistent | Spikes during compaction |

## Related

- [[Compaction]] — Merging logs into data files
- [[LSM-Tree]] — Production log-structured structure
- [[Write-Ahead Logging]] — Related but for recovery, not storage
- [[SSTable]] — Sorted String Table (compacted log format)