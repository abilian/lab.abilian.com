## Overview

The actor model is a conceptual model to deal with concurrent computation. It defines some general rules for how the system's components should behave and interact with each other. In the actor model, everything is an actor. An actor is a computational entity that, in response to a message it receives, can concurrently:

1. Make local decisions.
2. Create more actors.
3. Send more messages.
4. Determine how to respond to the next message received.

Actors can modify their own private state, but they cannot directly affect the state of other actors, making this model a powerful tool for designing and implementing systems that operate concurrently or in a distributed manner.

Source: <https://en.wikipedia.org/wiki/Actor_model>

## In Python

In Python, the actor model is not built into the core language, but it can be implemented through libraries that provide the necessary abstractions. Some of these libraries include:

- **[Pykka](https://github.com/jodal/pykka)**: Pykka is a Python implementation of the actor model, based on threads. The library provides simple and lightweight actor abstractions that allow you to build systems with concurrent processing without needing to deal with threads or locks directly.
- **[Thespian](https://github.com/kquick/Thespian)**: Thespian is a more feature-rich actor library for Python that supports local and distributed actors. It offers a flexible framework for managing actor behavior and communication in a way that scales from a single system to distributed systems.
- **Ray**: Though not limited to the actor model, Ray is a distributed execution framework that allows for easy scaling of Python applications. It includes support for actors, allowing developers to build systems that can easily scale across many nodes.

### Size

- Pykka: 1548 LOC
- Thespian: 12000 LOC

### Kamaelia

Kamaelia is a project aimed at building large scale online media delivery systems for the long term. Large scale media systems are naturally concurrent systems since they assume large numbers of people watching programmes simultaneously. In the long term the systems people will be using to access and serve BBC services online will also be naturally concurrent. A key aim of Kamaelia is to enable even novice programmers to create scalable and safe concurrent systems, quickly and easily.

Kamaelia provides a tool set for dealing with large scale concurrency in a manner very similar to UNIX pipelines, and is based on taking a hardware approach to software construction. This leads naturally to ease of system composition. The tool set includes a wide variety of pre-built components for creating network servers and clients along with components for handling media, interactive systems and text processing.

Kamaelia's architecture operates efficiently on existing single CPU architectures. It also encourages the construction of components that will also take advantage of the naturally parallel mainstream systems being developed by all major hardware vendors.

Kamaelia enables the majority of developers to create safer, more stable high performance systems, rather than a select few. Kamaelia encourages fine grained parallelism without the need for complex state-machine based designs or the overheads of large numbers of parallel threads of execution.

This tool set furthers the core goal in Kamaelia - allowing the BBC to experiment with systems for long term, large scale, online media delivery. By designing Kamaelia to lower the barrier to contribution we allow the community to join with us in building these systems.

"The second open-spaces session I attended was on [Kamaelia](http://www.kamaelia.org/Home), which is a very different approach to solving the concurrency challenge. This was convened by Kamaelia's creator. The question he asked was at the other end of the spectrum from things like "how do we prevent deadlock?" Instead, it was "what programming model is easiest for people to grasp and use" (which, of course, is the Pythonic way to look at the problem). His observation was that people make very effective use of Unix pipes and filters without knowing anything about concurrency, so Kamaelia is a system that allows you to create concurrent "filter" components with an easy way to wire such components together in sequence and in parallel. I found this approach quite compelling; one particularly attractive aspect is the ability to quickly wire together components for rapid testing and partial system building. Right now Kamaelia's concurrency is all process-based, but the use of threads (which would still be isolated like processes, but would just utilize threads if it helped performance) is a future consideration. I think Kamaelia is worth further exploration."

https://www.slideshare.net/kamaelian/kamaelia-europython-tutorial
https://www.bbc.com/rd/publications/whitepaper113

See also:

- **Guild**: https://pypi.org/project/guild/
- **Miniguild** - https://github.com/sparkslabs/guild/tree/master/examples/blog/miniguild

### More

- https://github.com/operand/agency A fast and minimal framework for building agent-integrated systems
- https://github.com/asynkron/protoactor-python/
- https://github.com/orsinium-labs/jockey Generic Python library for running asynchronous workers. Useful for building event handlers, web frameworks, and alike.
- https://github.com/SSripilaipong/lyrid
- https://github.com/tamland/python-actors.git
- https://pypi.org/project/pulsar/ (dead)
- Thoonk (dead)
- Parley (dead)
- Mochi Actors (again)
- Miniguild: https://github.com/sparkslabs/guild/tree/master/examples/blog/miniguild
- https://syndicate-lang.org/ a new model of concurrency, closely related to the actor, tuplespace, and publish/subscribe models.
- https://github.com/orsinium-labs/walnats Nats-powered event-driven background jobs and microservices framework for Python.

## In other languages

- Akka (Scala / Java)
- Celluloid (Ruby)
- Darlean (TypeScript): https://darlean.io/
- Kameo (Rust): https://docs.page/tqwewe/kameo

## Choice criteria

- need for distributed computing?
- scale of concurrency?
- complexity of the interactions between actors?

## Notes

When working with the actor model in Python (and choosing or developing an Actor framework), there are some important concepts to keep in mind:

- **Asynchronous Messaging**: Communication between actors is done via messages. This decouples the sender and receiver and allows for asynchronous processing.
- **Concurrency**: The actor model naturally supports concurrent execution, as each actor can potentially run in parallel, depending on the runtime environment and the library used.
- **Fault Tolerance**: Some actor model implementations provide strategies for dealing with actor failures, making the system more resilient.
- **Location Transparency**: The system can treat actors the same, regardless of whether they are on the same machine or distributed across a network. This simplifies the design of distributed applications.

## References

- **43 years of actors: a taxonomy of actor models and their key properties** (2016)
    The Actor Model is a message passing concurrency model that was originally proposed by Hewitt et al. in 1973. It is now 43 years later and since then researchers have explored a plethora of variations on this model. This paper presents a history of the Actor Model throughout those years. The goal of this paper is not to provide an exhaustive overview of every actor system in existence but rather to give an overview of some of the exemplar languages and libraries that influenced the design and rationale of other actor sys- tems throughout those years. This paper therefore shows that most actor systems can be roughly classified into four families, namely: Classic Actors, Active Objects, Processes and Communicating Event-Loops.
    http://soft.vub.ac.be/Publications/2016/vub-soft-tr-16-11.pdf
