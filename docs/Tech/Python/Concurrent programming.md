
## Using `concurrent.futures`

`concurrent.futures` is a high-level interface for asynchronously executing callables (i.e., functions, methods, or any object that can be called). It's part of the standard library and provides two main components: `ThreadPoolExecutor` and `ProcessPoolExecutor`.

`ThreadPoolExecutor` and `ProcessPoolExecutor` are implementations of an interface defined by the abstract base class `Executor`. They allow you to manage and control the execution of tasks in different threads or processes, respectively.

Here's a simple example of how you can use `concurrent.futures`:

```python
from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(n)
    return n

with ThreadPoolExecutor(max_workers=4) as executor:
    future = executor.submit(task, 5)
    print(future.result())  # this will print '5' after waiting for 5 seconds
```

In this example, we're using `ThreadPoolExecutor` to create a pool of worker threads. The `submit()` method schedules a callable to be executed as `task(5)` and returns a `Future` object. `Future` objects represent the execution of the operation and allow you to check on the operation's status or result.

The `result()` method of a `Future` object returns the result of the operation once it's completed. If the operation hasn't completed yet, it will wait until it does. If the operation completed successfully, `result()` will return its result. If the operation raised an exception, `result()` will raise the same exception.

For multiple tasks, you can use `as_completed` function which yields futures as they complete:

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def task(n):
    time.sleep(n)
    return n

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = {executor.submit(task, n) for n in range(5)}
    for future in as_completed(futures):
        print(future.result())  # this will print the numbers 0 to 4 as they complete
```

In this example, we're submitting multiple tasks to the executor and getting an iterable of `Future` objects. Then, we're using `as_completed()` to iterate over these futures as they complete.

The main benefits of `concurrent.futures` is that it provides a high-level, Pythonic way to do multithreading or multiprocessing. However, if you need more control over your threads or processes, you might need to use the lower-level `threading` or `multiprocessing` modules instead.

### References

- https://towardsdatascience.com/python-concurrency-concurrent-futures-15b56dc9a14d

## Using actors

The [actor concurrent programming model](https://en.wikipedia.org/wiki/Actor_model) is supported in Python vias 3rd-party libraries, like [Pykka](https://pypi.org/project/pykka/) and [Thespian](https://pypi.org/project/thespian/).

The actor model is a design pattern for concurrent computation where "actors" are the universal primitives. They encapsulate state and behavior, communicate exclusively by sending messages, and each actor processes messages sequentially in the order they were received. This model helps to manage and reason about concurrency and distributed computation.

### Using Pykka

Here's a brief description of how you might use an actor system in Python using Pykka:

1. **Define Actor Classes**: In Pykka, an actor is an instance of any Python class that subclasses `pykka.ThreadingActor` or `pykka.FutureActor`. Here's an example:

    ```python
    import pykka

    class MyActor(pykka.ThreadingActor):
        def __init__(self, my_value):
            super().__init__()
            self.my_value = my_value

        def get_value(self):
            return self.my_value
    ```

    In this example, `MyActor` is an actor class with a single method `get_value()`. It also has a constructor that accepts an argument `my_value`.

2. **Create Actors**: To create an actor, just instantiate your class. The actor will start running in its own thread or process immediately.

    ```python
    actor_ref = MyActor.start(my_value=42)
    ```

    In this example, `MyActor.start(my_value=42)` creates a new `MyActor` actor with `my_value` set to `42`. It returns an `ActorRef` that you can use to interact with the actor.

3. **Send Messages to Actors**: You can ask an actor to execute a method by sending it a message. In Pykka, you do this using the `tell()` method for sending a message without waiting for a reply, or the `ask()` method for sending a message and waiting for a reply.

    ```python
    future = actor_ref.ask({'method': 'get_value'})
    print(future.result())  # prints '42'
    ```

    In this example, `actor_ref.ask({'method': 'get_value'})` sends a message to the actor asking it to execute the `get_value()` method. This returns a `Future` that will be completed with the result of the method.

4. **Stop Actors**: When you're done with an actor, you should stop it to free up its resources.

    ```python
    actor_ref.stop()
    ```

    In this example, `actor_ref.stop()` stops the actor.

### Using Thespian

The following example shows how you can create an actor system using Thespian:

1. **Define Actor Classes**: In Thespian, an actor is an instance of any Python class that subclasses `thespian.actors.Actor`. Here's an example:

    ```python
    from thespian.actors import Actor

    class MyActor(Actor):
        def __init__(self, my_value):
            self.my_value = my_value

        def receiveMessage(self, message, sender):
            if message == 'get_value':
                self.send(sender, self.my_value)
    ```

    In this example, `MyActor` is an actor class with a single method `receiveMessage()`. This method is called whenever the actor receives a message. It also has a constructor that accepts an argument `my_value`.

2. **Create Actors**: To create an actor, you need to create an actor system first and then use it to create your actor.

    ```python
    from thespian.actors import ActorSystem

    actor_system = ActorSystem()
    actor_ref = actor_system.createActor(MyActor, globalName='MyActor', my_value=42)
    ```

    In this example, `ActorSystem()` creates a new actor system. `actor_system.createActor(MyActor, globalName='MyActor', my_value=42)` creates a new `MyActor` actor with `my_value` set to `42`. It returns an `ActorRef` that you can use to interact with the actor.

3. **Send Messages to Actors**: You can ask an actor to execute a method by sending it a message. In Thespian, you do this using the `tell()` method.

    ```python
    future = actor_system.ask(actor_ref, 'get_value')
    print(future)  # prints '42'
    ```

    In this example, `actor_system.ask(actor_ref, 'get_value')` sends a message to the actor asking it to execute the `get_value()` method. It returns the result of the method directly.

4. **Stop Actors**: When you're done with an actor, you should stop it to free up its resources.

    ```python
    actor_system.tell(actor_ref, ActorExitRequest())
    ```

    In this example, `actor_system.tell(actor_ref, ActorExitRequest())` sends a message to the actor telling it to stop.

Notes: Thespian actors can be distributed across multiple machines and support a variety of serialization methods for messages. Actor failure can be detected and managed, and actors can be dynamically added or removed from the system. The messages passed between actors can be any Python object.

### Pros and cons of the actor model (in Python)

The actor model, as a concurrent computational model, has its strengths and weaknesses. It works best for systems with many independent entities that need to maintain their own state and behavior while occasionally interacting with each other. However, it is probably not be the best choice for problems that require a lot of data sharing or tight coupling between entities.
