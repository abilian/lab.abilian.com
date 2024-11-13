"[Out of the Tar Pit](https://curtclifton.net/papers/MoseleyMarks06a.pdf)" is a highly influential computer science paper written by Ben Moseley and Peter Marks, published in 2006. The paper discusses the problem of complexity in software systems and proposes a new approach to tackle it.

The authors argue that complexity is the primary cause of many issues in software development, such as defects, cost overruns, and the need for constant maintenance. They identify two main sources of complexity: state and control. State refers to the data that a system manages, while control refers to the flow of execution within the system.

Moseley and Marks suggest that the traditional methods of handling complexity, like object-oriented programming and functional programming, are not sufficient to address these problems. Instead, they propose a new approach called "Functional Relational Programming" (FRP - not to be confused with "Functional Reactive Programming") which combines functional programming techniques with the relational model from database theory.

In FRP, a system is built around a single, unified data model that represents its state as a set of relations (similar to tables in a relational database). Functions are then used to manipulate this data, with the goal of minimizing or eliminating mutable state and control flow complexity. This is achieved by making extensive use of pure functions, which have no side effects and depend only on their input arguments.

The authors claim that FRP can lead to simpler, more reliable, and easier-to-understand systems. However, it's important to note that FRP is not a silver bullet for all software problems, and its adoption depends on the specific context and requirements of a project.

"Out of the Tar Pit" has had a significant impact on the software development community, inspiring many discussions and research efforts on complexity and software engineering. The ideas presented in the paper have influenced the design of various programming languages, frameworks, and tools aimed at simplifying software development and reducing complexity.

## Causes of software complexity

"Out of the Tar Pit" discusses several causes of software complexity:

1.  **State**: The paper highlights the impact of state on testing and informal reasoning. When the system has many possible states, testing becomes challenging, as it is difficult to ensure that the system behaves consistently across different runs. Informal reasoning also suffers due to the exponential growth in the number of states, making it harder to mentally simulate the system's behavior.

2.  **Contamination**: When a procedure depends on another stateful procedure, it becomes "contaminated," further increasing the overall complexity of the system.

3.  **Control**: The authors argue that control, or the order in which things happen, should not be a concern for developers. When control is implicitly part of a programming language, it forces developers to over-specify the problem. Concurrency, a control-related issue, also complicates testing and informal reasoning, as it introduces additional scenarios to consider.

4.  **Code Volume**: The paper identifies code volume as a secondary source of complexity, as it often arises from managing state or specifying control. Complexity increases non-linearly with code size, making it essential to minimize the amount of code.

5.  **Other Causes**: The authors mention additional causes of complexity, such as duplicated code, dead code, unnecessary or missed abstraction, poor modularity, and poor documentation. These issues stem from three main principles:
	a. Complexity breeds complexity: Complexity arises when developers cannot clearly understand a system, often due to time pressures.
	b. Simplicity is hard: Achieving simplicity requires recognizing, pursuing, and valuing it.
	c. Power corrupts: Powerful languages that permit state, even if discouraged, may lead to mistakes or abuses. The more powerful a language, the harder it is to understand systems built with it.

In summary, "Out of the Tar Pit" identifies state, contamination, control, code volume, and other factors as causes of software complexity. The paper emphasizes the need to manage and limit these factors to create simpler, more reliable software systems.

## Shortcomings of the classical approaches to managing complexity

The paper discusses classical approaches to managing complexity in software systems and their shortcomings, which necessitate an alternative approach.

1.  **Object-Orientation**:

    -   Encapsulation does not effectively enforce integrity constraints, especially when multiple objects are involved.
    -   Object identity complicates reasoning about systems.
    -   Object-oriented programming (OOP) relies on state, leading to state-derived and control-derived complexity.

2.  Functional Programming:

    -   Stateless and referential transparency improves testing and informal reasoning.
    -   Abstract control functionals reduce control complexity.
    -   Avoiding mutable state simplifies systems but also limits modularity.
    -   The main weakness of functional programming is handling systems that require state maintenance.

3.  Logic Programming:

    -   Logic programming avoids mutable state, benefiting from the same advantages as functional programming.
    -   The depth-first, textual order of processing introduces control complexity and challenges in informal reasoning.
    -   Despite its limitations, logic programming provides an escape from control-induced complexity.

In summary, classical approaches like object-oriented, functional, and logic programming have not been entirely successful in managing software complexity due to inherent issues with state, control, and modularity. These limitations highlight the need for alternative approaches to tackle the complexity problem more effectively.

## Accidental vs. essential complexity

In his seminal paper "No Silver Bullet," Fred Brooks distinguishes between two types of complexity in software systems: accidental complexity and essential complexity. "Out of the Tar Pit" further explores these concepts and their implications on software development.

