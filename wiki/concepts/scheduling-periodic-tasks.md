---
title: "Scheduling Periodic Tasks"
type: concept
tags: [scheduling, operations, automation]
created: 2026-04-23
sources: ["lethain.com/introduction-to-architecting-systems-for-scale/"]
---

# Scheduling Periodic Tasks

**Definition:** Running computation on a recurring schedule (hourly, daily, weekly) for maintenance, aggregation, or report generation.

## Common Use Cases

- **Daily analytics rollups** — Aggregate yesterday's metrics
- **Report generation** — Weekly usage reports
- **Cleanup jobs** — Delete expired sessions, old logs
- **Data aggregation** — Materialized views, denormalization
- **Health checks** — Monitoring and alerting

## Current Solutions

### Cron (The Standard)
Most systems still rely on cron despite its limitations:
- Simple time-based scheduling
- Runs on single machine
- No built-in redundancy

### Cron + Message Queue (Better)
```
[Cron schedule] → [Publishes to queue] → [Workers process]
```

Benefits:
- Cron machine only schedules, doesn't process
- Workers can run on multiple machines
- Recoverable from machine loss (queue persists)

### Modern Alternatives

| Tool | Pros | Cons |
|------|------|------|
| Cron | Ubiquitous, simple | No redundancy, brittle |
| Cron + Queue | Fault tolerant | Two systems to manage |
| Kubernetes CronJobs | Container-native | Additional complexity |
| Temporal | Workflow orchestration | Significant complexity |
| Airflow | Complex workflows, UI | Heavy for simple tasks |

## Redundancy Challenge

Periodic scheduling lacks a widely accepted solution for easy redundancy. Options:

1. **Puppet/Chef config** — Store cronjobs in configuration management, making recovery from losing the cron machine easy but manual
2. **Leader election** — Use distributed lock (ZooKeeper, etcd) to ensure only one machine runs each job
3. **Queue-based** — All scheduled tasks publish to queue; any worker can claim them

## Best Practice

```
# Instead of running heavy ETL in cron directly:
0 2 * * * /opt/jobs/daily_report.sh    # BAD: All work on cron machine

# Publish to queue, let workers handle:
0 2 * * * curl -X POST http://queue.example.com/jobs -d '{"job":"daily_report"}'
```

## Related Concepts

[[Offline Processing]], [[Message Queue]], [[Cron]], [[Map-Reduce]]