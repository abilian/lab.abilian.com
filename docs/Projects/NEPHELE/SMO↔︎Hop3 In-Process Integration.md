
In the current architecture, the Synergetic Meta-Orchestrator (SMO) is a distinct **microservice** – a separately deployable unit with its own API, database, and runtime environment. This aligns with common patterns where distinct functional domains are encapsulated. However, the H3NI project, aiming for deep integration between Hop3 and SMO's optimization capabilities, raises an architectural question: **Should SMO remain a separate microservice, or should its core functionalities be integrated directly into the Hop3 platform, transforming Hop3 into a more feature-rich, potentially "modular monolith"?**

This note explores [[Pros and Cons of Microservices|the trade-offs]] involved in shifting from a microservice interaction model (Hop3 calling SMO's API) to an integrated model (SMO's logic becoming part of the Hop3 codebase). We must weigh the operational simplicity and potential performance gains of integration against the increased complexity and coupling within Hop3.

It's also worth noting that if SMO were initially designed purely as a **Python library** (without the Flask web API layer), integrating its logic into Hop3 might be simpler, and a separate thin web API wrapper could still be created if needed for other consumers. However, given SMO's current structure as a web application, merging involves integrating not just the core logic but also its dependencies and interaction patterns with external systems (Karmada, Prometheus, etc.).

## The Scenario: Integrating SMO Functionality Directly into Hop3

This architectural shift implies that instead of deploying two separate services (SMO Flask app + DB, and the Hop3 platform), the core logic currently residing in SMO's services/ and utils/ directories would be refactored and incorporated directly into the Hop3 codebase and its runtime environment. This includes:

- HDAG descriptor parsing and interpretation.
- Placement and scaling optimization algorithms (including the CVXPY dependency and models).
- Interaction logic with Karmada (likely via the Kubernetes client library).
- Interaction logic with Prometheus (querying metrics, managing rules).
- Interaction logic with Grafana (dashboard generation/publishing).
- Logic for handling OCI artifacts (hdarctl dependency or reimplementation).
- (Optional) NFVCL integration logic.
- (Potentially) Management of the database state currently handled by SMO's models.

## Potential Benefits of Merging SMO into Hop3

