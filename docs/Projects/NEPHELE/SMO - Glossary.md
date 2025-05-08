
This glossary defines key terms, technologies, and concepts used within the Synergetic Meta-Orchestrator (SMO) project and its surrounding ecosystem.

**A**

*   **Alert (Prometheus)**
    *   **Definition:** A condition defined in Prometheus (using PromQL) that, when true for a specified duration, triggers a notification.
    *   **SMO Context:** SMO can dynamically create Prometheus alert rules. These alerts can then be configured (via Prometheus Alertmanager) to send a webhook to SMO's `/alerts` endpoint. This mechanism enables **conditional service deployment**, where a service within an HDAG is only deployed after a specific alert fires. The alert definition is stored in the `Service` model.
*   **API (Application Programming Interface)**
    *   **Definition:** A set of rules and protocols for building and interacting with software applications, allowing different software components to communicate.
    *   **SMO Context:** SMO itself is a Flask REST API. It also interacts with other APIs, such as the Karmada API, Kubernetes API, Prometheus API, Grafana API, and the NFVCL API.
*   **Artifact (OCI)**
    *   **Definition:** A package conforming to the Open Container Initiative (OCI) specifications, which can store various types of cloud-native content, not just container images.
    *   **SMO Context:** SMO expects application components and HDAG descriptors to be packaged as OCI artifacts (often Helm charts or YAML files within a tarball). The `hdarctl` tool is used to package and push these artifacts to an OCI-compliant registry. SMO uses `hdarctl` to pull these artifacts for deployment.
*   **Artifact Registry (OCI Registry / Distribution)**
    *   **Definition:** A storage system for OCI artifacts. "Distribution" is a well-known open-source OCI-compliant registry.
    *   **SMO Context:** SMO can pull HDAG descriptors and service artifacts (like Helm charts) from an OCI registry. The README provides instructions for setting up a local Distribution registry for testing, and SMO can be configured to use an insecure (HTTP) registry.

**B**

*   **Blueprint (Flask)**
    *   **Definition:** A way to organize a Flask application into smaller, reusable components.
    *   **SMO Context:** SMO uses blueprints to structure its API routes (e.g., `graph` for HDAG operations, `cluster` for cluster info, `os_k8s` and `vim` for NFVCL interactions). These are defined in the `src/routes/` directory.
*   **BM_K8S_cluster (Bare-Metal Kubernetes cluster)**
    *   **Definition (SMO Model):** A database model in SMO representing a Kubernetes cluster deployed on bare-metal servers, typically managed via the NFVCL.
    *   **SMO Context:** Part of the NFVCL integration, allowing SMO to track and potentially request the provisioning of bare-metal K8s clusters.

**C**

*   **CLI (Command-Line Interface)**
    *   **Definition:** A text-based interface used for interacting with software.
    *   **SMO Context:** SMO relies on external CLI tools like `helm` (for deploying Kubernetes applications) and `hdarctl` (for managing OCI artifacts). These are invoked using Python's `subprocess` module.
*   **Cluster (Kubernetes)**
    *   **Definition:** A set of node machines for running containerized applications managed by Kubernetes. It consists of a *control plane* and *worker nodes*.
    *   **SMO Context:** The fundamental unit of deployment infrastructure that SMO orchestrates across, primarily via Karmada. SMO maintains its own database model (`Cluster`) to store information about these clusters, including resources and Grafana dashboard links.
*   **Cluster Affinity**
    *   **Definition (SMO Context):** A property of an SMO `Service` indicating the primary Kubernetes cluster to which that service is (or should be) deployed. This is determined by SMO's placement algorithm.
    *   **SMO Context:** Stored in the `Service` model and used to configure the `clustersAffinity` field in Helm values for Karmada.
*   **Compute Continuum**
    *   **Definition:** A concept referring to the seamless and distributed availability of computing resources spanning from centralized cloud data centers through edge computing nodes to IoT devices.
    *   **SMO Context:** NEPHELE (the larger project SMO is part of) aims to orchestrate applications across this entire continuum. SMO's features like multi-cluster orchestration and potential NFVCL integration are steps towards managing this.
