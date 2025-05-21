
**1. Q: What is the main goal or objective of the EU OS Proof of Concept (PoC)?**

**A:** The primary goal is **not** to prove that an individual can use Linux. Instead, the PoC aims to demonstrate the feasibility for an **admin team** to effectively manage users, data, software, and devices using Linux-based systems. It focuses on showing that migration from Windows environments can be achieved manageably at scale, potentially integrating with or replacing systems like Active Directory, within a realistic timeframe (e.g., 2 years rather than 20).

**2. Q: Who is the target audience for testing EU OS – end-users or system administrators?**

**A:** The main target audience for the PoC testing phase is **system administrators**. The focus is on evaluating how EU OS allows them to customize Linux environments (e.g., add applications), deploy systems at scale, and manage updates efficiently.

**3. Q: What core technology does EU OS propose for deploying Linux to workstations?**

**A:** EU OS utilizes "bootable container technology" (specifically `bootc`). This involves building immutable OS images in a central location (cloud/server) which are then deployed to end-user workstations.

**4. Q: Does this image-based deployment replace the need for traditional configuration management software (like Ansible, Puppet, Chef)?**

**A:** It might reduce the need, or change how configuration is applied. The idea is that much of the base configuration is built *into* the image. If the image is well-prepared, separate configuration management *might* not be required. However, options exist for more dynamic configuration:

*   Files can be copied directly into the image during the build process (e.g., via `recipe.yml`).
*   Systemd unit scripts can be included in the image to run tasks upon user login or other events.
*   Layering configurations on top of images using technologies like `systemd-sysext` is discussed.
*   Integrating dedicated fleet/configuration management tools (like Foreman using pull-mode Ansible via MQTT) is also being considered for more complex needs.

So, it can be seen as potentially complementary rather than strictly alternative, depending on the complexity required.

**5. Q: How are configurations managed or changed within these bootable images?**

**A:** Configuration files and settings are typically defined in the build recipes (e.g., `recipe.yml`). Administrators modify these recipes or the files referenced by them, and then rebuild the image. Updates deploy the new image containing the changed configuration.

**6. Q: What administrative tasks is this EU OS model intended to support?**

**A:** The goal is to enable central management of:
*   Installed software (per user group or workplace type).
*   Automatic software updates (including security fixes).
*   Central configuration of system settings (e.g., enforcing data protection defaults).
*   Disabling specific hardware components (e.g., microphones).
*   Central monitoring of workstation properties (e.g., disk usage).

**7. Q: Technically, how does EU OS differ from a standard Linux distribution like Fedora? What does it add?**

**A:** Currently, EU OS is primarily about **combining existing software and technologies**. It builds upon established Linux distributions (the test builds use Fedora 100%, but CentOS, AlmaLinux, RHEL are also possibilities). EU OS itself doesn't introduce fundamentally new OS components. Its value lies in:
*   Providing the framework and recipes (`recipe.yml`) for building bootable OS images tailored for administration needs.
*   Integrating the tools and processes for scalable deployment and updates using `bootc`.
*   Focusing on the *management architecture* for enterprise/organizational use.
*   Potentially defining templates or blueprints to lower the barrier to adoption.

**8. Q: Does EU OS prescribe a specific set of software packages or a desktop environment?**

**A:** The specific software installed on the host systems is determined by the administrator during the image build process via the recipe file. Regarding the desktop environment, KDE (potentially version 6) is used or considered by some parties (like Schleswig Holstein and Spain), partly for its familiarity to Windows users. However, the architecture likely allows for flexibility.

**9. Q: Can EU OS, in its PoC phase, be deployed directly to mission-critical workplaces?**

**A:** Deploying a PoC directly to mission-critical systems is generally ill-advised. We will build a specific *test scenario* to evaluate how EU OS *could* be deployed for mission-critical work, rather than using it live immediately. Reliability needs to be proven in a controlled environment first.

**10. Q: How does EU OS address the challenge of training Windows administrators for Linux and providing ongoing technical support?**

**A:** EU OS itself doesn't inherently solve the significant non-technical challenges of migration, such as training staff accustomed to Windows GUI/CLI, providing support materials (potentially in multiple languages), and managing user adoption. The project will mitigate this by choosing robust tools and fostering a community that can co-create documentation and share best practices. This challenge is common to any large-scale OS migration.

**11. Q: Where can I find more technical information or join the discussion?**

**A:**
*   **Use Cases:** `https://eu-os.eu/use-cases`
*   **Technical Example (Recipe):** `https://gitlab.com/eu-os/workspace-images/eu-os-base-demo/-/blob/main/recipes/recipe.yml?ref_type=heads#L17`
*   **Project Issues/Tasks (example):** `https://gitlab.com/eu-os/eu-os.gitlab.io/-/issues/31`
*   **Community Discussion:** Matrix channel `#eu-os:kde.org`
