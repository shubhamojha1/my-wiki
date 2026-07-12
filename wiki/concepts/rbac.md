---
title: "RBAC"
type: concept
tags: [api, security, auth]
created: 2026-07-10
sources: ["hellointerview-api-design"]
---

# RBAC

**Role-Based Access Control** — an authorization model that assigns *roles* to users and *permissions* to roles, rather than granting permissions to individual users directly.

## Example

A ticketing platform's roles:

- **Customer** — can book tickets, view own bookings
- **Venue manager** — can create events, view sales for their venues
- **Admin** — can access everything

A request handler checks the caller's role against the permission required for the action, in addition to the separate check that the caller is authenticated at all.

## Why Roles Instead of Per-User Permissions

Assigning permissions per-role instead of per-user keeps the permission set small and centrally auditable — adding a new customer doesn't require configuring their individual permissions, it just requires assigning the existing `customer` role. Changing what customers can do means editing one role definition, not every customer's record.

## Related Concepts

- [[Authentication vs. Authorization]] — RBAC is the mechanism that implements the authorization half of that distinction
- [[JWT]] — role claims are often embedded directly in a JWT so authorization checks don't require a separate lookup
- [[Access Modifiers]] — a loosely analogous idea at the code level (private/protected/public) rather than the request level
