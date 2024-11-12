
## Dependency injector

```python
from dependency_injector import containers, providers
from dependency_injector.wiring import Provide, inject

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    api_client = providers.Singleton(
        ApiClient,
        api_key=config.api_key,
        timeout=config.timeout,
    )

    service = providers.Factory(
        Service,
        api_client=api_client,
    )

@inject
def main(service: Service = Provide[Container.service]) -> None:
    ...

if __name__ == "__main__":
    container = Container()
    container.config.api_key.from_env("API_KEY", required=True)
    container.config.timeout.from_env("TIMEOUT", as_=int, default=5)
    container.wire(modules=[__name__])

    main()  # <-- dependency is injected automatically

    with container.api_client.override(mock.Mock()):
        main()  # <-- overridden dependency is injected automatically
```

## Injector

```python

from dataclasses import dataclass
from injector import Injector, inject
class Inner:
    def __init__(self):
        self.forty_two = 42

@inject
@dataclass
class Outer:
    inner: Inner

injector = Injector()
outer = injector.get(Outer)
print(outer.inner.forty_two)  # Prints 42

```

See: https://injector.readthedocs.io/en/latest/practices.html

## Inject

```python
# Import the inject module.
import inject


# `inject.instance` requests dependencies from the injector.
def foo(bar):
    cache = inject.instance(Cache)
    cache.save('bar', bar)


# `inject.params` injects dependencies as keyword arguments or positional argument. 
# Also you can use @inject.autoparams in Python 3.5, see the example above.
@inject.params(cache=Cache, user=CurrentUser)
def baz(foo, cache=None, user=None):
    cache.save('foo', foo, user)

# this can be called in different ways:
# with injected arguments
baz('foo')

# with positional arguments
baz('foo', my_cache)

# with keyword arguments
baz('foo', my_cache, user=current_user)


# `inject.param` is deprecated, use `inject.params` instead.
@inject.param('cache', Cache)
def bar(foo, cache=None):
    cache.save('foo', foo)


# `inject.attr` creates properties (descriptors) which request dependencies on access.
class User(object):
    cache = inject.attr(Cache)
            
    def __init__(self, id):
        self.id = id

    def save(self):
        self.cache.save('users', self)
    
    @classmethod
    def load(cls, id):
        return cls.cache.load('users', id)


# Create an optional configuration.
def my_config(binder):
    binder.bind(Cache, RedisCache('localhost:1234'))

# Configure a shared injector.
inject.configure(my_config)


# Instantiate User as a normal class. Its `cache` dependency is injected when accessed.
user = User(10)
user.save()

# Call the functions, the dependencies are automatically injected.
foo('Hello')
bar('world')
```

## Punq

```python
class FileWritingGreeter:
   def __init__(self, path, greeting):
      self.path = path
      self.message = greeting
      self.file = open(self.path, 'w')

   def greet(self):
      self.file.write(self.message)

container.register(Greeter)

# or
one_true_greeter = FileWritingGreeter("/tmp/greetings", "Hello world")
container.register(Greeter, instance=one_true_greeter)

# Use it
greeter = container.resolve(Greeter, path="/tmp/foo", greeting="Hello world")
```

## Kink

```python
from kink import inject, di
import MySQLdb

# Set dependencies
di["db_host"] = "localhost"
di["db_name"] = "test"
di["db_user"] = "user"
di["db_password"] = "password"
di["db_connection"] = lambda di: MySQLdb.connect(host=di["db_host"], user=di["db_user"], passwd=di["db_password"], db=di["db_name"])

@inject
class AbstractRepository:
    def __init__(self, db_connection):
        self.connection = db_connection

class UserRepository(AbstractRepository):
    ...

repository = di[UserRepository] # will retrieve instance of UserRepository from di container
repository.connection # mysql db connection is resolved and available to use.
```

## DI

```python
from dataclasses import dataclass

from di import Container
from di.dependent import Dependent
from di.executors import SyncExecutor

class A:
    ...

class B:
    ...

@dataclass
class C:
    a: A
    b: B

def main():
    container = Container()
    executor = SyncExecutor()
    solved = container.solve(Dependent(C, scope="request"), scopes=["request"])
    with container.enter_scope("request") as state:
        c = solved.execute_sync(executor=executor, state=state)
    assert isinstance(c, C)
    assert isinstance(c.a, A)
    assert isinstance(c.b, B)
```

## RODI

The `ContainerProtocol` for v2 is inspired by [punq](https://github.com/bobthemighty/punq).

```python
"""
This example illustrates a basic usage of the Container class to register
two types, and automatic resolution achieved through types inspection.

Two services are registered as "transient" services, meaning that a new instance is
created whenever needed.
"""

from rodi import Container


class A:
    pass


class B:
    friend: A


container = Container()

container.register(A)
container.register(B)

example_1 = container.resolve(B)

assert isinstance(example_1, B)
assert isinstance(example_1.friend, A)


example_2 = container.resolve(B)

assert isinstance(example_2, B)
assert isinstance(example_2.friend, A)

assert example_1 is not example_2
```

More examples: https://github.com/Neoteroi/rodi/tree/main/examples

## Opyiod

```python
from opyoid import Module, Injector


class MyClass:
    pass


class MyParentClass:
    def __init__(self, my_param: MyClass):
        self.my_param = my_param


class MyModule(Module):
    def configure(self) -> None:
        self.bind(MyClass)
        self.bind(MyParentClass)


injector = Injector([MyModule])
my_instance = injector.inject(MyParentClass)
assert isinstance(my_instance, MyParentClass)
assert isinstance(my_instance.my_param, MyClass)
```

<!-- Keywords -->
#dependency_injector #injector
<!-- /Keywords -->
