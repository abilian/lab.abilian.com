In his 2022 talk, "The Classic Design Patterns: Where Are They Now?", Brandon Rhodes provides a modern survey of the 23 patterns from the influential 1994 "Gang of Four" book, Design Patterns. His goal is to evaluate their relevance in an era of powerful, multi-paradigm languages. Rhodes argues that while some patterns remain foundational, many have become obsolete workarounds, have been absorbed into languages as built-in features, or even represent anti-patterns in a modern, data-centric world. By categorizing each pattern, he reveals the major shifts in software design over the last three decades, offering a lens through which to understand how we program today.

Based on: https://rhodesmill.org/brandon/slides/2022-11-codedive/slides.html

See also:
- https://www.norvig.com/design-patterns/ (1996!)
- http://www.aleax.it/gdd_pydp.pdf / https://www.youtube.com/watch?v=4KZx8bATBFs (2007)
- More: https://github.com/slavikdev/design-patterns-in-dynamic-languages

### **6 patterns: useless if you have 1st-class functions**

These patterns are workarounds for object-oriented languages that lack the ability to pass functions or classes as arguments. In modern languages, they are replaced by simpler, more direct approaches.

1.  **Strategy:** Instead of creating multiple single-method classes to hold different algorithms, you can just pass the required function directly.
2.  **Command:** While useful in some contexts (see below), the basic idea of wrapping an action in an object is often replaced by passing a function (e.g., a callback).
3.  **Template Method:** This pattern uses inheritance to customize an algorithm's steps. The modern approach is to favor composition and simply pass in the functions that perform the custom steps.
4.  **Factory Method & Abstract Factory:** These patterns create objects. This is now more easily solved by passing the class constructor or a function that creates the object.
5.  **Prototype:** This pattern uses a `clone()` method on a pre-built object to create new instances. This is unnecessary when you can just pass the class and its constructor arguments to whatever needs to create the object.
6.  **Singleton:** The *pattern* of contorting a class to prevent more than one instance is overly complex. It's simpler to just create a single instance and make it globally available.

### **2 patterns: language built-ins**

These patterns were so useful that their core concepts have been integrated directly into modern programming languages, making the manual pattern obsolete.

1.  **Iterator:** This pattern for sequential access is now handled by language features like **generators** (`yield`), which allow both the producer and consumer of data to be written with simple, linear control flow.
2.  **Visitor:** This pattern for performing an operation on all elements of a complex data structure is also solved more elegantly by **generators**, which can traverse the structure and `yield` each item.

### **3 patterns: are anti-patterns that obscure our data**

These patterns violate the principle of putting data first, instead hiding it behind complex layers of control flow or language-specific formats.

1.  **Proxy:** This pattern hides the reality of network communication. Instead of using a transparent object proxy, modern services use explicit data formats (like JSON) over well-defined remote procedures.
2.  **Memento:** This pattern saves an object's state in an opaque, often language-specific binary format. Data should be persisted in an independent, accessible format (like JSON, CSV, or a database).
3.  **Observer:** This pattern creates a complex web of objects subscribed to each other's state changes. Modern approaches (like React) favor a centralized state data structure that, when changed, triggers a re-render of the view.

### **4 patterns: decompose big classes, but are obscure**

These patterns break the assumption that one real-world concept should be one class. They disassemble functionality into multiple classes, using them to organize procedures into layers rather than to represent data.

1.  **Bridge:** Separates an abstraction from its implementation, resulting in two class hierarchies instead of one.
2.  **Decorator:** Wraps an object with another object of the same interface to add functionality, leading to layers of objects.
3.  **Mediator:** Centralizes complex communications between objects into a separate mediator object, rather than having the objects interact directly.
4.  **State:** Encapsulates the varying behavior of an object into separate state objects, replacing a large conditional block.

### **3 patterns: small but useful**

These are practical, focused patterns that remain useful for solving specific, common problems.

