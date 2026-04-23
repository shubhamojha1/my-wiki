---
title: "Composition"
type: concept
tags: [oop, relationships, has-a, ownership]
created: 2026-04-23
sources: ["blog.algomaster.io/p/12-oop-concepts-every-developer-should-know"]
---

# Composition

**Definition:** A strong "has-a" relationship where the whole **owns** the parts entirely. When the whole is destroyed, the parts are destroyed with it. Parts have no meaning outside the whole.

## Real-World Example

Order ↔ LineItems:
- Each line item (2x T-Shirt, 1x Laptop) only exists as part of that order
- If the order is cancelled/deleted, line items go with it
- A line item floating around without an order makes no sense

## Code Example

```java
public class Order {
    private String orderId;
    private List<LineItem> lineItems;  // Order owns these

    public Order(String orderId) {
        this.orderId = orderId;
        this.lineItems = new ArrayList<>();
    }

    // Order creates line items internally
    public void addItem(String productId, String productName, int quantity, double price) {
        lineItems.add(new LineItem(productId, productName, quantity, price));
    }

    public double getTotal() {
        return lineItems.stream()
            .mapToDouble(LineItem::getSubtotal)
            .sum();
    }

    public void cancel() {
        lineItems.clear();  // Line items destroyed with order
    }
}

public class LineItem {
    private String productId;
    private String productName;
    private int quantity;
    private double unitPrice;

    // Package-private: only Order creates line items
    LineItem(...) { ... }

    double getSubtotal() {
        return quantity * unitPrice;
    }
}

// Order creates line items internally
Order order = new Order("ORD-001");
order.addItem("SKU-100", "Mechanical Keyboard", 1, 149.99);
order.addItem("SKU-200", "USB-C Hub", 2, 39.99);
order.cancel();  // Line items destroyed
```

## Composition vs Aggregation

| Aspect | Composition | Aggregation |
|--------|-------------|-------------|
| Creation | Whole creates parts | Parts passed in from outside |
| Lifecycle | Parts die with whole | Parts survive whole |
| Ownership | Strong (owns) | Weak (references) |
| "Is-a" test | "Order has LineItems" | "Team has Services" |

## Related Concepts

[[Aggregation]], [[Association]], [[Ownership]], [[Lifecycle Control]]