*   **Conditional Service Deployment**
    *   **Definition (SMO Feature):** The ability for SMO to deploy a specific service within an HDAG only when a predefined Prometheus alert is triggered.
    *   **SMO Context:** Implemented by SMO creating Prometheus alert rules. When an alert fires, Alertmanager calls SMO's `/alerts` endpoint, which then triggers the Helm deployment of the associated service.
*   **Containerd**
    *   **Definition:** An industry-standard core container runtime that manages the complete container lifecycle on a host system. It's a CNCF graduated project.
    *   **SMO Context:** SMO's prerequisites state that the Kubernetes clusters should use containerd as the CRI. This is relevant for configuring insecure registries for local testing, as both the Docker daemon and containerd need to be aware of them.
*   **CRI (Container Runtime Interface)**
    *   **Definition:** A plugin interface that enables a Kubernetes kubelet to use different container runtimes (like containerd or CRI-O) without needing to recompile.
    *   **SMO Context:** Prerequisite for SMO, specifically mentioning `containerd`.
*   **CRD (Custom Resource Definition)**
    *   **Definition (Kubernetes):** A way to extend the Kubernetes API by adding new types of resources that behave like native Kubernetes objects.
    *   **SMO Context:**
        *   Prometheus Operator CRDs (e.g., `ServiceMonitor`, `PrometheusRule`) are prerequisites if Prometheus monitoring is desired via this mechanism. SMO directly manages `PrometheusRule` CRs.
        *   Karmada and Submariner also introduce their own CRDs that SMO interacts with indirectly (via their APIs or client libraries).
*   **CVXPY**
    *   **Definition:** A Python-embedded modeling language for convex optimization problems. It allows users to express optimization problems in a natural, mathematical syntax.
    *   **SMO Context:** Used critically in `utils/placement.py` and `utils/scaling.py` to solve the mathematical optimization problems for service placement and replica scaling, respectively. This is a core part of SMO's "intelligence."

**D**

*   **Database (PostgreSQL)**
    *   **Definition:** An organized collection of data. PostgreSQL is a powerful, open-source object-relational database system.
    *   **SMO Context:** SMO uses PostgreSQL to store its internal state, including information about HDAGs, services, clusters, VIMs, and their configurations. SQLAlchemy is used as the ORM.
*   **Deployment (Kubernetes)**
    *   **Definition:** A Kubernetes object that declaratively manages a set of replica Pods, providing features like rolling updates and rollbacks.
    *   **SMO Context:** Individual services within an HDAG are typically deployed as Kubernetes Deployments (packaged within Helm charts). SMO, via Karmada, manages the lifecycle and scaling of these Deployments.
*   **Deployment Plan**
    *   **Definition (SMO Context):** The concrete set of actions and configurations SMO derives from an intent formulation and an HDAG definition. This plan specifies which services run on which clusters, with how many replicas, and with what specific configurations.
    *   **SMO Context:** Constructed by SMO's internal logic (including placement and scaling algorithms) and then enforced by instructing Karmada (e.g., by generating Helm values and running `helm install/upgrade`).
*   **Descriptor (HDAG Descriptor)**
    *   **Definition (SMO Context):** A file (typically YAML or JSON) that defines the structure and characteristics of a Hyper Distributed Application Graph. It details the services, their artifacts, dependencies (connection points), resource intents, and potentially deployment triggers.
    *   **SMO Context:** This is a primary input to SMO's deployment process. It can be provided directly in an API request or pulled from an OCI artifact. Stored as `graph_descriptor` in the `Graph` model.
*   **Docker**
    *   **Definition:** A platform for developing, shipping, and running applications in containers.
    *   **SMO Context:** Used for containerizing the SMO application itself. Also, application services within an HDAG are deployed as Docker container images. The README provides instructions for configuring Docker to use a local insecure registry.
*   **Docker Compose**
    *   **Definition:** A tool for defining and running multi-container Docker applications.
    *   **SMO Context:** Used to easily deploy the SMO application and its associated PostgreSQL database for local development and testing. Separate Docker Compose files are provided for SMO and the local test registry.

