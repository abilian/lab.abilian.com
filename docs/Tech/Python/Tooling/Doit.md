
[`Doit`](https://pydoit.org/) is a task runner and build tool for Python that aims to help automate tasks and manage dependencies between tasks. It is quite versatile and can be used for various purposes, including managing build processes, running tests, deploying code, and more.

Some advantages of using "doit" as a task runner are:

1.  Flexibility: Doit allows you to define tasks in Python, which means you can use the full power of Python when creating your tasks and workflows.
2.  Dependency management: Doit helps you manage dependencies between tasks, ensuring that tasks are executed in the correct order and only when necessary.
3.  Incremental builds: Doit supports incremental builds, which means it can skip tasks that have already been completed, reducing the time it takes to run your build or test process.
4.  Extensibility: Doit has a plugin system that allows you to extend its functionality and integrate with other tools and libraries.
5.  Cross-platform: As a Python-based tool, Doit can run on any platform where Python is supported.

## History

The history of doit can be traced back to the late 2000s, when it was created by [Eduardo Naufel Schettino](https://github.com/schettino72).

Eduardo started working on doit as an internal tool to automate the build process of his own Python projects. At the time, there were no task runners that were both easy to use and flexible enough for his needs. Existing tools like Make and SCons were powerful but required learning a domain-specific language, which was not ideal for Python projects. As a result, he decided to create a task runner that allowed users to define tasks using Python code and manage dependencies more efficiently.

Doit was officially released as an open-source project in 2008. Since then, it has been actively developed and maintained, with several releases and improvements being made over time. Doit has gained a dedicated user base due to its flexibility, simplicity, and dependency management capabilities.

### Usage

To get started with Doit, you'll need to install it, create a configuration file, and define tasks. Here's a step-by-step guide on how to use Doit:

#### Install Doit:

You can install Doit using `pip`, Python's package manager. Open a terminal or command prompt and run:

```
pip install doit
```

#### Create a `dodo.py` file:

Doit looks for a configuration file named `dodo.py` in your project directory. This file contains the tasks and their dependencies. Create a new file named `dodo.py` in your project's root folder.

#### Define tasks:

Tasks are defined as Python functions in the `dodo.py` file. Each function should return a dictionary with task metadata, such as the task's name, actions to perform, and dependencies.

Here's an example of a simple `dodo.py` file with two tasks:

```python
def task_hello():
    return {
        'actions': ['echo "Hello, World!"'],
        'verbosity': 2,
    }

def task_goodbye():
    return {
        'actions': ['echo "Goodbye, World!"'],
        'verbosity': 2,
    }
```

In this example, we've defined two tasks: `hello` and `goodbye`. Each task has a single action, which is a shell command that prints a message. The `verbosity` key is set to 2 to print more information when the tasks are executed.

#### Run tasks:

To run tasks, use the `doit` command followed by the task name. For example, to run the `hello` task, open a terminal or command prompt in your project directory and run:

```
doit hello
```

To run the `goodbye` task, run:

```
doit goodbye
```

To run all tasks, just run `doit` without any arguments:

```
doit
```

#### Manage dependencies between tasks:

You can define dependencies between tasks by using the `task_dep` key in the task dictionary. For example, let's add a new task named `greet` that depends on the `hello` and `goodbye` tasks:

```python
def task_greet():
    return {
        'actions': ['echo "Greet the world!"'],
        'task_dep': ['hello', 'goodbye'],
        'verbosity': 2,
    }
```

Now, when you run the `greet` task, Doit will automatically run the `hello` and `goodbye` tasks first:

```
doit greet
```

These are the basic steps to use Doit as a task runner. You can find more advanced features and examples in the [official documentation](https://pydoit.org/contents.html).

### References

- https://bitecode.substack.com/p/doit-the-goodest-python-task-runner

<!-- Keywords -->
#doit #tasks #python
<!-- /Keywords -->
