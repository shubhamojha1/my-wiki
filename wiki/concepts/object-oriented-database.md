---
title: "Object-Oriented Database"
type: concept
tags: [database, oop]
created: 2026-05-11
updated: 2026-05-20
sources: [algomaster-15-db-types]
---

# Object-Oriented Database (OODB)

An **object-oriented database** stores and retrieves data as full objects — instances of classes with attributes, methods, inheritance, and reference relationships — eliminating the **object-relational impedance mismatch** that requires an ORM layer in traditional relational databases.

## The Impedance Mismatch Problem

In relational databases, a tree of in-memory objects must be flattened into tables (one table per class, join tables for associations, serialized BLOBs for nested objects). OODBs eliminate this by persisting objects directly in the format the application uses them.

```
OOP model:                      Relational model:
                                (requires ORM mapping)
Order {                         orders(id, customer_id, date)
  customer: Customer,   →       customers(id, name, email)
  items: [OrderItem],           order_items(order_id, product_id, qty)
  total(): float                products(id, name, price)
}
```

## Characteristics

| Property | Description |
|----------|-------------|
| **Object persistence** | Objects stored in native form; no ORM needed |
| **Encapsulation** | Methods stored alongside data |
| **Inheritance** | Class hierarchies modeled directly in the schema |
| **Object identity** | Each object has a unique OID; references are navigated, not joined |
| **Complex types** | Lists, nested objects, polymorphism — native support |

## Navigation vs Queries

OODBs use **object navigation** (follow references between objects) rather than SQL JOINs:

```java
// ODB navigation (no SQL)
Order order = db.getObjectById(orderId);
String customerName = order.getCustomer().getName();

// vs. SQL JOIN
SELECT c.name FROM orders o JOIN customers c ON o.customer_id = c.id WHERE o.id = ?
```

## Trade-offs vs Relational

| Aspect | OODB | Relational DB |
|--------|------|--------------|
| Impedance mismatch | None | Requires ORM |
| Ad-hoc queries | Limited (schema tied to app) | Flexible SQL |
| Analytics / reporting | Poor | Excellent |
| Maturity / ecosystem | Niche | Dominant |
| Standardization | Lacks a universal query language | SQL standard |

## Where OODBs Are Used Today

Object-oriented databases peaked in the 1990s and never displaced relational databases. Today their concepts survive in:
- **Document databases** (MongoDB, CouchDB): JSON documents ≈ serialized objects
- **ORMs** (Hibernate, SQLAlchemy): simulate OODB experience on top of relational
- **Embedded databases** (realm for mobile): object persistence without a server

## Related Concepts

- [[Relational Model]] — the dominant alternative; requires ORM for OOP languages
- [[Document Database]] — the modern heir to OODB concepts
- [[Embedded Database]] — common deployment model for OODBs
