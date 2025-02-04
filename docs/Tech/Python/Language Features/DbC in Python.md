[Design by Contract (DbC)](https://en.wikipedia.org/wiki/Design_by_contract) is a software development methodology aimed at improving software correctness by defining formal, precise, and verifiable interface specifications. Initially popularized in languages like Eiffel, DbC focuses on creating clear contracts between software components, particularly functions or methods, where each component must fulfill specific obligations, known as "contracts." These contracts generally consist of three main elements:

1. **Preconditions** - Requirements that must be true before a function or method can be executed.
2. **Postconditions** - Conditions that should hold after the function or method has been executed.
3. **Invariants** - Conditions that remain true during the lifetime of an object, ensuring the object’s consistency.

Python does not natively support DbC, as languages like Eiffel do, but various strategies and libraries enable developers to approximate the DbC paradigm effectively.

## Implementing DbC in Python

In Python, DbC can be implemented using:

### Assertions:

- Assertions allow for basic contract validation by checking that conditions hold true at certain points in a function.
- Preconditions are implemented at the start of the function to ensure that arguments are valid.
- Postconditions are checked at the end of the function to confirm that the function has produced the correct output.
- Assertions can also be used to enforce invariants within methods to maintain consistent object state.

```python
def withdraw(account, amount):
   # Precondition
   assert amount > 0, "Withdrawal amount must be positive"
   assert account.balance >= amount, "Insufficient funds"

   # Withdraw amount
   account.balance -= amount

   # Postcondition
   assert account.balance >= 0, "Balance cannot be negative"
   return account.balance
```

While assertions are helpful, they can be turned off in production if Python runs in optimized mode (`python -O`), which could inadvertently disable contract checks. Wether you are using DbC or not, you should never consider contracts or assertions a runtime feature of your software!

### Type Hints and Annotations:

- Python's type hints, introduced in PEP 484, enhance DbC by enabling parameter and return type constraints, though they are not enforced at runtime (unless you are using something like [typeguard](https://github.com/agronholm/typeguard) or [beartype](https://github.com/beartype/beartype) - which are cool BTW). Type hints make contracts clearer to the developer and tools like `mypy` and `pyright` can statically verify type correctness.

```python
def add(x: int, y: int) -> int:
   return x + y
```

### 3rd-Party Libraries:

- Libraries such as [`icontract`](https://pypi.org/project/icontract/) and [`deal`](https://pypi.org/project/deal/) provide more sophisticated support for DbC in Python by adding decorators to enforce preconditions, postconditions, and invariants.

```python
import icontract

@icontract.require(lambda x: x > 0)
@icontract.ensure(lambda result: result > 0)
def sqrt(x: float) -> float:
   return x ** 0.5
```

These libraries throw custom exceptions if conditions are violated, making it easier to track and handle contract violations in a structured way.

### `post_init` in Data Classes:

- Python’s data classes provide a `__post_init__` method, which can be used to enforce invariants and preconditions immediately after object initialization.

```python
from dataclasses import dataclass

@dataclass
class Account:
   balance: float

   def __post_init__(self):
       assert self.balance >= 0, "Initial balance cannot be negative"
   ```

## Relationship with type hints

Contracts and type hints serve complementary roles in enforcing code correctness: type hints specify data types and enable static checking through tools like `mypy`, while contracts add behavioral constraints, usually runtime-enforced.

While type hints improve code clarity and prevent certain type errors before execution, they cannot, in practice, enforce value-specific conditions (e.g., requiring positive integers). Contracts fill this gap by providing preconditions, postconditions, and invariants to ensure logical consistency beyond what types alone can validate.

## Advantages and Limitations of DbC in Python

Given the above techniques, our experience with contracts is the following:

#### Advantages
- **Improved Code Correctness**: Explicitly defined contracts make it easier to identify and prevent errors by ensuring that function inputs and outputs adhere to specified conditions.
- **Enhanced Code Readability**: Contracts improve documentation by clearly specifying the expected behavior of functions and classes, making it easier for other developers to understand and use the code.
- **Easier Testing**: Predefined contracts simplify test cases, as they document the expected behavior and help identify edge cases more easily. They might also help in generated automated tests (e.g. property-based testing).

#### Limitations
- **Performance Overhead**: Contracts, especially if enforced via extensive checks, introduce significant performance overhead.
- **Lack of Native Support**: Since Python lacks native DbC support, developers rely on third-party libraries or conventions, which might lead to inconsistencies or incomplete contract enforcement.
- **Lack of reasoning capabilities**: Python and most of the third-party libraries that support contracts do not inherently support reasoning about contracts, meaning there is limited automatic analysis for proving or disproving contract correctness. Unlike in languages with formal DbC support, where contracts can be formally verified (e.g., using theorem provers or static analyzers), Python lacks the tooling for formally reasoning about the behavior of contracts. As a result, Python's DbC relies heavily on runtime checks rather than compile-time guarantees, which can miss certain edge cases or logical contradictions within complex systems.
- **Limited Enforcement in Production**: Assertions, commonly used for contracts, can be turned off in production environments. This might leave software without crucial checks if not handled carefully.

### Example of a Python Function with DbC

Using a mix of assertions and the `icontract` library, here’s an example of a Python function implementing DbC principles:

```python
import icontract

class BankAccount:
    def __init__(self, balance: float):
        assert balance >= 0, "Initial balance must be non-negative"
        self.balance = balance

    @icontract.require(lambda self, amount: amount > 0)
    @icontract.require(lambda self, amount: self.balance >= amount, "Insufficient balance")
    @icontract.ensure(lambda self, result: result >= 0, "Balance should be non-negative")
    def withdraw(self, amount: float) -> float:
        self.balance -= amount
        return self.balance
```

In this code:
- Preconditions ensure a positive `amount` and sufficient balance for withdrawal.
- A postcondition ensures the balance remains non-negative after the operation.

## References

- [deal](https://github.com/life4/deal),
- [icontract](https://pypi.org/project/icontract/),
- [PyContracts](https://pypi.org/project/PyContracts/),
- [dpcontracts](https://pypi.org/project/dpcontracts/)
- Language support for design by contracts was proposed in [PEP-316](https://peps.python.org/pep-0316/) in 2003, but is deferred.
- [Design by Contract in Python: Present and Future](https://indico.cern.ch/event/44/contributions/1942565/attachments/940379/1333607/presentation.pdf) - This presentation from 2006 concludes "(We) need a tool to control contract checking at package, module, class, and method level without editing affected module"
