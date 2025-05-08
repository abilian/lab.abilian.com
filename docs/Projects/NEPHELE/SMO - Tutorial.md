## Abstract

This tutorial serves as a comprehensive guide for newcomers to the Synergetic Meta-Orchestrator (SMO), a system designed to simplify the deployment and management of complex, Hyper Distributed Applications (HDAs) across multiple Kubernetes clusters. Recognizing that the official README can be dense for those unfamiliar with its specialized concepts, this tutorial aims to bridge that gap by elucidating core SMO terminologies such as Hyper Distributed Application Graphs (HDAGs) and intent formulations. It explains SMO's role as a high-level orchestrator that leverages underlying technologies like Karmada for multi-cluster execution and Submariner for inter-cluster communication.

The guide walks users through a practical, hands-on example—the "Brussels Demo"—to illustrate SMO's workflow, from configuring a local development environment and starting SMO, to deploying a sample HDA. While this tutorial focuses primarily on the SMO's interaction patterns and its value proposition in abstracting multi-cluster complexity, it acknowledges that setting up the prerequisite Kubernetes, Karmada, and Submariner environment can be a significant undertaking for users and thus assumes a foundational layer is either pre-existing or will be established separately. By following this tutorial, users will gain a functional understanding of SMO's capabilities and be equipped to explore its more advanced features.

---

## Introduction

This is a tutorial for the Synergetic Meta-Orchestrator (SMO). This tutorial will guide you through understanding what SMO is, why it's useful, and how to take your first steps with it.

**Goal of this Tutorial:**

By the end, you'll understand:

1.  What problem SMO solves.
2.  The core concepts: Hyper Distributed Applications (HDAs), HDAGs, and Intent Formulations.
3.  How SMO uses tools like Karmada.
4.  How to run the provided "Brussels Demo" example.

**Who is this for?**

Anyone who needs to manage complex applications spread across multiple locations or Kubernetes clusters and wants a higher-level way to do it. You don't need to be a Kubernetes expert to start, but familiarity with containers (like Docker) will be helpful.

## Part 1: The "Why" - What Problem Does SMO Solve?

Imagine you're building a massive online service – maybe a global e-commerce platform, a worldwide logistics tracker, or a large-scale IoT data processor. Your application isn't just one program; it's a collection of many smaller services (microservices) that need to work together.

Now, imagine these services need to run:

*   In different data centers around the world (Europe, Asia, North America) for low latency.
*   Across various Kubernetes clusters (some on public cloud, some private).
*   With complex connections and dependencies between them.
*   And they need to scale up or down automatically based on demand.

Managing all of this manually is a nightmare! This is where the SMO steps in.

**The SMO is designed to be the "brain" that simplifies deploying and managing these super-complex, widely spread applications (which we call Hyper Distributed Applications or HDAs).**

Instead of telling Kubernetes *exactly how* to run every little piece in every location, you tell the SMO *what you want your overall application to look like and how it should behave (your "intent")*. The SMO then figures out the "how" and uses other tools to make it happen.

## Part 2: Understanding the Lingo - Core SMO Concepts

Let's break down those key terms from the README:

1.  **Hyper Distributed Application (HDA):**
    *   Think of this as your entire complex, globally-spread application system.
    *   It's "hyper" distributed because its components are likely running across *multiple Kubernetes clusters*, potentially in different geographical regions, and have intricate interdependencies.
    *   **Analogy:** If a small local website is a "distributed application," then Netflix (with servers everywhere) is a "hyper-distributed application."

2.  **Hyper Distributed Application Graph (HDAG):**
    *   This is SMO's *blueprint* or *model* of your HDA.
    *   It's a "graph" because it shows:
        *   **Nodes:** The individual services or components of your HDA.
        *   **Edges:** The connections and dependencies between these services.
    *   The HDAG also includes information about where components *could* or *should* run, and what resources they need.
    *   **Analogy:** If your HDA is the running Netflix service, the HDAG is the detailed architectural diagram showing all its parts and how they connect.
    *   The `hdarctl` tool (mentioned in the README) is likely used to package these HDAG definitions along with the Helm charts that define how each individual service in the graph should run.

