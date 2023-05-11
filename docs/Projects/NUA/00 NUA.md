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
    - SlapOS
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
