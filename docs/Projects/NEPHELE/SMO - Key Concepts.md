## What is the SMO (Synergetic Meta-Orchestrator)?

The Synergetic Meta-Orchestrator (SMO) is a sophisticated system designed to simplify the deployment, management, and scaling of complex, multi-component applications across distributed Kubernetes environments. To understand its unique contributions, it's helpful to distinguish between standard cloud-native technologies and the specific functionalities and concepts introduced by SMO.

### 1. Foundation: Common Kubernetes & Cloud-Native Ecosystem Knowledge

SMO builds upon a rich ecosystem of established technologies. Familiarity with these will aid in understanding SMO's operational context:

1.  **Kubernetes Cluster:** The fundamental container orchestration platform. SMO manages applications deployed *across* multiple such clusters.
2.  **Container Runtimes (e.g., `containerd`):** Software responsible for running containers. SMO's prerequisites mention `containerd`, and its configuration (e.g., for insecure registries) is a standard task.
3.  **`kubectl`:** The standard CLI for Kubernetes interaction.
4.  **Kubeconfig Files:** Standard files for configuring client access to Kubernetes clusters. SMO uses these to connect to Karmada and Submariner.
5.  **Docker & Docker Compose:** Docker for container image management; Docker Compose for running SMO and its dependencies (like PostgreSQL and a test registry) locally.
6.  **Container/Artifact Registry (e.g., Distribution):** OCI-compliant registries store container images and other artifacts (like Helm charts). SMO pulls application artifacts from such registries.
7.  **OCI (Open Container Initiative) Artifacts:** A standard for packaging cloud-native content. SMO expects application components and HDAG descriptors to be packaged as OCI artifacts.
8.  **Helm:** The de facto package manager for Kubernetes. SMO uses Helm (via its CLI) to deploy individual application services (packaged as Helm charts) into Karmada-managed clusters.
9.  **Prometheus & Prometheus Operator:**
    *   **Prometheus:** A leading open-source monitoring and alerting system.
    *   **Prometheus Operator:** Simplifies Prometheus deployment on Kubernetes and introduces Custom Resource Definitions (CRDs) like `ServiceMonitor` (for service discovery) and `PrometheusRule` (for alert definitions).
    *   SMO deeply integrates with Prometheus: it queries metrics for its scaling algorithms and dynamically manages `PrometheusRule` CRs for conditional service deployments.
10. **REST APIs & Swagger/OpenAPI:** SMO exposes its functionality via a REST API, documented using Swagger/OpenAPI (accessible at `/docs`).
11. **Namespaces (Kubernetes):** Used for resource isolation within Kubernetes. SMO deploys HDAGs into project-specific namespaces.
12. **OpenStack:** A popular open-source IaaS cloud platform. SMO can integrate with an NFVCL to provision Kubernetes clusters on OpenStack.
13. **SQLAlchemy & PostgreSQL:** SMO uses SQLAlchemy as an ORM to interact with a PostgreSQL database for persisting its internal state (HDAGs, services, cluster info, etc.).
14. **CVXPY:** A Python library for modeling and solving convex optimization problems. This is a key technology underpinning SMO's intelligent placement and scaling decisions.

### 2. Specific to the SMO Project: Core Concepts and Components

This is where SMO introduces its unique value and concepts. The SMO acts as an intelligent "meta-orchestrator" by:

*   Introducing abstractions like **HDAGs** and **Intent Formulations**.
*   Performing sophisticated **intent translation** using **optimization algorithms (CVXPY)** for placement and scaling.
*   Orchestrating **Karmada** for multi-cluster deployment execution.
*   Deeply integrating with **Prometheus and Grafana** for monitoring-driven actions and rich observability.
*   Managing its own **stateful understanding** of applications and infrastructure.
*   Utilizing tools like **`hdarctl`** for artifact management within the NEPHELE ecosystem.

Detailed descriptions:

