# From Concept to Implementation: Object-Oriented Programming in Action

This repository presents three Python projects designed to illuminate key principles of **Object-Oriented Programming (OOP)**—including **encapsulation**, **initialization**, **instance variables**, **data validation**, and **library-based inheritance**.

Each script introduces or interacts with custom classes and methods that reflect OOP usage in real-world software design.

##  1. `jar.py` — Cookie Jar Class

### 📘 Concept
`jar.py` implements a `Jar` class to simulate a cookie jar. The program leverages **encapsulation**, **property decorators**, and **method design** to provide controlled interaction with the jar's internal state.

### 🧱 Class Breakdown

```python
class Jar:
    def __init__(self, capacity=12):
        ...
    def __str__(self): 
        ...
    def deposit(self, n):
        ...
    def withdraw(self, n):
        ...
    @property
    def capacity(self):
        ...
    @property
    def size(self):
        ...
```

OOP Features
- **Encapsulation**: The `Jar` class encapsulates cookie management logic, exposing only necessary methods and properties. Encapsulation ensures `size` is private and accessible via methods/properties only.
- **Initialization**: The `__init__` method sets up the jar with a default capacity of 12 cookies, which can be adjusted.
- **Instance Variables**: The `size` variable tracks the current number of cookies, while `capacity` defines the maximum allowed.
- **Data Validation**: Methods like `deposit` and `withdraw` include checks to ensure cookie counts remain within bounds, preventing overfilling or negative counts.
- **String Representation**: The `__str__()` method returns a visual emoji-based representation of jar contents.

## 2. seasons.py — Lifetime Minutes Converter

### 📘 Concept
seasons.py prompts the user for a birth date and converts their age into minutes lived, expressed in natural language. While primarily functional, it demonstrates modular design, data parsing, and composition.

### Core Functions

- **get_birth_date()** handles input parsing and validation.

- **calculate_minutes(birth_date)** computes elapsed minutes.

- **convert_to_words(minutes)** uses inflect to return verbal output.

Though not class-based, the design is structured and could be extended into a class model in future iterations.

### Tests
Includes test_seasons.py for unit testing with pytest.

## 3. shirtificate.py — Personalized PDF Generator

### 📘 Concept
Generates a PDF certificate with the user's name on a CS50 shirt graphic. The script interacts with the FPDF class, showcasing class instantiation, method chaining, and library-based inheritance.

### Implementation Flow

```python   
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Helvetica", size=32)
pdf.image("shirtificate.png", x=10, y=30, w=190)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 10, "CS50 Shirtificate", align="C")
pdf.output("shirtificate.pdf")
```

OOP Interactions

- Utilizes FPDF as a third-party class with extensible methods.

- Dynamically adds content and styles to a blank PDF canvas.

- Centers the user's name on a shirt template to create a personalized certificate.


### Summary

Each project demonstrates a core OOP principle:

- jar.py: Encapsulation, properties, and validation

- seasons.py: Modular logic and data composition

- shirtificate.py: Inheritance and method chaining with a third-party class

Together, these scripts help solidify object-oriented design patterns in Python.

Feel free to fork, modify, and build upon these examples to further explore OOP design.