In web development, striving for separation of concerns is key. The list below lists key areas of concern for a "full-stack" web developer or for a multi-functional (e.g. front-end vs. back-end) development team, with an holistic view.

By explicitly identifying the areas below, you can design more modular, maintainable, and testable applications. The specific boundaries and names might vary depending on the architectural patterns you adopt (e.g., Clean Architecture, Hexagonal Architecture, traditional N-Tier).

## The key areas

1.  **Business Logic (The "How" and "Why" of the application's purpose):**
    *   **Domain Logic:**
        *   **Entities:** Core objects with identity and lifecycle (e.g., `User`, `Order`, `Product`).
        *   **Value Objects:** Immutable objects describing characteristics (e.g., `Address`, `Money`).
        *   **Domain Services:** Operations that don't naturally belong to a single entity but involve multiple domain objects (e.g., `OrderFulfillmentService`).
        *   **Domain Events:** Significant occurrences within the domain (e.g., `OrderPlaced`, `PaymentProcessed`).
        *   **Repositories (Interface):** Abstractions for data persistence, defined in the domain.
    *   **Application Logic (Use Cases / Application Services):**
        *   Orchestrates domain logic to fulfill specific application use cases (e.g., "Place Order," "Register User").
        *   Coordinates calls to domain objects and infrastructure services.
        *   Handles transaction management.
        *   Often interacts with DTOs (Data Transfer Objects) for input/output.

2.  **Web Logic (Handling HTTP requests and responses):**
    *   **Routing:** Mapping URLs/HTTP methods to specific handlers/controllers.
    *   **Controllers/Handlers:** Receiving requests, validating basic input (format, not business rules), invoking application services, and preparing data for the presentation layer.
    *   **Request/Response Parsing & Formatting:** Handling JSON, XML, form data, setting headers.
    *   **Middleware/Filters:** Intercepting requests/responses for cross-cutting concerns at the web layer (e.g., authentication checks, logging, CORS).
    *   **API Versioning:** If you expose APIs.

3.  **Presentation Logic (How data is displayed to the user and user interactions are captured):**
    *   **UI Rendering (Server-Side):**
        *   Templating engines (e.g., Jinja2, Thymeleaf, EJS, Blade) to generate HTML.
        *   ViewModel/Presenter preparation: Adapting data from application/domain layers into a format suitable for views.
    *   **UI Rendering (Client-Side):**
        *   JavaScript frameworks/libraries (React, Angular, Vue, Svelte) building components.
        *   Client-side templating.
        *   Managing UI state.
    *   **User Interaction Handling (Client-Side):** Event handling, local validation, dynamic updates.
    *   **Asset Management:** Bundling, minifying, and serving CSS, JavaScript, images, fonts.

4.  **Infrastructure Logic (External concerns & technical details):**
    *   **Data Access/Persistence Logic (Implementations of Repositories):**
        *   ORM (Object-Relational Mapper) configurations and usage (e.g., SQLAlchemy, Hibernate, Entity Framework).
        *   Database interaction (SQL, NoSQL queries).
        *   Connection management.
    *   **External Service Integration:**
        *   Clients for third-party APIs (payment gateways, email services, social media APIs).
        *   Adapters for message queues (RabbitMQ, Kafka).
        *   File system access, cloud storage interaction.
    *   **Caching Implementation:** Interacting with caching services (Redis, Memcached).
    *   **Search Engine Integration:** (Elasticsearch, Solr).

5.  **Data Validation Logic:**
    *   Can exist at multiple levels:
        *   **Presentation/Web Layer:** Basic format validation (e.g., "is this an email?").
        *   **Application Layer:** Validating DTOs, ensuring required fields are present for a use case.
        *   **Domain Layer:** Enforcing business rules and invariants (e.g., "an order total cannot be negative").

6.  **Security Logic:**
    *   **Authentication:** Verifying user identity (login, sessions, tokens - JWT).
    *   **Authorization:** Determining what an authenticated user is allowed to do (roles, permissions).
    *   **Input Sanitization/Validation (Security context):** Preventing XSS, SQL injection.
    *   **Output Encoding:** Ensuring data displayed is safe.
    *   **CSRF Protection.**
    *   **Secrets Management.**
    *   **Rate Limiting/Throttling.**

7.  **Cross-Cutting Concerns (often implemented via AOP, middleware, or decorators):**
    *   **Logging:** Recording application events, errors, and diagnostic information.
    *   **Monitoring & Alerting:** Tracking application health, performance, and sending notifications.
    *   **Error Handling & Exception Management:** Consistent strategies for catching, logging, and responding to errors.
    *   **Configuration Management:** Loading and accessing application settings for different environments.
    *   **Internationalization (i18n) & Localization (l10n):** Adapting the application for different languages and regions.
    *   **Transaction Management:** Ensuring data consistency, often straddling application and infrastructure layers.

8.  **Communication Logic (especially in distributed systems/microservices):**
    *   **Inter-service communication protocols:** REST, gRPC, message queues.
    *   **Service Discovery.**
    *   **Circuit Breakers/Resilience Patterns.**
    *   **API Gateway Logic:** Routing, aggregation, authentication for microservices.

9.  **Testing Logic:**
    *   Unit tests (for individual components/functions).
    *   Integration tests (for interactions between components/layers).
    *   End-to-end tests (simulating user flows).
    *   Test data setup and teardown.

10. **Build & Deployment Logic:**
    *   CI/CD pipeline configuration.
    *   Containerization (Dockerfiles).
    *   Infrastructure as Code (Terraform, CloudFormation).
    *   Database migration scripts.

## Generic vs. specific

Excellent question. Drawing this line is crucial for understanding a framework's value and for knowing where to focus your development efforts.

This distinction is fundamentally about **The "What" vs. The "How"**:
*   **Specific Logic (The "What"):** *What* your application uniquely does. This is the code you write to solve your specific business problem.
*   **Generic Logic (The "How"):** *How* common web application tasks are accomplished. This is the plumbing and infrastructure provided by frameworks, libraries, and servers.

Here’s a breakdown by the areas we've discussed:

---

### 1. Business & Application Logic

This area is **almost entirely application-specific**. It's the heart of your application's value.

| Specific (You Write This)                                                                                                    | Generic (Framework/Library Provides)                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Domain Logic:** The rules, entities, and value objects that model your problem (e.g., `Order`, `Product`, `User` classes). | **Patterns & Tools:** Libraries for implementing patterns like Domain Events or State Machines, but not the events/states themselves. |
| **Application Logic (Use Cases):** The step-by-step orchestration of domain objects to achieve a goal (e.g., `PlaceOrderService`). | **Dependency Injection Container:** A mechanism to wire your services together, but you define the services and their dependencies.   |
| **Business Rules:** The specific conditions and invariants of your domain (e.g., "An order cannot be shipped if unpaid").      | **(Rarely anything)** This logic is, by definition, unique to you.                                                                   |

**Key Takeaway:** Frameworks stay out of your business logic. Your goal should be to write this logic so it has zero dependencies on any specific web or database framework.

---

### 2. Web Logic

This is a classic example of a partnership between your code and a framework.

| Specific (You Write This)                                                                                                 | Generic (Framework/Library Provides)                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| **Route Definitions:** The specific URL paths and the HTTP methods they respond to (e.g., `GET /api/users/{id}`).            | **Router:** The core engine that parses incoming request URLs and dispatches them to the correct handler code.                       |
| **Controller/Handler Logic:** The code that calls your application services and prepares the response.                      | **Request/Response Objects:** The entire object model for handling HTTP requests and building responses (headers, body, status codes). |
| **Request DTOs/Validation Rules:** Defining the expected shape and basic format of incoming data.                          | **Validation Engine:** The mechanism that runs your defined validation rules against the request data.                                |
| **Middleware Logic:** The code inside a specific middleware (e.g., a custom logging or permission-checking middleware).     | **Middleware Pipeline:** The system that allows for the chaining and execution of middleware components.                              |
| **API Versioning Strategy:** Your specific choice of how to version your API (e.g., `/api/v2/...`).                         | **Server:** The underlying HTTP server that listens on a port and handles the raw network connections.                               |

**Key Takeaway:** The framework (e.g., Django, Express, Spring MVC, ASP.NET Core) provides the entire scaffolding and event loop for handling HTTP. You simply "fill in the blanks" with your specific routes and handlers.

---

### 3. Presentation Logic

This is another area with a strong partnership, especially with modern front-end frameworks.

| Specific (You Write This)                                                                                                 | Generic (Framework/Library Provides)                                                                                                      |
| ------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **HTML Structure & Content:** The actual HTML tags, text, and layout within your components or templates.                   | **Templating Engine:** The syntax and rendering engine for templates (e.g., Jinja2's `{{...}}`, JSX's `{...}`).                            |
| **Component Hierarchy & State:** How you structure your UI into components and manage the data they display.                | **Component Model & Lifecycle:** The entire concept of a component, its lifecycle methods (e.g., `useEffect`), and rendering logic.         |
| **CSS Rules:** Your custom styles, class names, and design system.                                                         | **Virtual DOM / Reactivity System:** The core engine in frameworks like React or Vue that efficiently updates the browser's DOM.          |
| **Client-Side Event Handlers:** The JavaScript code that runs when a user clicks a button or fills a form.                  | **Asset Bundler/Compiler:** Tools (like Webpack, Vite) that transpile, bundle, and optimize your CSS and JS for the browser.            |
| **ViewModel Data:** The specific data structure you pass to the view.                                                     | **CSS Frameworks:** Pre-built classes and components (e.g., Bootstrap's `.btn`, Tailwind's utility classes).                              |

---

### 4. Infrastructure & Data Access Logic

Here, you define the "what to save" and the library/framework handles the "how to save it."

| Specific (You Write This)                                                                                                | Generic (Framework/Library Provides)                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Database Schema / ORM Models:** The definition of your tables and columns as code (e.g., a `User` class mapping to a `users` table). | **ORM (Object-Relational Mapper):** The library itself (e.g., SQLAlchemy, Hibernate, Entity Framework) that translates objects to SQL. |
| **Repository Implementations:** The specific queries to fetch or save your data (e.g., `userRepository.findByEmail(email)`). | **Database Driver:** The low-level library that handles the actual network communication with the database (e.g., `psycopg2`).       |
| **Database Migrations:** Scripts that modify the database schema over time.                                              | **Migration Tool:** The framework command-line tool that applies your migration scripts.                                             |
| **Configuration:** Your database connection string, API keys for external services, etc.                                 | **Configuration Loader:** A library that reads `.env` files, JSON, or YAML and makes the values available to the app.                |
| **API Client Logic:** The code that calls a specific third-party API endpoint and parses its response.                     | **HTTP Client Library:** A library (like `axios` or `requests`) for making HTTP requests.                                            |

---

### 5. Security Logic

Security is a shared responsibility. The framework provides the tools; you provide the rules.

| Specific (You Write This)                                                                                            | Generic (Framework/Library Provides)                                                                                                    |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **Authorization Rules:** Who is allowed to do what (e.g., "Only 'ADMIN' role can access `/admin`").                    | **Authentication Middleware:** The mechanism that checks for a valid session cookie or JWT on incoming requests.                        |
| **User Roles & Permissions:** The definition of what roles like `ADMIN`, `EDITOR`, or `MEMBER` mean in your app.      | **Password Hashing Library:** The implementation of secure hashing algorithms (e.g., bcrypt, Argon2).                                   |
| **JWT Payload:** The specific data (claims) you choose to put inside your JSON Web Tokens.                             | **JWT Library:** The tool for signing and verifying tokens.                                                                              |
| **CORS Configuration:** Which origins are allowed to access your API.                                                | **CSRF Protection:** The mechanism for generating and validating anti-forgery tokens.                                                   |
| **Secrets:** Your actual API keys, signing keys, and database passwords.                                               | **Secrets Management Integration:** Libraries for connecting to services like AWS Secrets Manager or HashiCorp Vault.                   |

By understanding this separation, you can evaluate frameworks more effectively and spend your time building the unique, valuable parts of your application, while letting the generic, battle-tested framework code handle the common, complex, and error-prone tasks.

