
## Glossary

### Anomaly

A recurring failure detected by a Promise in SlapOS. When multiple failures are logged over a specified number of tests, the system triggers an alert (called a "bang") to initiate corrective actions. This mechanism ensures that only persistent issues lead to interventions.

### Atomic Parameters

Instance parameters that are granular and independent, ensuring modularity and flexibility. For example, specifying `host` and `port` separately rather than combining them into a single parameter. This approach simplifies configuration management and reduces the risk of conflicts.

### Bang

An automated action triggered by SlapOS in response to anomalies detected by Promises. This action can include restarting instances, reinitializing processes, reporting issues to the Master, or other predefined corrective measures. It is a key part of SlapOS's self-healing capabilities.

### Bang Quota

A limit on the number of "bang" actions a SlapOS partition can trigger within a day. It prevents excessive retries or alerts in case of persistent failures that cannot be automatically resolved, conserving resources and preventing alert fatigue.

### Bootstrap

The initial step of setting up Buildout or SlapOS on a node. It involves creating the necessary environment, downloading essential tools like `bootstrap.py`, and preparing the system for running Buildout configurations.

### Buildout

A powerful, Python-based build system used extensively by SlapOS to define, install, and manage software environments. It uses configuration files (`software.cfg`, `instance.cfg.in`, and others) to automate the setup, configuration, and instantiation of applications. Buildout excels at handling complex dependencies, ensuring reproducibility, and supporting various software components, whether Python-based or not.

### Cache Consistency

The practice of ensuring that all nodes in a SlapOS environment use the same precompiled software and resources from Shacache. This prevents discrepancies between deployments, ensures uniformity, and improves efficiency.

### Component

A reusable building block in SlapOS that provides a specific library, utility, or functionality (e.g., MariaDB, Apache, or a specific Python library). Components are stored in the `component` directory and shared across multiple software profiles, promoting modularity and code reuse.

### Computer Partition

A self-contained, lightweight container within a SlapOS Node. It isolates resources (e.g., storage, configurations, services) to host individual software instances securely and efficiently. Each partition operates independently, minimizing interference between different software deployments on the same node. Also known as a **Software Instance** or simply **Partition**.

### Custom Recipe

A Python class or script written to handle complex or unique configuration tasks in SlapOS that are not covered by standard Buildout recipes. It extends the functionality of Buildout, allowing for greater flexibility and customization.

### Directory Recipe

A predefined recipe in SlapOS (`slapos.cookbook:makedirectory`) used to create directories for storing logs, configuration files, or runtime data in a software instance, ensuring a consistent and organized file structure.

### Dynamic Configuration

A powerful technique in SlapOS where instance parameters or environment-specific values are dynamically injected into templates (using Jinja2) to create tailored configurations during instantiation. This allows for flexible and automated customization of software instances based on specific requirements.

### Eggs

Python packages distributed in `.egg` format. Buildout uses eggs to install Python dependencies as part of a software or instance profile, ensuring that the correct versions of libraries are available.

### Extensions

Additional Buildout functionalities, such as `buildout-versions`, that enhance the management of dependencies, versions, or other aspects of the build process. They extend the capabilities of Buildout beyond its core features.

### Instance Profile

A configuration file (`instance.cfg.in`) that defines how a specific instance of software should behave when deployed within a Computer Partition. It includes instance-specific parameters, dynamic configurations (often using Jinja2 templating), and monitoring logic (via Promises). It acts as a template that is rendered into a final configuration during instantiation.

### Instance-Parameter Section

A section within the `instance.cfg.in` file that defines the default values and configuration parameters for a software instance. These parameters can be overridden when requesting a new instance, allowing for customization.

### Isolation

The ability of SlapOS to run multiple software instances (in separate Computer Partitions) on the same node without interference. This is a crucial feature for security, stability, and efficient resource utilization. Achieved through the use of **Computer Partitions**.

### Jinja2

A powerful and flexible templating engine used extensively in SlapOS to dynamically generate configuration files based on instance parameters. It simplifies configuration management, supports complex logic, and allows for a high degree of customization during instantiation.

### Log Promise

A type of Promise script in SlapOS that checks the health or activity of an application by analyzing its log files for errors or expected patterns. It's a valuable tool for detecting issues that might not be apparent from external metrics.

### Logrotate

A utility integrated into SlapOS to manage application logs. It rotates, compresses, and archives logs to ensure efficient storage usage, prevent overflow, and facilitate log analysis.

### Master

The central management system in SlapOS. It handles node orchestration, monitors software instances, manages the software catalog (list of available Software Releases), and processes requests for new deployments. It's the brain of the SlapOS infrastructure.

### MD5 Checksum

A cryptographic hash used to verify the integrity of downloaded resources in SlapOS, such as during the Buildout process. Each external resource referenced in `software.cfg` must include its MD5 checksum to ensure consistency, security, and prevent the use of corrupted or tampered files.

### Monitoring Plugin

