#python #cli

## CLI frameworks

### From the standard library

1.  **argparse**: argparse is a built-in Python module that provides a way to parse command-line arguments. It's easy to use and provides a lot of flexibility, making it a popular choice for writing command-line interfaces in Python.
    - → More info + tutorial: [[Argparse]]

\+ Others, not recommended (IMHO).

### Frameworks based on argparse

See [[Argparse#Usage in higher-level CLI frameworks]]

### Click family

1.  **Click**: a popular Python CLI framework that is built on top of `optparse`. It provides a more user-friendly interface than `argparse` and adds several useful features, such as command grouping, automatic help page generation, and more.
2.  **Typer**: a relatively new Python CLI framework that is also built on top of Click. It provides a simpler interface than Click and aims to be very easy to use. Typer is particularly well-suited for creating CLI tools that interact with APIs.

Click is internally based on `optparse` instead of `argparse`. This is an implementation detail that a user does not have to be concerned with. Click is not based on `argparse` because it has some behaviors that make handling arbitrary command line interfaces hard:
-   `argparse` has built-in behavior to guess if something is an argument or an option. This becomes a problem when dealing with incomplete command lines; the behaviour becomes unpredictable without full knowledge of a command line. This goes against Click's ambitions of dispatching to subparsers.
-   `argparse` does not support disabling interspersed arguments. Without this feature, it's not possible to safely implement Click's nested parsing.

### Others

1. **docopt**: docopt is another Python package that provides a way to define a CLI by describing it in a docstring. It automatically generates the parser and makes it easy to define complex command-line interfaces.

### Other frameworks

- Tyro: https://brentyi.github.io/tyro/ Uses type annotations in functions or dataclasses.
- https://github.com/BrianPugh/cyclopts "Cyclopts is what you thought Typer was. Cyclopts's includes information from docstrings, support more complex types (even Unions and Literals!), and include proper validation support."

### CLI best practices

- <https://clig.dev/>
- <https://medium.com/jit-team/guidelines-for-creating-your-own-cli-tool-c95d4af62919>
- https://zapier.com/engineering/how-to-cli/
- https://hackmd.io/@arturtamborski/cli-best-practices
- https://eng.localytics.com/exploring-cli-best-practices/

## Other topics

### Terminal output

- https://bernsteinbear.com/blog/python-parallel-output/

### Tab completion

- https://github.com/iterative/shtab
- https://pypi.org/project/argcomplete/ (slower)

### Console utilities

- Rich (lots of - maybe to many - features)
- Colorama
- https://pypi.org/project/wasabi/ "wasabi: A lightweight console printing and formatting toolkit"


### Formatting

How to get terminal width?

```python
import os
width = os.get_terminal_size().columns
print(f"Terminal width: {width}")
```

## Older notes

Existing frameworks:

- Fire: https://github.com/google/python-fire
- Click: https://pypi.org/project/click/
- Typer (= click extension, driven by type annotations)
- Cleo: https://github.com/sdispater/cleo


More

- Clint (obsolete) = mostly convenience functions.

<!-- Keywords -->
#argparse #python
<!-- /Keywords -->
