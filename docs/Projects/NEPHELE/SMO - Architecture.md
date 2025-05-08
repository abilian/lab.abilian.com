The Synergetic Meta-Orchestrator (SMO) is a Python Flask-based application that provides a sophisticated framework for orchestrating Hyper Distributed Applications (HDAs) across multiple Kubernetes clusters. It achieves this by translating high-level, declarative user **intents** (embodied in **HDAG Descriptors**) into optimized, concrete deployment plans. Key to its operation is the use of mathematical optimization (via CVXPY) for service placement and dynamic scaling, deep integration with **Karmada** for multi-cluster execution, and proactive observability through **Prometheus** and **Grafana**. SMO also offers optional integration with an **NFVCL** for on-demand provisioning of Kubernetes clusters on IaaS platforms like OpenStack. It maintains its own stateful understanding of deployed applications and infrastructure within a PostgreSQL database.

### Core Functionality

1.  **Intent Translation and Optimized Deployment Planning:**
    *   Receives HDAG Descriptors (YAML/JSON) defining application structure, service artifacts (OCI Helm charts), abstract resource needs, connectivity, and operational policies (e.g., conditional deployment).
    *   Translates abstract intents (e.g., 'light' CPU) into concrete resource values.
    *   Utilizes **CVXPY-based optimization algorithms** (`utils.placement.py`) to determine optimal cluster placement for each service, considering resource availability (CPU, GPU), current deployments (to minimize churn), and other constraints.
    *   Generates detailed Helm `values_overwrite` data for each service, injecting placement affinity and cross-cluster networking configurations.

2.  **HDAG Deployment and Lifecycle Management:**
    *   Orchestrates the deployment of HDAG services onto Karmada-managed clusters using the `helm` CLI.
    *   Manages the full lifecycle: deploy (from OCI artifact or descriptor), start, stop (uninstalling Helm charts while retaining SMO state), remove (full cleanup), and trigger re-placement.
    *   Supports **conditional service deployment**: services are only deployed when specific Prometheus alerts (dynamically configured by SMO) are triggered.

3.  **Multi-Cluster Orchestration with Karmada:**
    *   Leverages Karmada as the execution engine for distributing and managing Kubernetes resources (defined in Helm charts) across a federation of member clusters.
    *   SMO's `KarmadaHelper` interacts with the Karmada control plane to fetch cluster information and manage deployment scaling.

4.  **Intelligent, Monitoring-Driven Resource Scaling:**
    *   Deeply integrates with Prometheus: queries real-time service metrics (e.g., request rates, CPU utilization).
    *   Employs a **CVXPY-based scaling algorithm** (`utils.scaling.py`) in background threads to dynamically adjust service replica counts. This algorithm uses service-specific performance models (e.g., linear capacity `y=ax+b`) and aims to meet demand while optimizing resource usage and minimizing transitions.
    *   Can trigger a full graph re-placement if scaling constraints cannot be met within the current placement.

5.  **Proactive Observability Setup:**
    *   Automatically generates and publishes detailed **Grafana dashboards** for deployed HDAGs, individual services, and discovered Kubernetes clusters, providing immediate operational visibility.
    *   Dynamically creates and manages **Prometheus alert rules** to enable conditional deployments and potentially other monitoring-driven actions.

6.  **NFVCL Integration (Optional):**
    *   Provides API endpoints to interact with an external NFVCL (Network Function Virtualization Cluster Lifecycle manager).
    *   Enables SMO to request the on-demand provisioning, management, and deletion of Kubernetes clusters on IaaS platforms (primarily OpenStack), by orchestrating the NFVCL which in turn manages **VIMs** (Virtual Infrastructure Managers like OpenStack).

### Current Project Structure

*   **`src/`:** Main SMO application source code.
    *   **`app.py`:** Flask application factory; initializes app, Swagger, DB, registers blueprints, and performs startup tasks like initial cluster sync.
    *   **`config.py`:** Manages environment-based configurations (DB connections, kubeconfig paths, external service URLs).
    *   **`errors/`:** Custom Flask error handlers (e.g., for `subprocess` failures).
    *   **`models/`:** SQLAlchemy database models defining SMO's internal state (HDAGs as `Graph`, `Service` components, `Cluster` info, NFVCL entities like `VIM`, `OS_K8S_cluster`). Utilizes JSONB for flexible structured data.
    *   **`routes/`:** Flask Blueprints defining the REST API endpoints for:
        *   `hdag/graph`: Core HDAG operations (deploy, get, placement, start/stop, remove, alerts).
        *   `cluster/cluster`: Fetching SMO's view of cluster information.
        *   `nfvcl/os_k8s`, `nfvcl/vim`: Managing K8s clusters and VIMs via NFVCL.
    *   **`services/`:** The business logic layer implementing the functionalities exposed by the routes.
        *   `hdag/graph_service.py`: Orchestrates HDAG deployment, placement, scaling, lifecycle, conditional deployment, and interacts with Helm/`hdarctl`. Manages background scaling threads.
        *   `cluster/cluster_service.py`: Synchronizes cluster data from Karmada/Submariner into SMO's DB and creates Grafana dashboards.
        *   `nfvcl/*_service.py`: Implements logic for interacting with the NFVCL API.
    *   **`utils/`:** Core helper modules and algorithms.
        *   `karmada_helper.py`, `submariner_helper.py`: Wrappers for Kubernetes Python client interactions with Karmada and Submariner CRDs/APIs.
        *   `prometheus_helper.py`: Queries Prometheus and manages `PrometheusRule` CRs.
        *   `grafana_helper.py`, `grafana_template.py`: Programmatically generate and publish Grafana dashboards.
        *   `placement.py`: Contains both naive and **CVXPY-based optimization algorithms for service placement**.
        *   `scaling.py`: Contains the **CVXPY-based optimization algorithm for replica scaling**.
        *   `intent_translation.py`: Maps abstract resource intents to concrete values.
        *   `helpers.py`: General utility functions (e.g., `format_memory`).