3.  **Intent Formulation:**
    *   This is how *you* tell SMO what you want. It's a high-level description of your desired HDA.
    *   Instead of writing tons of complex Kubernetes YAML for every cluster, you provide an "intent."
    *   **Examples of what an intent might say (conceptually):**
        *   "Deploy my 'GlobalStore' application."
        *   "The 'GlobalStore' has a 'ProductCatalog' service, an 'OrderProcessing' service, and a 'UserAccounts' service."
        *   "Ensure 'ProductCatalog' is fast for users in Europe and North America."
        *   "The 'OrderProcessing' service needs to be robust and have at least 3 copies running."
    *   **Format:** The README doesn't specify the exact file format (it's likely YAML or JSON). You'll see it in action in the demo's `create-existing-artifact.sh` script, which sends this intent to the SMO API.
    *   SMO reads your intent and translates it into a concrete plan.

See [[SMO - Key Concepts]] and [[SMO - Glossary]] for more detail.

## Part 3: The SMO's Ecosystem - How It Works with Other Tools

The SMO doesn't do everything alone. It orchestrates other powerful tools:

*   **Karmada:**
    *   Think of Karmada as a "Kubernetes of Kubernetes." It allows you to manage applications across *multiple* Kubernetes clusters from a single control point.
    *   **The SMO's Role:** The SMO decides *what* services from your HDAG go to *which* clusters.
    *   **Karmada's Role:** The SMO then tells Karmada, "Deploy service X to cluster A and service Y to cluster B with these settings." Karmada carries out these instructions.
    *   So, the SMO is the strategic planner; Karmada is the fleet commander executing the deployment plan across your clusters.

*   **Submariner:**
    *   When your application components are running in different Kubernetes clusters, they need a way to talk to each other. Submariner creates secure network connections between these clusters.
    *   The SMO relies on Submariner (implicitly) so that the distributed parts of your HDAG can communicate seamlessly.

*   **NFVCL (Optional Integration):**
    *   Imagine your intent says, "I need a new, dedicated cluster in Asia for this part of my application."
    *   If an NFVCL (Network Function Virtualization Cluster Lifecycle manager) is set up (often with OpenStack), The SMO can ask the NFVCL to automatically create that new Kubernetes cluster for you. This is for dynamic infrastructure provisioning.

**The Core SMO Workflow:**

1.  **You (the User):** Define your **Intent Formulation** (what your HDA should look like and do) and package your application components (e.g., as Helm charts within an HDAG definition using `hdarctl`).
2.  **SMO:**
    *   **Translates** your intent.
    *   **Constructs a deployment plan** for your HDAG (deciding where each piece goes, how many copies, etc.).
    *   **Enforces** this plan by giving instructions to Karmada.
3.  **Karmada:** Deploys and manages the application components on the actual Kubernetes clusters.
4.  **SMO (Ongoing):** Monitors the application (e.g., using Prometheus) and can make adjustments (like scaling) based on the initial intent and current conditions.

See [[SMO - Key Concepts]] and [[SMO - Architecture]] for more details.

## Part 4: Getting Your Hands Dirty - The Brussels Demo

Now for the fun part! Let's try to run the example provided with the SMO. This will make the concepts much clearer.

**What the Brussels Demo Does (Conceptual):**
It deploys a sample Hyper Distributed Application, likely consisting of a few microservices. These services will be pushed as Docker images to a local registry, their Helm charts (packaged as OCI artifacts) will also go to this registry, and then SMO will be instructed to deploy this application graph based on a descriptor.

**Prerequisites (Simplified for this Tutorial):**

*   **Docker and Docker Compose:** You need these installed to run SMO and the local registry.
*   **`kubectl`:** To interact with Kubernetes (though for the demo, SMO and Karmada handle most of this).
*   **`hdarctl`:** Make sure you've downloaded it and it's in your `PATH` as per the README.
    ```bash
    wget https://gitlab.eclipse.org/eclipse-research-labs/nephele-project/nephele-development-sandbox/-/raw/main/tools/hdarctl
    sudo chmod u+x hdarctl
    sudo mv hdarctl /usr/local/bin
    ```
