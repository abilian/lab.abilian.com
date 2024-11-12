Message queues are a foundational component in modern [[00 Intro to software architecture|Software Architecture]], essential for enabling asynchronous communication between different parts of a system. They, however, comme in a large variety of approaches, fonctionnalities and use cases. To navigate this landscape, it's beneficial to first understand the core concepts, the advantages they offer, the considerations for effective usage, and the general principles that apply across different implementations. They we will discuss a few solutions available for the Python developers.

### What Are Message Queues?

At their most basic, message queues are a form of asynchronous service-to-service communication used in serverless and microservices architectures. They allow different parts of a system to communicate and process operations without blocking the sender's operations. A message queue provides a buffer that temporarily stores messages until the receiving service can process them.

### Why Are They Useful?

1. **Decoupling of Processes:** Producers of data (senders) and consumers of data (receivers) operate independently. The producer doesn't need to wait for the consumer to be ready or available to process the data.
2. **Scalability:** Systems can scale more easily. Workloads can be distributed across multiple consumers, and additional consumers can be added to handle high load.
3. **Reliability:** They can ensure that messages are not lost, even if the consumer is down or busy, the messages are stored and can be retried.
4. **Asynchronous Processing:** They enable asynchronous data processing, which is essential for tasks that are resource-intensive or require significant time to complete.

### How to Use Them Effectively?