A reusable Promise script integrated into SlapOS via the `slapos.cookbook:promise.plugin` recipe. It provides modular and easily configurable monitoring capabilities that can be shared across different software releases.

### Multi-Instance Deployment

A SlapOS deployment scenario where multiple instances of a software release run on the same or different nodes, each tailored to specific configurations using different Instance Profiles. This allows for scaling and flexibility in deploying software.

### Node

A physical or virtual machine that hosts SlapOS instances. Each node is divided into Computer Partitions, which are managed by the SlapOS Master. Nodes are the fundamental building blocks of the SlapOS infrastructure. Also called **Slave Node**.

### Partition Key

A unique identifier for a Computer Partition, used by SlapOS to manage and reference partitions within nodes. It ensures that each partition can be uniquely addressed within the distributed environment.

### Pinning Versions

The practice of locking specific versions of dependencies (especially Python eggs) in the `[versions]` section of `software.cfg`. This ensures repeatability, prevents unexpected updates that could break compatibility, and guarantees that the same software environment is consistently deployed.

### Process Manager (Supervisor)

A service in SlapOS (often `supervisord`) that manages and monitors the execution of processes within a Computer Partition. It ensures that all services defined for an instance are running, restarts them if they fail, and can trigger alerts (bangs) through the Watchdog mechanism if a process exits unexpectedly.

### Promise

A lightweight monitoring script in SlapOS, typically written in Python. Promises ensure the reliability of software instances by checking specific metrics, such as process health, network connectivity, or application-specific indicators. They are a fundamental part of SlapOS's self-healing and monitoring capabilities.

### Promise-Based Deployment

A core SlapOS principle where every software instance includes at least one Promise to verify its functionality and reliability after deployment. This ensures that instances are continuously monitored and that corrective actions are taken if problems arise.

### Recipe

A Python class within a Buildout configuration that encapsulates a set of instructions for performing a specific task during the build or deployment process. Recipes can be used to download files, compile code, create directories, generate configuration files, and more. SlapOS provides a library of recipes (e.g., `slapos.cookbook:makedirectory`, `slapos.cookbook:wrapper`), and users can create custom recipes to handle specific needs.

### Reusable Component

See **Component**.

### Sense-Test-Anomaly Workflow

The three-phase process used by Promises in SlapOS to monitor the health of instances:

*   **Sense:** Collect system data or metrics relevant to the aspect being monitored.
*   **Test:** Evaluate the collected data to determine the health of the instance based on predefined criteria.
*   **Anomaly:** Trigger corrective actions (e.g., a "bang") if repeated failures are detected, indicating a persistent issue.

### Service Wrapper

A script or binary created by SlapOS (often using the `slapos.cookbook:wrapper` recipe) to start, stop, or restart a service within a SlapOS instance. It often includes parameters such as configuration paths or runtime options specific to the instance.

### Shacache

A distributed cache system used by SlapOS to store precompiled binaries and software resources. It speeds up deployments by avoiding the need to recompile code on each node, ensures consistency across nodes, and reduces the load on external resources.

### SlapOS

An open-source, decentralized cloud operating system that automates the deployment, management, and monitoring of software across distributed infrastructure. It leverages technologies like Buildout, Jinja2, and Promises to provide a robust, flexible, and self-healing platform for deploying and managing applications.

### SlapProxy

A component that can act as a "mini SlapOS Master". The **Webrunner** is an example of a SlapProxy.

### Software Catalog

The list of available Software Releases managed by the SlapOS Master. Users can request instances from this catalog, which acts as a central repository of deployable software.

### Software Directory

The folder containing all the profiles (`software.cfg`, `instance.cfg.in`), components, and templates needed to build and deploy a particular software release in SlapOS.

### Software Instance

A specific deployment of a Software Release within a Computer Partition. Instances are tailored to user requirements using Instance Profiles, which provide instance-specific configurations. Also referred to as a **Computer Partition** or simply **Partition**.

### Software Profile

A configuration file (`software.cfg`) that defines how to install software and its dependencies in SlapOS. It provides the blueprint for creating reusable Software Releases, including information about source code locations, dependencies, build steps, and any necessary patches.

### Software Release

A reusable, versioned package of software created using a Software Profile. It includes all dependencies and installation instructions but lacks instance-specific configurations. Think of it as a template or a blueprint for creating instances of a particular software.

### Static Configuration

A fixed configuration approach where all settings are hardcoded into the instance or software profile. This is the opposite of Dynamic Configuration, offering less flexibility but potentially more simplicity in certain scenarios.

### Template Context

The key-value mapping passed to a Jinja2 template in SlapOS. It provides dynamic data that is used to render configuration files during instantiation, allowing for customized configurations based on instance parameters.

### Testless Promise

A Promise configured only to sense anomalies but not to perform direct tests. It is often used for advanced monitoring setups where the focus is on detecting deviations from expected behavior rather than running explicit tests.

### Watchdog