*   **A working Kubernetes environment with Karmada and Submariner.** *This tutorial won't cover setting up Karmada and Submariner from scratch, as that's a more involved process. For now, let's assume you have this environment, or you're focusing on understanding the SMO's interaction with the demo's pre-packaged elements.* If you don't, you can still follow along with the registry and the SMO setup to see those parts work.
*   **Prometheus CRDs (Optional but Recommended for full demo):** If you want ServiceMonitors to work, install these as per the README. If not, you can skip or (as a last resort for the demo) the Helm charts might need to have `servicemonitor.yaml` files removed/disabled.

**Step 1: Configure your Local Environment for an Insecure Registry**

The SMO and Kubernetes need to be able to pull images from a local registry running on your machine. This registry will be "insecure" (HTTP, not HTTPS) for simplicity in a local test environment.

*   **Find Your Host IP (`<Host-IP>`):** This is the IP address of your main machine (e.g., your laptop or server where you are running Docker). It should be an IP reachable by your Kubernetes nodes if they are on different machines/VMs. If everything (Docker, K8s via minikube/kind) is on the same machine, `127.0.0.1` or your local network IP (e.g., `192.168.1.X`) might work. Let's assume it's `192.168.1.100` for this example. **Replace `192.168.1.100` with your actual IP.**

*   **A. Configure Docker Daemon:**
    1.  Edit/create `/etc/docker/daemon.json`:
        ```json
        {
          "insecure-registries" : ["192.168.1.100:5000"]
        }
        ```
    2.  Restart Docker: `sudo systemctl restart docker`

*   **B. Configure Containerd (on your Kubernetes Nodes):**
    *If your Kubernetes nodes are separate from the machine running the registry, you need to do this on each node.*
    1.  Modify `/etc/containerd/config.toml` to ensure `config_path` is set:
        ```toml
        [plugins."io.containerd.grpc.v1.cri".registry]
          config_path = "/etc/containerd/certs.d"
        ```
    2.  Create directories:
        ```bash
        sudo mkdir -p /etc/containerd/certs.d/192.168.1.100:5000
        ```
    3.  Create `/etc/containerd/certs.d/192.168.1.100:5000/hosts.toml`:
        ```toml
        server = "http://192.168.1.100:5000"
        [host."http://192.168.1.100:5000"]
          capabilities = ["pull", "resolve", "push"]
          skip_verify = true
        ```
    4.  Restart Containerd: `sudo systemctl restart containerd`

**Step 2: Start the Local Container/Artifact Registry**

Navigate to the SMO project directory in your terminal.

```bash
# From the root of the SMO project
docker compose -f registry/docker-compose.yaml up -d
```
This starts a registry listening on port `5000` of your host.

**Step 3: Configure and Start the SMO**

1.  **Configuration:**
    *   Go to the `config/` directory.
    *   **Database:** `flask.env` and `postgres.env` should have matching `POSTGRES_USER`, `POSTGRES_PASSWORD`, `POSTGRES_DB`. The defaults are usually fine for a local test.
    *   **Karmada:** In `config/flask.env`, ensure `KARMADA_KUBECONFIG` points to the *name* of your Karmada kubeconfig file (e.g., `karmada-apiserver.config`). The `docker-compose.yaml` for SMO mounts your `~/.kube` directory, so the file should be in there.
        ```env
        # Example line in config/flask.env
        KARMADA_KUBECONFIG=karmada-apiserver.config
        ```

