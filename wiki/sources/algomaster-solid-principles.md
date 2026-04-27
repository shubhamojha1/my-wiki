---
title: "SOLID Principles Explained With Code"
type: source
tags: [lld, solid-principles]
created: 2026-04-27
sources: ["blog.algomaster.io/p/solid-principles-explained-with-code"]
author: Ashish Pratap Singh
---

# SOLID Principles Explained With Code

**Source:** AlgoMaster.io — SOLID Principles Chapter

Introduced by **Robert C. Martin (Uncle Bob)** in the early 2000s.

---

## Overview

| Principle | Core Concept |
|-----------|-------------|
| **S** | Single Responsibility |
| **O** | Open/Closed |
| **L** | Liskov Substitution |
| **I** | Interface Segregation |
| **D** | Dependency Inversion |

---

## S: Single Responsibility Principle (SRP)

> A class should have one, and only one, reason to change.

### Violation

```python
class UserManager:
    def authenticate(self, username, password):
        pass
    
    def update_profile(self, user_id, data):
        pass
    
    def send_email(self, recipient, subject, body):
        pass
```

Three responsibilities: auth, profile, email.

### Fix

```python
class Authenticator:
    def authenticate(self, username, password):
        pass

class UserProfileManager:
    def update_profile(self, user_id, data):
        pass

class EmailNotifier:
    def send_email(self, recipient, subject, body):
        pass
```

---

## O: Open/Closed Principle (OCP)

> Software entities should be open for extension, but closed for modification.

### Violation

```python
class ShapeCalculator:
    def calculate_area(self, shape):
        if shape.type == "rectangle":
            return shape.width * shape.height
        elif shape.type == "circle":
            return 3.14 * shape.radius * shape.radius
```

To add triangle → modify existing code.

### Fix

```python
class Shape(ABC):
    @abstractmethod
    def calculate_area(self): pass

class Rectangle(Shape):
    def calculate_area(self): return self.width * self.height

class Circle(Shape):
    def calculate_area(self): return 3.14 * self.radius * self.radius

class ShapeCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()
```

Add new shapes → new classes, no modification.

---

## L: Liskov Substitution Principle (LSP)

> Objects of a superclass should be replaceable with subclass objects.

### Violation

```python
class Vehicle:
    def start_engine(self): pass
    def stop_engine(self): pass

class Bicycle(Vehicle):
    def start_engine(self):
        print("This shouldn't be here...")  # Doesn't make sense
```

Bicycle has engine methods that don't apply.

### Fix

```python
class Vehicle:
    def start(self): pass

class Car(Vehicle):
    def start(self): print("Starting car engine...")

class Bicycle(Vehicle):
    def start(self): print("Rider is pedaling...")
```

All subclasses fulfill the contract meaningfully.

---

## I: Interface Segregation Principle (ISP)

> No client should be forced to depend on interfaces they don't use.

### Violation

```python
class MediaPlayer(ABC):
    @abstractmethod
    def play_audio(self): pass
    @abstractmethod
    def play_video(self): pass
    @abstractmethod
    def adjust_video_brightness(self): pass

class MP3Player(MediaPlayer):
    def play_video(self): pass  # Must implement unused methods
```

### Fix

```python
class AudioPlayer(ABC):
    @abstractmethod
    def play_audio(self): pass

class VideoPlayer(ABC):
    @abstractmethod
    def play_video(self): pass
    @abstractmethod
    def adjust_video_brightness(self): pass

class MP3Player(AudioPlayer):
    def play_audio(self): pass
```

Clients only depend on what they need.

---

## D: Dependency Inversion Principle (DIP)

> High-level modules should not depend on low-level modules; both should depend on abstractions.

### Violation

```python
class EmailService:
    def __init__(self):
        self.client = GmailClient()  # Concrete dependency
```

### Fix

```python
class EmailClient(ABC):
    @abstractmethod
    def send(self, to, subject, body): pass

class GmailClient(EmailClient):
    def send(self, to, subject, body): pass

class EmailService:
    def __init__(self, client: EmailClient):
        self.client = client

# Easy to swap implementations
gmail = EmailService(GmailClient())
outlook = EmailService(OutlookClient())
```

---

## Key Takeaways

1. **SRP** — One reason to change per class
2. **OCP** — Add features by extending, not modifying
3. **LSP** — Subclasses must fulfill base contracts
4. **ISP** — Small, focused interfaces
5. **DIP** — Depend on abstractions, not concretions