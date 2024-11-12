
[Dramatiq](https://dramatiq.io/)" is an open-source Python library that provides a simple and reliable framework for distributed task processing and background job execution. It was created by [Bogdan Popa](https://github.com/Bogdanp/) and is designed to be easy to use and efficient. It uses RabbitMQ or Redis (PostgreSQL, and maybe others, can also be used with appropriate extensions) as message brokers and is designed to be simple to use, while also providing robustness and flexibility.

## Key features

1. **Simple and expressive API**: Dramatiq's API is designed to be straightforward and easy to use, making it approachable for developers of all skill levels.

2. **Thread-based workers**: The library uses threads for its workers, which can be more efficient than process-based workers because they share memory and have lower startup costs.

3. **Automatic message acknowledgment**: Messages are automatically acknowledged only after they have been fully processed, which helps to ensure message durability.

4. **Rate limiting**: Dramatiq provides a rate limiting feature that makes it possible to limit the rate at which tasks are executed.

5. **Middleware system**: The library includes a middleware system that can be used to customize its behavior, such as by adding logging or metrics collection.

7.  **Retry and Error Handling**: Dramatiq provides built-in support for retrying failed tasks. You can configure the number of retries, backoff strategies, and error handling behaviors to handle task failures gracefully.
    
5.  **Task Prioritization**: Tasks in Dramatiq can be assigned different priorities, allowing you to control the order in which they are processed. Higher-priority tasks are processed before lower-priority ones.
    
6.  **Result Tracking**: Dramatiq allows you to track the status and results of your tasks. You can access task results synchronously or asynchronously, enabling you to handle task outcomes and perform subsequent actions based on the results.

8.  **Monitoring and Metrics**: Dramatiq integrates with [[Prometheus]], a popular open-source monitoring system, to help you track the performance and health of your task processing system.
    
10.  **Integration Ecosystem**: Dramatiq offers integrations with various Python frameworks and libraries, such as Flask, Django, and SQLAlchemy, allowing you to seamlessly incorporate task processing into your existing applications.

11. **Dashboard**: `dramatiq_dashboard` is dashboard for dramatiq, specific to its Redis broker. Very alpha stuff. It comes in the form of a WSGI middleware, with as few dependencies as possible (`dramatiq`, `jinja2` and `redis`) so it's super easy to plug into whatever web application you have.


## How it works

1.  **Task-based Architecture**: Dramatiq allows you to define tasks as Python functions or classes. These tasks represent units of work that can be executed asynchronously in the background.
    
2.  **Distributed Task Processing**: Dramatiq supports distributed task processing by leveraging a message broker, such as RabbitMQ or Redis. It uses the broker to send and receive messages, enabling the distribution of tasks across multiple workers or machines.
    
3.  **Message Passing**: Tasks in Dramatiq communicate through messages. When a task is enqueued, a message is created and sent to the message broker. Workers receive and process these messages, executing the associated tasks.

## Example

Here is an example (from the doc) of how you might use Dramatiq to define and enqueue a task:

```python
import dramatiq

@dramatiq.actor
def count_words(url):
    response = requests.get(url)
    count = len(response.text.split(" "))
    print(f"There are {count} words at {url}.")

# Later, you can enqueue tasks:
count_words.send("http://example.com")
```

Dramatiq is well-documented, and you can find installation instructions, usage examples, and detailed information on its features and configuration options on the official documentation website at [https://dramatiq.io/](https://dramatiq.io/).

<!-- Keywords -->
#rabbitmq #dramatiq #middleware
<!-- /Keywords -->
