
**[Starlette](https://www.starlette.io/)** is a high-performance, lightweight web framework designed specifically for building asynchronous web applications and APIs. It is built on the emerging ASGI (Asynchronous Server Gateway Interface) standard, which makes it suitable for modern, highly concurrent applications. With a focus on simplicity, modularity, and speed, Starlette has become a popular choice for developers looking for a minimal yet powerful framework.

## Key Characteristics of Starlette

#### ASGI-Centric Design

Starlette is built natively on ASGI, the successor to the traditional WSGI standard. This makes it ideal for handling asynchronous programming paradigms, allowing applications to:

- Manage WebSocket connections.
- Handle long-lived connections (e.g., Server-Sent Events).
- Integrate easily with other asynchronous tools and frameworks.

#### Lightweight and Modular

Starlette’s design philosophy emphasizes minimalism and modularity. It provides just enough features to get started with modern web applications, leaving additional complexity to optional components or external libraries. This modularity ensures Starlette remains lightweight and flexible.

#### High Performance

Starlette’s asynchronous architecture is inherently non-blocking, making it capable of handling thousands of concurrent requests efficiently. Benchmarks often rank Starlette among the fastest Python web frameworks.

#### Comprehensive Feature Set

Despite its minimalism, Starlette includes a robust set of features that cater to most modern web application requirements:

- **Routing**: Intuitive, declarative route definitions for views, static files, and more.
- **Middleware**: Support for adding custom or pre-built middleware to handle cross-cutting concerns like authentication, CORS, or request logging.
- **WebSocket Support**: Full native support for WebSockets for real-time communication.
- **Dependency Injection**: First-class support for dependencies in routes or other components.
- **Templating**: Integration with Jinja2 for server-side rendering of HTML templates.
- **Background Tasks**: Easy execution of background tasks alongside HTTP request handling.
- **Static Files**: Built-in capability to serve static assets like CSS, JavaScript, and images.
- **Test Client**: A built-in testing client for writing fast and efficient integration tests.

#### Interoperability

Starlette is compatible with a wide range of ASGI servers and tools, such as:

- **ASGI Servers**: Works seamlessly with servers like Uvicorn, Daphne, and Hypercorn.
- **Framework Ecosystem**: Can serve as the foundation for higher-level frameworks like FastAPI, which builds on Starlette for routing, middleware, and more.
- **Async Libraries**: Integrates well with Python’s asynchronous libraries such as HTTPX, SQLAlchemy (async mode), and Tortoise ORM.

### Why Choose Starlette?

#### Ideal for APIs
Starlette is purpose-built for APIs. Its asynchronous nature and lightweight design make it an excellent choice for microservices, RESTful APIs, and GraphQL endpoints.

#### Flexible Application Types

Beyond APIs, Starlette can handle diverse application types, including:

- Real-time applications (WebSockets, live updates).
- Server-side rendered web applications using Jinja2 or similar templating engines.
- Event-driven systems that leverage ASGI’s concurrency model.

#### Modern Development Practices

Starlette encourages best practices for modern web development, including:

- Asynchronous programming with `async`/`await`.
- Separation of concerns through modular architecture.
- Strong testability with an included `TestClient`.

#### Rapid Prototyping

Thanks to its simplicity and robust feature set, Starlette is ideal for rapid prototyping. Developers can quickly scaffold applications while maintaining the flexibility to scale or adapt to production requirements.

### Core Use Cases

#### High-Concurrency Applications
Applications that require handling many simultaneous connections—such as chat applications, collaborative tools, or streaming platforms—benefit greatly from Starlette’s asynchronous capabilities.

#### APIs for Microservices
Starlette’s minimal footprint and high performance make it a natural fit for microservices architectures, where lightweight, efficient API endpoints are critical.

#### Proxies and Gateways
Starlette’s support for middleware and background tasks allows it to act as a powerful proxy or gateway, routing requests or performing pre-processing on behalf of other services.

#### Real-Time Data Streams
Starlette supports WebSockets and Server-Sent Events (SSE) out of the box, enabling real-time data delivery for applications like dashboards or IoT systems.

### How Starlette Compares

#### Against Traditional Frameworks (e.g., Django, Flask)
- **Asynchronous Nature**: Unlike Flask and Django (WSGI-based frameworks), Starlette is natively asynchronous, offering better concurrency for I/O-bound tasks.
- **Modularity**: Starlette focuses on being minimal and extensible, whereas traditional frameworks often come with batteries included.
- **Performance**: Starlette is faster due to its asynchronous design and smaller footprint.

#### Against FastAPI
- Starlette is a foundation for FastAPI, meaning it is lower-level and does not include FastAPI’s data validation or OpenAPI support. Developers seeking a more structured framework with these features may prefer FastAPI, while those looking for minimalism will appreciate Starlette.


### Conclusion

Starlette is a modern, efficient choice for Python developers building asynchronous web applications and APIs. Its lightweight, modular design provides a strong foundation for scalable applications while remaining simple enough for rapid prototyping and experimentation. Whether you're building a real-time application, a microservice, or a server-side rendered web app, Starlette offers the performance and flexibility to meet your needs.

## References / links

### Frameworks based on Starlette

- https://github.com/adriangb/xpresso = Xpresso is an ASGI web framework built on top of [Starlette](https://github.com/encode/starlette), [Pydantic](https://github.com/samuelcolvin/pydantic/) and [di](https://github.com/adriangb/di), with heavy inspiration from [FastAPI](https://github.com/adriangb/xpresso). (NB: Dead project)
- https://github.com/posit-dev/py-shiny = Shiny for Python is the best way to build fast, beautiful web applications in Python. Built on Starlette.

### Extensions

- https://github.com/florimondmanca/asgi-htmx/ - HTMX integration for ASGI applications (not specific to Starlette nbut useful)
- https://github.com/MrPigss/DecoRouter = Flask-like router (via decorators)

### Templates / starter apps

- https://github.com/encode/starlette-example (old)


## Structuring Starlette Projects

(Adapted from: https://florimond.dev/en/posts/2020/06/structuring-starlette-projects, which was down at the time).

Starlette’s lightweight, modular design is ideal for building fast, asynchronous web applications. However, its flexibility often leaves developers uncertain about the best way to structure projects. This guide outlines a practical, scalable approach to organizing Starlette applications while addressing common challenges like circular dependencies and ensuring maintainability.

### The Importance of Project Structure

A well-structured project promotes:

- **Separation of Concerns**: Each module handles a distinct responsibility.
- **Maintainability**: Clear boundaries between components simplify updates and debugging.
- **Scalability**: New features can be added without disrupting existing functionality.
- **Avoidance of Circular Dependencies**: Logical separation prevents cross-import conflicts.

### Recommended Directory Layout

A typical Starlette project structure might look like this:

```
project_name/
├── app/
│   ├── __init__.py
│   ├── main.py              # Application entry point
│   ├── settings.py          # Configuration
│   ├── routes.py            # Route definitions
│   ├── views.py             # Views/Handlers
│   ├── resources.py         # Shared resources (e.g., database clients)
│   ├── middleware.py        # Custom middleware
│   ├── event_handlers.py    # Startup/Shutdown handlers
│   ├── templates/           # HTML templates
│   └── static/              # Static files (CSS, JS, etc.)
├── tests/                   # Test suite
│   ├── __init__.py
│   └── test_main.py
├── .env                     # Environment variables
├── requirements.txt         # Dependencies
└── README.md
```


### Step-by-Step Structuring

#### a. Configuration (`settings.py`)

Centralize environment-specific settings and file paths in `settings.py`. Use Starlette's `Config` for loading `.env` variables.

```python
from pathlib import Path
from starlette.config import Config

config = Config(".env")

BASE_DIR = Path(__file__).parent
TEMPLATES_DIR = BASE_DIR / "templates"
STATIC_DIR = BASE_DIR / "static"

DEBUG = config("DEBUG", cast=bool, default=False)
DATABASE_URL = config("DATABASE_URL", default="sqlite:///db.sqlite3")
```

#### b. Shared Resources (`resources.py`)

Define reusable resources like HTTP clients, database connections, or template engines in `resources.py`. This avoids circular dependencies and keeps your code clean.

```python
import httpx
from databases import Database
from starlette.templating import JinjaTemplates
from . import settings

# Shared resources
client = httpx.AsyncClient()
database = Database(settings.DATABASE_URL)
templates = JinjaTemplates(directory=str(settings.TEMPLATES_DIR))
```

#### c. Views (`views.py`)

Views handle requests and return responses. Import shared resources where needed.

```python
from starlette.responses import JSONResponse
from .resources import database, templates

async def home(request):
    query = "SELECT * FROM articles"
    articles = await database.fetch_all(query)
    context = {"request": request, "articles": articles}
    return templates.TemplateResponse("index.html", context)

async def api_example(request):
    response = await client.get("https://api.example.com/data")
    return JSONResponse(response.json())
```

#### d. Routes (`routes.py`)

Keep route definitions in a single module to maintain clarity and avoid cluttering other components.

```python
from starlette.routing import Route, Mount
from . import views, resources

routes = [
    Route("/", views.home, name="home"),
    Mount("/static", resources.static, name="static"),
]
```

#### e. Middleware (`middleware.py`)

Define custom middleware in a dedicated module. Middleware should address cross-cutting concerns like logging or authentication.

```python
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        print(f"Request to {request.url}")
        response = await call_next(request)
        return response
```


#### f. Application Entry Point (`main.py`)

The `main.py` module initializes the Starlette application, wiring up routes, middleware, and event handlers.

```python
from starlette.applications import Starlette
from starlette.middleware import Middleware
from .routes import routes
from .middleware import LoggingMiddleware
from .event_handlers import on_startup, on_shutdown
from .settings import DEBUG

middleware = [
    Middleware(LoggingMiddleware),
]

app = Starlette(
    debug=DEBUG,
    routes=routes,
    middleware=middleware,
    on_startup=on_startup,
    on_shutdown=on_shutdown,
)
```

#### g. Event Handlers (`event_handlers.py`)

Use Starlette’s `on_startup` and `on_shutdown` hooks to manage application lifecycle events like opening and closing database connections.

```python
from .resources import database, client

on_startup = [
    database.connect,
]

on_shutdown = [
    database.disconnect,
    client.aclose,
]
```

### Advanced Tips

#### Avoiding Circular Imports

Circular dependencies often occur when modules import each other directly. This can be avoided by:
- Using a dedicated `resources.py` module for shared objects.
- Passing dependencies as function arguments rather than importing them globally.
- Structuring modules to focus on a single logical responsibility.

#### Using an Application Factory

While the singleton `app` approach is straightforward, an application factory allows for multiple instances with distinct configurations. This is especially useful in testing or multi-app contexts.

```python
def create_app():
    app = Starlette(
        debug=settings.DEBUG,
        routes=routes,
        middleware=middleware,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
    )
    return app
```


#### Testing

Place all test cases in the `tests/` directory. Use `pytest` for writing and executing tests. Mock shared resources for isolated testing.

```python
from starlette.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
```

#### Singleton Warning

While using singleton resources like `client` and `database` is common, it can limit reusability and scalability:
- **Drawback**: Singleton resources are hard to decouple for modular or reusable applications.
- **Alternative**: Use dependency injection or application factories for more flexible designs.

> **Note**: The structure suggested here is sufficient for most small to medium-sized Starlette projects. For larger applications or shared libraries, consider advanced patterns like dependency injection.


### Final Structure

At this stage, your Starlette project should look like this:

```
project_name/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── settings.py
│   ├── routes.py
│   ├── views.py
│   ├── resources.py
│   ├── middleware.py
│   ├── event_handlers.py
│   ├── templates/
│   └── static/
├── tests/
│   └── test_main.py
├── .env
└── README.md
```

### Conclusion

This modular structure ensures that your Starlette application is maintainable, scalable, and free from circular dependencies.
