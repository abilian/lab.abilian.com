## References

[Design Patterns in Python for the Untrained Eye](https://arielortiz.info/s201911/pycon2019/docs/design_patterns.html) (Tutorial @ [PyCon USA 2019](https://us.pycon.org/2019/schedule/presentation/83/). May 1, 2019. Cleveland, OH. U.S.A.)

## Tayloring the classic design patterns to Python

The "Gang of Four" (GoF) design patterns were introduced in the book "Design Patterns: Elements of Reusable Object-Oriented Software" by Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides. While these patterns are generally language-agnostic, some are less relevant in Python due to its dynamic nature, built-in features, or Pythonic idioms. A few of these patterns include:

1.  **Singleton**: While the Singleton pattern is still relevant in Python, its implementation is simpler thanks to module-level variables. When you create a module-level variable in Python, it is effectively a singleton, as importing the module multiple times will not create new instances.
    
2.  **Factory Method**: In Python, you can use first-class functions and the dynamic nature of the language to achieve the same goal without explicitly implementing the Factory Method pattern. You can simply pass functions or classes around as objects, reducing the need for a separate factory class.
    
3.  **Template Method**: Python supports multiple inheritance and mixins, which can offer more flexibility than the Template Method pattern. Additionally, Python's first-class functions and dynamic typing allow for more straightforward alternatives, such as passing a function as an argument or using decorators.
    
4.  **Iterator**: In Python, the Iterator pattern is largely unnecessary due to the built-in support for iteration with the `for` loop, generators, and the iterator protocol. Python's language features make it easy to create custom iterable objects without needing to implement the pattern explicitly.
    
5.  **Command**: With Python's first-class functions and support for closures, you can often achieve the same goals as the Command pattern by passing functions as arguments or using lambda functions. This approach can be more concise and easier to read than explicitly implementing the Command pattern.
    
6.  **Strategy**: While the Strategy pattern is still relevant in Python, its implementation can be simplified using first-class functions. You can pass a function as an argument to a method, allowing you to change the algorithm at runtime without the need for a separate strategy class.

Please note that although these patterns may be less relevant or have simpler implementations in Python, they can still provide valuable insights into software design principles. Understanding the underlying concepts and trade-offs can help you make better design decisions, even if the patterns themselves are not explicitly applied.


## Overusing design patterns

"Patternitis" is an informal term used to describe the overuse or misuse of design patterns in software development. It occurs when developers become overly reliant on design patterns and apply them inappropriately or excessively, leading to overly complex and convoluted code. Patternitis can have several negative consequences, such as reduced code readability, maintainability, and flexibility.

1.  **Overengineering**: Applying design patterns when they are not needed can lead to overly complex and convoluted code. This can make the system harder to understand, maintain, and modify.
    
2.  **Premature optimization**: Implementing design patterns too early in the development process can cause developers to make assumptions about the system's requirements and constraints. This may result in an inflexible design that does not meet actual needs.
    
3.  **Inappropriate application**: Using a design pattern that does not fit the problem at hand can introduce unnecessary complexity or fail to address the underlying issue.

5. Excessive abstraction: Introducing too many layers of abstraction or indirection, making the code harder to understand and maintain.

6.  **Lack of understanding**: Applying design patterns without fully understanding their intent and trade-offs can result in incorrect or suboptimal implementations.
    
5.  **Reduced readability**: Overusing design patterns can lead to code that is difficult to read and understand, particularly for developers who are not familiar with the specific patterns used.
    
6.  **Neglecting simpler solutions**: Relying too heavily on design patterns may cause developers to overlook simpler, more efficient solutions that do not require a formal pattern.

To avoid these issues, it's essential to use design patterns judiciously and consider the following:

1.  **Understand the problem**: Make sure you have a clear understanding of the problem you're trying to solve before applying a design pattern.
    
2.  **Choose the right pattern**: Select the appropriate design pattern that addresses the specific problem and fits the context of your application.
    
3.  **Keep it simple**: Favor simplicity over complexity. Only use design patterns when they genuinely help solve a problem or improve the code's structure.
    
4.  **Know the trade-offs**: Be aware of the potential trade-offs and limitations of each design pattern, and ensure that the benefits outweigh the drawbacks in your specific case.
    
5.  **Continuously evaluate**: Regularly assess your codebase and refactor as needed to ensure that design patterns are used effectively and appropriately.

<!-- Keywords -->
#design_patterns
<!-- /Keywords -->
