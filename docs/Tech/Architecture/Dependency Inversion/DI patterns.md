Here's a list of common Dependency Injection (DI) patterns that promote loose coupling and maintainability in software design:

1. **Constructor Injection**: This pattern involves providing the required dependencies through the class's constructor. It's the most common DI pattern and ensures that the object is always in a fully initialized state.

2. **Property Injection**: Also known as Setter Injection, this pattern provides the dependency through a public property of the class. It's useful when the dependency is optional or when circular dependencies must be resolved.

3. **Method Injection**: Dependencies are provided through a method rather than a constructor or property. This is ideal for situations where the dependency is only needed for the duration of a method call.

4. **Interface Injection**: In this pattern, the dependent class implements an interface that includes a method for injecting the dependency. It’s less common but can be used to enforce the presence of a setter method for the dependency.

5. **Service Locator**: Although considered an anti-pattern when overused, the Service Locator can be used as a DI pattern when properly managed, typically at the composition root. It involves a central registry that provides access to services and dependencies.

6. **Ambient Context**: This pattern provides a way to access dependencies that are global or ambient to the application context. It is often implemented as a static context or through thread-local storage.

7. **Factory Pattern**: Factories abstract the creation logic of objects and can be injected to provide the dependent objects with the ability to create instances of their dependencies.

8. **Abstract Factory**: An extension of the Factory pattern, this pattern uses a single interface to create families of related or dependent objects without specifying their concrete classes.

9. **Lazy Injection**: Dependencies are provided as a proxy or a factory that delays the creation of the actual dependency until it's really needed. This can improve startup time and resource usage.

10. **Provider or Resolver Pattern**: Similar to factories, a provider or resolver is responsible for abstracting the logic needed to retrieve dependencies.

11. **Composition Root**: A pattern where all the bindings and configurations of dependencies are centralized in a single location, typically at the entry point of the application.

12. **Registry Pattern**: Similar to the Service Locator but typically used within a DI container, a registry pattern maintains a registry of types and their corresponding constructors, which the DI container uses to instantiate objects.

13. **Decorator Pattern**: When using DI, decorators can be injected in place of an instance to add additional behavior while still adhering to the interface.

## The patterns in details

### Composition Root

**Composition Root** is a pattern where all the composition of your objects happens in a centralized place in the application, typically at the entry point. This is where you would create instances of your objects and wire them together (i.e., satisfy their dependencies).

#### How Composition Root Works

The Composition Root is responsible for creating and managing the lifetime of dependencies. It's the only place in the application where the DI container is directly referenced, ensuring that the rest of the application can remain unaware of the container's existence.

#### Using a DI Container in a Composition Root

A DI container can be used to automatically resolve dependencies based on pre-configured bindings. When a request for a type comes in, the DI container constructs the object graph needed to fulfill the request.

#### Implementing a Composition Root Using Pure DI

