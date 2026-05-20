---
title: "HTTP 202 Accepted"
type: concept
tags: [http, api, status-code]
created: 2026-05-01
updated: 2026-05-20
sources: [rest-api-design-best-practices.md]
---

# HTTP 202 Accepted

`202 Accepted` tells the client: "I received and validated your request, but the processing is not done yet and may not complete immediately." It decouples request receipt from processing completion.

## Semantics

- The request has been **accepted** for processing.
- Processing is **deferred** (asynchronous) — the server cannot confirm success or failure at response time.
- The resource **may or may not** be created/modified by the time the client checks back.
- The response is **not a final state** — unlike 200 OK or 201 Created.

## When to Use 202

| Scenario | Why 202 |
|----------|---------|
| Background job queued (video transcoding, PDF generation) | Processing takes seconds to minutes; don't hold the connection |
| Bulk operation submitted (import 10,000 records) | Accept the batch, process asynchronously |
| Message published to a queue | Server accepted it; delivery/processing is eventual |
| Asynchronous workflow triggered | Downstream services process at their own pace |

## Response Body and Headers

Best practice: include a way for the client to track progress.

```
POST /export-reports
HTTP/1.1 202 Accepted
Content-Type: application/json
Location: /jobs/job-abc123

{
  "jobId": "job-abc123",
  "status": "queued",
  "statusUrl": "/jobs/job-abc123",
  "estimatedCompletionTime": "2026-05-20T12:05:00Z"
}
```

The client polls `GET /jobs/job-abc123` for completion status.

## Polling Pattern

```
POST /export          → 202 Accepted, Location: /jobs/abc
GET  /jobs/abc        → 200 { status: "processing", progress: 40% }
GET  /jobs/abc        → 200 { status: "processing", progress: 80% }
GET  /jobs/abc        → 200 { status: "complete", result: "/exports/result.csv" }
```

Alternatively, use webhooks or SSE to push completion notification instead of polling.

## 201 vs 202 vs 200

| Code | Meaning | When |
|------|---------|------|
| **200 OK** | Request processed, response body is the result | Synchronous GET, PUT |
| **201 Created** | Resource created synchronously | POST that immediately creates |
| **202 Accepted** | Request accepted, processing deferred | Long-running async operation |

## Related Concepts

- [[REST API]] — the design principles that 202 supports for async patterns
- [[Webhooks]] — push-based alternative to polling after 202
- [[Message Queue]] — common backend implementation for 202 workflows