1.  **SMO (Synergetic Meta-Orchestrator):**
    *   The Flask-based application itself, acting as a high-level control plane.
    *   **Core Responsibility (refined):** To receive declarative **intent formulations** (often as **HDAG descriptors**), translate them into concrete, optimized deployment plans (including service placement and replica counts), and then enforce these plans across multiple Kubernetes clusters by orchestrating **Karmada** (for deployment) and integrating with **Prometheus** (for monitoring-driven actions and scaling) and **Grafana** (for observability). It also manages the lifecycle of these **HDAGs**.

2.  **Hyper Distributed Application Graph (HDAG):**
    *   SMO's central abstraction for a complex, multi-component application. It's a graph structure where nodes are individual services and edges represent dependencies or communication paths.
    *   **Defined by:** An "HDAG Descriptor" (typically YAML), which specifies:
        *   Services, their OCI artifact references (e.g., Helm chart locations).
        *   Resource intents (CPU, memory, GPU – translated by SMO using `utils.intent_translation.py`).
        *   Connection points between services (used by SMO to configure cross-cluster communication, likely via Submariner).
        *   Deployment triggers (e.g., conditional deployment based on Prometheus alerts).
    *   SMO stores the descriptor and the calculated placement in its database (`Graph` model).

3.  **Intent Formulation & Translation:**
    *   **Intent Formulation:** The high-level, declarative input provided by the user, primarily through the HDAG descriptor. It expresses *what* the application should look like and *what* operational characteristics it needs (e.g., resource profiles like 'light' CPU, conditional deployment rules).
    *   **Translation (multi-stage by SMO):**
        1.  Parsing the HDAG descriptor (from OCI artifact or direct input).
        2.  Mapping abstract resource intents (e.g., 'light' CPU) to concrete Kubernetes resource values (`utils.intent_translation.py`).
        3.  **Placement Decision:** Solving an optimization problem (using CVXPY in `utils.placement.py`) to determine the optimal cluster for each service, considering resource availability, GPU requirements, and minimizing deployment/re-optimization costs.
        4.  **Scaling Decision:** For ongoing management, solving another optimization problem (using CVXPY in `utils.scaling.py`) to determine optimal replica counts based on Prometheus metrics, service performance models (e.g., `y=ax+b`), and resource utilization goals.
        5.  Generating specific Helm `values_overwrite` data, including `clustersAffinity` (from placement) and `serviceImportClusters` (for Submariner-enabled connectivity).
        6.  Creating Prometheus alert rules and Grafana dashboards.