1.  **Reduced Operational Overhead:** This is a *major* advantage. Managing one deployable unit (Hop3) instead of two (Hop3 + SMO) simplifies infrastructure, monitoring, configuration management, CI/CD pipelines, and dependency tracking significantly. Fewer things can go wrong in the operational environment.
2.  **Simplified Data Consistency:** Ensuring that the state known by Hop3 (e.g., application status, cluster inventory) is consistent with the state used by the optimization logic (SMO's functions) becomes much easier if they share the same process space and potentially the same database transaction boundaries. No need for complex synchronization mechanisms or handling eventual consistency issues between separate databases.
3.  **Performance:** Eliminating REST API call latency between Hop3 needing an optimization decision and the logic providing it can be a real performance win, especially if these interactions are frequent or part of a time-sensitive workflow (like rapid scaling responses). Direct function calls are almost always faster.
4.  **Simplified Development & Debugging (Potentially):** If Hop3 and SMO logic are deeply intertwined (e.g., an optimization needs fine-grained access to Hop3's internal application model), developing and debugging this interaction *within a single codebase* can be simpler than dealing with API contracts, network issues, and distributed tracing across service boundaries.

##  Drawbacks

1.  **Increased Hop3 Complexity:** Hop3 will get bigger. Is this inherently bad? If SMO's functionality *is* considered a core part of the advanced PaaS features Hop3 *wants* to offer, then integrating it might be the most *cohesive* way to build it. The question becomes: can Hop3 maintain internal modularity *within* its codebase to manage this complexity? Good software design (clear interfaces, modules) inside the "monolith" is key.
2.  **Tight Coupling:** This is often cited as a negative, but it's a trade-off. If Hop3's core value proposition *includes* this specific type of advanced optimization, then maybe tight coupling is acceptable or even necessary for performance and consistency. The real risk is coupling unrelated parts, not necessarily parts that work together closely.
3.  **Technology Stack/Dependencies:** This remains a potential *technical blocker*. If Hop3 is *not* Python or cannot easily accommodate SMO's dependencies (CVXPY, specific K8s client versions), merging is likely infeasible. However, *if* Hop3 is Python-based and dependencies can be managed, this hurdle might be overcome.
4.  **Loss of SMO Reusability:** Is reusing SMO *outside* the context of Hop3 (or a very similar PaaS) a primary, practical goal for Abilian or NEPHELE? If not, then prioritizing the best integrated experience for Hop3 users might be more valuable than keeping SMO theoretically reusable but potentially clunkier to integrate with Hop3.
5.  **Development Focus/Team Structure:** Can the Hop3 team effectively own and develop the specialized optimization logic? This depends entirely on the team's skills and priorities. It might require dedicated expertise within the team.
6.  **Scalability:** Can the optimization components (which might be CPU-intensive) be scaled appropriately *within* the Hop3 architecture? Perhaps they run in separate worker processes managed by Hop3, mitigating the risk of blocking core PaaS functions.

## Conclusion

Merging SMO's functionalities directly into Hop3, creating a more "modular monolith," **is a viable architectural option, but the decision requires careful consideration of specific trade-offs, moving beyond a default preference for microservices.** It could make sense primarily if:

1. **Technical Feasibility:** Hop3's technology stack (ideally Python) can cleanly incorporate SMO's code and, crucially, its dependencies (especially CVXPY and Kubernetes client libraries) without major conflicts.
2. **High Functional Cohesion:** The advanced orchestration/optimization features are deemed essential and inseparable parts of Hop3's core value proposition for its target users, justifying the tight integration.
3. **Operational Simplicity is Prioritized:** The benefits of managing a single deployable unit significantly outweigh the challenges of increased internal codebase complexity and potential coupling.
4. **Independent Reusability of SMO is Not Required:** The need to use SMO outside the Hop3 context is low or non-existent.
5. **Strong Internal Modularity within Hop3:** The Hop3 team commits to maintaining clear boundaries and interfaces within the monolithic codebase to manage complexity effectively.
6. **Team Capability:** The Hop3 team is prepared to own, maintain, and evolve the specialized optimization logic.

## The Decision Path

Given these considerations, the H3NI project should explicitly evaluate this architectural choice:

1. **Technical Spike:** Conduct a focused investigation into the technical feasibility of embedding SMO's core logic and dependencies within Hop3's build system and runtime environment. Identify potential conflicts.
2. **Analyze Functional Coupling:** Detail the exact nature and frequency of interactions required between Hop3's existing features and SMO's logic. Are they frequent, low-latency calls tightly bound to Hop3 state, or more asynchronous, batch-like operations?
3. **Evaluate Performance Needs vs. API Latency:** Quantify the expected performance impact of using API calls versus direct function calls for critical H3NI use cases (e.g., meeting the 5-second elasticity KPI).
4. **Assess Maintainability & Team Impact:** Evaluate the long-term maintainability of the potentially larger Hop3 codebase and ensure the team has the necessary skills (or a plan to acquire them) for the optimization components.
5. **Strategic Alignment (Hop3 & NEPHELE):** Consider the strategic goals. Is Hop3 aiming to be the platform incorporating this level of optimization, or is SMO meant to be a reusable NEPHELE component?

If the technical path is clear and the functional cohesion and operational benefits are high, then adopting a well-structured modular monolith approach by integrating SMO's logic could be the superior path for the Hop3+H3NI combination, despite diverging from a pure microservice architecture. However, if technical hurdles are significant or if independent evolution and reusability are valued, maintaining SMO as a separate service with enhanced pluggability remains the safer, more flexible default.

## References

- [[Pros and Cons of Microservices]]
- [[Alternatives to Microservices]]
