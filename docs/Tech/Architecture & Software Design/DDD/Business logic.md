In [[Domain-Driven Design]] (DDD), business logic primarily resides in three main areas:

1.  **[[Entities]]:** Entities encapsulate business rules that are related to the concept that the entity models. For instance, an `Order` entity could have a method to calculate the total price of the order. This is logic that naturally belongs to the order concept in the business domain.
    
2.  **[[Value objects]]:** Value objects can also contain business logic, especially when that logic pertains to the value concept that the object represents. For example, a `Money` value object could have a method to convert the amount to a different currency.
    
3.  **Domain Services:** Sometimes, business rules or procedures span multiple entities or value objects, or they don't naturally fit within a single entity or value object. In such cases, we create a Domain Service to handle this logic. For instance, a `PaymentProcessingService` might coordinate the interaction between `Order`, `Customer`, and `PaymentMethod` entities.

In addition, there are two more places where business logic may reside:

4.  **Aggregates:** An Aggregate is a cluster of associated objects that are treated as a unit for the purpose of data changes. The root of the Aggregate enforces the invariants (business rules) for the entire Aggregate.
    
5.  **Domain Events:** Domain Events represent something interesting that happened in the domain. They can be used to encapsulate business logic that needs to happen as a result of the event and propagate the impact of the event to other parts of the domain.

While the business logic is mostly present in the areas mentioned above, it's worth noting that DDD also emphasizes the importance of strategic design and context mapping. This means that the organization of business logic can depend on the specific context and that different models might be appropriate for different parts of the system.

## Example: an invoicing system

Sure, assuming that `InvoiceLine` can't exist independently of an `Invoice`, we can treat it as a Value Object. Let's modify the example:

1. **Entities:** In this case, `Customer`, `Invoice`, and `Product` would be entities. The `Invoice` entity might have a method `calculate_total` that sums up the totals of its `InvoiceLine` value objects.

```python
class Invoice:
    def __init__(self, invoice_lines):
        self.invoice_lines = invoice_lines

    def calculate_total(self):
        return sum(line.total for line in self.invoice_lines)
```

2. **Value Objects:** `InvoiceLine` and `Money` could be value objects. `InvoiceLine` represents the combination of a `Product`, a quantity, and a price (represented as a `Money` value object), and it can calculate its own total.

```python
@dataclasses.dataclass(frozen=True)
class InvoiceLine:
    product: Product
    quantity: int
    price: Money

    @property
    def total(self):
        return self.price * self.quantity
```

3. **Domain Services:** Suppose we have a business rule that says "when a Customer's total purchases exceed a certain amount, they are upgraded to a premium status." This rule spans multiple entities (`Customer`, `Invoice`) and thus might be implemented in a domain service.

```python
class CustomerStatusService:
    def upgrade_customer_status(self, customer):
        total_purchases = sum(invoice.calculate_total() 
                              for invoice in customer.invoices)
        if total_purchases > PREMIUM_THRESHOLD:
            customer.status = 'premium'
```

4. **Aggregates:** In this case, `Invoice` could be an aggregate root that ensures the consistency of the entire invoice - for example, it could ensure that there's at least one `InvoiceLine` in an `Invoice`, and that each `InvoiceLine` has a positive quantity.

5. **Domain Events:** When an `Invoice` is paid, an `InvoicePaid` domain event could be triggered, which might kick off other business processes - for example, it could reduce the quantity of the purchased products in stock, or it could update the customer's total purchases for the status upgrade rule mentioned above.

Remember, these are just examples. The actual design and organization of the business logic would depend on the specific requirements and constraints of your domain.

<!-- Keywords -->
#business #domain #entities #dataclasses #ddd
<!-- /Keywords -->
