---
title: "Spatial Index"
type: concept
tags: [database, index, spatial, geo]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-indexing]
---

# Spatial Index

A **spatial index** organizes multi-dimensional geometric or geographic data to enable efficient spatial queries — nearest-neighbor, range, intersection, and containment searches. Standard B+tree indexes are useless for 2D/3D data because they can only sort on one dimension at a time.

## Why B+Tree Fails for Spatial Data

A B+tree on latitude finds rows with latitude ≈ 37.7 quickly, but still requires a full scan over those rows to filter by longitude. The dimensionality mismatch makes it O(n) in the worst case for bounding-box queries.

## Underlying Data Structures

### R-Tree (Most Common)

Groups nearby objects into hierarchical **minimum bounding rectangles (MBRs)**:

```
Root MBR: [US bounding box]
  ├─ MBR1: [California bounding box]
  │    ├─ Point: San Francisco (37.77, -122.41)
  │    └─ Point: Los Angeles   (34.05, -118.24)
  └─ MBR2: [New York bounding box]
       └─ Point: New York City (40.71, -74.00)
```

Lookup: compare query bounding box with MBRs top-down; prune branches that don't intersect. O(log n) for well-distributed data.

### Other Structures

| Structure | Description | Best For |
|-----------|-------------|---------|
| **R-Tree** | Hierarchical MBRs | General polygons, bounding boxes |
| **R*-Tree** | Optimized R-Tree with better splitting heuristic | Higher query performance |
| **Quadtree** | Recursive 4-way space partitioning | Uniform point data |
| **KD-Tree** | Alternating axis splits (K-dimensional) | Nearest-neighbor in low dimensions |
| **S2 / Geohash** | Project globe onto grid (S2 uses Hilbert curve cells) | Global geo data, cell-based indexing |

## Supported Query Types

| Query | Example | Operator |
|-------|---------|---------|
| **Point in polygon** | Is this coordinate inside the delivery zone? | `ST_Contains` |
| **Intersects** | Which roads cross this bounding box? | `ST_Intersects` |
| **Within distance** | Restaurants within 500m | `ST_DWithin` |
| **Nearest neighbor** | Closest 5 ATMs to my location | `<->` (KNN) |
| **Bounding box** | Objects in view port [lat1,lon1,lat2,lon2] | `&&` |

## Database Support

| Database | Spatial Extension | Index Type |
|----------|------------------|-----------|
| PostgreSQL | PostGIS | GiST / SP-GiST / BRIN |
| MySQL 8+ | Native geometry | R-Tree (`SPATIAL INDEX`) |
| Oracle | Oracle Spatial | R-Tree |
| SQLite | SpatiaLite | R-Tree (via FTS5) |
| MongoDB | Native geo | 2dsphere (S2 cells) |

## Related Concepts

- [[Database Index]] — general index concepts
- [[B+Tree]] — one-dimensional; unsuitable for spatial data
- [[Geo-Based Sharding]] — sharding by geography; uses spatial locality