1. **Understand the Problem Domain:** Assess if a message queue fits the architectural needs of your system. Not all inter-service communication needs a message queue.
2. **Choose the Right Tool:** Consider factors like throughput, latency, message size, and system reliability. Different message queues offer different features and trade-offs.
3. **Idempotency:** Ensure that your system can handle duplicate messages gracefully. Message delivery might not always be once and only once.
4. **Error Handling:** Plan for message processing failures (e.g., dead letter queues for messages that can't be processed after several attempts).
5. **Monitoring and Alerting:** Implement proper monitoring to track queue length, error rates, and processing times to prevent issues from going unnoticed.

### Which Implementation to Pick? Does It Matter?

It does matter, but the extent depends on specific use cases and requirements. Some popular message queue systems include RabbitMQ, Apache Kafka, AWS SQS, and Google Pub/Sub. While they all provide the basic functionality of a message queue, they differ in terms of scalability, durability, delivery guarantees, and other features.

### Learning Curve: Specifics vs. General Concepts

While each message queue implementation has its own specifics, many concepts are general:

- **Producers and Consumers:** Understanding the roles of message producers and consumers is fundamental.
- **Message Durability:** Knowing how a message queue handles persistence allows you to design for system failures.
- **Delivery Guarantees:** Concepts like "at-least-once," "at-most-once," or "exactly-once" delivery are common across many systems.
- **Message Ordering:** Some systems guarantee order, others do not.
- **Back Pressure Management:** Understanding how a system handles an overload of messages is crucial.

## Solutions

### General-Purpose Message Queues and Enabling Technologies

1. **RabbitMQ**
   
   - **Language:** Erlang
   - **Python Integration:** Libraries like `pika` or `kombu`
   - **Features:** Supports multiple messaging protocols (AMQP, STOMP, MQTT), durable message delivery, complex routing capabilities, and plugin system for extensibility.

2. **Apache Kafka**
   
   - **Language:** Scala and Java
   - **Python Integration:** Clients such as `confluent-kafka-python` and `kafka-python`
   - **Features:** High throughput, built for distributed systems, offers persistent storage of messages, supports stream processing, and provides strong ordering guarantees.

3. **Redis**
   
   - **Language:** C
   - **Python Integration:** Clients like `redis-py`
   - **Features:** In-memory data structure store, used as a database, cache, and message broker. Supports various data structures, transactions, and has built-in replication.

4. **Apache ActiveMQ**
   
   - **Language:** Java
   - **Python Integration:** Libraries like `stomp.py`
   - **Features:** Supports multiple cross-language clients and protocols (AMQP, MQTT, OpenWire, Stomp), offers features like message groups, virtual destinations, and broker networks.

5. **Zeromq**
   
   - **Language:** C++ and C
   - **Python Integration:** `pyzmq`
   - **Features:** High-performance asynchronous messaging library, provides a message queue but with a sockets interface, supporting various patterns (pub-sub, push-pull, request-reply).

6. **NSQ**
   
   - **Language:** Go
   - **Python Integration:** Library `pynsq`
   - **Features:** Real-time distributed messaging platform, promotes distributed and decentralized topologies, no single point of failure, and built-in fault tolerance.

7. **Others**
    - https://github.com/tembo-io/pgmq "A lightweight message queue. Like AWS SQS and RSMQ but on Postgres."
    - https://adriano.fyi/posts/2023-09-24-choose-postgres-queue-technology/ "Postgres queue tech consists of two parts: announcing and listening for new jobs (pub/sub) and mutual exclusion (row locks)."
    - https://github.com/smrchy/rsmq (JS, dead)
    - https://github.com/poundifdef/SmoothMQ  "SmoothMQ is a drop-in replacement for SQS with a much smoother developer experience. It has a functional UI, observability, tracing, message scheduling, and rate-limiting. SmoothMQ lets you run a private SQS instance on any cloud." (Go + SQlite)
    - https://github.com/hatchet-dev/hatchet = Hatchet replaces difficult to manage legacy queues or pub/sub systems so you can design durable workloads that recover from failure and solve for problems like **concurrency**, **fairness**, and **rate limiting**. Instead of managing your own task queue or pub/sub system, you can use Hatchet to distribute your functions between a set of workers with minimal configuration or infrastructure (Go).
    - https://docs.bullmq.io/ = BullMQ is a [Node.js](https://nodejs.org) library that implements a fast and robust queue system built on top of [Redis](https://redis.io) that helps in resolving many modern age micro-services architectures.

### Python-Centric Task Queues

1. **Celery with RabbitMQ or Redis**
   
   - **Language:** Python
   - **Python Integration:** Natively integrates with Python
   - **Features:** Distributed task queue, supports scheduling, and integrates with a variety of message brokers (RabbitMQ, Redis). Offers result storage, task retries, and failure handling.
   - Notes:
       - https://docs.hatchet.run/blog/problems-with-celery
       - https://denibertovic.com/posts/celery-best-practices/
       - https://news.ycombinator.com/item?id=7909201

2. **Dramatiq**
   
   - **Language:** Python
   - **Python Integration:** Natively integrates with Python
   - **Features:** Simple to use and setup, supports automatic retries, late acknowledgment, and offers a middleware system for extending functionality. Claims higher reliability and performance compared to Celery.

3. **RQ (Redis Queue)**
   
   - **Language:** Python
   - **Python Integration:** Natively integrates with Python
   - **Features:** Simple Python library for queueing jobs and processing them in the background. Integrates with Redis, supports job result storage and failure handling.

4. **Huey**
   
  - **Language:** Python
  - **Python Integration:** Natively integrates with Python
  - **Features:** Supports multi-process, thread, or greenlet-based execution, periodic task execution, and simple API. Offers result storage, task prioritization, and supports Redis, SQLite, and in-memory storage.

5. More
    1. https://github.com/closeio/tasktiger (uses Redis)
    2. WakaQ - cf. https://wakatime.com/blog/56-building-a-background-task-queue-in-python

## Choosing the "best" system

The choice of system should align with the specific needs of the application, such as performance requirements, fault tolerance, message delivery guarantees, and the existing technology stack, as well as the operational constraints specific to your organisation.
#### Evaluate Your Requirements

- **Task Complexity:** Are your tasks simple or complex? Do they involve chains, groups, or workflows?
- **Performance Needs:** What is the expected load? Do you need the system to handle a high throughput?
- **Scalability:** Will the system need to scale horizontally, and how robust does the scaling mechanism need to be?
- **Reliability:** How critical are the tasks? Do you need sophisticated failure handling and retry mechanisms?
- **Broker Support:** Are you tied to a specific message broker, or are you flexible in that regard?

#### Consider Operational Overhead

- **Ease of Setup and Use:** Some systems are easier to set up and use than others. Consider the time and effort required to implement and maintain the system.
- **Monitoring and Management:** Does the system provide tools or integrations for monitoring job statuses, retries, and failures?
- **Community and Documentation:** A strong community and good documentation can significantly ease the process of implementation and troubleshooting.

### Comparison of the most popular Python task queues

#### Celery

  - Best for complex task workflows with features like chains, groups, and chords.
  - Supports multiple message brokers (RabbitMQ, Redis, Amazon SQS, etc.).
  - Offers a mature solution with extensive documentation and a large community.
  - Comes with a monitoring tool, Flower.
  - Can be heavier and more complex to set up and maintain.
  
#### Dramatiq

  - Good for both simple and complex tasks, with a focus on performance and reliability.
  - Supports multiple brokers (RabbitMQ, Redis) and provides a simple API.
  - Claims to offer better performance and reliability than Celery.
  - Middleware support for extending functionality.
  - Smaller community and less extensive documentation compared to Celery.

#### RQ (Redis Queue)

  - Best for simple tasks with lightweight requirements.
  - Tightly integrated with Redis, offering high performance.
  - Very easy to set up and use, with a minimalistic approach.
  - Comes with `rq-dashboard` for monitoring.
  - Limited by the features and scalability of Redis.

#### Huey

  - Suitable for small to medium workloads.
  - Supports multiple storage backends (Redis, SQLite, in-memory).
  - Provides periodic task execution and simple API.
  - Lightweight and straightforward but less feature-rich compared to Celery.
  - Offers crontab-like scheduling.

## More info / references

- https://sudhir.io/the-big-little-guide-to-message-queues
- https://sharmarajdaksh.github.io/blog/the-what-why-and-how-of-message-queues
- https://en.wikipedia.org/wiki/Message_queue
- https://stackshare.io/message-queue

<!-- Keywords -->
#message_queue #microservices #queueing #queues #middleware
<!-- /Keywords -->
