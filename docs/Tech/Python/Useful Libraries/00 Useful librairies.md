Some (potentially) useful Python libraries.

## Web

https://github.com/tartiflette/tartiflette "GraphQL Engine built with Python 3.6+ / asyncio"
See also: <https://github.com/sfermigier/awesome-python-web-frameworks>

## Serialization / deserialization

Currently using Marshmallow.
Not a fan of Pydantic.

Potentially useful:

- https://github.com/python-desert/desert (combines Attrs and Marshmallow)
- https://pypi.org/project/dataclasses-json/
- https://github.com/Tinche/cattrs

## HTML / XML generation

-> [[Templating]]

## Configuration

- https://www.dynaconf.com/ "Configuration Management for Python."
- or: https://typed-settings.readthedocs.io/
- Or: https://github.com/zifeo/dataconf
- https://omegaconf.readthedocs.io/ (YAML based)
- GIN: https://github.com/google/gin-config (a lightweight configuration framework for Python)
- https://hydra.cc/
- https://pypi.org/project/upsilonconf/
- https://pypi.org/project/python-decouple/
- https://pypi.org/project/ConfigFramework/

Blog posts:

- https://dxiaochuan.medium.com/summary-of-python-config-626f2d5f6041

## Distributed systems

https://pypi.org/project/janus/ "Mixed sync-async queue, supposed to be used for communicating between classic synchronous (threaded) code and asynchronous (in terms of [asyncio](https://docs.python.org/3/library/asyncio.html)) one."

## Parsing

https://pypi.org/project/lark/ "Lark is a modern general-purpose parsing library for Python." (LALR(1), Earley parsing)

https://github.com/dabeaz/sly "Lex + YACC in Python" (When you already have a YACC grammar for a language).

## Dev tooling

Were currently using:

- Poetry
- Black
- Flake8 + additional plugins (Bandit...)
- Pytest
- Tox
- Mypy

See [[Project templates]] for how to set up these tools properly.

Some additional resources:

- https://pypi.org/project/devtools/ "Python's missing debug print command and other development tools." (Detailed discussion [[Python debug tools]]).
- https://pypi.org/project/stdeb/ "produces Debian source packages from Python packages"
- https://pypi.org/project/hupper/ "hupper is an integrated process monitor that will track changes to any imported Python files in sys.modules as well as custom paths. When files are changed the process is restarted."

## CLI

Now using [[Cleez]].

Before that, we were using Fire because it's the simplest one.

- https://github.com/google/python-fire "Python Fire is a library for automatically generating command line interfaces (CLIs) from absolutely any Python object."

Other useful libraries include Click and Typer.

## Devops

- https://pypi.org/project/py-healthcheck/ (Adds healthcheck endpoints to Flask or Tornado apps)

## URL manipulation

- https://github.com/gruns/furl
- https://github.com/aio-libs/yarl/

## Authentication

2 librairies are maintained:

- https://github.com/lepture/authlib
- https://github.com/oauthlib/oauthlib

## Storage / cache

- https://github.com/BuzonIO/zipfly -> manage ZIP files without blowing up your memory.
- https://github.com/grantjenks/python-diskcache
- https://www.pyfilesystem.org/