### Workflow

1.  **SMO Deployment & Setup:**
    *   SMO (Flask app) and PostgreSQL are deployed (e.g., via `docker compose`).
    *   On startup, SMO (`app.py`) connects to its database, creates tables if needed, and performs an initial sync (`fetch_clusters`) to populate its `Cluster` table with data from Karmada and Submariner, also creating initial Grafana dashboards for these clusters.
2.  **Environment Prerequisites:**
    *   A Karmada control plane is operational with member Kubernetes clusters joined.
    *   Submariner is configured for inter-cluster networking.
    *   Prometheus (ideally with Prometheus Operator) is set up for monitoring. Grafana is available.
    *   (Optional) An NFVCL API endpoint is configured if dynamic cluster provisioning is needed.
3.  **HDAG Definition & Packaging:**
    *   Users define their Hyper Distributed Application as an **HDAG Descriptor (YAML file)**, detailing services, OCI artifact URIs (for Helm charts), resource intents, `connectionPoints` for inter-service communication, and any conditional deployment triggers (Prometheus alert conditions).
    *   This descriptor, along with service Helm charts, can be packaged into an OCI artifact using `hdarctl` and pushed to an OCI registry.
4.  **Deployment Request to SMO:**
    *   User sends a `POST` request to SMO's `/project/<project>/graphs` API endpoint.
    *   The request can either contain the raw HDAG descriptor or an OCI artifact URL pointing to it. If an URL is provided, SMO uses `hdarctl pull --untar` to fetch and parse the descriptor.
5.  **SMO's Intent Translation & Placement:**
    *   SMO (`graph_service.deploy_graph`) parses the descriptor.
    *   Abstract resource intents are translated to concrete values (`utils.intent_translation.py`).
    *   The **initial placement algorithm** (`utils.placement.calculate_naive_placement`) determines the target cluster for each service based on resource needs (CPU, GPU) and cluster capacities.
    *   Service import configurations (`serviceImportClusters`) are determined from `connectionPoints`.
    *   Prometheus alert rules are defined if conditional deployments are specified.
    *   Grafana dashboards for the graph and its services are generated.
6.  **Helm Deployment via Karmada:**
    *   For each service, SMO constructs Helm `values_overwrite` data containing placement affinity, service import details, etc.
    *   SMO invokes `helm install` (via `subprocess`), targeting the Karmada control plane's kubeconfig.
    *   Karmada applies its propagation logic to deploy the Helm releases to the designated member clusters.
    *   If conditional, services are only deployed once their triggering Prometheus alert fires (activating via SMO's `/alerts` webhook).
7.  **Ongoing Monitoring, Scaling, and Management:**
    *   **Monitoring:** Prometheus scrapes metrics from deployed services. Users can view Grafana dashboards auto-generated by SMO.
    *   **Scaling:** If `SCALING_ENABLED`, background threads in SMO (`utils.scaling.scaling_loop`) periodically:
        *   Query Prometheus for relevant service metrics (e.g., request rates).
        *   Run the **CVXPY-based scaling optimization** (`utils.scaling.decide_replicas`) to determine new optimal replica counts based on the metrics and service performance models.
        *   If new replica counts are determined, SMO calls `KarmadaHelper.scale_deployment` to adjust.
        *   If scaling is infeasible, it may trigger a full graph re-placement.
    *   **Management:** Users can interact with SMO's API to:
        *   Fetch graph/service status.
        *   Trigger a re-evaluation of placement (`GET /graphs/<name>/placement`), which uses the more advanced `utils.placement.decide_placement` CVXPY algorithm.
        *   Start, stop, or completely remove the HDAG.
        *   (If NFVCL is used) Manage VIMs and request/manage OpenStack-based Kubernetes clusters.
