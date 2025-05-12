
**EU OS Project: Report on Use Cases and Technical Specifications**

**1. Introduction**

This report summarizes discussions surrounding the intended use cases and technical specifications for the EU OS project. The project's primary goal is to create a **Proof-of-Concept (PoC) for the deployment and management of a Linux-based operating system** tailored for the European public sector. It aims to address challenges related to deployability, maintainability, user management, and compliance within this context, rather than creating a new Linux distribution from scratch. The following points synthesize community input and align it with the PoC's defined scope and objectives.

**2. Identified Use Cases and Target Audiences**

Based on discussions and the project's stated goals, the primary target audience and use cases for the EU OS PoC are:

*   **Primary Target:** Administrative workers and general office staff within EU public sector organizations (e.g., government agencies, municipalities, potentially EU institutions themselves). This includes tasks related to document processing, communication, web browsing, and accessing internal corporate systems.
*   **Strong Secondary Focus:** Educational institutions (public universities, potentially schools, building on experiences like So.Di.Linux, Pardus, Linux+1, and potentially collaborating with CERN). The need for cost-effective, manageable, and secure systems is high in this sector.
*   **Out of Scope for Initial PoC:** While NGOs, SMEs, corporations, and the general public *might* benefit from the outcomes or adopt similar approaches later, they are not the primary design target for this initial PoC phase. The focus remains on the specific requirements of public administration workstations.

**3. Core Technical Principles & Specifications**

To meet the goals of manageability, security, and deployability with potentially limited resources, the following technical principles and specifications are adopted for the PoC:

*   **Base Operating System:** The PoC will continue to build upon **Fedora Linux**, specifically leveraging its **atomic/immutable variants (e.g., Fedora Kinoite)**.
    *   *Rationale:* Fedora provides a modern, secure (SELinux integration, leading Wayland support, rapid security updates), and fully open-source foundation. Its atomic nature facilitates reliable updates and centralized management, key goals for the PoC. While concerns about US ties (Red Hat sponsorship) are noted, Fedora's open nature allows for independent mirroring, auditing, and modification. Potential commercial support avenues also exist if needed post-PoC. Alternatives like openSUSE or Debian are acknowledged but Fedora Kinoite aligns best with the PoC's technical approach.
*   **Desktop Environment:** **KDE Plasma** is the default desktop environment.
    *   *Rationale:* Offers a modern, feature-rich, highly customizable environment often perceived as familiar to users migrating from Windows. Its Qt base aligns well with cross-platform goals. While alternatives like GNOME exist and are capable, KDE is selected for the PoC. Concerns about GTK's perceived shortcomings (raised by blackPanther OS) are noted but are less impactful given the KDE focus.
*   **Display Server:** **Wayland** is the default display server.
    *   *Rationale:* Represents the future direction for Linux desktops, offering potential security and performance improvements over X11. While acknowledging that Wayland compatibility and driver support are still maturing, the PoC adopts it as the forward-looking choice, assuming target deployments can select compatible hardware.
*   **System Architecture:** An **immutable core system (OSTree-based)** is employed.
    *   *Rationale:* Essential for reliable, image-based deployments and updates, simplifying management across large fleets and enhancing system integrity and security. This directly addresses the PoC's core challenge of maintainability with minimal resources. Mutable systems, while offering flexibility, complicate centralized management and security assurance at scale, which is the PoC's focus.
*   **Layered Customization:** The system will utilize a layered approach (building on the base image) for customization.
    *   *Rationale:* Allows for a common EU base layer, with subsequent layers for national, regional, or organizational specifics (e.g., language packs, specific configurations, pre-installed applications). This balances standardization with necessary flexibility.
*   **Security:**
    *   **Secure Boot:** Support for UEFI Secure Boot is a requirement.
    *   **Hardening:** While advanced mandatory access control (MAC) systems like SELinux/AppArmor are fundamental to the base OS (Fedora), the PoC will focus on a *usable default configuration* rather than deep customization of these complex systems, which requires significant expertise beyond the PoC scope.
    *   **Firewall:** Basic firewall capabilities are expected, leveraging standard Linux tools manageable through the chosen desktop environment where possible. Concerns about specific GUI tool compatibility (e.g., UFW GUIs and Wayland) are noted for future consideration.
*   **Authentication:** The PoC will focus on **integration with standard corporate identity management systems** (e.g., LDAP, Kerberos, solutions compatible with FreeIPA/SSSD).
    *   *Rationale:* This is the immediate requirement for public sector deployment (NIS2 compliance mentioned). Integration with the future EU Digital Identity Wallet (EUID) or custom EIDAS Certificate Authorities is **out of scope for the initial PoC** but could be explored in future phases.
*   **Project Hosting:** The project currently uses GitLab.com for PoC development.
    *   *Rationale:* Pragmatic choice for collaboration during the early phase. A transition to EU-based, self-hosted, or trusted FOSS infrastructure (like Codeberg or a dedicated Forgejo instance) would be necessary for any operational deployment to fully align with sovereignty goals, but this migration is outside the immediate PoC scope.

**4. Application Strategy**

*   **Core Principle:** Maintain a **minimal base image** containing only essential system components, the desktop environment, and a core application set.
    *   *Rationale:* Reduces attack surface, simplifies maintenance and updates, lowers resource consumption, and provides a clean foundation for customization via layers or user-installed applications.
*   **Default Applications (Base Image):**
    *   **Web Browser:** Firefox (or potentially another reputable open source browser).
    *   **Office Suite:** LibreOffice.
    *   *(Possibly)* Basic utilities integrated with KDE Plasma (text editor, file manager, PDF viewer, etc.).
    *   *Rationale:* This minimal set covers the most fundamental needs of the target administrative user.