4.  **Orchestration of Karmada & Submariner:**
    *   **Karmada:** SMO's primary execution engine for multi-cluster deployments. SMO uses `KarmadaHelper` to:
        *   Query cluster resource availability from Karmada's aggregated view.
        *   Instruct Karmada (via `helm` CLI calls targeted at Karmada's kubeconfig) to deploy, upgrade, or uninstall Helm charts representing HDAG services. Karmada's propagation policies then distribute these to member clusters.
        *   Scale Kubernetes Deployments managed by Karmada.
    *   **Submariner:** Facilitates inter-cluster L3 connectivity. SMO:
        *   Uses `SubmarinerHelper` to gather network CIDR information from Submariner CRDs.
        *   Implicitly relies on Submariner for HDAG component communication by configuring `serviceImportClusters` in Helm values, which likely triggers Submariner's service export/import mechanisms.

5.  **`hdarctl` Tool:**
    *   A command-line utility from the NEPHELE project.
    *   SMO uses it (via `subprocess` in `graph_service.get_descriptor_from_artifact`) to pull OCI artifacts (which can contain HDAG descriptors and associated Helm charts) from a registry and untar them.

6.  **HDAR (Hyper-Distributed Application Registry):**
    *   A concept from the NEPHELE project for a specialized registry.
    *   In practice for SMO, this usually refers to any OCI-compliant registry (like the local "Distribution" registry used for testing) where HDAG artifacts are stored.

7.  **SMO's Internal State & Configuration:**
    *   **Database (`models/`):** SMO maintains a PostgreSQL database to store its state: HDAG definitions, service details (including artifact info, placement, Helm overrides, alert rules), cluster resource snapshots, Grafana dashboard links, and NFVCL-related entities. This stateful nature is crucial for its advanced orchestration logic.
    *   **Configuration (`config/`, `flask.env`):** Specific environment variables (`KARMADA_KUBECONFIG`, `SUBMARINER_KUBECONFIG`, `NFVCL_URL`, `PROMETHEUS_HOST`, `GRAFANA_HOST`, `SCALING_ENABLED`, etc.) tailor SMO's behavior and its connections to external systems.

8.  **SMO API Endpoints & Logic (`routes/`, `services/`):**
    *   The REST API exposes functionalities for HDAG lifecycle management (deploy, get, placement, start, stop, remove), cluster information, and NFVCL operations.
    *   The `services/` layer contains the core business logic, including parsing descriptors, invoking placement/scaling algorithms, interacting with helper modules (for Karmada, Prometheus, Grafana, Helm, `hdarctl`), and managing the database.

9.  **NFVCL API Integration & VIMs:**
    *   An optional feature allowing SMO to request the provisioning and management of Kubernetes clusters (primarily on OpenStack) via an external NFVCL API.
    *   **VIM (Virtual Infrastructure Manager):** In this context, typically an OpenStack deployment that the NFVCL manages. SMO stores metadata about VIMs (registered via the NFVCL) to inform cluster creation requests. SMO communicates with the NFVCL, which in turn interacts with the VIM.

10. **Advanced Features Revealed by Code:**
    *   **Optimization-Driven Placement & Scaling:** Use of CVXPY to solve MILPs for intelligent resource allocation.
    *   **Proactive Observability:** Automatic generation of detailed Grafana dashboards and Prometheus alert rules.
    *   **Conditional Service Deployment:** Deploying services based on Prometheus alert triggers.
    *   **Service Performance Modeling:** The scaling algorithm uses a linear model (`y=ax+b`) to represent service capacity, with coefficients currently hardcoded for specific services, implying a need for service profiling.

## Core SMO Concepts

This section defines the fundamental concepts and abstractions used by the Synergetic Meta-Orchestrator (SMO).

### 1. Hyper Distributed Application (HDA)

At the highest level, SMO manages **Hyper Distributed Applications (HDAs)**. While most modern applications are *distributed* (components running on multiple servers), an HDA, in the context of SMO and the NEPHELE project, represents an application with a significantly higher degree of distribution and complexity.

Key characteristics include:

*   **Multi-Cluster Deployment:** Components are intentionally spread across multiple, potentially geographically dispersed, independent Kubernetes clusters.
*   **Geographical Dispersion:** Services may be located in different data centers or edge locations to meet latency, regulatory, or availability requirements.
*   **Heterogeneous Environments:** The underlying clusters might run on diverse infrastructures (public cloud, private cloud like OpenStack, bare-metal, edge devices).
*   **Complex Interdependencies:** Services within the HDA have defined communication paths and dependencies, requiring robust inter-cluster networking (facilitated by tools like Submariner).
*   **Dynamic Operational Needs:** The application requires intelligent resource management, including dynamic scaling based on load, optimal placement based on resource availability and service requirements (e.g., GPU access), and potentially automated responses to environmental changes.

**SMO's Role:** The SMO is specifically designed to abstract away the complexities of deploying, managing, and optimizing these HDAs, providing a unified, intelligent control plane for their entire lifecycle.

### 2. Hyper Distributed Application Graph (HDAG) and Intent Formulation

To manage an HDA, the SMO uses a detailed blueprint called a **Hyper Distributed Application Graph (HDAG)**. This goes beyond a simple component diagram (an "Application Graph") by capturing not just the structure but also the operational **intent** for the application across multiple clusters.

The HDAG is defined in a descriptor file, typically written in **YAML**. This **HDAG Descriptor *is* the primary "Intent Formulation"** for the SMO – it's how users declare their desired state and high-level objectives for the HDA.

**Key Information Defined in an HDAG Descriptor:**

The descriptor provides the SMO with all necessary details:

1.  **Graph Identity:** A unique identifier for this specific deployment instance (`hdaGraph.id`).
2.  **Services:** Definitions for each individual microservice or functional component (`hdaGraph.services` list, each with a unique `id`).
3.  **Artifacts (`service.artifact`):** Specifies the deployable package for each service, usually an OCI artifact URL (`ociImage`) pointing to a Helm chart. Includes metadata like the chart type/implementer (`ociConfig`).
4.  **Resource Intents (`service.deployment.intent.compute`):** Declares high-level resource needs using abstract terms (e.g., `cpu: light`, `ram: medium`, `gpu: enabled: 'True'`). SMO translates these into concrete Kubernetes resource requests/limits (using `utils.intent_translation.py`).
5.  **Connection Points (`service.deployment.intent.connectionPoints`):** Crucially lists the `id`s of *other* services within the HDAG that *this* service needs to connect to. This allows SMO to configure necessary cross-cluster networking (likely via Submariner).
6.  **Deployment Triggers (`service.deployment.trigger`):** Defines *how* a service is deployed. It can be `standard` (deploy immediately) or `event` (deploy conditionally based on external events, currently Prometheus alerts). For event triggers, it specifies the Prometheus query, duration, etc.
7.  **Baseline Helm Overrides (`service.artifact.valuesOverwrite`):** Allows specifying default Helm values to customize the service's chart. SMO merges its dynamically generated values (placement, networking) with these baseline overrides.

**SMO's Role with the HDAG Descriptor:** SMO parses this descriptor (fetched directly or via `hdarctl` from an OCI artifact), treats it as the authoritative statement of user intent, and uses its contents as direct input for its optimization algorithms (placement, scaling) and orchestration workflow (generating Helm values, interacting with Karmada, Prometheus, Grafana).

**Concrete HDAG Descriptor Example (YAML):**

This example shows a 3-service application (`web-frontend`, `api-backend`, `user-db`) with resource intents, connection points, and a conditional deployment trigger for the database.

```yaml
# Example HDAG Descriptor: my-webapp.yaml
hdaGraph:
  id: my-webapp-graph # Unique identifier for this HDAG instance
  services:
    # --- Service 1: Web Frontend ---
    - id: web-frontend
      artifact:
        ociImage: oci://registry.example.com/my-project/frontend-chart:v1.2.0
        ociConfig: { implementer: Helm, type: Application }
        valuesOverwrite: { serviceType: ClusterIP, image: { tag: "latest" } }
      deployment:
        intent:
          compute: { cpu: light, ram: small, storage: none, gpu: { enabled: 'False' } }
          connectionPoints: [ api-backend ] # Connects TO api-backend
        trigger: { type: standard }

    # --- Service 2: API Backend ---
    - id: api-backend
      artifact:
        ociImage: oci://registry.example.com/my-project/backend-chart:v1.1.5
        ociConfig: { implementer: Helm, type: Application }
        valuesOverwrite: { replicaCount: 1 } # Base replica count
      deployment:
        intent:
          compute: { cpu: medium, ram: medium, storage: none, gpu: { enabled: 'False' } }
          connectionPoints: [ user-db ] # Connects TO user-db
        trigger: { type: standard }

    # --- Service 3: User Database (Conditional Deployment) ---
    - id: user-db
      artifact:
        ociImage: oci://registry.example.com/my-project/database-chart:v2.0.0
        ociConfig: { implementer: Helm, type: Database }
        valuesOverwrite: { persistence: { enabled: true } }
      deployment:
        intent:
          compute: { cpu: small, ram: medium, storage: medium, gpu: { enabled: 'False' } }
          connectionPoints: [] # Does not initiate connections
        trigger: # Deploys only when event occurs
          type: event
          event:
            condition: AND
            events:
              - id: backend-high-load # Unique ID for the Prometheus Rule
                source: prometheus
                condition:
                  promQuery: 'sum(rate(http_requests_total{job="api-backend"}[1m])) > 10'
                  gracePeriod: '1m'
                  description: 'Deploy user-db when backend load exceeds 10 req/sec for 1 min'
```

**Syntax and Semantics Explained (Key Fields):**

*   **`hdaGraph.id` (String):** Instance name for this deployment. Maps to `Graph.name`.
*   **`hdaGraph.services` (List):** Array of service objects.
*   **`service.id` (String):** Unique name within the graph. Maps to `Service.name`.
*   **`service.artifact.ociImage` (String):** OCI URL for the service's Helm chart. Maps to `Service.artifact_ref`. Used by `hdarctl` and `helm`.
*   **`service.artifact.ociConfig.{implementer|type}` (String):** Metadata about the artifact. Mapped to `Service.artifact_implementer`, `Service.artifact_type`.
*   **`service.artifact.valuesOverwrite` (Mapping):** Baseline Helm overrides provided by the user. Merged with SMO-generated values. Stored in `Service.values_overwrite`.
*   **`service.deployment.intent.compute.{cpu|ram|storage}` (String):** Abstract resource level ('light', 'small', etc.). Translated by `utils.intent_translation.py` into concrete values (e.g., '0.5', '1GiB') stored in `Service.cpu`, `Service.memory`, `Service.storage` and used by optimization algorithms.
*   **`service.deployment.intent.compute.gpu.enabled` (String 'True'/'False'):** GPU requirement. Used by placement algorithm. Stored as `Service.gpu` (0 or 1).
*   **`service.deployment.intent.connectionPoints` (List of Strings):** Lists target service `id`s this service connects *to*. Processed by `create_service_imports` to configure cross-cluster networking (likely via Submariner exports/imports injected into Helm values as `serviceImportClusters`).
*   **`service.deployment.trigger.type` (String):** `'standard'` or `'event'`.
*   **`service.deployment.trigger.event...` (Mapping):** Defines the Prometheus alert details if `type` is `'event'`. These are used by `create_alert` and `PrometheusHelper.update_alert_rules` to manage a `PrometheusRule` resource. Stored in `Service.alert`.

### 3. The SMO's Core Orchestration Process (Conceptual Flow)

At its core, the SMO executes a continuous cycle driven by user intent:

1.  **Intent Ingestion & Translation:** the SMO receives the HDAG descriptor (the intent). It parses this, translating abstract requirements (like 'light' CPU) into concrete parameters and identifying deployment conditions (like Prometheus alerts).
2.  **Plan Construction (Optimization):** Using the translated intent and real-time/cached information about available cluster resources (from Karmada/its DB), SMO's optimization algorithms (`utils/placement.py`, `utils/scaling.py`) construct a deployment plan. This includes:
    *   Deciding the optimal cluster placement for each service.
    *   Determining the necessary initial (or ongoing optimal) number of replicas for scaling.
    *   Calculating required network configurations (e.g., `serviceImportClusters`).
    *   Generating configurations for observability (Grafana dashboards, Prometheus rules).
3.  **Plan Enforcement (Execution & Reconciliation):** the SMO enforces the plan by interacting with other systems:
    *   It uses **Helm** (via `subprocess`) directed at **Karmada** to deploy/update services according to the plan (passing placement, replicas, network config as Helm value overrides).
    *   It configures **Prometheus** alerts and publishes **Grafana** dashboards.
    *   It **continuously monitors** key metrics (via Prometheus) and re-runs its scaling optimization, instructing **Karmada** to adjust replicas as needed.
    *   It handles explicit lifecycle commands (start, stop, remove, re-place) initiated via its API.

This process transforms a high-level declarative intent into a dynamically managed, optimized, multi-cluster application deployment.

## Other Components / Subsystems

### What's Karmada and what role does it play in the system?

*   **Karmada:** A CNCF open-source project providing a unified control plane for managing applications across multiple Kubernetes clusters ("multi-cluster application management"). It allows users to define how applications are distributed and customized across different "member clusters."
*   **Role in the SMO System (Critical Execution Engine):**
    *   The SMO *makes strategic decisions*: *what* services to deploy, *where* (on which cluster or clusters), with *how many* replicas, and with *what specific configurations*.
    *   Karmada *executes these decisions*:
        1.  The SMO uses its `KarmadaHelper` to get aggregated resource information from clusters registered with Karmada.
        2.  The SMO invokes the `helm` CLI, directing it to the Karmada control plane's `kubeconfig`.
        3.  The SMO provides Helm with `values_overwrite` data that includes `clustersAffinity` (telling Karmada which cluster(s) a service is primarily for) and other configurations.
        4.  Karmada's internal mechanisms (like Propagation Policies and Override Policies, though the SMO doesn't directly create these YAMLs) then ensure that the Helm release (and its underlying Kubernetes resources like Deployments, Services) are created and managed on the correct member cluster(s) as per SMO's plan.
        5.  The SMO also uses Karmada's API to scale Kubernetes Deployments.
    *   In essence, the SMO is the "brains" formulating the multi-cluster deployment strategy, and Karmada is the "distributed muscle" that implements that strategy across the federated Kubernetes environment.

