
"An anti-pattern is a commonly occurring solution to a problem, which generates decidedly negative consequences, although other documented solutions that prove to be more effective are available."

## Control Freak

The control freak anti-pattern occurs when a class takes over functions that should be left to the dependency injection container, leading to tight coupling and less maintainable code.

- **Newing Up Dependencies**: This is when classes create instances of their dependencies using the `new` keyword, instead of allowing them to be injected. This hard-codes the dependency and makes it difficult to replace for testing or further development.

- **Using Factories**: Sometimes factories are used within a class to create dependencies. While factories are a valid pattern, the misuse lies in the class itself controlling which implementation of the dependency is used, rather than letting the DI container manage this.

- **Overloaded Constructors**: Providing multiple constructors with different sets of dependencies can be a form of the control freak pattern. It might be done to allow different configurations of the class, but it can make it unclear which constructor should be used by the DI container.

## Service Locator

The service locator pattern can be an anti-pattern in DI when it's used as a mechanism to fetch dependencies on demand inside a class, rather than having them injected. Specifically, it is when classes directly reference the DI container to resolve their dependencies, rather than having them injected.

- **ProductService Using a Service Locator**: A `ProductService` class might use a service locator to obtain instances of required services such as logging or data access. This hides the service's true dependencies, can lead to runtime errors if the service locator isn't properly configured, and makes the code harder to test.

This anti-pattern can lead to several issues:

- **Tight Coupling**: Classes become tightly coupled to the specific DI container, making it harder to change or replace the container later on.
  
- **Hidden Dependencies**: By fetching dependencies from the container directly, the class hides its dependencies, making them implicit rather than explicit. This can make the code more difficult to understand and maintain.
  
- **Difficulties in Testing**: It becomes harder to test classes that use the service locator pattern since you have to mock the service locator and its behavior, rather than simply injecting mock dependencies.

The recommended approach is to use constructor injection, property injection, or method injection to pass dependencies to a class. This way, the class doesn't need to know about the existence of a container, leading to more maintainable and testable code.

## Ambient Context

Ambient Context is an anti-pattern when it's used to provide global access to a service within an application, which can lead to hidden dependencies and problems with concurrency and testing.

- **Accessing Time through Ambient Context**: Using a static/global object to access the current time instead of injecting a time provider means that the dependency on the system clock is hidden and can't be easily controlled or mocked for testing.

- **Logging through Ambient Context**: Similar to the time example, using a static logging service makes it difficult to adapt the logging strategy or format and to control or test the logging behavior.

## Constrained Construction

Constrained construction refers to a scenario where the DI container is limited in its ability to construct objects due to their design.

- **Late Binding a ProductRepository**: This could involve a `ProductRepository` that requires a runtime value to construct, like a database connection string that's only known at runtime. If the repository doesn't allow this to be set post-construction, it constrains how the DI container can manage the repository's lifecycle.

## Bastard Injection (Poor Man's Injection)

This is when a class can be instantiated with or without its dependencies being passed in (often through overloaded constructors). If the dependencies are not provided, the class will create them itself, typically using the `new` operator or a static reference.

- **Example**: A `NotificationService` might have a constructor that accepts an `IEmailClient` interface, but it also has a parameterless constructor that instantiates a specific `EmailClient` implementation. This can lead to a situation where it's unclear when to inject the dependency and when it's okay for the class to instantiate it itself.

## Static Cling

The static cling anti-pattern involves the use of static methods or properties for managing dependencies, which leads to hidden dependencies and difficulty in testing.

- **Example**: If a service class has a static `DbContext` that it uses to access the database, it's not possible to replace this with a mock or alternative implementation for testing or to manage the lifetime of the database context effectively.

## Tight Coupling

Tight coupling occurs when a class is dependent on concrete implementations rather than abstractions of its dependencies. This goes against the Dependency Inversion Principle, one of the SOLID principles of object-oriented design.

