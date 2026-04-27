---
title: "AlgoMaster: Aggregation"
type: source
tags: [lld, oop, relationships]
created: 2026-04-27
sources: ["algomaster.io/learn/lld/aggregation"]
author: Ashish Pratap Singh
---

# Aggregation

**Source:** AlgoMaster.io Low-Level Design Course — Aggregation Chapter

## Definition

**Aggregation** is a structural UML relationship representing a **"Has-A" relationship**. One class is part of another, but **both can exist independently**. This makes the relationship **loosely coupled**.

> "One class contains or references other objects that have their own lifecycle"

---

## UML Representation

- **Symbol**: Hollow diamond (◇) on containing class side + solid line
- **Direction**: From containing class to contained class

```
┌─────────────────┐◇─────────┐─────────────────┐
│    Department   │──────────│    Employee     │
├─────────────────┤          ├─────────────────┤
│ - name          │          │ - name          │
│ - employees[]   │──────▶   │ - id            │
└─────────────────┘          └─────────────────┘
```

### Multiplicity

| Notation | Meaning |
|----------|---------|
| `1` | Exactly one |
| `0..*` or `*` | Zero or more |
| `1..*` | One or more |
| `0..1` | Zero or one |
| `2..5` | Between 2 and 5 |

---

## Aggregation vs Association vs Composition

| Aspect | Association | Aggregation | Composition |
|--------|------------|-------------|-------------|
| Relationship | "Knows-about" | "Has-A" | "Owns-A" |
| Coupling | Loosest | Moderate | Tightest |
| Lifecycle | Independent | Independent | Parts die with whole |
| Symbol | Solid line | ◇ (hollow diamond) | ◆ (filled diamond) |
| Creation | Both created separately | Parts created outside | Whole creates parts |

---

## Code Examples

### Java

```java
public class Employee {
    private String name;
    private String empId;
    
    public Employee(String name, String empId) {
        this.name = name;
        this.empId = empId;
    }
}

public class Department {
    private String name;
    private List<Employee> employees = new ArrayList<>();
    
    public void addEmployee(Employee emp) {
        employees.add(emp);
    }
    
    public void removeEmployee(Employee emp) {
        employees.remove(emp);
    }
}

// Employee created independently
Employee emp = new Employee("Alice", "E001");

// Department Agregate: employee passed in (not created by department)
Department dept = new Department("Engineering");
dept.addEmployee(emp);

// Employee survives department deletion
```

### Python

```python
class Employee:
    def __init__(self, name: str, emp_id: str):
        self.name = name
        self.emp_id = emp_id

class Department:
    def __init__(self, name: str):
        self.name = name
        self._employees = []
    
    def add_employee(self, employee: Employee):
        self._employees.append(employee)
    
    def remove_employee(self, employee: Employee):
        self._employees.remove(employee)
```

---

## Key Insights

1. **Parts survive the whole** — Deleting Department doesn't delete Employee
2. **Parts created externally** — Employees exist before being added
3. **Reassignment allowed** — Employee can move to another Department
4. **Hollow diamond** distinguishes from Composition (filled diamond)

---

## Key Takeaways

1. Aggregation is a **"Has-A"** relationship with **independent lifecycle**
2. Represented by **hollow diamond (◇)** in UML
3. Parts can be **reassigned** to different wholes
4. Looser coupling than Composition, tighter than Association
5. Use when parts have meaning outside the container