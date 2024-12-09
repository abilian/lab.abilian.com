Python docstrings are an integral part of writing clear and maintainable code. They provide inline documentation for modules, classes, methods, and functions, enabling both developers and automated tools to better understand the code's purpose and usage. Docstrings are enclosed in triple quotes (`"""`) and must be placed as the first statement inside the respective code block.

Choosing the right docstring format is crucial for readability and compatibility with documentation generation tools. Common formats include **PEP 257**, **Google Style**, **NumPy Style**, and **reStructuredText (reST)**. These formats differ in structure, readability, and support for automated documentation tools.

## Standards and conventions for docstrings

### PEP 257 (Standard Python Style)

PEP 257 defines Python's official guidelines for docstrings. It emphasizes simplicity and clarity, making it a good fit for basic projects.

#### Features:

- Use triple double quotes (`"""`) for all docstrings, including one-liners.
- For one-liners, place the closing quotes on the same line.
- Start with a summary line followed by a blank line, then provide additional details if necessary.

**Example**:

```python
def add(a, b):
    """Add two numbers and return the result.

    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b
```


### Google Style

The Google Style docstring format is widely used due to its clean and intuitive structure. It breaks documentation into clearly marked sections.

#### Features:

- Use headers like `Args`, `Returns`, and `Raises`.
- Provide concise yet descriptive entries for each parameter and return type.

**Example**:

```python
def divide(a, b):
    """Divide two numbers.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Returns:
        float: The result of the division.

    Raises:
        ZeroDivisionError: If the denominator is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b
```


### NumPy Style

NumPy Style is the standard for scientific computing libraries. It organizes documentation into well-structured sections with tabular formats for parameters and return types.

#### Features:

- Headers like `Parameters`, `Returns`, and `Raises`.
- Each section uses a table-like format, making it detailed and clear.

**Example**:

```python
def multiply(a, b):
    """
    Multiply two numbers.

    Parameters
    ----------
    a : int or float
        The first number.
    b : int or float
        The second number.

    Returns
    -------
    int or float
        The product of `a` and `b`.
    """
    return a * b
```


### reStructuredText (reST) Style

reStructuredText is a versatile and powerful format often used with Sphinx for generating static documentation. It supports advanced markup for headings, code, and links.

#### Features:

- Integrates well with Sphinx for generating HTML, PDF, and other formats.
- Supports rich formatting, including cross-references and inline markup.

**Example**:

```python
def subtract(a, b):
    """
    Subtract one number from another.

    :param a: The number to subtract from.
    :type a: int or float
    :param b: The number to subtract.
    :type b: int or float
    :return: The result of `a - b`.
    :rtype: int or float
    :raises ValueError: If the inputs are not numbers.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Inputs must be numbers.")
    return a - b
```


## Tools for Docstring-Based Documentation

To maximize the value of docstrings, you can use tools to automatically generate rich documentation for your project:

### MkDocs

- A lightweight static site generator that uses Markdown for documentation.
- Extensions like `mkdocstrings` can render Python docstrings as Markdown.
- Great for developers looking for quick, visually appealing documentation with minimal setup.

### MkDocs-Material

- A popular theme for MkDocs with enhanced design and interactivity.
- Features like dark mode, versioning, and navigation make it ideal for modern documentation.

### pdoc

- A straightforward tool for generating Python API documentation directly from code.
- Uses Markdown for output, making it compatible with tools like MkDocs.
- Use `pdoc`, not `pdoc3` or `pdocs`.

### Sphinx

- A powerful documentation generator.
- Integrates with reST and supports Markdown via **MyST-Parser**.
- Autodoc extensions extract docstrings directly into HTML or PDF outputs.
- Ideal for large-scale projects requiring cross-references, indices, and multi-language support.

### Portray

- Focused on simplicity and automation, Portray generates project documentation with minimal configuration.
- Extracts docstrings to build intuitive and consistent documentation sites.
- Abandonware.

### Epydoc

- An older tool designed for documenting Python APIs, particularly with reST.
- Provides output in HTML and PDF but is less commonly used in modern workflows.

## Caveats about import side effects

When tools like **Sphinx**, **pdoc**, or others parse Python files to extract docstrings, they may import modules and execute code. This can result in unintended side effects, such as:

1. **Database Connections or API Calls**: Modules that establish connections during import can inadvertently trigger live queries or transactions.
2. **Resource Usage**: Code that initializes resources (e.g., creating files, spawning threads) on import may consume unnecessary memory or disk space.
3. **Execution of Scripts**: If a file uses `if __name__ == "__main__":` and is improperly structured, parts of the script could execute unintentionally.
4. **Errors or Crashes**: Errors in module-level code may prevent the tool from successfully parsing docstrings.

### Mitigations

1. **Guard Against Execution**: Always use `if __name__ == "__main__":` guards to prevent unintended execution of code during imports.
2. **Minimal Module Initialization**: Avoid heavy computations or resource initialization in the global scope of a module.
3. **Dedicated Configuration**: Some tools, like Sphinx, allow you to use a custom configuration file (e.g., `conf.py`) to fine-tune imports and avoid issues.
4. **Testing Before Generation**: Ensure the codebase is clean and free of errors to prevent complications during parsing.

## Summary: Comparison of Docstring Formats

| **Feature**             | **PEP 257** | **Google Style** | **NumPy Style** | **reST Style** |
| ----------------------- | ----------- | ---------------- | --------------- | -------------- |
| **Readability**         | Moderate    | High             | High            | Moderate       |
| **Ease of Parsing**     | Simple      | Simple           | Simple          | Complex        |
| **Structured Sections** | Minimal     | Yes              | Yes             | Yes            |
| **Tool Compatibility**  | High        | High             | High            | High (Sphinx)  |

### Choosing a Docstring Format

- **PEP 257**: Best for simple scripts and small projects.
- **Google Style**: Preferred for general-purpose Python projects.
- **NumPy Style**: Ideal for scientific, data analysis, and machine learning libraries.
- **reST Style**: Suitable for projects requiring detailed Sphinx-based documentation.
