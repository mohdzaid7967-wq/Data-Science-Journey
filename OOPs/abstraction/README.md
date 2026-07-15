# Python Abstraction

This folder contains examples of **Abstraction** in Python using the `abc` (Abstract Base Class) module.

## What is Abstraction?

Abstraction is one of the four pillars of Object-Oriented Programming (OOP).

It means **hiding the implementation details and showing only the essential functionality**.

In Python, abstraction is implemented using the `ABC` module and the `@abstractmethod` decorator.

---

## Example

In this example:

- `Greet` is an abstract base class.
- `say_hello()` is an abstract method.
- `English` inherits from `Greet` and provides the implementation of `say_hello()`.

### Code

```python
from abc import ABC, abstractmethod

class Greet(ABC):
    @abstractmethod
    def say_hello(self):
        pass

class English(Greet):
    def say_hello(self):
        return "Hello!"

g = English()
print(g.say_hello())
```

---

## Output

```
Hello!
```

---

## Key Concepts

- Abstract Base Class (`ABC`)
- `@abstractmethod`
- Method Implementation
- Inheritance
- Object-Oriented Programming (OOP)

---

## Learning Outcome

After completing this example, you will understand:

- What abstraction is
- Why abstract classes are used
- How to create an abstract class
- How child classes implement abstract methods
- How abstraction helps create clean and maintainable code

---

## Author

**Mohd Zaid**

Learning Python and Data Science 🚀