**E**

*   **Edge Computing**
    *   **Definition:** A distributed computing paradigm that brings computation and data storage closer to the sources of data – typically IoT devices or local users – to improve response times and save bandwidth.
    *   **SMO Context:** NEPHELE (and by extension SMO) aims to manage applications that can span across edge locations as part of the compute continuum.
*   **Environment Variables**
    *   **Definition:** Variables whose values are set outside the program, typically in the shell or an environment file, and can be accessed by the running process.
    *   **SMO Context:** Heavily used for configuration (e.g., `DB_USER`, `KARMADA_KUBECONFIG`, `FLASK_ENV`). Loaded via `python-dotenv` in `config.py`.

**F**

*   **Flask**
    *   **Definition:** A lightweight WSGI web application framework in Python.
    *   **SMO Context:** The core framework used to build the SMO's REST API server (`src/app.py`).
*   **Flasgger**
    *   **Definition:** A Flask extension for generating Swagger/OpenAPI documentation from Flask route definitions and docstrings.
    *   **SMO Context:** Used to provide the interactive API documentation at the `/docs` endpoint.

**G**

*   **Grafana**
    *   **Definition:** An open-source platform for monitoring and observability, widely used for visualizing time-series data from sources like Prometheus.
    *   **SMO Context:** SMO has deep integration with Grafana. It programmatically creates and publishes dashboards for deployed HDAGs, individual services, and managed clusters, providing immediate visual feedback on their status and performance. The `GrafanaHelper` and `grafana_template.py` utilities manage this.
*   **Graph (HDAG)**
    *   See **Hyper Distributed Application Graph (HDAG)**.

**H**

*   **HDAG (Hyper Distributed Application Graph)**
    *   **Definition (SMO Concept):** SMO's model or blueprint for a Hyper Distributed Application. It represents the application as a graph of interconnected services (nodes) and their dependencies/communication paths (edges), along with their deployment characteristics and intents.
    *   **SMO Context:** The central abstraction SMO manages. Users define HDAGs (via descriptors), and SMO translates these into deployment plans. Stored in the `Graph` database model.
*   **HDAR (Hyper-Distributed Application Registry)**
    *   **Definition (NEPHELE Concept):** A specialized registry envisioned by the NEPHELE project for storing and managing components of Hyper Distributed Applications (HDAGs, VOs, etc.).
    *   **SMO Context:** While the README mentions the Nephele platform works with an HDAR, for SMO's testing purposes, a standard OCI-compliant Distribution registry is used. `hdarctl` is the tool associated with packaging for and interacting with such a registry.
*   **`hdarctl`**
    *   **Definition:** A command-line tool provided by the NEPHELE project.
    *   **SMO Context:** Used by SMO (via `subprocess`) to pull OCI artifacts (containing HDAG descriptors and/or Helm charts) from a registry. Users also use it to package their HDAG components and Helm charts into OCI artifacts and push them to a registry.
*   **Helm**
    *   **Definition:** A package manager for Kubernetes that helps define, install, and upgrade complex Kubernetes applications using "charts."
    *   **SMO Context:** SMO uses Helm (via its CLI) as the primary mechanism to deploy individual services of an HDAG onto Kubernetes clusters managed by Karmada. Service configurations and placement decisions are passed as Helm values overrides.
*   **Helm Chart**
    *   **Definition:** A collection of files that describe a related set of Kubernetes resources, packaged by Helm.
    *   **SMO Context:** Individual services within an HDAG are expected to be packaged as Helm charts. These charts are then deployed by SMO.
*   **Hop3**
    *   **Definition:** An open-source orchestration platform developed by Abilian, described as "your own PaaS," designed for deploying and managing distributed applications with a focus on flexibility, security, and ease of use.
    *   **SMO Context:** Abilian's role in NEPHELE involves integrating Hop3 with SMO to enhance overall orchestration capabilities, combining Hop3's deployment mechanisms with SMO's advanced multi-cluster orchestration and optimization.
