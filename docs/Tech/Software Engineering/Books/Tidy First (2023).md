A book by Kent Beck (co-creator of "eXtreme Programming").

From the intro: "Messy code is a nuisance. "Tidying" code, to make it more readable, requires breaking it up into manageable sections. In this practical guide, author Kent Beck, creator of Extreme Programming and pioneer of software patterns, suggests when and where you might apply tidyings to improve your code while keeping the overall structure of the system in mind. Instead of trying to master tidying all at once, this book lets you try out a few examples that make sense for your problem."

## Main techniques

1. **Guard Clause**: This is a very effective technique for reducing code complexity and improving readability. By handling edge cases or invalid conditions at the beginning of a function, the main logic remains less indented and clearer.

1. **Normalize Symmetries**: Consistency in expressing similar logic is crucial for maintainability. It helps in understanding the codebase and reduces the cognitive load on developers.

1. **Explaining Variables/Constants**: This practice can significantly improve code readability. Naming a variable after the intention of the expression makes the code self-documenting, aiding in quicker comprehension.

1. **New Interface, Old Implementation**: This technique aligns with the principle of iterative development. It allows for gradually evolving a codebase without disrupting the existing functionality, making the transition smoother.

1. **Chunk Statements**: Properly organizing code with blank lines or in logical blocks enhances readability. It's a simple yet effective way to make the code more approachable and understandable.

1. **Extract Helper**: This technique is about breaking down complex logic into smaller, more manageable functions. It not only makes the code more readable but also encourages code reuse.

1. **One Pile**: This approach can be useful in situations where separating code obscures its understanding. By bringing related parts together, it can provide a more holistic view, aiding in better comprehension and further refactoring.

1. **Explaining Comments/Delete Redundant Comments**: Comments should provide additional context that is not immediately apparent from the code. Redundant comments that just restate the code should be avoided as they add noise.

1. **Delete Dead Code**: Keeping the codebase clean from unused code is crucial for maintainability. It reduces confusion and clutter.

1. **Reading Order and Cohesion Order**: Organizing code in a logical flow improves readability and maintainability. It's about making the codebase intuitive to navigate.

1. **Move Declaration and Initialization Together**: Keeping declaration close to its usage reduces the mental mapping required and makes the code more understandable.

1. **Explicit Parameters over Map/Dict**: Using explicit parameters for function arguments makes the interface of the function clearer and self-documenting.

In all these practices, the key is balance and context. What works best in one scenario might not be as effective in another. Kent Beck's advice to try changes and evaluate them is sound — often, the true impact of a change is best understood by seeing it in action and not just theoretically. This experimental approach, combined with good version control practices, allows for safe exploration and improvement of codebases.

## References

- The book: https://www.goodreads.com/book/show/171691901-tidy-first
- A review of the book: https://henrikwarne.com/2024/01/10/tidy-first/