- **Example**: Injecting a `MySQLDatabase` class rather than an `IDatabase` interface. This means the class is directly dependent on MySQL, and changing the database would require modifying the class.

However, depending on concrete implementations rather than abstractions is not inherently bad; it's context-dependent. The Dependency Inversion Principle suggests that high-level modules should not depend on low-level modules but should depend on abstractions. This is a guideline to reduce coupling and increase the modularity of the code, making it easier to maintain, test, and scale.

There are scenarios where depending directly on concrete implementations can be acceptable or even preferable:

1. **Simple Applications**: In a small or simple application where the overhead of creating abstractions might not be justified, directly using concrete classes can be more straightforward and less over-engineered.

2. **Prototyping**: When rapidly prototyping an application, it might be more efficient to use concrete implementations to get immediate feedback without the upfront cost of designing abstractions.

3. **No Anticipated Changes**: If a particular implementation is stable and there are no foreseeable reasons why it would need to be swapped out or its behavior changed, then the additional abstraction layer could be unnecessary.

4. **Performance Concerns**: In performance-critical paths of an application, the slight overhead of calling through an abstraction can sometimes be a valid concern, and direct implementation can be warranted.

5. **Framework or Language Limitations**: Some programming languages or frameworks make it cumbersome to use abstractions for certain types of dependencies, such as UI components in certain desktop or mobile frameworks.

6. **Specific Functionality**: When a dependency provides a specific functionality that is unlikely to have different implementations, using a concrete class may make sense.

7. **Domain-Driven Design (DDD)**: In DDD, the focus is on the domain model, which can sometimes lead to using concrete entities and value objects directly because they represent domain concepts rather than interchangeable components.

8. **Final Classes**: Some classes are designed to be final or non-inheritable. In such cases, if the design is solid and the use case is clear, it may be acceptable to depend on the concrete class.

It's essential to consider the trade-offs when choosing between abstractions and concrete implementations. While abstractions can provide flexibility and maintainability, they also introduce complexity and indirection. The key is to apply the principle judiciously, abstracting only when it provides tangible benefits and aligns with the application's goals and constraints.

## Volatile Injection

Injecting dependencies that have volatile states or lifecycles can lead to unpredictable behavior. Volatile dependencies should be wrapped in abstractions that ensure a consistent state is presented to the consumer.

- **Example**: Injecting a `Cache` object that might be shared across threads without proper synchronization, potentially causing race conditions and inconsistent data.

## Ambiguous Interfaces

When interfaces are not designed with clear and single responsibilities, they can lead to confusion about their implementations. This ambiguity can make it difficult to understand or predict the behavior of classes depending on these interfaces.

- **Example**: An `IUserRepository` interface with methods for data access as well as caching. Implementing classes must then handle both concerns, which may not be desirable.

## Circular Dependencies

Circular dependencies occur when two or more classes depend on each other. This can create a deadlock situation for the dependency injection container, which cannot instantiate either without instantiating the other.

- **Example**: A `ReportGenerator` that depends on a `DataManager`, which in turn depends on the `ReportGenerator` for some functionality.

## Annotation Abuse

Reliance on extensive use of annotations or attributes to drive DI behavior can lead to cluttered code, which becomes difficult to understand without the aid of specialized tools or knowledge of the annotations' effects.

- **Example**: Annotating every method, parameter, or property in a class to control DI behavior, rather than configuring the container in a centralized and clear manner.

## Summary

In all cases, the underlying issue is a deviation from the core principles of DI, which are to manage dependencies in a way that promotes loose coupling, maintainability, and testability. These anti-patterns usually emerge from a lack of understanding of these principles or from attempts to take shortcuts in design and implementation. 

A common theme is taking control away from the DI container. **The recommended approach is to rely on the DI container to manage object creation and dependency resolution, keeping classes focused on their primary responsibilities and making them agnostic of the larger application's configuration and lifecycle management.**


## References

See also: [[DI patterns]]