*   **Application Delivery:** **Flatpak** is the preferred method for delivering and managing user-facing applications.
    *   *Rationale:* Provides sandboxing for security, decouples applications from the base OS for stability, simplifies dependency management, and aligns well with the immutable system architecture. Allows users/admins to install applications without altering the core OS.
*   **Flatpak Repositories:** A tiered approach is envisioned for potential deployment:
    1.  **Audited EU OS Core Repository (Conceptual):** A future goal could be a centrally managed repository containing essential, vetted applications (like Firefox, LibreOffice, potentially others relevant across the EU). This would require significant resources for auditing and maintenance, thus is **not part of the PoC build**, but the *concept* is relevant.
    2.  **National/Institutional Repositories:** Deploying organizations/nations could set up their own repositories for specific applications (e.g., AusweisApp, Elster for Germany) layered on top.
    3.  **Flathub:** Access could be enabled but likely restricted or discouraged in production environments due to the lack of centralized vetting for all applications. Direct use might be suitable for testing/development phases.
    *   *PoC Implementation:* The PoC will demonstrate *how* to configure Flatpak repositories and potentially include a simple, *example* custom repository, but will not build or maintain a large-scale audited repository.
*   **Windows Application Support:** Supporting Windows applications (via Wine, Bottles, virtualization like QEMU/VirtualBox) is **explicitly out of scope for the EU OS base PoC**.
    *   *Rationale:* Ensuring compatibility is complex, resource-intensive, and often requires commercial support (e.g., Crossover) or per-application tuning. While the need exists for legacy applications, the focus of EU OS is on building a native Linux-based environment and promoting FOSS/web alternatives. Organizations needing Windows compatibility would need to implement and support solutions independently.
*   **Android Emulation:** This is **out of scope**.
*   **Specific Application Requests:** The extensive list of desired applications (KeepassXC, GIMP, Inkscape, Veracrypt, development tools, etc.) is acknowledged. These will **not** be included in the base image but serve as excellent examples of software that can be:
    *   Added to custom layers via the build recipes (e.g., `recipe.yml`).
    *   Made available via institutional Flatpak repositories.
    *   Installed by users via Flatpak if permitted by policy.

**5. Addressing Key Concerns**

*   **"Yet Another Linux Distro" (YaLD):** EU OS is positioned as a **deployment specification and methodology**, not a new distribution. It leverages an existing, robust base (Fedora) and adds value through its layered approach, management concept, and focus on public sector needs. Its success depends on demonstrating this added value in deployment and maintenance, not on unique core technology.
*   **Hardware Drivers (Printers, Scanners, etc.):** This remains a significant challenge for all Linux desktop adoption. The EU OS PoC relies on the driver support provided by the upstream kernel and Fedora project. While acknowledging usability concerns (e.g., CUPS interface), the PoC itself cannot solve fundamental driver issues or compel hardware vendor support. This requires broader ecosystem and potentially policy efforts.
*   **Organizational Adoption & Ease of Use:** The choice of KDE Plasma aims for user familiarity. The immutable model aims to simplify administration. However, successful adoption requires more than just the OS – training, support, change management, and addressing user resistance (as highlighted by blackPanther OS) are crucial but fall outside the technical PoC's scope. Learning from past projects (LiMux successes *and* failures) is important.
*   **Comparison to Commercial EU Distros (SUSE/Canonical):** While SUSE (Germany-owned, EQT HQ in Sweden) and Canonical (UK-based) offer mature solutions, the EU OS PoC explores a community-driven approach potentially offering greater transparency, customization, and direct alignment with specific EU public sector needs, potentially using a different technical base (Fedora Atomic). The aim is to provide a *concept* that could be implemented or adapted, potentially even using SUSE/Ubuntu bases if an organization chose to.

**6. Out of Scope Considerations (Acknowledged but Deferred)**

The following important topics, raised during discussions, are acknowledged as critical for broader digital sovereignty but are considered out of scope for the *initial technical PoC* phase of EU OS:

*   Addressing systemic market distortions, corruption, educational system reform, hardware vendor lock-in, illegal software use (Points raised extensively by blackPanther OS).
*   Implementing EU Digital Identity Wallet (EUID) integration.
*   Developing and enforcing EU-wide development standards, guidelines, and qualification frameworks (though the PoC aims for best practices).
*   Resolving fundamental Linux kernel licensing debates.
*   Mandating specific programming languages or development methodologies beyond using standard FOSS tools.
*   Negotiating directly with proprietary software vendors (e.g., Adobe) for Linux support.
*   Providing official support for non-workstation devices (smartphones, tablets).
*   Establishing and funding a permanent maintenance/governance body for EU OS beyond the PoC.
*   Self-hosting all development infrastructure during the PoC phase.
*   Translation and adaptation of external frameworks like the German National IT Architecture Guidelines.

**7. Next Steps & Recommendations (PoC Focus)**

*   Refine the base Fedora Kinoite image build process using the layered approach.
*   Document clearly how organizations can create custom layers (e.g., adding specific applications like LibreOffice, configuring settings).
*   Demonstrate configuration of Flatpak sources, potentially setting up a small example repository.
*   Test deployment and update mechanisms on representative hardware.
*   Develop basic documentation outlining the management concept for users/devices/software within the PoC framework.

**8. Conclusion**

The EU OS PoC focuses on delivering a practical, technically sound concept for deploying and managing a secure, open source desktop environment within the European public sector. By leveraging Fedora Kinoite, KDE Plasma, OSTree, and Flatpak, and adopting a minimal-base philosophy with layered customization, the project aims to demonstrate a viable path towards greater digital autonomy and efficiency for public administrations. While acknowledging the significant broader systemic challenges, this PoC concentrates on solving the immediate technical hurdles of scalable and maintainable deployment.
