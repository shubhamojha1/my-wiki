---
title: "HTTP 202 Accepted"
type: concept
tags: [http, api, status-code]
created: 2026-05-01
sources: [rest-api-design-best-practices.md]
---

# HTTP 202 Accepted

HTTP status code indicating the server has accepted the request for processing, but the processing is not yet complete.

## Meaning

The request is valid and has been queued for asynchronous processing. The resource may or may not be created eventually.

## Use Cases

1. **Async resource creation**: The resource will be created after a background job completes (e.g., video processing, report generation)
2. **Idempotent re-submission**: The resource already existed in some way, but this should not be treated as an error

## vs [[HTTP 201]] (Created)

| 201 Created | 202 Accepted |
|-------------|--------------|
| Resource created synchronously | Resource creation deferred |
| Response includes resource location | May include status/progress endpoint |
| Final state | Intermediate state |

## Example

```
POST /reports
HTTP/1.1 202 Accepted
Location: /reports/job-abc123/status
```