*   **Hyper Distributed Application (HDA)**
    *   **Definition (SMO/NEPHELE Concept):** An application distributed on a significantly large and complex scale, typically spanning multiple Kubernetes clusters, geographical regions, and potentially heterogeneous environments, with intricate interdependencies.
    *   **SMO Context:** The type of application SMO is designed to orchestrate.

**I**

*   **Intent Formulation / Intent-Based System**
    *   **Definition:** A system where users declare their desired end state or high-level goals ("what" they want) rather than specifying the exact low-level steps to achieve it ("how").
    *   **SMO Context:** SMO aims to be an intent-based system. Users provide an "intent formulation" (likely an HDAG descriptor with high-level requirements like "Service A needs to be highly available in Europe"). SMO then translates this intent into a concrete deployment plan. The `utils.intent_translation.py` file shows a basic form of this by mapping abstract terms like 'light' CPU to concrete values.
*   **IoT (Internet of Things)**
    *   **Definition:** A network of physical devices, vehicles, home appliances, and other items embedded with electronics, software, sensors, actuators, and connectivity which enables these objects to connect and exchange data.
    *   **SMO Context:** NEPHELE, the parent project, has a strong focus on IoT, and SMO is designed to orchestrate applications that might include IoT components or process IoT data, potentially spanning from IoT devices to the edge and cloud.
*   **Insecure Registry**
    *   **Definition:** A container image registry that communicates over HTTP instead of HTTPS, or uses self-signed certificates.
    *   **SMO Context:** For local development and testing, SMO supports using an insecure registry. Both Docker and containerd need to be configured to trust it. The `INSECURE_REGISTRY` config flag in SMO enables the `--plain-http` option for Helm.

**J**

*   **JSON (JavaScript Object Notation)**
    *   **Definition:** A lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate.
    *   **SMO Context:** Used for API request/response bodies and for storing structured data in the PostgreSQL database via the JSONB type (e.g., `graph_descriptor`, `placement`, `values_overwrite`).
*   **JSONB**
    *   **Definition (PostgreSQL):** A binary JSON data type in PostgreSQL that stores JSON data in a decomposed binary format, which is faster to process and supports indexing.
    *   **SMO Context:** Used for several columns in SMO's database models (`Graph`, `Service`) to efficiently store and query structured but flexible data like HDAG descriptors and Helm value overrides.

**K**

*   **Karmada**
    *   **Definition:** An open-source (CNCF) multi-cluster Kubernetes management system. It provides a unified control plane to manage applications across multiple Kubernetes clusters.
    *   **SMO Context:** A critical prerequisite and component for SMO. SMO uses Karmada as its "execution engine" to deploy and manage application components (via Helm) across various member Kubernetes clusters. SMO interacts with Karmada's API (via `KarmadaHelper`) to get cluster information and manage deployments.