1.  **Essential Complexity**: Essential complexity refers to the inherent complexity that stems from the problem domain itself. It represents the minimum level of complexity that a software system must possess to address the requirements of the problem it aims to solve. Essential complexity cannot be eliminated, as it is a fundamental aspect of the problem domain. Developers must understand and manage essential complexity to build effective and reliable software systems.

2.  **Accidental Complexity**: Accidental complexity, on the other hand, arises from the development process, tools, and technologies used to build the software. It is not inherent to the problem domain and can be attributed to limitations, inefficiencies, or errors in the design, implementation, and management of the software system. Accidental complexity can be reduced or eliminated by improving development methodologies, languages, tools, and practices.

"Out of the Tar Pit" argues that conventional approaches to software development, such as object-oriented, functional, and logic programming, have failed to adequately address the complexity problem, often introducing accidental complexity. The paper proposes Functional Relational Programming (FRP) as an alternative approach to tackle complexity by focusing on reducing accidental complexity and managing essential complexity more effectively. By minimizing state, control, and code volume, FRP aims to simplify software systems and make them easier to reason about, test, and maintain.

## Recommended approach

The recommended general approach advocated by "Out of the Tar Pit" emphasizes minimizing complexity and clearly separating components. Here is a summary of the approach:

1.  Acknowledge that some complexity is unavoidable even in the ideal world.
2.  Focus on declarative programming by specifying the required outcome rather than the exact process.
3.  Aim to eliminate mutable state and minimize essential state.
4.  Avoid control flow where possible and consider it accidental complexity.
5.  Recognize that some accidental complexity may be necessary for performance or ease of expression.
6.  Separate components by dividing complexity between accidental and essential, and maintain clean distinctions among them.
7.  Use different languages for each component to facilitate reasoning about them.

The proposed architecture includes essential state as the foundation, essential logic (or "business" logic) to express what must be true, and accidental state and control as the least important part of the system:

-   Essential state: This serves as the system's foundation and should not refer to other components. Modifications in other specifications should not necessitate changes to the essential state's specifications.
-   Essential logic: Often called "business" logic, this expresses what needs to be true based on the state without specifying how it should be achieved. Changes in the essential state may lead to adjustments in the logic specifications, which in turn may require alterations in the accidental state and control specifications. It must not refer to any part of the accidental specifications.
-   Accidental state and control: This component is the least crucial in the system. Any changes to it should not impact the other specifications.

This separation ensures that changes in one component do not unnecessarily affect the others, ultimately reducing overall system complexity.

## The relational model, according to "out of the tar pit"

"Out of the Tar Pit" describes the relational model, which is not exclusively related to databases. The relational model's features, such as structuring and manipulating data, as well as maintaining the integrity and consistency of state, apply to any context involving state and data.

Additionally, the relational model allows for a clear separation between the logical and physical layers of a system, providing data independence.

**Structure**:

-   Relations: A relation is a homogeneous set of records, with each record consisting of multiple attributes. Relations can be base relations (stored directly) or derived relations (also known as views, defined in relation to other relations). A relation can be considered a value, with mutable state represented as a variable containing a particular relation value (relation variables or relvars).
-   Structuring benefits of relations and access path independence: Structuring data using relations is beneficial because it eliminates the need for upfront decisions about later access paths. The relational model's ability to avoid access paths was a primary reason for its success.

**Manipulation**:

-   Relational calculus and relational algebra are two mechanisms for expressing the manipulation aspects of the relational model. Relational algebra includes several operations that can be nested in various ways, offering closure as a significant advantage.

**Integrity**:

-   Constraints can be specified in a purely declarative manner to maintain integrity. Primary keys and foreign keys are common constraint types, while database management systems (DBMSs) provide imperative mechanisms like triggers for integrity maintenance.

**Data independence**:

-   This principle involves separating the logical model from the physical storage representation.

**Extensions**:

-   Relational algebra is computationally restrictive and often requires augmentation. Common extensions include general computation capabilities, aggregate operators, grouping and summarization capabilities, and renaming capabilities.

## Solution: Functional Relational Programming

Functional Relational Programming (FRP) is a hypothetical concept that has not been proven in practice (at the time of the paper). FRP aims to eliminate complexity by having all essential state in the form of relations and expressing essential logic using relational algebra extended with pure user-defined functions.

Components of an FRP system include:

- Essential state: A relational definition of the stateful components of the system.
- Essential logic: Derived-relation definitions, integrity constraints, and pure functions.
- Accidental state and control: A declarative specification of performance optimizations.
- Other: Interfaces to the outside world.

