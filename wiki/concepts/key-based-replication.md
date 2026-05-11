---
title: "Key-Based Replication"
type: concept
tags: [distributed-systems, replication, cdc]
created: 2026-05-11
sources: [redis-data-replication]
---

# Key-Based Replication

**Key-based incremental replication** uses a replication key — typically a timestamp or incrementing ID column — to identify only records that changed since the last replication cycle.

## How It Works

```sql
SELECT * FROM orders
WHERE updated_at > last_replication_timestamp;
```

## Characteristics

- **Fast**: Only queries the changed rows
- **Low overhead**: Minimal load on source system
- **Simple**: No CDC infrastructure needed
- **Limitation**: Cannot detect deleted records (rows removed)

## Comparison with CDC

| Aspect | Key-Based | Log-Based CDC |
|--------|-----------|---------------|
| Detection | Column value comparison | Transaction log |
| Deletes | Not captured | Captured |
| Schema changes | Resilient | May break |
| Setup complexity | Low | Medium |

## Related

- [[Data Replication]] — General concept
- [[Change Data Capture (CDC)]] — Log-based alternative
- [[Transactional Replication]] — Can use CDC or key-based
