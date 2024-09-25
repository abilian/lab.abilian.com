#nua #public #cloud

## Key info

- Source code: <https://github.com/abilian/nua>
- Doc: <https://nua.rocks/>

## Keywords

- Resilience
- Repeatability
- Security

## Use cases

- Production:
  - Single server, all services on server
  - Single server, leveraging external services (including databases)
  - Multiple servers (later)
    - Leverage SlapOS, Swarm, Nomad or K8S...
- Development
  - PaaS experience for developers
- Preprod / demo
  - Deploy as many demos as needed (use case for SaaS vendors)

## Features

### For users

- Installation
  - "One click" install of pre-packaged applications (from an "app store" like webapp)
  - Deployment of custom apps (useing development tools, e.g. CLI and CI)
- Backups and disaster recovery
- Monitoring (app up / down, performance...)
- Logs
- Security
  - SSL Certificates (via Let's Enrcrypt)
  - Alerts when supported packages need to be upgraded
  - Firewall / intrusion detection (basic)
  - User management
    - User base may be exposed through a SSO mechanism (SAML, Shibboleth...)
  - Access control
    - Basic: apps can be private or public
    - Fine-grained: rules to control access to certain URL patterns
- Upgrades and server migration

### For developers / package builders

- Build tools (either add-ons or in replacement to a Dockerfile)
- Way to provide dev / ops parity

## Technical vision

### Overall philosophy

- "12 factor apps" (read: https://xenitab.github.io/blog/2022/02/23/12factor/#what-else-is-there for a state-of-the-art on the subject)
- Promise Theory: <https://en.wikipedia.org/wiki/Promise_theory>

### Architecture

- Build time: leverage Docker (initially)
  - Use (or fork) existing dockerfiles when possible, but try to abstract it away → `nua-config.toml`
  - Docker is probably the right tool to build the images
- Runtime: start with Docker, but should also support:
  - QEMU or othe lightweight / micro-VMs
  - "Unix native isolation" (maybe using just `chroot`).
  - lxc ?
- Services needed
  - WebUI (with a pleasant UI/UX) and CLI
  - Daemon (aka "Orchestrator")
  - Docker (when using Docker)
  - Backing services:
    - Databases / storage:
      - MySQL
      - Postgres
      - Mongo
      - Redis
      - S3 / minio
      - Others (pluggable)
    - Email
    - Message queues
  - "Registry": apps are configured using a centalised interface, if needed (e.g. if env variables are not enoigh, config files can be generated from the data in the Registry)

### Implementation details

- Everything is in Python
  - Daemon, cli, build scripts, web app, supporting scripts.
  - With some exceptions: config files (TOML), dockerfiles, some shell scripting

## Narrative

Nua isn't just another platform for deploying and managing web applications; it's an ambitious project that aims to be a one-stop solution for a variety of deployment scenarios. Built with resilience, repeatability, and security at its core, Nua aspires to be the foundation of your production, development, and pre-production needs.

Imagine you're running a production environment. With Nua, you have options. If you're just starting out and operating on a single server, Nua's got your back. It gracefully handles everything in-house, on that one server. As you scale and externalize some of your services, perhaps databases for instance, Nua seamlessly adapts, managing the complexities for you. Down the road, when you're big enough to require multiple servers, Nua plans to integrate with container orchestration titans like Kubernetes, Swarm, Nomad, or SlapOS to make your life even easier.

Developers are in for a treat, too. Nua aims to deliver a seamless Platform-as-a-Service experience, making the transition from development to production as smooth as possible. And if you're a SaaS vendor looking to deploy multiple demos, Nua makes it effortless to spin up as many as you need.

Let's talk features. One of the most user-friendly aspects is the "one-click" install for pre-packaged applications. Just select the app you need from an app-store-like interface, click, and you're good to go. Prefer a custom app? No problem—Nua allows you to deploy your unique applications using CLI and CI tools.

But what about disaster scenarios? Nua offers robust backup and disaster recovery options, so you can have peace of mind. The platform also gives you real-time monitoring capabilities and log management, helping you stay on top of things.

Now, you may be wondering about security. Nua takes it seriously. SSL certificates are managed via Let’s Encrypt, ensuring encrypted connections. The platform keeps you in the loop with alerts for package upgrades and offers basic firewall and intrusion detection features. Access control is both granular and flexible, with support for Single Sign-On mechanisms like SAML and Shibboleth.

For the tech-savvy, Nua’s architecture initially leverages Docker for both build and runtime but has plans to extend its support to other environments, like QEMU and Unix native isolation. Whether you're looking at a pleasant Web UI or need to dive deep with CLI, Nua provides both, backed by a variety of services like databases, email, and message queues. Nua is primarily coded in Python, making it a versatile choice for a broad range of developers.

Nua brings all this together with a clear technical vision, adhering to the "12-factor apps" methodology and incorporating Promise Theory. This well-thought-out blend of features and technical depth makes Nua a compelling choice for anyone looking to deploy and manage web applications securely and efficiently.
