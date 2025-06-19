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