Pure DI (also known as Poor Man's DI) involves manual construction and wiring of dependencies without the use of a DI container. It's more verbose but can be useful for understanding DI principles or in scenarios where a DI container is not desired.

#### The Apparent Dependency Explosion

As more classes and dependencies are added to an application, the Composition Root can seem to "explode" with complexity. This is a natural consequence of explicitly stating dependencies, but it can be managed by grouping related dependencies into composable modules.

### Constructor Injection

**Constructor Injection** is the most common DI pattern and involves providing the required dependencies through the class's constructor.

#### How Constructor Injection Works

Constructor injection ensures that a class has all its required dependencies before it is used. The dependencies are provided as arguments to the constructor, making it clear what dependencies the class needs.

#### When to Use Constructor Injection

Constructor Injection should be used when a dependency is essential for the class's functionality and the class cannot operate without it. It's also useful for immutable dependencies and when aiming for thread safety.

#### Known Use of Constructor Injection

Many frameworks and libraries use constructor injection due to its benefits in terms of clarity, testability, and compliance with the Dependency Inversion Principle.

#### Example: Adding Currency Conversions to the Featured Products

This would involve creating a `CurrencyConverter` class and passing it to the constructors of the classes responsible for representing and displaying featured products.

#### Wrap-Up

Constructor Injection helps maintain a clear contract for class dependencies, promoting better maintainability and testability.

### Method Injection

**Method Injection** is where dependencies are provided through a method.

#### How Method Injection Works

Instead of supplying the dependency at the time of object construction, it is provided at the time the method is called. This is useful when the dependency varies with each method call.

#### When to Use Method Injection

Use Method Injection when the dependency is only required for the duration of a specific method and not for the lifetime of the consuming object.

#### Known Use of Method Injection

This is often seen in libraries where the context can change frequently, and the consumer needs to pass different data or services each time the method is called.

#### Example: Adding Currency Conversions to the Product Entity

Method injection would be appropriate if the `Product` entity requires currency conversion only for certain operations. The conversion rate or service could be injected into the method that needs to perform the conversion.

### Property Injection

**Property Injection** is also referred to as Setter Injection.

#### How Property Injection Works

Property Injection involves injecting dependencies by setting a property on the class after the object has been constructed. This can be done manually or by a DI container.

#### When to Use Property Injection

It is used for optional dependencies that can be set or changed after the object has been constructed or when dealing with circular dependencies.

#### Known Uses of Property Injection

Property Injection is often used in situations where a class requires certain services or configurations that can be provided after the class has been constructed, such as in the configuration of plugins or in frameworks that support late binding.

#### Example: Property Injection as an Extensibility Model of a Reusable Library

In a reusable library, you might not know all the dependencies upfront. Property injection allows consumers of the library to configure or extend functionality by setting properties, which can define or override the behavior of the library.

### Lazy Injection

**Lazy Injection** refers to a pattern where the dependency is provided through a proxy or a factory that delays the creation of the actual dependency until it is really needed.

#### How Lazy Injection Works

Lazy Injection often involves wrapping the dependency with a `Lazy[T]` type or a similar construct. The DI container or factory is responsible for providing this wrapper instead of the actual object. The creation of the object is deferred until the `Value` property of the `Lazy[T]` is accessed.

#### When to Use Lazy Injection

Lazy Injection is useful when the dependency is expensive to create or may not be used at all during the lifetime of the consuming object. It's also beneficial for breaking circular dependencies.

#### Known Use of Lazy Injection

This pattern is particularly advantageous in applications that need to start up quickly and delay the initialization of heavy resources until they are actually needed.

### Ambient Injection

**Ambient Injection** involves using a static or global variable to hold a dependency that can be accessed from many different places in the application without being explicitly passed around.

#### How Ambient Injection Works

Ambient Injection typically uses a static property or method that can be set at the beginning of an operation and then accessed from anywhere in the application. This is often implemented using a Thread-Local storage or a context-specific storage that preserves the dependency throughout a given context's execution.

#### When to Use Ambient Injection

This pattern is used sparingly, typically in legacy code migration or in frameworks where passing dependencies explicitly is not feasible. However, overuse can lead to code that is difficult to understand and maintain.

#### Known Use of Ambient Injection

Frameworks or libraries that manage a context or provide services that are widely used across different parts of an application might use this pattern, such as logging contexts or transaction management.

### Interface Injection

**Interface Injection** is a less common form of DI where an interface is used to inject dependencies through a method defined in the interface.

#### How Interface Injection Works

An interface will declare a method like `InjectDependency`. Any class that requires a dependency implements this interface, and the injection framework will call the `InjectDependency` method to pass in the dependency.

#### When to Use Interface Injection

This pattern can be used when you want to enforce that a dependency must be set for a class to function properly, and you want the class itself to be in control of how the dependency is set.

#### Known Use of Interface Injection

Interface Injection can be seen in plugin architectures where the host application needs to provide certain services to the plugin, and the plugin is expected to expose an interface to receive those services.

### Service Locator

**Service Locator** is a pattern where a central registry is used to provide dependencies at runtime. Unlike other forms of DI, it requires the consuming class to request its dependencies from the locator rather than being provided them.

#### How Service Locator Works

The service locator holds references to services and is responsible for their lifecycle. A consumer will ask the service locator for a service by type or by key, and the locator will return the appropriate instance.

#### When to Use Service Locator

The Service Locator pattern is generally discouraged in modern DI practices due to its potential to obscure a class's dependencies and make testing more difficult. However, it may be used in applications where DI container usage is impractical or when transitioning legacy code towards DI patterns.

#### Known Use of Service Locator

It is often used in large applications with complex configurations, or in applications where dependencies are dynamic and determined at runtime.