1.  **Builder:** Provides a dedicated object whose methods are used to construct a complex object or hierarchy of objects (e.g., Matplotlib's `axis` object building a plot).
2.  **Adapter:** Wraps an object to provide a different interface that a client expects (e.g., Python's `socket.makefile()` making a network socket behave like a file).
3.  **Flyweight:** A memory optimization that allows many objects to share common, immutable data instead of each holding its own copy (e.g., Python caching small integer objects).

### **4 patterns: huge and dominate our frameworks**

These patterns are foundational to the architecture of most modern GUI and web frameworks.

1.  **Composite:** Gives all nodes in a tree structure (like UI elements) the same interface, allowing individual objects and compositions of objects to be treated uniformly (e.g., the browser DOM).
2.  **Chain of Responsibility:** Passes a request along a chain of handlers. In UI frameworks, this is how events "bubble" up from a child element to its parent.
3.  **Command:** Represents an action as an object, which is essential for implementing undo/redo functionality in GUIs and transactional operations like database migrations (e.g., Django migrations).
4.  **Interpreter:** Uses a composite structure (an Abstract Syntax Tree) to represent and execute operations, where each node in the tree has an `eval()` or `execute()` method.

### **1 pattern: ambitious but fatally limited**

This pattern describes an idea that is useful in theory but whose strict definition doesn't align with how real-world systems are actually built.

1.  **Facade:** Proposes hiding a complex subsystem behind a *single* API object. In practice, powerful APIs like jQuery or Pandas are not single objects—they provide access to a system through multiple interacting objects (e.g., a Pandas DataFrame returns a Series) and usually allow access to the underlying system.

### Conclusion

Brandon Rhodes' survey of the classic design patterns illustrates a clear trajectory in software engineering. The patterns that have faded are largely those that compensate for language deficiencies (like a lack of first-class functions) or that violate the modern principle of prioritizing clear, explicit data structures. The talk champions a data-centric philosophy—epitomized by React's state model and Fred Brooks' maxim, "Show me your tables"—over complex, hidden control flow. The patterns that endure, particularly the "framework patterns," remain powerful because they provide robust architectural skeletons for complex systems. Ultimately, the presentation uses the Gang of Four's work as a historical benchmark to demonstrate how the industry has moved toward more direct, flexible, and data-oriented solutions.

---
## Annex: Comparison with Historical Perspectives

Brandon Rhodes’ 2022 presentation provides a modern, retrospective analysis of the Gang of Four (GoF) design patterns. However, his core conclusions are not new; they represent the culmination of decades of experience from programmers using dynamic languages. Presentations from Peter Norvig (1996) and Alex Martelli (2007) show that many of Rhodes' key arguments were being made long ago, illustrating a consistent evolution of thought.

### Peter Norvig (1996): The Dynamic Language Perspective

Presented just two years after the GoF book was published, Norvig's talk is a direct reaction from the perspective of dynamic languages like Lisp and Dylan. It makes a powerful argument that the GoF patterns are largely workarounds for the limitations of static languages like C++.

*   **Core Argument:** Norvig’s central thesis is that "Dynamic Languages have fewer language limitations," and therefore "less need for bookkeeping objects and classes." He states that **16 of the 23 GoF patterns** have a "qualitatively simpler implementation" or are "invisible" in Lisp/Dylan.

*   **Direct Parallels to Rhodes:** Norvig anticipates Rhodes' primary critique almost perfectly.
    *   **First-Class Functions & Types:** Norvig’s main argument rests on the power of first-class functions and types, the same foundation as Rhodes’ first category ("useless if you have 1st-class functions").
        *   **Abstract Factory:** Norvig shows that the dual hierarchy of `GUIFactory` and `Window` is unnecessary. You can just pass the `NTWindow` or `MotifWindow` *type* itself as an argument, because types are runtime objects. This is identical to Rhodes' point.
        *   **Strategy:** Norvig states the pattern becomes "invisible" because the strategy is simply a variable whose value is a function. No `Strategy` class is needed.
        *   **Command, Visitor, Template-Method:** These are also listed by Norvig as being simplified by first-class functions.

*   **Unique Contributions:**
    *   **Broader Language Features:** Norvig attributes pattern simplification to a wider range of dynamic features beyond first-class functions, including **Macros** (simplifying Interpreter and Iterator), **Multimethods** (simplifying Builder), and **Modules** (making Facade invisible).
    *   **New Dynamic Patterns:** Norvig goes further than just simplifying existing patterns; he proposes new patterns enabled by dynamic languages, such as **Memoization**, **Compiler**, and **Partial Evaluation**.

In essence, Norvig's 1996 talk is the original blueprint for Rhodes' 2022 critique, demonstrating that from the very beginning, the dynamic language community viewed many GoF patterns as solutions to problems they didn't have.

### Alex Martelli (2007): The Pythonic Perspective

Martelli's 2007 talk, focused specifically on Python, serves as a practical bridge between Norvig's abstract argument and Rhodes' modern summary. It is less a critique of the GoF book and more a guide on how to "translate" its concepts into idiomatic Python, a process that often results in the original pattern dissolving.

*   **Core Argument:** Design patterns MUST be studied in a language's context. In Python, features like duck typing, first-class callables, and dynamic composition change how patterns are implemented, often making them simpler or different in form.

*   **Direct Parallels to Rhodes:**
    *   **Creational Patterns:** Martelli explicitly states that creational patterns are "not very common in Python...because 'factory' is essentially built-in!" This mirrors Rhodes’ conclusion that factories are unnecessary when you can just pass a class or function.
    *   **Singleton:** Martelli provides a detailed, practical look at the problematic `Singleton` pattern and offers the `Monostate` ("Borg") pattern as a more flexible Pythonic alternative, reinforcing Rhodes' point that the classic pattern is flawed.
    *   **Favor Composition:** He emphasizes the principle "favor object composition over class inheritance," which is a cornerstone of Rhodes' reasoning, and shows how Python does this via holding and wrapping.

*   **Unique Contributions:**
    *   **Practical Implementation:** Where Norvig and Rhodes are more conceptual, Martelli provides concrete code for Pythonic adaptations, such as different forms of the **Adapter** pattern (object, class, mixin) and variations on the **Template Method**.
    *   **Clarifying Language:** He re-brands the "Template Method" pattern with the more descriptive name **"self-delegation"** to better capture its essence, and shows how Python's introspection (`getattr`) makes it especially powerful.

Martelli’s presentation shows the principles Norvig discussed fully realized in a mature, mainstream dynamic language. He demonstrates *how* the patterns transform, providing the practical evidence for the high-level conclusions Rhodes would later summarize.

### Conclusion

The three presentations tell a remarkably consistent story across a 26-year span.

1.  **Norvig (1996)** made the initial, prescient argument that the GoF patterns were heavily influenced by the constraints of C++ and that dynamic languages had already solved many of the underlying problems.
2.  **Martelli (2007)** provided a practical, code-driven demonstration of Norvig’s thesis within the Python ecosystem, showing how to implement pattern *intent* in a "Pythonic" way, which often meant the formal pattern disappeared.
3.  **Rhodes (2022)** offers a modern capstone to this line of thinking. He synthesizes these long-standing arguments and adds a new, contemporary layer of analysis focused on **data-centric architecture** (e.g., React, shallow call stacks), using it to critique patterns like Observer, Proxy, and Memento—a perspective not present in the earlier talks.

## Bonus: Extra Patterns

Besides the Gof, there are several other patterns that are highly relevant to modern Python development.

The core philosophy derived from these presentations is that a "Pythonic" pattern should:
*   Leverage the language's dynamic features (first-class functions, generators, introspection).
*   Favor simple data structures and composition over complex class hierarchies.
*   Feel natural and idiomatic, rather than a direct translation from a more rigid language like C++ or Java.

Here are some non-GoF patterns that fit this philosophy perfectly:

### 1. The Context Manager Pattern

**Intent:** To allocate and release resources precisely when needed, ensuring cleanup happens even in the case of errors.

**Implementation:** This pattern is formalized directly into the language via the `with` statement and the `__enter__` and `__exit__` dunder methods, or the `@contextmanager` decorator in the `contextlib` module.

**How it Aligns with the Insights:**
*   **Replaces Manual Workarounds:** It provides a robust, built-in solution for a problem that would otherwise require a verbose and error-prone `try...finally` block. This aligns with Norvig's point about good language features making patterns "invisible."
*   **Explicitness and Readability:** The `with` block clearly defines the scope where a resource is active, aligning with Python's "explicit is better than implicit" ethos.
*   **Composition:** Context managers are highly composable. You can nest `with` statements or manage multiple items in a single statement (in Python 3).

**Example:**
```python
# Instead of this:
lock.acquire()
try:
    # do something...
finally:
    lock.release()

# The pattern provides this:
with lock:
    # do something...
```

### 2. The Decorator Pattern (Python's Implementation)

**Intent:** To add functionality to an existing function or method dynamically without changing its source code.

**Implementation:** While Decorator is a GoF pattern, its Pythonic implementation using the `@` syntax is a language feature that makes it a fundamentally different experience. It's a direct application of higher-order functions.

**How it Aligns with the Insights:**
*   **First-Class Functions:** This is the poster child for leveraging first-class functions, a key point from both Norvig and Rhodes for simplifying patterns.
*   **Syntactic Abstraction (Norvig):** The `@` syntax is a form of macro that builds a more expressive language. You are modifying behavior declaratively.
*   **Composition Over Inheritance (Martelli):** Decorators are a prime way to add behavior (like logging, caching, or authentication) to functions without forcing them into a class hierarchy.

**Example (Memoization, another pattern Norvig mentioned):**

```python
import functools

@functools.lru_cache(maxsize=None)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

### 3. The Pipeline Pattern (using Generators)

**Intent:** To process a stream of data through a series of lazy, memory-efficient, composable steps.

**Implementation:** This pattern is achieved by chaining generators together. Each generator performs one step of the work and `yield`s its result to the next stage in the pipeline.

**How it Aligns with the Insights:**
*   **Data-Centric & Lazy Evaluation (Rhodes):** This pattern is the epitome of Rhodes' advice. It processes data efficiently without loading everything into memory. The control flow is simple and linear.
*   **Decoupling Producer/Consumer:** Each step in the pipeline is a self-contained unit, completely decoupled from the others. You can easily add, remove, or reorder steps.
*   **Simplicity:** It avoids the need for complex Iterator classes (Norvig) by using a fundamental language feature (`yield`).

**Example:**

```python
def read_logs(filename):
    with open(filename) as f:
        for line in f:
            yield line

def filter_errors(lines):
    for line in lines:
        if "ERROR" in line:
            yield line

def parse_log_entry(lines):
    for line in lines:
        yield {'timestamp': line[0:19], 'message': line[20:].strip()}

# The pipeline
logs = read_logs('app.log')
errors = filter_errors(logs)
parsed = parse_log_entry(errors)

for entry in parsed:
    print(entry)
```

### 4. Dependency Injection (Lightweight)

**Intent:** To decouple a component from its dependencies by "injecting" them from the outside, rather than having the component create them itself.

**Implementation:** In Python, this rarely requires a complex framework. It's most often implemented by simply passing dependencies (objects, functions, or configurations) as arguments to a class's `__init__` method or to a function.

**How it Aligns with the Insights:**
*   **Favors Composition (Martelli):** An object is *composed* with its dependencies, which are "held" as instance attributes.
*   **Avoids Global State & Singletons (Rhodes):** Instead of a function reaching out to a global singleton (`logging.getLogger()`), the logger can be passed in. This makes code more testable and explicit about its needs.
*   **Simplicity:** It avoids the need for Abstract Factories. You don't need a factory to decide which database connection to create; you just pass the created connection object into the component that needs it.

**Example:**

```python
class ReportGenerator:
    def __init__(self, database_connection, email_service):
        self.db = database_connection
        self.email = email_service

    def generate_and_send(self, user_id):
        data = self.db.query(f"SELECT * FROM sales WHERE user_id={user_id}")
        # ... process data to create report ...
        self.email.send("report@example.com", "Your report", "...")

# In main application or test setup:
db = ProductionDB()
email = SMTPEmailService()
reporter = ReportGenerator(db, email)
```

### 5. Publish/Subscribe (Pub/Sub)

**Intent:** To allow multiple components to subscribe to specific types of events or messages without being directly coupled to the publisher.

**Implementation:** This is a modern, data-flow-oriented alternative to the GoF Observer pattern. In Python, it's often implemented with queues (like `asyncio.Queue` for asynchronous code or `queue.Queue` for threaded code) or specialized libraries like `blinker`.

**How it Aligns with the Insights:**
*   **Decoupled & Data-Centric (Rhodes):** Publishers and subscribers are completely decoupled. The publisher's only job is to put a message (data) onto a channel/topic. It doesn't know or care who is listening. This avoids the tangled object graph of the Observer pattern that Rhodes criticized.
*   **Addresses Observer's Flaws:** It naturally supports asynchronous workflows and makes the flow of information explicit through named channels, rather than implicit through direct object subscriptions.

**Example (conceptual, using a simple dispatcher):**

```python
class PubSub:
    def __init__(self):
        self.subscribers = {}

    def subscribe(self, event_type, callback):
        self.subscribers.setdefault(event_type, []).append(callback)

    def publish(self, event_type, data):
        for callback in self.subscribers.get(event_type, []):
            callback(data)

# Usage
def user_created_handler(data):
    print(f"LOGGING: New user created: {data['username']}")

def send_welcome_email(data):
    print(f"EMAIL: Sending welcome email to {data['email']}")

bus = PubSub()
bus.subscribe("user_created", user_created_handler)
bus.subscribe("user_created", send_welcome_email)

bus.publish("user_created", {"username": "alex", "email": "alex@example.com"})
```

### 6. The Mixin Pattern

**Intent:** To add a common set of methods to multiple classes without forcing them into a rigid inheritance hierarchy. A Mixin is a class that provides functionality but is not intended to be instantiated on its own.

**Implementation:** This pattern is a canonical use of Python's multiple inheritance. A class inherits from both its primary base class and one or more Mixin classes.

**How it Aligns with the Insights:**
*   **Composition Over Inheritance (Martelli):** This is a form of composition at the class level. You are "mixing in" behavior rather than asserting an "is-a" relationship. Martelli's `Adapter` example even uses a mixin.
*   **Decoupling and Reusability:** Mixins decouple specific functionalities (like JSON serialization, logging, or debugging representations) into reusable components that can be applied across different, unrelated class trees.
*   **Pragmatism:** It avoids the "diamond problem" of deep, complex inheritance hierarchies by keeping mixins focused and stateless.

**Example:**
```python
class AsDictMixin:
    def to_dict(self):
        # A simple implementation; could be more robust
        return {k: v for k, v in self.__dict__.items() if not k.startswith('_')}

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class SerializableUser(User, AsDictMixin):
    pass # Inherits to_dict functionality for free

user = SerializableUser("Grace Hopper", "grace@example.com")
print(user.to_dict())  # Output: {'name': 'Grace Hopper', 'email': 'grace@example.com'}
```

### 7. The Result Object Pattern

**Intent:** To handle operations that can fail by returning an explicit result object that encapsulates either a success value or an error, instead of raising an exception.

**Implementation:** A simple class hierarchy (e.g., `Success` and `Failure` both inheriting from a `Result` base) or a dataclass containing both a value and an error field (with one being `None`).

**How it Aligns with the Insights:**
*   **Data-Centric Error Handling (Rhodes):** This pattern turns an error from a disruptive control-flow event (an exception) into a piece of data that can be passed around, inspected, and handled gracefully. It makes the possibility of failure explicit in the function's return signature.
*   **Avoids Deep Call Stacks:** It helps prevent exceptions from bubbling up through many layers, allowing for local and explicit error handling at the point of call, which aligns with Rhodes' preference for shallow, understandable control flows.

**Example:**

```python
from dataclasses import dataclass

@dataclass
class Result:
    success: bool
    value: any = None
    error: str = None

def parse_int(s: str) -> Result:
    try:
        return Result(success=True, value=int(s))
    except ValueError:
        return Result(success=False, error=f"'{s}' is not a valid integer.")

result = parse_int("123")
if result.success:
    print(f"Success! Value is {result.value}")

result = parse_int("abc")
if not result.success:
    print(f"Failure! Error was: {result.error}")
```

### 8. The Plain Old Data Object Pattern

**Intent:** To use simple, attribute-focused objects primarily for holding data, with minimal or no custom methods.

**Implementation:** Historically done with `__init__`-only classes or `namedtuple`. In modern Python, this is perfectly embodied by `dataclasses` and external libraries like `pydantic`.

**How it Aligns with the Insights:**
*   **Putting Data First (Rhodes):** This pattern is the ultimate expression of data-centric design. The object *is* the data structure, free from the complex behaviors that obscure it.
*   **Reduces Boilerplate (Norvig):** Features like `dataclasses` make the pattern "invisible" by automating the creation of `__init__`, `__repr__`, `__eq__`, etc., allowing the programmer to focus purely on the data schema.
*   **Explicitness:** It provides a clear, self-documenting schema for the data being passed around, which is more robust than a plain dictionary.

**Example:**

```python
from dataclasses import dataclass

@dataclass
class UserProfile:
    user_id: int
    username: str
    is_active: bool = True

# The object's purpose is simply to hold this structured data
profile = UserProfile(101, "ada_lovelace")
print(profile) # Output: UserProfile(user_id=101, username='ada_lovelace', is_active=True)
```

### 9. The Fluent Interface / Chaining Pattern

**Intent:** To make code more readable and expressive by creating APIs where methods return `self`, allowing calls to be chained together in a sequence.

**Implementation:** Each method in the chain performs an action and concludes with `return self`.

**How it Aligns with the Insights:**
*   **Higher-Level Abstraction (Norvig):** This pattern creates a mini "Domain Specific Language" (DSL) for configuring or building an object. It abstracts away the intermediate steps of assigning to temporary variables.
*   **Pythonic Builder:** It serves as a more readable and idiomatic alternative to the formal GoF Builder pattern. Rhodes' `matplotlib` example is a form of this.
*   **Readability:** The resulting code often reads like a sentence describing the actions being taken.

**Example:**

```python
class QueryBuilder:
    def __init__(self, table):
        self._table = table
        self._filters = []

    def select(self, *columns):
        self._columns = columns
        return self # Return self to allow chaining

    def where(self, condition):
        self._filters.append(condition)
        return self # And again

    def __str__(self):
        return f"SELECT {', '.join(self._columns)} FROM {self._table} WHERE {' AND '.join(self._filters)};"

# Chained calls create a readable query
query = (
    QueryBuilder("users")
    .select("name", "email")
    .where("age > 30")
    .where("status = 'active'")
)
print(query)
```

### 10. The Actor Model Pattern (with asyncio)

**Intent:** To handle concurrency by using isolated, independent actors that communicate with each other exclusively through messages, avoiding the problems of shared state and locks.

**Implementation:** In modern Python, this is beautifully implemented using `asyncio`. Each actor is an `async` function running in its own `Task`. Communication is handled via `asyncio.Queue`.

**How it Aligns with the Insights:**
*   **Data-Centric Concurrency (Rhodes):** This is a perfect example of managing complex control flow (concurrency) by passing simple, inert data (messages) between decoupled components. It directly addresses the flaws of the Observer pattern in a concurrent context.
*   **Language-Enabled Pattern (Norvig):** The `async/await` syntax and the `asyncio` library provide the core primitives that make this pattern elegant and viable, where it would be extremely cumbersome otherwise.

**Example (conceptual):**

```python
import asyncio

async def data_processor_actor(in_queue, out_queue):
    while True:
        raw_data = await in_queue.get()
        processed_data = raw_data.upper() # Perform work
        await out_queue.put(processed_data)
        in_queue.task_done()

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()

    # Start the actor
    asyncio.create_task(data_processor_actor(q1, q2))

    # Publish work to the actor
    await q1.put("hello")
    await q1.put("world")

    # Consume results
    print(await q2.get()) # HELLO
    print(await q2.get()) # WORLD
```