A simple SlapOS Node feature allowing to watch any process managed by supervisord. All processes scripts into `PARTITION_DIRECTORY/etc/service` directory are watched. They are automatically configured in supervisord with an added `on-watch` suffix on their `process_name`. Whenever one of them exits, watchdog will trigger an alert (bang) that is sent to the Master. Bang will force SlapGrid to reprocess all instances of the service. This also forces recheck of all promises and post the result to master, letting the master decide whether the partition state is Green or Red.

### Webrunner

A development IDE that contains a "mini SlapOS Master" for deploying a single software. Useful for development, testing, and hosting simple software releases due to its resiliency and ability to be patched. Behaves like a **SlapProxy**.

### Wrapper

A script or executable created by SlapOS (often during the Buildout process) to manage the execution of software or services within an instance. Wrappers often include parameters, paths, and environmental variables specific to the instance, providing a consistent interface for starting, stopping, and interacting with services.

### Wrapper Path

The file path to a service wrapper created during the Buildout process, typically defined in the `slapos.cookbook:wrapper` recipe. It specifies the location of the wrapper script that can be used to control a particular service.

### YAML Integration

The optional use of YAML files to define instance parameters or configurations in a structured and human-readable format. While not native to SlapOS, which primarily uses Buildout configuration files, YAML can be converted for compatibility using external tools or custom recipes.

## Relationships between Concepts

Here's a description of how the concepts relate to each other, grouped by category:

**A. Core Architecture:**

*   **SlapOS** is the overarching system that connects everything.
*   **Master** is the central control unit of SlapOS.
*   **Node** (Slave Node) is a server managed by the **Master**.
*   **Computer Partition** (or Software Instance or Partition) is a container on a **Node**.
*   **Webrunner** and **SlapProxy** are like "mini-Masters" or proxies for the Master.

**B. Software Deployment:**

*   **Software Release** is built using a **Software Profile** (`software.cfg`).
*   **Software Instance** is created within a **Computer Partition** based on a **Software Release** and configured by an **Instance Profile** (`instance.cfg.in`).
*   **Software Catalog** is a list of available **Software Releases** managed by the **Master**.
*   **Software Directory** contains all files needed for a **Software Release**.
*   **Component** is a reusable part of a **Software Release**.
*   **Multi-Instance Deployment** involves multiple **Software Instances** of the same **Software Release**.

**C. Build and Configuration (Buildout):**

*   **Buildout** is the build system used by SlapOS.
*   **Software Profile** and **Instance Profile** are **Buildout** configuration files.
*   **Bootstrap** initializes **Buildout** or SlapOS.
*   **Recipe** is a set of instructions used by **Buildout**.
*   **Custom Recipe** extends **Buildout**'s capabilities.
*   **Directory Recipe** is a specific type of **Recipe**.
*   **Wrapper** is created by **Buildout** to manage services.
*   **Service Wrapper** is a specific type of **Wrapper** for managing services.
*   **Wrapper Path** is the location of a **Service Wrapper**.
*   **Eggs** are Python packages used by **Buildout**.
*   **Extensions** enhance **Buildout**'s functionality.
*   **MD5 Checksum** ensures the integrity of files downloaded by **Buildout**.
*   **Pinning Versions** ensures consistent **Buildout** builds.

**D. Monitoring and Reliability (Promises):**

*   **Promise** monitors a **Software Instance**.
*   **Sense-Test-Anomaly Workflow** is the process used by a **Promise**.
*   **Anomaly** is a failure detected by a **Promise**.
*   **Bang** is an action triggered by an **Anomaly**.
*   **Bang Quota** limits the number of **Bangs**.
*   **Monitoring Plugin** is a reusable **Promise** script.
*   **Log Promise** is a type of **Promise** that analyzes logs.
*   **Testless Promise** is a type of **Promise** that only senses anomalies.
*   **Promise-Based Deployment** ensures every instance has a **Promise**.
*   **Watchdog** is a feature that triggers alerts based on process status.

**E. Configuration and Templating:**

*   **Jinja2** is the templating engine used by SlapOS.
*   **Template Context** provides data for **Jinja2** templates.
*   **Dynamic Configuration** uses **Jinja2** to create tailored configurations.
*   **Static Configuration** is hardcoded configuration.
*   **Atomic Parameters** are used in **Dynamic Configuration**.
*   **Instance-Parameter Section** defines parameters in the **Instance Profile**.
*   **YAML Integration** allows the use of YAML for configuration.

**F. Other Important Relationships:**

*   **Isolation** is achieved through **Computer Partitions**.
*   **Process Manager (Supervisor)** manages processes within a **Computer Partition**.
*   **Shacache** stores precompiled binaries used by **Software Releases**.
*   **Cache Consistency** ensures all **Nodes** use the same data from **Shacache**.
*   **Partition Key** uniquely identifies a **Computer Partition**.
*   **Logrotate** manages logs for a **Software Instance**.
