In Domain-Driven Design ([[DDD]]), a Value Object is an object that contains attributes but has no conceptual identity. They are used to represent concepts in the domain that are purely defined by their state (attributes) and not by any unique identifier.

Value Objects are often used to represent simple objects whose equality isn't based on identity. Two Value Objects are equal when their values are equal.

Here are a few characteristics of Value Objects:

1. **Immutability:** Value Objects are usually designed to be immutable. Once a Value Object is created, it cannot be modified. If you want to change a Value Object, you create a new one.

2. **Equality:** Value Objects are equal if all their fields are equal.

3. **Lack of identity:** Unlike entities, Value Objects don't have a unique identifier. A Value Object doesn't have an identity like an Entity does.

Let's look at a Python example of a Value Object:

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Address:
    street: str
    city: str
    state: str
    zip_code: str

address1 = Address("123 Main St", "Springfield", "IL", "12345")
address2 = Address("123 Main St", "Springfield", "IL", "12345")

assert address1 == address2
```

In this example, `Address` is a Value Object. It has no identity or identifier; it's purely a collection of values. We've made it immutable by using a dataclass with `frozen=True`. Two `Address` objects with the same values are considered equal.

Value Objects are quite powerful, and using them can help make your code more understandable and correct by aligning it with the actual domain concepts. For example, in the domain of a certain application, it might make sense to have a `PhoneNumber` or an `Email` Value Object, rather than just representing these as simple strings. By creating a Value Object, you can encapsulate any behavior related to these concepts (like formatting or validation) within the Value Object itself, rather than spreading this logic throughout your application.

## Business logic on value objects

The number of methods in a Value Object can vary depending on the complexity of the concept it's modeling and the use cases in your domain.

In some cases, a Value Object may simply be a "dumb" data container with no methods other than perhaps some basic validation in its constructor. This might be the case for something like an `Address` or a `DateRange` that simply groups related values together without adding much additional behavior.

However, Value Objects can also encapsulate more complex behavior related to the concept they're modeling. For example, a `Money` Value Object might include methods for adding or subtracting amounts, converting currencies, or formatting the amount for display. A `DateRange` might include methods for checking whether a given date falls within the range or whether it overlaps with another range.

As a rule of thumb, behavior that relates to the concept being modeled should be encapsulated within the Value Object itself. This helps to keep your domain model clean and cohesive, and ensures that related behavior is located in a logical place.

It's also worth noting that, due to their immutability, methods on a Value Object that would "modify" it in some way should instead return a new Value Object with the modified state. For example, a `DateRange.extend` method might return a new `DateRange` that extends the original by a given amount.

Finally, it's generally a good idea to keep your Value Objects relatively small and simple. If you find that a Value Object is growing very large or complex, it might be a sign that you need to refactor it into multiple smaller Value Objects or even consider whether it should be an Entity instead.

<!-- Keywords -->
#values #dataclasses #dataclass
<!-- /Keywords -->
