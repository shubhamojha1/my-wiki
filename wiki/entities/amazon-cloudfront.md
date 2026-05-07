---
title: "Amazon CloudFront"
type: entity
tags: [aws, cdn, caching, edge-computing]
created: 2026-05-08
sources: ["https://aws.amazon.com/caching/"]
---

# Amazon CloudFront

**Type:** Global Content Delivery Network (CDN) service  
**Website:** [aws.amazon.com/cloudfront](https://aws.amazon.com/cloudfront/)

## Overview

Amazon CloudFront is a global CDN service that accelerates delivery of websites, APIs, video content, and other web assets. It uses a global network of edge locations to deliver cached copies of content to users from the nearest edge location.

## Key Capabilities

- Global edge network for low-latency content delivery
- Cache static: videos, webpages, images, JavaScript, CSS
- Configurable to retrieve dynamic data from origin servers
- Integrates with other AWS services
- No minimum usage commitments

## How It Works

- User requests content → routed to nearest edge location
- Cache hit: served immediately from edge
- Cache miss: fetched from origin, cached at edge, served to user
- Dramatically increases throughput for static assets

## Related Pages

- [[CDN]], [[Caching]], [[Web Caching]]
