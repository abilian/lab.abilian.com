
The `argparse` module in Python provides a convenient way to parse command-line arguments. It allows developers to define the arguments and options that their script should accept and will automatically generate a help message that can be displayed to users.

## Basic usage

The following is a basic example of how to use `argparse` in Python:

```python
import argparse

# Set up the parser
parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator"
)
parser.add_argument(
    "--sum",
    dest="accumulate",
    action="store_const",
    const=sum,
    default=max,
    help="sum the integers (default: find the max)",
)

# run
args = parser.parse_args(["--sum", "10"])
print(args.accumulate(args.integers))
# → 10
args = parser.parse_args(["--sum", "10", "20"])
print(args.accumulate(args.integers))
# → 30
```

In this example, we are defining a parser object and adding two arguments to it. The first argument, `integers`, is a positional argument that accepts one or more integers. The second argument, `--sum`, is an optional argument that sets the `accumulate` attribute to `sum` if it is present. Otherwise, it defaults to `max`.

The `parse_args()` method is called to parse the arguments passed to the script. The parsed arguments are stored in the `args` variable. In this example, we are using the `accumulate` attribute to either sum or find the maximum of the integers depending on the presence of the `--sum` argument.

## Positional arguments

Positional arguments are mandatory arguments that must be provided to the script. They are defined by calling the `add_argument()` method on the parser object and passing the name of the argument, a metavariable to be used in the help message, the type of the argument, and any other options that are required.

```python
parser.add_argument('filename', help='the name of the file to be processed')
```

In this example, we are defining a positional argument called `filename`. The `help` option is used to provide a description of what the argument is for. The metavariable is not specified, so it will default to the name of the argument.

## Optional arguments

Optional arguments are not mandatory and are prefixed by one or two hyphens (`-` or `--`). They are defined by calling the `add_argument()` method on the parser object and passing the name of the argument with a hyphen prefix, a metavariable to be used in the help message, and any other options that are required.

```python
parser.add_argument('--verbose', '-v', action='store_true', help='increase output verbosity')
```

In this example, we are defining an optional argument called `verbose` with two possible names: `--verbose` and `-v`. The `action` option is used to specify that the argument should be treated as a boolean flag. The `store_true` value indicates that if the flag is present, the `verbose` attribute will be set to `True`.

## Other options

The `argparse` module provides several other options that can be used when defining arguments. Here are some of the most commonly used options:

- `nargs`: The number of arguments to be consumed. The default value is `1`.
- `type`: The type of the argument. For example, `int`, `float`, `str`, etc.
- `choices`: A list of valid values that the argument can take.
- `default`: The default value of the argument.
- `required`: Whether or not the argument is required. The default value is `False`.
- `help`: A description of the argument that will be displayed in the help message.

## Usage in higher-level CLI frameworks

There are frameworks that provide higher-level abstractions on top of `argparse`, which can make it easier to create and maintain CLI tools. However, they still rely on `argparse` as a lower-level building block, which means that they provide all the same capabilities as `argparse`.

Examples include:

1. [**Cleez**](https://github.com/abilian/cleez): a Python CLI framework developped and used by Abilian. Cleez is a library that provides a high-level interface for building command-line interfaces in Python. It uses `argparse` as its underlying command-line parser and adds several features to make it easier to define and organize commands.
2. [**Cleo**](https://github.com/python-poetry/cleo), the CLI framework used by the Poetry project. Cleo is a library that provides a high-level interface for building command-line interfaces in Python. It uses `argparse` as its underlying command-line parser and adds several features to make it easier to define and organize commands. [NB: the documentation is not up to date.]
3.  [**Fire**](https://github.com/google/python-fire/blob/master/docs/guide.md): a Python CLI framework that uses `argparse` to automatically generate CLI commands from Python code. It can be used to create CLI tools with minimal effort and is particularly well-suited for data exploration and manipulation tasks.
5.  [**cement**](https://builtoncement.com/): a Python CLI framework that uses `argparse` as its underlying command-line parser. It provides a more high-level interface than `argparse` and adds several features to make it easier to define CLI tools, such as command nesting and configuration handling.
6.  **cliff**: a Python CLI framework that is built on top of `argparse`. It provides a higher-level interface than `argparse` and adds several useful features, such as command discovery, subcommand grouping, and more.

## Cons of using `arparse`

According to [Armin Ronacher]():

> `argparse` [...] has some behaviors that make handling arbitrary command line interfaces hard:
> -   `argparse` has built-in behavior to guess if something is an argument or an option. This becomes a problem when dealing with incomplete command lines; the behaviour becomes unpredictable without full knowledge of a command line. This goes against Click's ambitions of dispatching to subparsers.
> -  `argparse` does not support disabling interspersed arguments. Without this feature, it's not possible to safely implement Click's nested parsing.

## Conclusion

In this tutorial, we covered the basics of using the `argparse` module in Python to parse command-line arguments. We learned how to define positional and optional arguments and explored some of the other options that are available.

One of the great things about `argparse` is that it automatically generates a help message based on the arguments that are defined. This means that users of your script will be able to easily understand what each argument does and how to use them.

In addition to what we covered in this tutorial, `argparse` also provides a variety of other features, such as sub-commands, custom argument types, and more. If you're interested in learning more about these features, I recommend checking out the official documentation: [https://docs.python.org/3/library/argparse.html](https://docs.python.org/3/library/argparse.html).