*   **Kubeconfig**
    *   **Definition (Kubernetes):** A file used to configure access to Kubernetes clusters. It contains information about clusters, users, namespaces, and authentication mechanisms.
    *   **SMO Context:** SMO requires paths to `KARMADA_KUBECONFIG` (for the Karmada control plane) and `SUBMARINER_KUBECONFIG` (for Submariner, likely the broker's kubeconfig) to be configured. These are used by the Kubernetes Python client.
*   **Kubernetes**
    *   **Definition:** An open-source container orchestration platform for automating the deployment, scaling, and management of containerized applications.
    *   **SMO Context:** The target environment for the applications SMO orchestrates. SMO itself runs as a containerized application and interacts heavily with Kubernetes APIs (primarily through Karmada).
*   **`kubectl`**
    *   **Definition:** The command-line tool for interacting with Kubernetes clusters.
    *   **SMO Context:** While SMO uses the Kubernetes Python client for programmatic interaction, `kubectl` is essential for users to inspect the state of Karmada, member clusters, and deployed resources.

**L**

*   **Lifecycle Management**
    *   **Definition:** The process of managing an application or system through all its stages, from initial deployment to ongoing operation, updates, scaling, and eventual decommissioning.
    *   **SMO Context:** SMO provides lifecycle management for HDAGs, including deploying, starting, stopping, scaling, triggering re-placement, and removing them.

**M**

*   **Meta-Orchestrator**
    *   **Definition:** An orchestrator that manages or coordinates other orchestrators or complex systems.
    *   **SMO Context:** SMO acts as a meta-orchestrator because it doesn't directly manage individual pods on specific nodes. Instead, it orchestrates Karmada (which in turn orchestrates deployments on member clusters) and potentially an NFVCL (which orchestrates the creation of Kubernetes clusters on VIMs).
*   **Microservices**
    *   **Definition:** An architectural style that structures an application as a collection of small, autonomous services, modeled around a business domain.
    *   **SMO Context:** HDAGs are typically composed of multiple services, which are often implemented as microservices, each packaged (e.g., as a Helm chart) and deployed by SMO.
*   **MILP (Mixed-Integer Linear Program)**
    *   **Definition:** A type of optimization problem where some decision variables are constrained to be integers, while others can be continuous, and the objective function and constraints are linear.
    *   **SMO Context:** The placement and scaling problems solved by CVXPY in SMO are formulated as MILPs, given the boolean (placement decisions) and integer (replica counts) variables.

**N**

*   **Namespace (Kubernetes)**
    *   **Definition:** A way to divide cluster resources between multiple users or projects. Resources within one namespace are isolated from resources in other namespaces.
    *   **SMO Context:**
        *   The Prometheus CRDs are recommended to be installed in a `monitoring` namespace.
        *   HDAGs are deployed into a specific `project` (which acts as a namespace in Karmada/Kubernetes).
        *   Submariner often uses a `submariner-k8s-broker` namespace.
*   **NEPHELE**
    *   **Definition:** The larger European research and innovation project of which SMO is a component. NEPHELE aims to create an open reference architecture for orchestrating hyper-distributed applications across the IoT-edge-cloud continuum.
    *   **SMO Context:** SMO is the "synergetic meta-orchestrator" developed within NEPHELE. `hdarctl` and concepts like HDAR also originate from this project.
*   **NFV (Network Function Virtualization)**
    *   **Definition:** An initiative to virtualize network services (like firewalls, load balancers, routers) so they can run as software on standard IT infrastructure (servers, switches, storage) instead of proprietary hardware.
    *   **SMO Context:** Relevant because of the NFVCL integration.
*   **NFVCL (Network Function Virtualization Cluster Lifecycle manager)**
    *   **Definition (SMO Context):** An external system/API that SMO can interact with to automate the provisioning, management, and deletion of Kubernetes clusters, typically on IaaS platforms like OpenStack, often for hosting VNFs or other distributed applications.
    *   **SMO Context:** An optional integration. If configured with an `NFVCL_BASE_URL`, SMO can make API calls to request new Kubernetes clusters or manage existing ones (see `src/routes/nfvcl/` and `src/services/nfvcl/`).
*   **Node (Kubernetes)**
    *   **Definition:** A worker machine in a Kubernetes cluster where containers (as part of Pods) are run.
    *   **SMO Context:** SMO's placement algorithms decide which cluster (a collection of nodes) will host services, implicitly managing load across nodes within those clusters via Kubernetes' own scheduling.

**O**

*   **Observability**
    *   **Definition:** The ability to measure the internal states of a system by examining its outputs (logs, metrics, traces).
    *   **SMO Context:** SMO strongly promotes observability by automatically generating Grafana dashboards and integrating with Prometheus for metrics and alerts.
*   **OCI (Open Container Initiative)**
    *   **Definition:** A project that develops open industry standards around container formats and runtimes.
    *   **SMO Context:** SMO deals with OCI artifacts (for HDAGs and services) and OCI-compliant registries.
*   **OpenAPI Specification (formerly Swagger Specification)**
    *   **Definition:** A standard, language-agnostic interface description for RESTful APIs, which allows both humans and computers to discover and understand the capabilities of a service without access to source code or documentation.
    *   **SMO Context:** Flasgger generates an OpenAPI spec for the SMO API, making it explorable via the Swagger UI.
*   **OpenStack**
    *   **Definition:** A free, open-standard cloud computing platform, primarily deployed as Infrastructure-as-a-Service (IaaS) in both public and private clouds.
    *   **SMO Context:** The primary IaaS platform targeted by SMO's NFVCL integration for dynamic Kubernetes cluster provisioning.
*   **Optimization Problem**
    *   **Definition:** The problem of finding the best solution from all feasible solutions, typically by maximizing or minimizing an objective function subject to a set of constraints.
    *   **SMO Context:** SMO formulates its service placement and replica scaling tasks as optimization problems, solved using CVXPY.
*   **Orchestration**
    *   **Definition:** The automated configuration, coordination, and management of computer systems and software.
    *   **SMO Context:** SMO is a "meta-orchestrator," coordinating Karmada and potentially NFVCL to manage the end-to-end deployment and lifecycle of HDAGs.
*   **ORM (Object-Relational Mapper)**
    *   **Definition:** A programming technique for converting data between incompatible type systems using object-oriented programming languages. It creates a "virtual object database" that can be used from within the programming language.
    *   **SMO Context:** SQLAlchemy is the ORM used by SMO to interact with its PostgreSQL database, allowing developers to work with Python `Model` objects instead of writing raw SQL.

**P**

*   **PaaS (Platform as a Service)**
    *   **Definition:** A cloud computing model where a third-party provider delivers hardware and software tools—usually those needed for application development—to users as a service.
    *   **SMO Context:** Hop3, which integrates with SMO, is described as "your own PaaS."
*   **Placement (Service Placement)**
    *   **Definition (SMO Context):** The process and result of deciding which Kubernetes cluster(s) each service component of an HDAG should be deployed to.
    *   **SMO Context:** A core function of SMO, performed by algorithms in `utils/placement.py` (both a naive initial placement and a CVXPY-based optimization). The result is stored in the `Graph` model's `placement` field.
*   **Pod (Kubernetes)**
    *   **Definition:** The smallest and simplest unit in the Kubernetes object model that you create or deploy. A Pod represents a running process on your cluster and can contain one or more containers.
    *   **SMO Context:** Services deployed by SMO run as Pods (managed by Deployments) within Kubernetes clusters.
*   **Point of Presence (POP / pop_area)**
    *   **Definition:** An access point or location where multiple networks or communication devices share a connection. In cloud contexts, it often refers to a data center or geographical region.
    *   **SMO Context:** Used in the NFVCL integration to specify the location/area for VIMs and Kubernetes cluster provisioning. Appears in `VIM` and `OS_K8S_cluster` models.
*   **Prometheus**
    *   **Definition:** An open-source systems monitoring and alerting toolkit, widely used with Kubernetes. It collects metrics from configured targets, evaluates rule expressions, displays results, and can trigger alerts if some condition is observed to be true.
    *   **SMO Context:** A critical component.
        *   SMO queries Prometheus (via `PrometheusHelper`) for metrics (request rates, CPU utilization) that drive its scaling algorithm.
        *   SMO creates Prometheus alert rules (via `PrometheusHelper`) to enable conditional service deployment.
        *   The Prometheus Operator CRDs are a prerequisite for some of these functionalities.
*   **Prometheus Operator**
    *   **Definition:** A Kubernetes operator that simplifies the deployment and management of Prometheus, Alertmanager, and related monitoring components on Kubernetes. It introduces CRDs like `ServiceMonitor` and `PrometheusRule`.
    *   **SMO Context:** If Prometheus monitoring is desired using ServiceMonitors, or if SMO's conditional deployment via Prometheus alerts is used, the Prometheus Operator and its CRDs need to be installed in the Karmada control plane (or relevant clusters). SMO directly manages `PrometheusRule` CRs.
*   **PromQL (Prometheus Query Language)**
    *   **Definition:** The powerful query language used by Prometheus to select and aggregate time-series data.
    *   **SMO Context:** Embedded within `PrometheusHelper` (for metrics) and used in the alert definitions created by SMO for conditional deployments.
*   **Propagation Policy (Karmada)**
    *   **Definition:** A Karmada custom resource that defines how a Kubernetes resource (like a Deployment or Service) should be propagated (distributed) to member clusters.
    *   **SMO Context:** While not directly creating PropagationPolicy YAMLs in the code shown, SMO's use of Helm via Karmada implies that Karmada's propagation mechanisms (which use these policies) are leveraged under the hood to distribute the Helm releases to the target clusters determined by SMO's placement algorithm.

**R**

*   **RBAC (Role-Based Access Control)**
    *   **Definition (Kubernetes):** A method of regulating access to computer or network resources based on the roles of individual users within an enterprise.
    *   **SMO Context:** The SMO service account/pod will need appropriate RBAC permissions in the Karmada control plane (and potentially member clusters) to perform its actions (e.g., read cluster info, manage deployments via Karmada, manage `PrometheusRule` CRs in the `monitoring` namespace).
*   **REST (Representational State Transfer)**
    *   **Definition:** An architectural style for designing networked applications, relying on a stateless, client-server, cacheable communications protocol—typically HTTP.
    *   **SMO Context:** SMO provides a REST API for all its functionalities.
*   **Registry**
    *   See **Artifact Registry**.

**S**

*   **Scaling (Service Scaling)**
    *   **Definition:** The process of adjusting the number of running instances (replicas) of a service or application to meet demand, improve performance, or optimize resource usage.
    *   **SMO Context:** A core function of SMO. It uses a CVXPY-based optimization algorithm (`utils/scaling.decide_replicas`) driven by Prometheus metrics and service performance models to dynamically adjust the replica count of services within an HDAG. This is performed in background threads.
*   **Service (Kubernetes)**
    *   **Definition:** An abstract way to expose an application running on a set of Pods as a network service.
    *   **SMO Context:** Individual components of an HDAG are typically exposed as Kubernetes Services (defined within their Helm charts). SMO manages the deployment of these services.
*   **Service (SMO Model)**
    *   **Definition:** A database model in SMO representing a single component or microservice within a Hyper Distributed Application Graph.
    *   **SMO Context:** Stores metadata about the service, its artifact, deployment intent, current status, placement, and links it to its parent `Graph`.
*   **Service Import/Export (Submariner)**
    *   **Definition:** A Submariner feature that allows services running in one Kubernetes cluster to be discovered and accessed by Pods in other connected clusters.
    *   **SMO Context:** The `create_service_imports` function in `graph_service.py` analyzes HDAG connection points and generates `serviceImportClusters` Helm values. This likely configures Submariner ServiceExports/Imports to enable the necessary cross-cluster communication for the HDAG.
*   **ServiceMonitor (Prometheus Operator CRD)**
    *   **Definition:** A Prometheus Operator CRD that declaratively specifies how groups of Kubernetes services should be monitored by Prometheus.
    *   **SMO Context:** If Helm charts for services include `ServiceMonitor` definitions, installing the Prometheus CRDs (as mentioned in prerequisites) allows Prometheus to automatically discover and scrape metrics from these services.
*   **SLO (Service Level Objective)**
    *   **Definition:** A target value or range of values for a service level indicator (SLI), such as availability or latency.
    *   **SMO Context:** The scaling algorithm's constraint `alpha[s] * r_current[s] + beta[s] >= request_rates[s]` acts like an SLO. It ensures that the deployed capacity (modeled by `alpha * replicas + beta`) is sufficient to handle the observed `request_rates`.
*   **SQLAlchemy**
    *   **Definition:** A Python SQL toolkit and Object-Relational Mapper (ORM) that gives application developers the full power and flexibility of SQL.
    *   **SMO Context:** Used as the ORM to interact with the PostgreSQL database, defining models and handling database sessions (`db` object initialized in `models/__init__.py`).
*   **Submariner**
    *   **Definition:** An open-source project that enables direct L3 network connectivity between Pods and Services in different Kubernetes clusters, whether on-premises or in the cloud.
    *   **SMO Context:** A prerequisite for SMO. SMO uses `SubmarinerHelper` to get cluster network CIDR information. More importantly, SMO relies on Submariner (configured independently) to provide the underlying network fabric that allows services within an HDAG, potentially deployed across different clusters, to communicate with each other as specified by `serviceImportClusters`.
*   **`subprocess` (Python module)**
    *   **Definition:** A standard Python module used to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.
    *   **SMO Context:** Used to execute external CLI commands like `helm` and `hdarctl`.
*   **Swagger / Swagger UI**
    *   **Definition:** Swagger is a set of open-source tools built around the OpenAPI Specification that can help design, build, document, and consume REST APIs. Swagger UI provides a web interface to explore and interact with an API documented with OpenAPI.
    *   **SMO Context:** Flasgger integrates Swagger into the SMO Flask app, making the API explorable at the `/docs` endpoint.

**T**

*   **Threading (Python)**
    *   **Definition:** A way to achieve concurrency by allowing multiple parts of a program to run apparently simultaneously.
    *   **SMO Context:** Used in `graph_service.py` to run the `scaling_loop` for each managed graph/cluster in a separate background thread, allowing continuous, non-blocking monitoring and scaling adjustments.
*   **Translation (Intent Translation)**
    *   See **Intent Formulation**.

**V**

*   **Values Overwrite (Helm)**
    *   **Definition:** A mechanism in Helm to override default values defined in a chart's `values.yaml` file, typically by providing a custom YAML file or command-line flags during `helm install` or `helm upgrade`.
    *   **SMO Context:** SMO dynamically generates `values_overwrite` data (stored as JSONB in the `Service` model). This is crucial for injecting placement decisions (`clustersAffinity`), service import configurations (`serviceImportClusters`), and other SMO-determined parameters into the Helm charts of deployed services.
*   **VIM (Virtual Infrastructure Manager)**
    *   **Definition (SMO/NFVCL Context):** The platform that manages the underlying virtualized hardware resources (compute, storage, network). Typically, this refers to an IaaS platform like OpenStack.
    *   **SMO Context:** SMO, via an NFVCL, can request the provisioning of Kubernetes clusters on infrastructure managed by a VIM. SMO stores VIM details (e.g., OpenStack API endpoint, credentials – though credentials themselves are used by NFVCL, not stored directly by SMO long-term for API calls) to facilitate these requests. Defined in the `VIM` model and managed through routes in `src/routes/nfvcl/vim.py`.
*   **VO (Virtual Object / Virtualized Object)**
    *   **Definition (NEPHELE Context):** A concept within the NEPHELE project related to the "VOStack," a software stack for virtualizing IoT devices and functions at the edge. A VO likely represents a virtualized instance of an IoT device or function.
    *   **SMO Context:** The term "voChartOverwrite" appears in `graph_service.py` when handling services with an `implementer == 'WOT'` (Web of Things). This suggests that some services deployed by SMO might be VOs from the NEPHELE VOStack, and their Helm charts might have a specific structure requiring overrides in a `voChartOverwrite` section.
*   **VOStack**
    *   **Definition (NEPHELE Context):** A multi-layered lightweight software stack developed by the NEPHELE project for virtualization of IoT devices and functions at the edge, aiming to tackle IoT technologies convergence and interoperability.
    *   **SMO Context:** Services deployed by SMO might be based on or interact with components from the VOStack, especially if they are `WOT` (Web of Things) implementers.

**W**

*   **WOT (Web of Things)**
    *   **Definition:** A set of standards and practices aimed at integrating smart things (IoT devices) into the World Wide Web, typically by giving them REST APIs and standard data models.
    *   **SMO Context:** Mentioned as an `artifact_implementer` type in `graph_service.py`. Services implemented using WOT principles might have specific Helm chart structures (e.g., requiring `voChartOverwrite`) that SMO accounts for.

**Y**

*   **YAML (YAML Ain't Markup Language)**
    *   **Definition:** A human-readable data serialization standard that is often used for configuration files and in applications where data is being stored or transmitted.
    *   **SMO Context:**
        *   HDAG descriptors are typically written in YAML.
        *   Helm charts heavily use YAML for defining Kubernetes resources and chart values.
        *   SMO uses `pyyaml` to parse YAML input and to dump Helm `values_overwrite` files.
        *   Swagger/OpenAPI specifications for API documentation are often written in YAML.
