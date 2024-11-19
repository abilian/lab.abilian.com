Effective collaboration and version control are essential for software developping organisations (SDOs) for delivering robust, maintainable, and high-quality code. Software "forges"—platforms designed for code hosting, management, and collaborative development—play a pivotal role in enabling these practices. While cloud-hosted solutions like GitHub and GitLab dominate the landscape, on-premises (or :self-hosted") software forges provide an alternative for organizations seeking greater control over their infrastructure, enhanced privacy, and tailored functionality.

This document explores a range of open-source, on-premises software forges, each uniquely suited to specific development needs and organizational contexts. From lightweight, easy-to-deploy solutions like **Gogs** to enterprise-grade platforms such as **Tuleap**, these tools cater to diverse workflows and project scales. With features encompassing code review, issue tracking, continuous integration, and project management, on-premises forges empower teams to align their development practices with their technical, operational, and governance requirements.

The comparison presented here aims to guide organizations and developers in selecting a forge that aligns with their use cases—whether it’s individual developers seeking simplicity, enterprises prioritizing structured workflows, or teams needing comprehensive project lifecycle management. By understanding the capabilities, strengths, and trade-offs of each forge, users can make informed decisions to optimize their software development ecosystems.

## Detailed descriptions

### Gerrit

- **Purpose**: A code review and collaboration tool tightly integrated with Git. Designed for rigorous workflows in enterprise environments.
- **Technologies**: Java backend, Polymer UI, uses Elasticsearch for search and NoteDB for metadata. Requires Java SE Runtime Environment and Unix-based systems.
- **Key Features**:
    - Advanced code review with approval workflows.
    - Integration with CI/CD pipelines.
    - Support for large binary files via Git LFS.
    - Authentication support (LDAP, OAuth, SSH).
- **Community**:
    - Corporate contributors (e.g., Google, SAP).
    - Active mailing list for support.
- **Ideal For**: Large teams with structured development and review processes.
- **Challenges**: UI is considered outdated and complex for new users.

### Gogs

- **Purpose**: Lightweight and easy-to-install Git service for individuals or small teams.
- **Technologies**: Written in Go, uses Macaron for web framework, and XORM for ORM. Supports MySQL, PostgreSQL, and SQLite.
- **Key Features**:
    - Basic Git repository hosting.
    - Simple installation and minimal resource requirements.
    - Issue tracking and lightweight UI.
- **Community**:
    - Small but active.
    - Contributions via GitHub.
- **Ideal For**: Small-scale projects or developers new to Git hosting.
- **Challenges**: Limited features compared to other platforms.

### Gitea

- **Purpose**: Self-hosted Git service offering extensive features for collaborative development.
- **Technologies**: Built with Go, runs on Linux, macOS, Windows, and Raspberry Pi.
- **Key Features**:
    - Code hosting, review, CI/CD integration with Gitea Actions.
    - Repository mirroring and webhooks.
    - Extensive customization options.
- **Community**:
    - Broad open-source community with diverse contributors.
    - Strong plugin ecosystem.
- **Ideal For**: Small to medium teams seeking a robust and flexible Git hosting solution.
- **Challenges**: Some overlap with Forgejo due to shared origins.

### Forgejo

- **Purpose**: A community-driven fork of Gitea, emphasizing sustainability and open governance.
- **Technologies**: Same as Gitea; Go-based with cross-platform support.
- **Key Features**:
    - Similar to Gitea but with a focus on governance transparency.
    - Active community and long-term development goals.
- **Community**:
    - Open governance model encouraging broad participation.
- **Ideal For**: Organizations valuing community-driven development and governance.
- **Challenges**: Feature development may overlap with Gitea.

### Redmine

- **Purpose**: A project management tool integrating Git with task and issue tracking.
- **Technologies**: Built with Ruby on Rails, supports MySQL, PostgreSQL, and SQLite.
- **Key Features**:
    - Advanced issue tracking.
    - Task management and Gantt charts.
    - Extensible with numerous plugins.
- **Community**:
    - Long-established and active.
    - Supported by a plugin ecosystem.
- **Ideal For**: Teams managing both project tasks and version control.
- **Challenges**: Outdated UI and complex setup.

### SourceHut

- **Purpose**: A minimalist and scriptable Git hosting service for advanced workflows.
- **Technologies**: Python and Go; lightweight and designed for Unix environments.
- **Key Features**:
    - Email-driven issue tracking and patch-based contributions.
    - Scriptable workflows and API-driven operations.
    - Minimalist UI focusing on functionality.
- **Community**:
    - Niche community of advanced users and developers.
- **Ideal For**: Power users and teams favoring automation and customization.
- **Challenges**: Steeper learning curve for newcomers.

### Trac

- **Purpose**: Combines wiki-style documentation and issue tracking with Git/Subversion integration.
- **Technologies**: Python-based; integrates with multiple version control systems.
- **Key Features**:
    - Strong documentation and issue tracking.
    - Integration with Git and Subversion.
    - Flexible customization through plugins.
- **Community**:
    - Stable and long-standing.
- **Ideal For**: Projects needing integrated documentation and issue management.
- **Challenges**: Dated interface and slower development pace.

### Tuleap

- **Purpose**: A comprehensive application lifecycle management (ALM) tool covering project management, version control, and CI/CD.
- **Technologies**: Built with PHP and Java; supports PostgreSQL.
- **Key Features**:
    - Advanced project and task management.
    - Integrated Git support with CI/CD pipelines.
    - Support for Agile and waterfall methodologies.
- **Community**:
    - Enterprise-oriented with smaller open-source contributions.
- **Ideal For**: Enterprises managing complex, multi-team projects.
- **Challenges**: Complex installation and higher resource requirements.

## Features Comparison

| **Feature**           | **Gerrit** | **Gogs** | **Gitea** | **Forgejo** | **Redmine**  | **SourceHut** | **Trac** | **Tuleap** |
| --------------------- | ---------- | -------- | --------- | ----------- | ------------ | ------------- | -------- | ---------- |
| **Code Review**       | Advanced   | Basic    | Moderate  | Moderate    | None         | Advanced      | None     | Basic      |
| **CI/CD Integration** | Strong     | Limited  | Built-in  | Built-in    | Plugin-based | Scriptable    | Limited  | Extensive  |
| **Task Management**   | None       | Basic    | Moderate  | Moderate    | Advanced     | None          | Advanced | Advanced   |
| **Ease of Use**       | Moderate   | High     | High      | High        | Moderate     | Low           | Low      | Low        |
| **Customization**     | Moderate   | Limited  | High      | High        | High         | High          | Moderate | High       |
| **Resource Needs**    | High       | Low      | Low       | Low         | Moderate     | Moderate      | Moderate | High       |

## Use Cases and Conclusion


1. **Gerrit**:

    - **Use Case**: Large-scale teams requiring structured code review workflows, strict approval processes, and integration with CI/CD pipelines.
    - **Best For**: Enterprises, open-source projects with rigorous quality control.

1. **Gogs**:

    - **Use Case**: Lightweight Git hosting for individual developers or small teams needing basic repository management with minimal setup.
    - **Best For**: Personal projects, startups, and teams with limited resources.

1. **Gitea**:

    - **Use Case**: Full-featured Git hosting with flexibility for small-to-medium teams and integration with CI/CD.
    - **Best For**: Developers and organizations looking for an extensible, user-friendly self-hosted alternative to GitHub or GitLab.

1. **Forgejo**:

    - **Use Case**: Community-driven projects prioritizing open governance and sustainability, with features similar to Gitea.
    - **Best For**: Organizations valuing transparency and long-term support in their tools.

1. **Redmine**:

    - **Use Case**: Teams requiring integrated task management, issue tracking, and Git support for software or project development.
    - **Best For**: Project-heavy teams managing complex workflows alongside version control.

1. **SourceHut**:

    - **Use Case**: Developers and power users needing scriptable workflows, email-based issue tracking, and minimalistic Git hosting.
    - **Best For**: Advanced users, automation-heavy workflows, and highly customized development environments.

1. **Trac**:

    - **Use Case**: Projects that combine version control with comprehensive wiki-style documentation and issue tracking.
    - **Best For**: Teams requiring detailed documentation integration alongside source control.

1. **Tuleap**:

    - **Use Case**: Comprehensive project management and ALM for large enterprises managing multiple teams, Agile, or waterfall workflows.
    - **Best For**: Enterprises needing an all-in-one tool for complex project lifecycles.
