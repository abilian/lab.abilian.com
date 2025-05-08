
This note provides an overview of the H3NI project, funded under the [[Public/Projects/NEPHELE/00 NEPHELE|NEPHELE]] Open Call framework. H3NI aims to significantly enhance the capabilities and usability of the NEPHELE ecosystem by integrating **Hop3**, Abilian's open-source Platform as a Service (PaaS), with the **Synergetic Meta-Orchestrator (SMO)**. In this note, we assume familiarity with [[SMO - Key Concepts|the SMO's core concepts]] (HDAGs, intent translation, placement/scaling optimization) and its role in orchestrating multi-cluster deployments via Karmada.

### What is Hop3?

Briefly, [[Public/Projects/Hop3/Hop3|Hop3]] is an open-source PaaS designed to simplify the deployment and lifecycle management of distributed applications across diverse infrastructures (on-premises, cloud, edge). It focuses on providing developer-friendly workflows (including GitOps and CLI interactions), flexibility, and promoting digital sovereignty by avoiding vendor lock-in.

### H3NI Project Vision: Synergy between Hop3 and SMO

The core vision of H3NI is to create a seamless, powerful, and user-friendly orchestration solution by combining the strengths of Hop3 and SMO:

*   **Hop3:** Provides the user-facing interface, application definition models, GitOps workflows, and potentially specific application lifecycle management features.
*   **SMO:** Provides the underlying multi-cluster orchestration intelligence, handling complex HDAG translation, optimized placement and scaling decisions across Karmada-managed clusters, and integration with monitoring systems.

H3NI aims to:

1.  **Enhance SMO's Capabilities:** Leverage Hop3's context and potentially new logic to drive more advanced SMO features, particularly in dynamic scaling, energy optimization, and specific workload management (e.g., AI/ML).
2.  **Simplify Complex Orchestration:** Use Hop3 as an intuitive front-end to SMO's powerful backend, abstracting the complexity of HDAG descriptors and multi-cluster operations for developers and operators.
3.  **Introduce New Optimization Dimensions:** Explicitly target energy efficiency and potentially other factors like financial cost or network latency within the orchestration decision-making process.
4.  **Ensure Interoperability:** Provide a robust, API-driven integration between Hop3 and SMO.
5.  **Contribute Open Source:** All integration code and potential SMO enhancements developed within H3NI will be contributed back to the NEPHELE ecosystem.

### How H3NI Will Interact with SMO

The primary integration model we are currently working on involves Hop3 acting as a client and potentially an enhancer of SMO:

1.  **Hop3 as an SMO Client:**
    *   Hop3 will translate its own application definitions into SMO-compatible **HDAG Descriptors**.
    *   It will use SMO's REST API (e.g., `POST /project/{project}/graphs`) to submit these descriptors for deployment.
    *   Hop3 will query SMO's API to retrieve status information about deployed HDAGs and services, presenting this information through its own interfaces.
    *   Hop3 workflows (like GitOps) will reconcile the desired state (represented as an HDAG) with SMO.

2.  **Leveraging SMO's Optimization:**
    *   Hop3 will delegate the core tasks of **service placement** and **replica scaling** across multiple clusters to SMO's optimization engines (utilizing `utils/placement.py` and `utils/scaling.py`).
    *   Hop3 will need to provide SMO with the necessary inputs, including application structure, resource requirements derived from Hop3 definitions, and potentially service performance parameters (`alpha`/`beta`) if known.

3.  **Enhancing SMO's Optimization (Potential H3NI Contributions):**
    *   For H3NI to achieve goals like explicit energy optimization or predictive scaling, enhancements to SMO are anticipated. The most effective way to achieve this appears to be by making SMO's optimization logic **pluggable** (as detailed in [[SMO - Potential Improvements]] and [[SMO↔︎H3NI Improvement Plan]]).
    *   H3NI could then contribute:
        *   **New Strategy Plugins:** Implementing `PlacementStrategy` or `ScalingStrategy` interfaces within SMO to incorporate energy metrics, predictive forecasts, or logic for compute offloading/migration.
        *   **Data Provision:** Hop3 would provide the necessary contextual data (e.g., cluster energy profiles, predicted request rates) required by these new strategies, potentially via new SMO API endpoints or extensions to the HDAG descriptor.
        *   **Intent Extensions:** Defining new intent types within the HDAG descriptor schema to express goals like energy preferences or offloading policies.

### Specific H3NI Goals Impacting SMO

*   **Energy Optimization (KPI: >15% improvement):** Requires SMO's placement/scaling to consider energy factors. This necessitates H3NI providing energy metadata for clusters and likely involves developing and plugging in new energy-aware optimization strategies into SMO.
*   **Predictive Scaling:** Requires feeding predicted workload metrics (potentially generated by an ML model within H3NI/Hop3) into SMO's scaling strategy mechanism, likely necessitating a flexible input interface for the scaling plugin.
*   **Compute Offloading / Live Migration:** These advanced workflows are not directly supported by SMO's current placement/scaling logic. H3NI would need to define corresponding intents and likely implement new, specialized strategy plugins within SMO to handle the decision-making for these actions.
*   **AI/ML Workflow Support:** Requires tailoring placement (GPU types, data locality) and scaling (specific metrics, responsiveness) for AI/ML workloads, likely via specialized optimization plugins and richer intent definitions.
*   **Elasticity Response Time (KPI: <5s):** While dependent on many factors, H3NI will work with SMO to optimize the interaction loop (metric collection -> SMO optimization -> Karmada scaling) to minimize delays.

### Expected Benefits

By integrating Hop3 and SMO, H3NI aims to deliver:

*   A **more accessible and user-friendly** experience for deploying and managing complex, optimized multi-cluster applications.
*   Improved **resource utilization and energy efficiency**, contributing to Green IT goals.
*   An **enhanced, open, and interoperable** orchestration solution within the NEPHELE ecosystem.
