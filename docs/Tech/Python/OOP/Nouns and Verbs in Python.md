This 2025 presentation by Brandon Rhodes, "[Skip the Design Patterns: Architecting with Nouns and Verbs](https://rhodesmill.org/brandon/slides/2025-04-pycon-lithuania.pdf)", is a direct and powerful follow-up to his previous work ([[GoF Pattern in Python]]). Where the 2022 talk was a *deconstruction* of the GoF patterns, this talk is a *reconstruction*—it proposes a new, positive architectural model to replace them.

Here are the core ideas that we could make of the presentation. For more details, see the presentation deck or [the video](https://www.youtube.com/watch?v=v-N6r8lcsNc).

### 1. The "Nouns and Verbs" Architectural Model

This is the central new thesis. While the previous talks praised functions and simple data, this presentation formalizes that preference into a concrete architectural philosophy:

*   **Verbs (Functions):** The locus of logic. They are stateless, idempotent, and composable. They form the call graph of the application.
*   **Nouns (Data Objects):** The locus of state. They are stateful, mutable data structures. Their methods should be **shallow**, meaning they perform a single, simple operation and return control, not orchestrate complex logic.

This model moves beyond criticizing old patterns to offering a new way to think about structuring code from the ground up. It provides a vocabulary for the data-centric style Rhodes previously advocated for.

### 2. A Three-Stage Model for Developer Progression

Rhodes reframes the journey from novice to expert programmer using his Noun/Verb model. This is a significant pedagogical insight not present in the earlier decks.

| Stage | Traditional View | Rhodes' "Nouns and Verbs" View |
| :--- | :--- | :--- |
| 1. **Procedural** | All code in `main()` | **Use** existing nouns and verbs. |
| 2. **Abstraction** | Writing functions | **Invent** new verbs (subroutines). |
| 3. **Encapsulation** | Writing classes | **Invent** new nouns (APIs, stateful objects).|

He argues that **Encapsulation (inventing nouns)** is the hardest and most expert-level task. This provides a clear roadmap for learning and a strong critique of traditional OO pedagogy, which he claims forces novices to start at the most difficult level.

### 3. The Concept of "µ-patterns" (Micro-patterns)

This is a new, granular concept. Instead of large, architectural "Design Patterns," Rhodes focuses on small, repeatable, almost tactical coding idioms he calls "µ-patterns." These are the building blocks a procedural coder uses to solve problems. The examples from his refactoring journey include:

*   µ-pattern #1: Extract a constant.
*   µ-pattern #2: Save the previous element (in a loop).
*   µ-pattern #3: Use a safe initial value.
*   µ-pattern #5: Avoid duplicate work.
*   µ-pattern #6: **Do one thing at a time.** (The most important one).

This gives a name to the intuitive, small-scale refactoring steps that experienced programmers perform without thinking, distinguishing them from the heavyweight GoF patterns.

### 4. A Sharper and More Fundamental Critique of Object Orientation

This talk contains Rhodes' most pointed critique of OO yet. He moves from saying some patterns are obsolete to diagnosing the core problem they were designed to fix.

*   **The Original Sin of OO:** "Object Orientation was a ban on standalone verbs." It recommended attaching every line of code (verb) to the nearest piece of data (noun).
*   **The Consequence:** This led to "method ping-pong" and deep, tangled call graphs that are hard to test and reason about.
*   **The GoF as an Escape Hatch:** He provocatively concludes that "Many Gang of Four ‘Design Patterns’ were designed to *escape* from Object Orientation." They were techniques to re-introduce a separation of concerns that a strict OO approach had erased. This explains *why* so many patterns feel unnecessary in Python, which never banned standalone verbs in the first place.

### 5. Formalized Habits for Clean Architecture

Rhodes elevates his personal coding preferences into three explicit architectural "Habits" for those "inventing new verbs" (the Abstraction stage).

1.  **Don't mix levels of abstraction.** (e.g., separate high-level I/O orchestration from low-level list iteration).
2.  **Keep I/O near the top.** This is a direct endorsement of principles from Clean/Hexagonal Architecture. He explicitly connects "burying I/O" to tight coupling and testability issues.
3.  **Shallow call graphs.** He re-iterates this point from 2022 but now provides a stronger rationale, explaining how deep graphs lead to difficult choices between "prop-drilling" parameters or using globals ("scary action at a distance").

### 6. A Definition for a "Pythonic Noun"

Finally, the talk provides a clear definition of what a well-designed API or encapsulated object should look like. A good "Noun" must be:

*   **Legible:** Its state must be transparent and inspectable. It should hide its *implementation*, but never its *state*. This directly echoes Fred Brooks' famous quote, which Rhodes includes.
*   **Shallow:** Its methods should be simple, single-purpose operations, leaving complex orchestration to the "verbs."

## Annex: "Execution in the Kingdom of Nouns"

Brandon Rhodes' presentation has its roots in a famous blog post by Steve Yegge from 2006: "[Execution in the Kingdom of Nouns](https://steve-yegge.blogspot.com/2006/03/execution-in-kingdom-of-nouns.html)". This post, combined with decades of community discussion, reveals that the "Nouns and Verbs" model is the culmination of a long-running conversation about the nature of Object-Oriented Programming, particularly in contrast to more flexible languages.

Here are some **additional insights** from this broader conversation:

### 1. The "Kingdom of Nouns" as a Central Metaphor

Yegge's central insight is that languages like 2000s-era Java, by lacking first-class functions (standalone "verbs"), force all logic into classes ("nouns").

*   **The Absurdity of Noun-Wrapping:** Yegge brilliantly satirizes the consequence: the creation of absurdly verbose classes whose only purpose is to wrap a single action. Examples like `TrashDisposalPlanExecutor.doIt()` and `RegistrationManager.register()` perfectly capture the anti-pattern of turning verbs into nouns. This is the intellectual origin of the critique against patterns like Command or Strategy when used merely to pass a piece of code.
*   **OOP as "Pants-Oriented Clothing":** Yegge argues that an obsessive focus on nouns is an artificial constraint that warps how we think. His analogy that "advocating Object-Oriented Programming is like advocating Pants-Oriented Clothing" suggests it's a skewed perspective that wrongly elevates one part of speech (nouns/objects) above all others.
*   **The Problem is Language Limitation, Not OO Itself:** Yegge correctly diagnoses that this "disease" is most virulent in languages that lack first-class functions. He notes that Python, Ruby, Perl, and functional languages don't suffer from this because their "verbs" can roam freely.

This provides the "why" for the arguments against heavyweight patterns: they are often symptoms of a language that forces you to live in the "Kingdom of Nouns."

### 2. A Tale of Two Kingdoms: Pernicious vs. Principled Nouns

This line of thinking leads to a crucial distinction: **not all nouns are created equal**. There is a "pernicious" Kingdom of Nouns (Yegge's target) and a "principled" one.

*   **The Pernicious Kingdom (Unnecessary Wrappers):** This is when a noun is created solely to compensate for a missing language feature. For example, refactoring a simple `anagrams` function into bloated `Word` and `Letter` classes creates massive incidental complexity and performance overhead for no real gain. This is the bad habit of over-objectification.
*   **The Principled Kingdom (Necessary Abstractions):** This is when a noun is created for a good architectural reason.
    *   **To name a *conformance* or *relationship***: Consider a type like `Int` which can conform to a mathematical `Semigroup` in two ways (with addition or multiplication). A wrapper noun like `Sum(Int)` or `Product(Int)` is a principled way to disambiguate which "verb" relationship we mean. The noun isn't the operation; it names the *conformance*.
    *   **To create a simple, granular component:** Similarly, a modern API like Jetpack Compose might have a `FocusRequester`. This isn't a bloated wrapper; it's a deliberate design choice to create a small, simple component that does one thing well, in service of a larger goal of making UI widgets easy to fork and clone.

This insight refines the blunt "[stop writing classes](https://www.youtube.com/watch?v=o9pEzgHorH0)" message into a more sophisticated guideline: **don't create a noun when a verb will do, but *do* create a noun to give a name to a meaningful relationship or a well-defined component.**

### 3. The Primacy of Simple Data and "Data as a Log of Events"

This data-centric view leads to two powerful principles.

*   **Hold Fast to Pure Data:** One core principle is to "hold fast to pure data, and only yield ground under exceptional circumstances." Custom objects can introduce opacity, statefulness, and complexity, making them hard to debug, serialize, and test. In contrast, "pure data" (like strings, lists, and dictionaries) is transparent. This provides the strongest argument yet for why well-designed "Nouns" should have shallow, legible methods—to keep them as close to pure data as possible.
*   **Flipping Nouns and Verbs (The Banking Example):** This leads to a more profound insight: what we perceive as nouns and verbs can often be flipped. For instance, our intuition says a bank account's `balance` is data (a noun) and a `transfer` is an action (a verb). A more robust, "real-world" design treats the **transaction as immutable data (a noun)** and the **balance as a derived calculation (a verb)** that operates on a log of transactions. This leads to a naturally immutable, auditable, and concurrent-friendly system. This "event sourcing" or "data as a log" model is a profound architectural pattern in its own right and the ultimate expression of data-centric design.

### 4. Naming as a Design Trade-off, Not a Dogma

This focus on simplicity and context also applies to a common source of debate: naming conventions.

*   **Heuristics, Not Laws:** Prescriptive rules, like avoiding words such as `Manager` or `Processor`, should be treated as guidelines, not laws. Sometimes a class *is* a processor (e.g., an annotation processor), and naming it as such is clear and honest.
*   **Consistency over Dogma:** The more important goal is to establish a clear, consistent pattern *within a project*. Whether you call your data access layers "Repositories," "Managers," or "Interactors" matters less than the fact that you pick one and stick to it, making the architecture predictable.
*   **Ambiguity is Unavoidable:** Words like "component," "scope," and "service" are inherently ambiguous. Good developers become skilled at understanding these terms within the context of a specific framework or codebase, rather than obsessing over a universally "perfect" name.

### References

- https://belkadan.com/blog/2017/09/The-New-Kingdom-of-Nouns/
- https://drawson.medium.com/this-is-how-you-dont-teach-software-design-featuring-clean-code-317707965f4a
