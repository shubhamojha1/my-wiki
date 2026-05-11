---
title: "Blob Datastore"
type: concept
tags: [database, storage, blob]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Blob Datastore

A **blob datastore** (Binary Large Object) is designed for storing, managing, and retrieving large blocks of unstructured data — images, audio, video, documents, and backups.

## Characteristics

- **Unstructured**: No schema, no fixed fields
- **Massive scale**: Petabytes+ of data
- **Durable**: Data replicated across multiple facilities
- **Cost-tiered**: Hot, cool, archive storage classes
- **HTTP-accessible**: RESTful API for upload/download

## Use Cases

- **CDN content**: Videos, images distributed globally
- **Backup and archival**: Cost-effective long-term retention
- **Big data storage**: Raw logs, sensor data for analytics
- **Static assets**: Application binaries, installers

## Examples

- Amazon S3 — Industry-standard object storage
- Azure Blob Storage — Microsoft's cloud object store
- HDFS — Hadoop Distributed File System for big data

## Related

- [[CDN]] — Often paired with blob datastores for delivery
- [[Key-Value Store]] — Similar key-based access, but for blobs
