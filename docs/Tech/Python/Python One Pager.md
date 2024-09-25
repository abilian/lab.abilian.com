## About this doc

This is a shorter, and hopefully more up to date, version of the [Abilian Developer Guide](https://abilian-developer-guide.readthedocs.io/) (unfortunately currently partly obsolete).

## Project organisation

### Tooling

The tools below are the standard tools we're using to keep project quality and developer efficiency high at Abilian.

#### Source control

- Git + GitHub
- Branching model: use short-lived feature branches.

#### Project management (including dependencies)

- Poetry
- Make
- [Abilian Devtools](https://pypi.org/project/abilian-devtools/)

#### Code formatting

- Black (format Python code - use default options)
- Isort (sort imports - use the "black" profile)
- DocFormatter (format docstrings)
- Pyupgrade / flynt (upgrade to take advantage of newer Python features)

#### Linting / static analysis

- Ruff
- Mypy
- Flake8 + additional plugins (Bandit...)
- pre-commit

#### TDD

- Pytest
- Nox (or Tox, for older projects)
- [Coverage.py](https://coverage.readthedocs.io/)
- Hypothesis

We don't recommend using the `unittest` package from the standard library, as its class-based design can lead to hard to understand test hierarchies.

More: [[Testing]]

#### CI

- GitHub Workflow
- Sourcehut CI

Note: the main CI script, for Python projects, is always the Nox or Tox file (`noxfile.py` / `tox.ini`). The GitHub Workflow config leverages it using proper plugins.

#### Debugging / profiling

- https://github.com/benfred/py-spy
- https://pypi.org/project/devtools/
- https://pypi.org/project/q/ (there are better, newer alternatives but I don't remember them)

#### Deployment

- We used to use Fabric but we're now switching to PaaS deployment (using the [12 factor](https://12factor.net/) principles). This is a WIP.

#### Documentation

Documentation starts with a good README (see: <https://tom.preston-werner.com/2010/08/23/readme-driven-development.html>).

Additionally, we use Sphinx but MkDocs can also be used. [Portray](https://github.com/timothycrosley/portray) could be useful.

### Project templates

Use [cookiecutter](https://github.com/cookiecutter/cookiecutter) templates to set up new projects.

Even better, use [Cruft](https://github.com/cruft/cruft) because it can update boilerplate after the initial project inception. ([Narative here](https://timothycrosley.com/project-6-cruft))

We have a project template here: https://github.com/abilian/cookiecutter-abilian-python (it needs to be updated regularly to keep up with best practices).

## General principles

Use Attrs and favor immutability when possible:

- <https://glyph.twistedmatrix.com/2016/08/attrs.html>
- <https://threeofwands.com/why-i-use-attrs-instead-of-pydantic/>

Things to know about subclassing:

- <https://hynek.me/articles/python-subclassing-redux/>

(TBC)

## Other resources

### Similar docs

- [The Best of the Best Practices (BOBP) Guide for Python](https://gist.github.com/sloria/7001839) (partly obsolete).
- Our own [Abilian Developer Guide](https://abilian-developer-guide.readthedocs.io/en/latest/) (unfortunately currently partly obsolete too).
- [Google's Python Style Guide](https://google.github.io/styleguide/pyguide.html)
- [Python Project Setup](https://github.com/alexpdp7/alexpdp7/blob/master/programming/python/project_setup.md)

### Great online Python docs / information sources

- [Full Stack Python](https://www.fullstackpython.com/table-of-contents.html)
- [Real Python](https://realpython.com/tutorials/intermediate/)
- [Awesome Python](https://github.com/vinta/awesome-python)
- [Awesome Cython](https://github.com/sfermigier/awesome-cython)

### Great Python books

- [Python Distilled](http://www.dabeaz.com/python-distilled/)
- [Fluent Python (2nd ed.)](https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/)
- [Robust Python](https://www.oreilly.com/library/view/robust-python/9781098100650/) (focusses on typed Python)

#python #one-pager