Unlike object-oriented approaches, FRP emphasizes a clear separation of state and behavior.

Essential state consists of base relvars, while essential logic includes both functional and algebraic relational components, along with user-defined functions and integrity constraints. Accidental state and control are composed of isolated, declarative performance hints.

The architecture of an FRP system includes components for interfacing with the outside world, such as feeders (converting input into relational assignments) and observers (generating output in response to changes in derived relvars). These components are minimal, focused on translating to and from relations.

To execute the FRP system specification, infrastructure is required for essential state, essential logic, accidental state and control, and feeders and observers. This infrastructure includes mechanisms for storing and retrieving data, evaluating relational expressions, specifying derived relvars, managing physical storage, and processing relational assignment commands. It is possible to develop FRP infrastructure using any general-purpose programming language, be it object-oriented, functional, or logic-based.

## Benefits

Benefits of the Functional Relational Programming (FRP) approach include the following:

1.  Benefits for state:

    -   Avoids unnecessary accidental state and prevents entering a "bad state."
    -   Essential state is seen as constant from the logic's perspective.
    -   The functional component is referentially transparent, having no access to any state.
    -   Adoption of relational data representation offers advantages like the elimination of data access path concerns.
    -   Integrity constraints ensure consistency of state in a declarative manner.

2.  Benefits of control:

    -   Control is entirely avoided, with logic consisting of a set of equations without any intrinsic ordering or control flow.
    -   An FRP-supporting infrastructure may leverage implicit parallelism to improve performance.
    -   Distributed implementations become easier to create.

3.  Benefits of code volume:

    -   Unnecessary accidental complexity is avoided, leading to less code.
    -   Separation reduces the harm caused by large volumes of code.

4.  Benefits of data abstraction:

    -   Unnecessary data abstraction is avoided, preventing issues like subjective reuse and data hiding.
    -   The relational model's strength lies in minimal commitment to subjective groupings.

5.  Other benefits:

    -   Potential performance improvements.
    -   Development teams can be organized around different components.

6.  Types:

    -   FRP allows the definition of new user types for essential state and essential logic components.
    -   It does not permit the creation of new product types to avoid unnecessary data abstraction.

## Legacy

While "Out of the Tar Pit" does not directly lead to the creation of specific programming languages, frameworks, or tools, its ideas and principles have had a significant impact on the software development community. The paper has inspired many discussions and research efforts on complexity and software engineering, which have indirectly influenced various programming languages, frameworks, and tools aimed at simplifying software development and reducing complexity. Some of these include:

6.  Datomic: A distributed, transactional, and immutable database system designed by Rich Hickey, the creator of Clojure. Datomic applies the principles of immutability and the relational model to manage complexity in database systems.

5.  DataScript: A lightweight, in-memory database and Datalog query engine for Clojure and ClojureScript, DataScript is influenced by the ideas of unifying state management using a relational data model, as proposed in "Out of the Tar Pit."

1.  Eve: Eve was an experimental programming language and environment that aimed to simplify software development by embracing FRP principles. It provided a unified relational data model and a rule-based programming paradigm to express computation. Unfortunately, development on Eve has been discontinued, but its design was heavily influenced by "Out of the Tar Pit."

2.  Relational Lenses: A research project that explores bidirectional programming in the context of relational databases. It incorporates functional and relational concepts to simplify the process of writing database transformations and synchronizations.

3.  Project:M36: A relational algebra database management system inspired by the ideas in "Out of the Tar Pit." It aims to provide a purely functional and algebraically-oriented approach to database management, with a focus on reducing complexity and increasing reliability.

4.  Logic programming languages: Languages like Prolog, Mercury, and miniKanren, which are based on formal logic and relational algebra, share some similarities with the FRP principles described in "Out of the Tar Pit." They emphasize declarative programming, where the focus is on specifying the relationships between data elements rather than the control flow.

While the adoption of FRP as proposed in "Out of the Tar Pit" has been limited, the paper has influenced the broader software development community and encouraged researchers and practitioners to explore new ways to manage complexity in software systems.

These are just a few examples of the programming languages, frameworks, and tools influenced by the ideas presented in "Out of the Tar Pit." The paper has had a widespread impact on the software development community, inspiring new ways to think about and manage complexity in software systems.


## References

- https://curtclifton.net/papers/MoseleyMarks06a.pdf
- https://www.youtube.com/watch?v=7y1phdZkLw4
- https://www.youtube.com/watch?v=AcLmiLYZF8Q
- http://kmdouglass.github.io/posts/summary-out-of-the-tar-pit/
- https://blog.acolyer.org/2015/03/20/out-of-the-tar-pit/

<!-- Keywords -->
#frameworks #programming
<!-- /Keywords -->
