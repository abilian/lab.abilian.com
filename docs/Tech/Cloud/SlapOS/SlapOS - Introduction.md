
## Key Characteristics of the System

### Decentralized Cloud Operating System

SlapOS is decentralized, meaning it avoids the pitfalls of single points of failure and can run on a wide variety of hardware setups. It can operate on anything from a network of low-power, personal devices to a large server farm. This makes it an incredibly flexible system suitable for a range of applications.

### Orchestration and Automation

SlapOS handles the orchestration of applications, which means it automates the deployment, scaling, networking, and management of applications. It manages these tasks across clusters of host machines, leveraging the combined power and resources of those machines.

### Application Support

SlapOS can support any application that can run on a Unix-like operating system. This broad compatibility is possible because it uses `buildout`, a Python-based build system, for application deployment. SlapOS can also automate the buildout and deployment processes.

### Resilience and Redundancy

SlapOS' decentralized structure means it doesn't rely on a central "master" node to coordinate its activities. Instead, each node in the network is equal, contributing its resources and sharing the workload. This makes the system more resilient against failures because if one node goes down, others can take over its tasks.

### Resource Allocation and Billing

SlapOS also includes features for resource allocation, accounting, and billing, which are necessary for commercial cloud services. It does this through a process called "billing by the slice," where users are only charged for the resources they use.

### Contribute to Resource Pool

With SlapOS, anyone can contribute their own resources (like storage or processing power) to the network in exchange for compensation. This contributes to the overall resilience and power of the cloud network.

### Edge Computing

With its distributed and decentralized nature, SlapOS is a suitable platform for edge computing. It can operate on the devices at the edge of the network, closer to where the data is generated, which can improve response times and save bandwidth.

## Technical Details

### Key Conventions

#### Software

- Use atomic parameters for instances.
- Ensure backward compatibility during updates.

#### Recipes

- Extend `GenericBaseRecipe` for consistency.
- Fail early and provide meaningful error messages.

#### Components

- Modularize patches and dependencies.
- Use clear, representative naming conventions.

#### Testing

- Integrate Promises in all Software Releases.
- Regularly test with pinned versions and automated systems.

### Understanding SlapOS Buildout

#### Buildout in SlapOS

- Buildout is a Python-based tool for assembling and deploying software.
- It enables repeatable builds, componentization, and automation.
- Essential in SlapOS for defining software installation and instantiation across nodes.

#### Core Features

- Handles versioning and patching to meet application-specific requirements.
- Automates the compilation of binaries and ensures consistent configurations.

#### Key Buildout Concepts

- **Profiles:** Define software parts and their execution order.
- **Recipes:** Python scripts that execute specific tasks, such as installing eggs or compiling binaries.
- **Extensions:** Mechanisms for modularizing configurations by referencing other profiles.

More details in [[Differences Between Upstream Buildout and SlapOS's Variant]].

### Monitoring with Promises

#### What are Promises?

- Python scripts that validate the state of an instance by checking specific conditions.
- Consist of:
    - **Sensors:** Collect monitoring data.
    - **Tests:** Evaluate if the instance state is valid.
    - **Anomaly Detectors:** Identify consistent failures to trigger corrective actions (e.g., `bang`).

#### Implementing Promises

- Use `GenericPromise` as a base class.
- Define methods: `sense`, `test`, and `anomaly`.

#### Advantages

- Promises ensure reliability by monitoring services and triggering recovery processes when necessary.
- Flexible integration with recipes for custom checks.

Note: "Promises" here are related to, but not the same as, promises in computer science: <https://en.wikipedia.org/wiki/Futures_and_promises> & <https://en.wikipedia.org/wiki/Promise_theory>.

### Developing Software Releases

#### Structure

- **Software Profile (`software.cfg`):** Handles software installation.
- **Instance Profile (`instance.cfg.in`):** Manages software instantiation.

#### Best Practices

- Use JSON schemas to define instance parameters.
- Modularize configurations with reusable components and recipes.
- Employ Promises to monitor instance health.

#### Componentization

- Store reusable components in a `component` directory.
- Maintain clear versioning and dependencies for components.

Full tutorial → [[Porting Software to SlapOS - Tutorial]].

### Extending Software Releases

#### Steps

- Modify configuration files (`software.cfg`, `instance.cfg.in`).
- Add new features or components (e.g., log rotation with `cron` and `logrotate`).
- Introduce templates and parameters using Jinja2.

#### Reusability

- Use existing recipes for common tasks (e.g., directory creation, wrapper generation).
- Extend base configurations to build custom solutions.

### Releasing and Upgrading Software

#### Release Process

- Freeze versions (pin eggs and use tags for repositories).
- Generate and validate MD5 checksums.
- Pre-cache resources in Shacache for faster deployment.

#### Testing and Quality Assurance

- Test installation and instantiation rigorously.
- Ensure compliance with conventions (naming, versioning, monitoring).

#### Publication

- Merge development branches into `master`.
- Create a new release tag.
- Add the Software Release to SlapOS automated testing pipelines.