### What's an NFVCL?

*   **NFV (Network Function Virtualization):** Decoupling network functions (firewalls, routers) from dedicated hardware, allowing them to run as software (VNFs) on standard IT infrastructure.
*   **CL (Cluster Lifecycle manager):** Software for managing the lifecycle (creation, deletion, scaling) of compute clusters.
*   **NFVCL (Network Function Virtualization Cluster Lifecycle manager - as used by the SMO):** An external API-driven system that SMO can optionally integrate with to automate the provisioning and lifecycle management of Kubernetes clusters, typically on an underlying IaaS platform like OpenStack.
*   **The SMO's Role:** If configured (via `NFVCL_BASE_URL`), the SMO can:
    *   Register/discover Virtual Infrastructure Managers (VIMs) through the NFVCL (see `vim_service.py`).
    *   Request the NFVCL to create new Kubernetes clusters on a specified VIM (e.g., an OpenStack instance) if the HDAG deployment requires additional capacity or specific cluster characteristics (see `os_k8s_service.py`).
    *   Synchronize cluster information from NFVCL into its own database.
    This allows the SMO to extend its orchestration capabilities down to the infrastructure provisioning layer.

### What's a VIM?

In the context of the SMO and its NFVCL integration, a **VIM** stands for **Virtual Infrastructure Manager**.

