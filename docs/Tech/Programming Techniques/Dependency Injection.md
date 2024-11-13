Dependency Injection (DI) is a fundamental concept in modern software design, promoting loose coupling and enhancing testability and maintainability.

## In Python

- https://github.com/sfermigier/awesome-dependency-injection-in-python

Sample APIs: [[Examples of DI API in Python]]
## In Java

- https://rskupnik.github.io/dependency-injection-in-pet-project-dagger2
- https://www.baeldung.com/java-ee-cdi
- https://dzone.com/articles/jsr-365-update-digging-into-cdi-20

## Patterns

see [[DI patterns]]

## When and how to apply DI?

#### Is this object a service or a utility class?

- **Service Classes:** These contain important business logic and should be injected using DI to promote loose coupling and facilitate testing.
- **Utility Classes:** These are stateless and contain helper methods. Since they don’t hold state, they can be instantiated directly without DI.

In Python, services are often classes that encapsulate business logic, whereas utility functions might be standalone functions or part of a module.

#### Will I need to swap this implementation for another?

Using direct instantiation tightly couples your code to a specific class, making it difficult to swap out implementations for testing or extended functionality. Instead, use abstract base classes (ABCs) or protocols and inject dependencies. This allows you to easily replace one implementation with another, improving flexibility and testability.

#### Does this object have external dependencies?

If an object has its own dependencies, instantiating it directly can lead to tight coupling with those dependencies. It’s better to let a DI framework or manual DI handle the instantiation and resolve all dependencies, ensuring cleaner and more manageable code.

#### Is the object for carrying data?

Data Transfer Objects (DTOs) or Plain Old Python Objects (POPOs) are typically used for carrying data and do not contain business logic. Such objects can be instantiated directly using `new` as they don’t benefit from DI.

#### Is the object relevant within a limited scope?

For objects that are temporary or transient, such as collections or state-holding objects with a limited lifecycle, direct instantiation is appropriate. DI is more suited for objects with a broader or more complex lifecycle.

#### Is this a configuration?

DI can centralize configuration management, making it easier to manage and change application settings. Inject configuration settings into services rather than loading them every time, promoting consistency and reducing redundancy.

#### Is this a Cross-Cutting Concern?

Cross-cutting concerns like logging, caching, and security typically need to be applied consistently across multiple components. DI is an effective way to implement these concerns, ensuring they are consistently and correctly applied.

#### Will the object’s lifecycle be managed differently from other objects?

DI frameworks or manual DI management in Python can handle lifecycle management, ensuring that objects are instantiated and disposed of correctly. If your object requires specific lifecycle management (singleton, scoped, or transient), DI is the appropriate choice.

#### Does the object have complex initialization logic?

Objects with complex setup or initialization logic benefit from DI, which can handle the instantiation sequence and ensure all dependencies are resolved before use.

#### Will this object be used in multiple contexts?

Reusing objects across different parts of the application is easier with DI, which ensures consistency and avoids duplication of initialization logic.

#### Is testability a primary concern?

DI makes it straightforward to mock or stub dependencies, leading to more isolated and effective tests. If testability is crucial, DI is highly beneficial.

#### Does the object participate in dependency graphs?

For objects that are part of a more extensive dependency graph, DI frameworks or manual DI in Python manage and resolve complex dependencies efficiently, reducing potential issues like circular dependencies.

#### Is the object required to be thread-safe?

In multi-threaded applications, DI frameworks or patterns can provide thread-safe singleton instances or appropriately scoped instances, ensuring thread safety without additional boilerplate code.

#### Are you following a particular architectural pattern?

Certain architectural patterns, such as Clean Architecture or Hexagonal Architecture, emphasize the use of DI to enforce separation of concerns and promote loose coupling. Adhering to these patterns can guide when to use DI.

#### Does the object participate in AOP (Aspect-Oriented Programming)?

DI can be crucial for objects participating in cross-cutting concerns managed through AOP, such as logging, transaction management, or security, ensuring these concerns are seamlessly integrated.

#### Are you aiming for SOLID principles compliance?

Using DI aligns with SOLID principles, particularly the Dependency Inversion Principle (DIP), ensuring high-level modules depend on abstractions rather than low-level modules.

#### Will the object benefit from central configuration or service location?

Centralizing configuration through a DI container or a configuration management pattern simplifies management and reduces redundancy, making it beneficial for objects needing consistent configuration.

<!-- Keywords -->
#dependency #dependencies #inject
<!-- /Keywords -->
