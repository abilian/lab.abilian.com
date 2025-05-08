
The debate between Server-Side Rendering (SSR) and Client-Side Rendering (CSR) centers on **where the rendering of the user interface happens: on the server or in the user's browser.**

## CSR (Client-Side Rendering)

*   **How it works:** The server sends a minimal HTML page with links to JavaScript files. The browser downloads these files and then *dynamically* renders the UI using JavaScript.
*   **The problem:** CSR introduces complexity by creating a *two-state problem.* The server holds the "source of truth" data, and the client holds a *copy* of that data to display. Keeping these two states synchronized is challenging. This often requires complex client-side logic and more sophisticated communication protocols. Another pain point is SEO, as search engine crawlers can sometimes struggle to properly index content rendered with CSR.
*   **Pros:** Rich user experiences (faster interactions *after* the initial load), separation of concerns (backend focuses on APIs, frontend on UI).
*   **Cons:**  Higher initial load time (as the browser needs to download and execute JavaScript), potential SEO issues, more client-side code, the complexity of managing state synchronization.

## SSR (Server-Side Rendering)

*   **How it works:** The server renders the *entire* HTML page, including the data, and sends it to the browser. The browser simply displays the received HTML.
*   **How it works, improved:** HTMX improves on this by only swapping the parts of the DOM that changed, using the server's response
*   **The problem:** The traditional SSR approach causes a complete page reload on every interaction, resulting in a noticeable "white flash" or flicker and interrupting the user experience.
*   **Pros:** Faster initial load time (content is immediately visible), better SEO (search engines can easily crawl the rendered HTML), simpler client-side code (less JavaScript required), a *single source of truth* on the server.
*   **Cons:**  Slower subsequent interactions (every interaction requires a server request and full page reload - unless improved by HTMX), increased server load.

## HTMX as a potential solution

[[HTMX]] can address the UX problem of SSR, which is page reloading. HTMX allows selectively updating parts of the page by sending HTML snippets from the server, leading to a smoother user experience without the complexity of CSR. The article also talks about the "HARM stack," a stack that uses HTMX to solve problems caused by complexity in modern web stacks.

## In summary

*   CSR offers rich interactions but introduces client-side complexity.
*   SSR is simpler but historically provided poorer user experiences due to full page reloads.
*   HTMX can offer the simplicity of SSR with a more interactive user experience by selectively updating parts of the page.

## References

- https://nguyenhuythanh.com/posts/the-harm-stack-considered-unharmful/
