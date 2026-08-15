# 🐍 Advanced Python for Data Domain : Learning Journey
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/OOP-Advanced-brightgreen?style=for-the-badge)
![Async](https://img.shields.io/badge/Async-Await-orange?style=for-the-badge)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-violet?style=for-the-badge)
![Multithreading](https://img.shields.io/badge/Multi--Threading-Enabled-lightgrey?style=for-the-badge)
![PyTest](https://img.shields.io/badge/Testing-PyTest-red?style=for-the-badge)

---

## 📌 Section Overview

This repository is a **structured record of my advanced Python learning journey**, focused specifically on the concepts needed to write **production-grade Python in the Data Domain** — going beyond basics like loops and if-else into the patterns actually used in real data engineering and backend code.

The course moves from **core OOP fundamentals** → **advanced OOP (inheritance, polymorphism, decorators)** → **concurrency (multi-threading, async)** → **data validation with Pydantic** → **working with real APIs** → **testing with PyTest** → **systems-level scripting with the OS module**.

> The goal wasn't just "learning Python syntax" — it was learning to write Python the way it's actually used in data pipelines, backend services, and API-driven systems.

---

## 🎯 Aim & Objectives

- Build a strong, practical foundation in **Object-Oriented Programming**
- Understand **inheritance and polymorphism** well enough to design clean class hierarchies
- Use **decorators** to write reusable, non-repetitive logic
- Apply **multi-threading** for parallel processing of I/O-bound tasks
- Validate and enforce data structure using **Pydantic**
- Write **asynchronous Python** using `async`/`await` and coroutine orchestration
- Fetch and process real-world data from **APIs**
- Write reliable, testable code using **PyTest**
- Use the **OS module** for file/system-level operations

---

## 🧰 Tech Stack & Concepts

| Concept | Purpose |
|---|---|
| Python 3.x | Core language |
| OOP (Classes, Objects, Constructors) | Structuring real-world entities as code |
| Encapsulation | Controlling access to internal state |
| Inheritance & Polymorphism | Reusable, extensible class hierarchies |
| Decorators | Reusable, injectable behavior around functions |
| Threading | Parallel execution for I/O-bound workloads |
| Asyncio | Non-blocking, concurrent I/O |
| Pydantic | Schema validation & data modeling |
| Requests / APIs | Fetching real-world data |
| PyTest | Automated testing |
| OS Module | File system & environment interaction |

---

## 🏗️ Learning Architecture

```
OOP Fundamentals (Classes, Objects, Constructors, Encapsulation)
        ↓
Applied OOP (End-to-End Data Example, Class vs Static Methods)
        ↓
Advanced OOP (Inheritance, Polymorphism, Decorators)
        ↓
Concurrency (Multi-Threading, Async/Await, Coroutines)
        ↓
Data Validation (Pydantic)
        ↓
Real-World Integration (APIs)
        ↓
Reliability & Tooling (PyTest, OS Module)
```

---

## 🧩 Topic-by-Topic Breakdown

| # | Topic | Key Concepts Practiced | 
|---|---|---|
| 1 | OOP Overview | Why OOP matters in data code |
| 2 | Classes & Objects | Blueprints, instances, attributes | 
| 3 | Constructors | `__init__`, object initialization | 
| 4 | Encapsulation | Access modifiers (public/protected/private) | 
| 5 | End-to-End Data Example | Applying OOP to a real data problem | 
| 6 | Class vs Static Methods | `@classmethod`, `@staticmethod`, `cls` vs `self` |
| 7 | Inheritance | Single, multi-level, multiple inheritance | 
| 8 | Polymorphism | Method overriding, dynamic behavior | 
| 9 | Decorators | Function wrapping, `@` syntax | 
| 10 | Multi-Threading | `threading` module, parallel I/O tasks | 
| 11 | Pydantic | Schema validation, `BaseModel` | 
| 12 | Async Python | `async`/`await`, event loop |
| 13 | Coroutines with Gather | `asyncio.gather()` for concurrent execution | 
| 14 | APIs Overview & Fetching | REST basics, `requests`, JSON handling | 
| 15 | PyTest | Test functions, assertions, fixtures | 
| 16 | OS Module | File paths, environment variables, directories |

---

## 📖 Detailed Learnings

### 📗 OOP Overview & Classes/Objects
**Focus:** Understanding why data-domain code is modeled with objects instead of loose functions and variables.

- Learned how classes model real-world entities (e.g., a `Customer`, a `DataPipeline`) as reusable blueprints
- Practiced creating objects and understanding the relationship between a class and its instances

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email

cust = Customer("Ansh", "ansh@example.com")
```
**Takeaway:** OOP isn't academic — it's how real data pipelines model entities like customers, records, and jobs in a way that scales.

---

### 📗 Constructors
**Focus:** Controlling exactly how an object is initialized.

- Used `__init__` to set required state at creation time
- Understood the difference between instance attributes and default values

**Takeaway:** A well-designed constructor prevents "half-initialized" objects — a common source of bugs in larger codebases.

---

### 📗 Encapsulation — Access Modifiers
**Focus:** Controlling what parts of a class are exposed vs. protected.

- Practiced Python's convention-based access control: public, `_protected`, and `__private` attributes
- Understood name mangling and why Python enforces encapsulation by convention rather than strict keywords

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance  # private

    def get_balance(self):
        return self.__balance
```
**Takeaway:** Encapsulation protects internal state from being modified in unsafe ways — critical when objects represent sensitive data.

---

### 📗 End-to-End Python Data Example
**Focus:** Applying OOP to an actual data workflow instead of toy examples.

- Combined classes, constructors, and encapsulation into a working mini data pipeline
- Practiced structuring a real problem the way it would be approached in a data engineering codebase

**Takeaway:** This was the bridge between "I understand OOP syntax" and "I can structure a real data project using OOP."

---

### 📗 Class Methods vs Static Methods
**Focus:** Knowing when a method needs the class, the instance, or neither.

- `@staticmethod` — utility logic with no dependency on class or instance state
- `@classmethod` — logic that operates on the class itself (e.g., alternate constructors)

```python
class DateUtils:
    @staticmethod
    def is_weekend(day):
        return day in ("Saturday", "Sunday")

    @classmethod
    def from_string(cls, date_str):
        return cls(date_str)
```
**Takeaway:** Choosing the right method type communicates intent clearly to anyone reading the code later.

---

### 📗 Inheritance — Single, Multi-Level, Multiple
**Focus:** Reusing and extending behavior across related classes.

- **Single inheritance:** one child, one parent
- **Multi-level inheritance:** a chain of parent → child → grandchild
- **Multiple inheritance:** a class inheriting from more than one parent, and how Python resolves method conflicts (MRO)

```python
class Employee:
    def work(self):
        return "Working..."

class Manager(Employee):
    def approve(self):
        return "Approved"
```
**Takeaway:** Inheritance done right avoids duplicated logic — done wrong, it creates fragile hierarchies. Understanding MRO was key to avoiding that trap.

---

### 📗 Polymorphism
**Focus:** Writing code that works across different object types without knowing their exact class in advance.

- Practiced method overriding so subclasses provide their own implementation of a shared interface
- Learned how polymorphism enables writing generic functions that work on any compatible object

```python
class Shape:
    def area(self):
        raise NotImplementedError

class Circle(Shape):
    def area(self):
        return 3.14 * self.radius ** 2
```
**Takeaway:** Polymorphism is what makes large codebases extensible — new types can be added without changing the code that consumes them.

---

### 📗 Decorators
**Focus:** Adding reusable behavior to functions without modifying their internals.

- Wrote custom decorators using `@` syntax
- Understood decorators as functions that wrap other functions — commonly used for logging, timing, and validation in real projects

```python
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@log_execution
def fetch_data():
    ...
```
**Takeaway:** Decorators are everywhere in real Python data code — from `@app.route` in Flask to `@retry` logic in data pipelines. This chapter demystified how they actually work.

---

### 📗 Multi-Threading for Parallel Processing
**Focus:** Speeding up I/O-bound tasks by running them concurrently.

- Used Python's `threading` module to run multiple tasks in parallel (e.g., simultaneous API calls or file reads)
- Understood where threading helps (I/O-bound work) versus where it doesn't (CPU-bound work, due to the GIL)

```python
import threading

def fetch(url):
    ...

threads = [threading.Thread(target=fetch, args=(url,)) for url in urls]
for t in threads: t.start()
for t in threads: t.join()
```
**Takeaway:** Threading is a practical tool for speeding up data pipelines that spend most of their time waiting on network or disk I/O.

---

### 📗 Pydantic for Schema Validation
**Focus:** Enforcing structure and type-safety on data flowing through a system.

- Defined data models using `BaseModel`
- Let Pydantic automatically validate types, required fields, and raise clear errors on bad data

```python
from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float

p = Product(id=1, name="Widget", price=9.99)
```
**Takeaway:** Pydantic turns "hope the data is correct" into "guarantee the data is correct" — essential when ingesting real-world, messy data.

---

### 📗 Async Python & Coroutines with Gather
**Focus:** Writing non-blocking code for high-throughput I/O operations.

- Learned `async`/`await` syntax and how Python's event loop schedules coroutines
- Used `asyncio.gather()` to run multiple coroutines concurrently and collect their results together

```python
import asyncio

async def fetch(url):
    ...

async def main():
    results = await asyncio.gather(fetch(u1), fetch(u2), fetch(u3))

asyncio.run(main())
```
**Takeaway:** Async is the modern approach to high-concurrency I/O — especially relevant when fetching data from multiple APIs or sources simultaneously.

---

### 📗 APIs Overview & Fetching Data
**Focus:** Getting real data into Python from external systems.

- Understood REST API fundamentals — endpoints, methods, status codes, headers
- Used `requests` to call APIs and parse JSON responses into usable Python objects
- Combined this with Pydantic to validate incoming API data

```python
import requests

response = requests.get("https://api.example.com/data")
data = response.json()
```
**Takeaway:** Almost every real data pipeline starts with pulling data from an API — this chapter connected everything learned so far (OOP, validation, async) into one practical skill.

---

### 📗 PyTest
**Focus:** Making sure code actually works, and keeps working.

- Wrote test functions using PyTest's simple `assert`-based syntax
- Learned how PyTest auto-discovers tests and reports failures clearly

```python
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
```
**Takeaway:** Untested code is a liability in any real project — PyTest made writing tests fast enough that there's no excuse to skip it.

---

### 📗 OS Module
**Focus:** Interacting with the file system and environment from Python.

- Used `os` to work with file paths, list directories, and read environment variables
- Practiced writing OS-aware code that behaves correctly across environments

```python
import os

files = os.listdir(".")
api_key = os.environ.get("API_KEY")
```
**Takeaway:** Real data scripts constantly touch the file system and environment configuration — the OS module is the practical glue for that.

---

## 🧠 Skills Demonstrated

- ✅ **Object-Oriented Design:** Classes, constructors, encapsulation, class/static methods
- ✅ **Advanced OOP:** Inheritance (single/multi-level/multiple), polymorphism
- ✅ **Reusable Patterns:** Decorators for cross-cutting logic
- ✅ **Concurrency:** Multi-threading for parallel I/O, async/await for non-blocking execution
- ✅ **Data Validation:** Pydantic-based schema enforcement
- ✅ **Real-World Integration:** Fetching and parsing data from live APIs
- ✅ **Reliability:** Automated testing with PyTest
- ✅ **Systems Scripting:** File and environment handling with the OS module

---

## ▶️ How to Run Locally

### Prerequisites
- Python 3.10+
- `pip`

### Steps
```bash
# 1. Clone the repository
git clone <repository-url>

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install pydantic requests pytest

# 4. Run any script
python <script_name>.py

# 5. Run tests
pytest
```

---

## 📂 Repository Structure

```
Python-Advanced/
├── Ch-1_OOP/
├── Ch-2_Inheritance/
├── Ch-3_Polymorphism&Decorators/
├── Ch-4_Multi-Threading/
├── Ch-5_Pydantic/
├── Ch-6_Async/
├── Ch-7_APIs/
├── Ch-8_PyTest/
└── Ch-9_OS/
```

---