2.  **Start the SMO:**
    ```bash
    # From the root of the SMO project
    docker compose up -d
    ```
    This starts the SMO API server and its PostgreSQL database.
    You can check logs: `docker compose logs -f smo` (or `flask-smo-1` if that's the container name).

3.  **Access SMO API Docs:** Open `http://localhost:8000/docs` in your browser. You should see the Swagger UI for the SMO API. This confirms SMO is running!

**Step 4: Prepare and Run the Brussels Demo**

1.  **Navigate to the demo directory:**
    ```bash
    cd examples/brussels-demo
    ```

2.  **Configure IPs in the Demo:**
    *   Open the `Makefile` in this directory.
    *   Look for a variable that represents your host IP (the `<Host-IP>` you used for the insecure registry, e.g., `192.168.1.100`). It might be called `HOST_IP` or similar, or you might need to edit commands directly. **Ensure this IP is correctly set.** This IP is used to:
        *   Tag Docker images so Kubernetes knows to pull them from `your-ip:5000`.
        *   Update Helm chart values so services know how to reach the registry or each other.

3.  **Build and Push Docker Images:**
    ```bash
    make push-images
    ```
    This command (defined in the `Makefile`) will:
    *   Build Docker images for the demo application's services (from Dockerfiles in the demo).
    *   Tag them with `<Host-IP>:5000/image-name`.
    *   Push them to your local registry running at `<Host-IP>:5000`.

4.  **Update Helm Charts and Descriptor with IPs:**
    ```bash
    make change-ips
    ```
    This likely updates placeholders in the Helm charts and any HDAG descriptor file with your `<Host-IP>`, so the deployed services point to the correct registry.

5.  **Package and Push Helm Chart OCI Artifacts:**
    ```bash
    make push-artifacts
    ```
    This will:
    *   Use `hdarctl` to package the Helm charts for the demo services into OCI artifact `.tar.gz` files.
    *   Use `hdarctl` to push these OCI artifacts to your local registry (e.g., `http://<Host-IP>:5000/brussels-demo/...`).

6.  **Prepare and Run the Deployment Script:**
    *   Open `create-existing-artifact.sh`.
    *   **Inspect it carefully!** This script is what actually sends the "intent formulation" to the SMO API to deploy your HDAG.
    *   Look for variables like registry URLs, project names, artifact names. Ensure they match your `<Host-IP>:5000` and the artifacts you just pushed.
        *   For example, a variable like `HDAG_URL` might need to be `oci://<Host-IP>:5000/brussels-demo/graph-descriptor` (this is a guess, the actual name will be in the script or Makefile output).
    *   Once you're confident in the script's variables:
        ```bash
        ./create-existing-artifact.sh
        ```

7.  **Monitor Deployment:**
    *   Check the SMO logs: `docker compose logs -f smo`
    *   Use `kubectl` (configured for your Karmada control plane) to see if Karmada is creating resources (`PropagationPolicies`, `ClusterPropagationPolicies`, etc.).
    *   Use `kubectl` (configured for your member clusters) to see if pods are running.
    *   Check the SMO API (e.g., via Swagger UI or `curl`) for the status of the deployed graph.

**Step 5: Clean Up (Optional)**

*   The demo probably has a `delete.sh` script or a `make delete-graph` target.
    ```bash
    ./delete.sh # Or whatever the delete script is named
    ```
*   Stop SMO and its database:
    ```bash
    # From the root of the SMO project
    docker compose down
    ```
*   Stop the local registry:
    ```bash
    # From the root of the SMO project
    docker compose -f registry/docker-compose.yaml down -v # -v removes the volume
    ```

## Part 5: What Next?

Congratulations! If you've gotten this far, you've taken significant steps into understanding and using the SMO.

*   **Explore the SMO API:** Use the Swagger UI (`http://localhost:8000/docs`) to see what other operations the SMO supports.
*   **Dive into the Code:** The `src/` directory contains the SMO's Flask application. `routes/` and `services/` are good places to start understanding its logic.
*   **Modify the Demo:** Try changing the number of replicas for a service in the demo's HDAG descriptor (or intent) and redeploying.
*   **Understand the "Intent":** Look closely at how the `create-existing-artifact.sh` script (and any YAML/JSON it uses) defines the HDAG and its deployment characteristics. This is the "intent formulation" in action.

## Key Takeaways:

*   The SMO simplifies managing complex, **Hyper Distributed Applications (HDAs)**.
*   It uses a blueprint called a **Hyper Distributed Application Graph (HDAG)**.
*   You tell SMO *what* you want via an **Intent Formulation**.
*   SMO translates your intent into a plan and uses **Karmada** (and other tools) to execute it across multiple Kubernetes clusters.

This is a complex system, so don't worry if it doesn't all click at once. Experiment with the demo, read the SMO logs, and refer back to the concepts. Good luck!