1.  **Virtual Infrastructure:** The underlying virtualized compute, storage, and network resources. In SMO's case, this primarily refers to **OpenStack** environments, as indicated by the code and examples.
2.  **Manager:** The VIM (e.g., OpenStack) is the IaaS platform that manages this virtual infrastructure, providing APIs for provisioning and managing VMs, networks, and storage.

A **VIM** is the IaaS platform (typically OpenStack) that the NFVCL controls to provide the foundational virtual resources for Kubernetes clusters requested by SMO. SMO orchestrates the NFVCL, which in turn orchestrates the VIM.

**How VIMs fit into the SMO/NFVCL Picture:**

SMO enables dynamic Kubernetes cluster creation for HDAGs when integrated with an NFVCL.
```
SMO (User's HDAG Intent & Cluster Needs)
  | --> (Requests K8s Cluster from NFVCL)
  v
NFVCL API (Cluster Lifecycle Manager)
  | --> (Instructs VIM to provision resources)
  v
VIM (e.g., OpenStack - provides VMs, networks)
  | --> (Runs on Physical Hardware)
  v
Actual Hardware
```

**The SMO's Interaction with VIMs (Indirectly, via NFVCL):**

*   **Registration/Discovery (via NFVCL):** SMO, through its `vim_service.py`, can sync VIM information from an NFVCL instance or allow users to register a VIM (providing OpenStack details like URL, tenant, credentials) *with the NFVCL*. SMO itself stores metadata about these VIMs (name, URL, POP area) in its database (`VIM` model).
*   **Usage in Cluster Creation (via NFVCL):** When SMO requests a new Kubernetes cluster from the NFVCL (through `os_k8s_service.py`), it specifies which registered VIM (and its associated POP area) the NFVCL should use. The NFVCL then uses the VIM's API (e.g., OpenStack APIs) to provision the necessary VMs and networks for the new Kubernetes cluster.
