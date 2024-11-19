The `baozi` library provides an alternative to `dataclasses` and `attrs`, emphasizing its own strengths in certain scenarios. Here's a detailed comparison of `baozi` to Python's `dataclasses` and the `attrs` library, particularly focusing on support for frozen objects.


### Comparison Overview

| Feature                           | `dataclasses`                          | `attrs`                               | `baozi`                                |
|------------------------------------|----------------------------------------|---------------------------------------|----------------------------------------|
| **Frozen Object Support**         | `@dataclass(frozen=True)`              | `@attrs(frozen=True)`                 | `FrozenStruct`                         |
| **Keyword-only Arguments**        | Supported (`kw_only=True` in Python 3.10+) | Fully supported                      | Default behavior                       |
| **Inheritance Handling**          | Limited, decorators need to be repeated | Fully supported                       | Enhanced with class-based configuration |
| **Pre-init Hook**                 | Not available                          | Partially available (via validators)  | `__pre_init__` for preprocessing       |
| **Typecasting**                   | Manual                                 | Via converters                        | Experimental support                   |
| **Field Defaults**                | Supported with `field(default=...)`    | Supported with `attrib(default=...)` | Supported with `field(default=...)`    |
| **Immutability Checks**           | Raises `FrozenInstanceError` for mutations | Enforces immutability at runtime     | Strict immutability, errors on mutable fields |
| **Slot Optimization**             | Optional (`slots=True`)                | Optional                              | Default for `FrozenStruct`             |
| **Configurability**               | Via `dataclass` arguments              | Via `@attrs` parameters or class config | Class-based inheritance or explicit config |
| **Performance**                   | Lightweight, faster than `attrs`       | Slightly slower than `dataclasses`    | Comparable to `dataclasses`, faster without validation |
| **Decorator-Free Approach**       | Not available                          | Not available                         | Classes inherently behave as structured objects |


### Frozen Objects in Particular

#### `dataclasses`
- **Freezing Behavior**: Achieved with `@dataclass(frozen=True)`. Immutable fields prevent reassignment, and attempts to modify raise a `FrozenInstanceError`.
- **Limitations**:
  - Mutability of default mutable fields like lists or dicts is not strictly enforced.
  - Manual declaration of `slots=True` is needed to optimize memory and performance.
  - Requires decorator repetition, especially when inheritance is involved.

#### `attrs`
- **Freezing Behavior**: Achieved with `@attrs(frozen=True)`. Similar to `dataclasses`, frozen instances prevent reassignment.
- **Strengths**:
  - Provides more robust support for immutability, with converters and validators enhancing type safety.
  - Integrates well with advanced features like `slots`.

#### `baozi`
- **Freezing Behavior**: Defaults to immutability for `FrozenStruct`:
  - `frozen=True`, `slots=True`, and `kw_only=True` by default.
  - If mutable fields like lists are declared, it raises a `MutableFieldError`, ensuring true immutability.
- **Advantages Over `dataclasses`**:
  - No decorator needed; immutability is inherent in `FrozenStruct`.
  - Provides enhanced runtime checks for immutability, avoiding pitfalls of mutable fields.
- **Advantages Over `attrs`**:
  - More performant due to its simpler design (no runtime validation unless explicitly defined).
  - Enforces stricter immutability rules by disallowing mutable fields entirely.
- **Limitations**:
  - Lacks the deep ecosystem and advanced validation options of `attrs`.


### Key Features Unique to `baozi`

1. **Inheritance with Configuration Propagation**:
   - Class-based structure allows easier inheritance of configurations, avoiding decorator repetition.
   - Configurable behavior through the `__model_config__` field or inheritance.

2. **`__pre_init__` Hook**:
   - Allows preprocessing of input data before object initialization, a feature not natively available in `dataclasses` or `attrs`.
   - Simplifies typecasting and pre-validation logic.

3. **Typecasting**:
   - Experimental support, making it easier to coerce input data types.

4. **Decorator-Free Approach**:
   - Avoids repetitive use of `@dataclass` or `@attrs` decorators, treating all classes inheriting `Struct` or `FrozenStruct` as structured objects.

5. **Slot Optimization by Default**:
   - `FrozenStruct` enables `slots` automatically, reducing memory usage and improving performance.


### Rationale for Using `baozi` Over Others

#### Advantages Over `dataclasses`:
- Simplifies class definitions by eliminating decorators.
- Ensures stricter immutability.
- Provides a more streamlined inheritance mechanism.
- Includes additional hooks (`__pre_init__`) for preprocessing.

#### Advantages Over `attrs`:
- Focuses on simplicity and performance, avoiding the overhead of validation unless explicitly needed.
- Enforces stricter immutability by disallowing mutable default fields.

#### When to Choose `baozi`:
- When you need strict immutability without worrying about mutable field pitfalls.
- When inheritance with consistent configuration is a requirement.
- When you prefer a decorator-free, class-based approach to defining structured objects.
- When preprocessing logic (`__pre_init__`) is necessary for initialization.


### Conclusion

`baozi` excels in scenarios where strict immutability, streamlined inheritance, and lightweight performance are critical. While it lacks the extensive ecosystem and validation features of `attrs`, its simplicity and class-based design make it a strong alternative to `dataclasses` and `attrs` for certain use cases. If frozen objects are a priority, `FrozenStruct` provides a robust, decorator-free solution with better immutability guarantees than `dataclasses` and a simpler approach than `attrs`.
