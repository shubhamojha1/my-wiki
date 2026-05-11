---
title: "Object-Oriented Database"
type: concept
tags: [database, oop]
created: 2026-05-11
sources: [algomaster-15-db-types]
---

# Object-Oriented Database

An **object-oriented database (OODB)** stores and manipulates data as objects — instances of classes that encapsulate both attributes and methods, mirroring object-oriented programming languages.

## Characteristics

- **Object persistence**: Store objects directly without ORM mapping
- **Encapsulation**: Data + methods stored together
- **Inheritance**: Class hierarchies supported
- **Navigation**: Follow object references (pointer chasing) instead of joins
- **Tight integration**: Works directly with OOP languages (Java, C++, Python)

## Use Cases

- **OOP-native applications**: Seamless persistence without ORM
- **Multimedia databases**: Images, videos, audio with embedded behaviors
- **CAD/CAM systems**: Complex engineering objects with nested structures

## Examples

- ObjectDB — Java-oriented OODB
- db4o — Embedded Java/.NET OODB

## Related

- [[Relational Model]] — Traditional alternative requiring ORM mapping
- [[Document Database]] — Stores objects as JSON/BSON documents
- [[Embedded Database]] — Often used for OODB deployment
