
This note explores several Python frameworks for building web applications, focusing on those that minimize or eliminate the need for direct JavaScript coding, thus simplifying the creation of dynamic and interactive web applications. They offer different approaches to achieve this, catering to various use cases and preferences, but the underlying goal is to make Python a first-class citizen in the web development landscape.

Links: https://github.com/sfermigier/awesome-python-web-frameworks?tab=readme-ov-file#front-end-frameworks

## Reflex

Under the hood, Reflex apps compile down to a [React](https://react.dev) frontend app and a [FastAPI](https://github.com/tiangolo/fastapi) backend app. Only the UI is compiled to Javascript; all the app logic and state management stays in Python and is run on the server. Reflex uses [WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API) to send events from the frontend to the backend, and to send state updates from the backend to the frontend.

When you `reflex run` your app, Reflex compiles the frontend down to a single-page [Next.js](https://nextjs.org) app and serves it on a port (by default `3000`) that you can access in your browser.

The frontend's job is to reflect the app's state, and send events to the backend when the user interacts with the UI. No actual logic is run on the frontend.

Many of our core components are based on [Radix](https://radix-ui.com/), a popular React component library. We also have many other components for graphing, datatables, and more.

## Tetra

Full stack component framework for [Django](http://djangoproject.com) using [Alpine.js](https://alpinejs.dev)

Tetra is a new full stack component framework for Django, bridging the gap between your server logic and front end presentation. It uses a public shared state and a resumable server state to enable inplace updates. It also encapsulates your Python, HTML, JavaScript and CSS into one file for close proximity of related concerns.

Seems similar to Livewire. Cf. https://calebporzio.com/how-livewire-works-a-deep-dive

→ https://www.tetraframework.com/

## Reactpy

[ReactPy](https://reactpy.dev/) is a library for building user interfaces in Python without Javascript. ReactPy interfaces are made from components that look and behave similar to those found in [ReactJS](https://reactjs.org/). Designed with simplicity in mind, ReactPy can be used by those without web development experience while also being powerful enough to grow with your ambitions.

## Dash & Streamlit

"On the other hand, pure Python libraries like [Dash](https://dash.plotly.com/) and [Streamlit](https://streamlit.io/) can be great for small projects, but they are limited to a specific use case and don't have the features and performance to build a full web app. As your app grows in features and complexity, you may find yourself hitting the limits of the framework, at which point you either have to limit your idea to fit the framework, or scrap your project and rebuild it using a "real web framework"." (Comments from the creator of Reflex).

## Flet

Flet is a framework for adding server-driven UI (SDUI) experiences to existing Flutter apps or building standalone web, mobile and desktop apps with Flutter UI. With Flet you just write a monolith stateful app in Python only and get multi-user, real-time Single-Page Application (SPA).

→ https://github.com/flet-dev/flet
→ https://flet.dev/


## Nicegui

NiceGUI is implemented with HTML components served by an HTTP server (FastAPI), even for native windows. If you already know HTML, everything will feel very familiar. If you don't know HTML, that's fine too! NiceGUI abstracts away the details, so you can focus on creating beautiful interfaces without worrying about how they are implemented.

## FastHTML

FastHTML is a system for writing web applications in Python. It is designed to be simple, powerful, and flexible. It is also designed to be easy to learn and use. The project is inspired by technologies such as React JSX, Hotwire, Astro, FastAPI, and Phoenix LiveView. FastHTML is small and simple—at the time of writing, it’s under 1000 lines of code. That’s because it’s built on top of powerful and flexible foundations: Python, Starlette, Uvicorn, and HTMX. If you’re a FastAPI user, much of FastHTML will look very familar; FastAPI was a major inspiration.

## Discussion

Despite their diverse implementations, several key common conceptual ideas emerge:

1.  **Python-Centric Development:** The desire to shift the development focus *away* from JavaScript and towards Python.  They aim to allow developers to build interactive web applications primarily, or even exclusively, using Python. This reduces the cognitive load of context-switching between languages and leverages developers' existing Python expertise.

2.  **State Management (Server-Side or Shared):**  A core challenge in web development is managing application state (the data that drives the UI). These frameworks tackle this in different ways, but the common theme is to either:

    *   **Keep state primarily on the server:**  Frameworks like Reflex and Tetra emphasize server-side state.  The Python code running on the server holds the "source of truth" for the application's data. Changes in state, triggered by user interactions, are typically communicated via WebSockets or AJAX requests (htmx in the case of FastHTML).
    *   **Shared State:** Some frameworks, like Tetra, explicitly mention a "public shared state," suggesting a mechanism where a subset of the state is synchronized between the server and the client, enabling more responsive updates.
    *   **Component-based UI, server-rendered**: Reactpy emulates React, using components that render server-side.

3.  **Abstraction of Web Technologies:** Many of these frameworks aim to abstract away the complexities of underlying web technologies like HTML, CSS, and JavaScript to varying degrees.  NiceGUI, for example, explicitly mentions abstracting HTML details.  Even frameworks that compile to React (like Reflex) provide a Pythonic way to define UI components, shielding the developer from directly writing React code.

4.  **Component-Based UI:**  Inspired by modern JavaScript frameworks like React, many of these frameworks adopt a component-based approach to building user interfaces.  This promotes modularity, reusability, and maintainability.  Reflex, ReactPy, and Tetra all explicitly mention components.

5.  **[[Server-Driven UI]] (SDUI) or "Live" Updates:** A significant number of these frameworks emphasize dynamic, real-time updates to the UI without full page reloads.  This is often achieved through technologies like WebSockets (Reflex), AJAX/htmx (FastHTML), or a similar mechanism for server-initiated updates (Tetra, Flet). This creates a more responsive and interactive user experience.

6.  **Leveraging Existing Ecosystems:** Rather than reinventing the wheel, many of these frameworks build upon established and robust libraries and tools.  Examples include:

    *   **FastAPI:** Used by Reflex, NiceGUI, and a strong influence on FastHTML.
    *   **React:**  Used under the hood by Reflex, and the inspiration for ReactPy.
    *   **Alpine.js:** Used by Tetra.
    *   **Flutter:** Used by Flet.
    * **HTMX**: Used by FastHTML

7. **Simplicity and Ease of Use:** A stated goal for many of these frameworks is to make web development more accessible and easier to learn, particularly for developers who may not have extensive front-end experience. They aim to provide a more streamlined and Pythonic development workflow.
