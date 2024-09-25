Domain-Driven Design (DDD) is an approach to software development that emphasizes the importance of understanding and modeling the business domain throughout the software development process. It was popularized by Eric Evans in his book "Domain-Driven Design: Tackling Complexity in the Heart of Software." (Also called "The Blue Book" due to its cover color).

The core idea behind DDD is to create a software model that reflects the real-world business domain. This model can then guide the design and implementation of the software system. The premise is that by aligning the software model with the business domain, the software is more likely to solve the right problems and will be easier to understand and maintain.

Here are some key concepts and principles in DDD:

1.  **Ubiquitous Language:** This is a common language established by developers and domain experts to describe the business domain that the software will model. It should be used consistently in all discussions, documentation, and the code itself to ensure clear communication and shared understanding.
    
2.  **Bounded Context:** A bounded context is a boundary within which a particular model is defined and applicable. Within each bounded context, everything makes sense in terms of the specific model and the ubiquitous language used there.
    
3.  **Entities and Value Objects:** 
    1. [[Entities]] are objects that have a distinct identity that persists over time and across different states. They are usually identified by a unique id, which can be created using different strategies.
    2. [[Value objects]], on the other hand, are defined only by their attributes and do not have an identity. They are immutable and in Python, an opportunity to use the `@define` from `attrs` (or `@dataclasse(frozen=True)` from the stdlib).
    
4.  **Aggregates:** An aggregate is a cluster of domain objects (entities and value objects) that can be treated as a single unit. Aggregates ensure the consistency of changes to the objects within the aggregate boundary.
    
5.  **Repositories and Factories:** Repositories provide methods to retrieve domain objects, while factories are responsible for creating complex objects.
    
6.  **Domain Events:** These are events that have meaning within the business domain and typically represent something important happening in the domain.
    
7.  **Strategic Design:** This includes concepts like context mapping, which is about understanding how different bounded contexts interact with each other, and the use of patterns like Anti-Corruption Layer (ACL) to translate between different models.

DDD is not about specific technologies or programming languages; rather, it's a way of thinking and a set of priorities aimed at accelerating software projects' complexity and promoting better communication between technical and domain experts.

## References

- The Blue Book
- https://lyz-code.github.io/blue-book/architecture/domain_driven_design/ (not from the same "Blue Book")
