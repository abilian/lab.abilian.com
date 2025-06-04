Puavo is a mature, comprehensive IT infrastructure management system with a **15-year development history**, primarily serving educational institutions but adaptable for other organizations. It provides a centralized, manageable, and robust environment for users and their devices. The project consists of two core, actively maintained components, each with at least one dedicated full-time developer:

1.  **The Puavo Operating System:** A Linux-based OS (based on Debian), developed over 15 years, tailored for classroom and administrative use within the Puavo ecosystem. It forms the foundation for user experiences and device management policies.

2.  **The Puavo Web Management Application:** Also 15 years in development, this web application is the central **control panel** for the Puavo environment. It utilizes an **LDAP directory** as its backbone for managing:
    *   **Identities & Access:** User lifecycles (students, teachers, admins), groups, and school affiliations.
    *   **Devices:** Registration, configuration (including PuavoConf JSON settings, WLAN, Puavomenu), and oversight of diverse hardware (laptops, servers, printers), including hardware inventory.
    *   **System-wide & Granular Configuration:** Defining and applying settings across the organization, schools, user groups, or individual devices.
    *   **Policy Enforcement:** Implementing security and usage policies, primarily through extensively tested LDAP Access Control Lists (ACLs).
    *   **User Self-Service:** Portals for profile editing, password changes, and Multi-Factor Authentication (MFA) setup.
    *   **Authentication & Authorization:** Handles LDAP, Kerberos, and MFA for resource access.
    *   **External Integrations:** Mechanisms for SSO and data synchronization with platforms like Google Workspace, Azure AD, and Citrix.

**Key Characteristics:**

*   **LDAP-Centric:** LDAP serves as the "single source of truth" for identities, memberships, device data, and configurations.
*   **Education-Focused:** Supports a wide array of educational software (STEM, programming/robotics, literacy, digital assessment, interactive whiteboards, learning games).
*   **Comprehensive Management:** Covers a broad spectrum of IT administration, from the OS to user accounts and application access.
*   **Maturity & Dedicated Development:** Long-term development and dedicated resources indicate a refined and actively supported system.
*   **Implied Modularity:** Separation of OS and web management, plus integration capabilities, suggest a modular design.

**Software Ecosystem Highlights:**

Puavo manages a diverse software suite, including:

*   **Educational Tools:** GeoGebra, Scratch variants, Arduino IDEs, Abitti clients.
*   **General Development & Productivity:** VSCode, Eclipse, Docker, Adobe Reader, project management.
*   **Communication & Collaboration:** Nextcloud, Slack, various video conferencing tools.
*   **Specialized Tools:** 3D printing software (Cura, PrusaSlicer), security tools (Bitwarden, Veracrypt).
*   **System Components:** Core OS libraries, fonts, Puavo-specific firmware, and maintenance packages.

**Overall:** Puavo is a robust, long-developed platform for managing IT in educational settings, heavily reliant on LDAP. Its strength lies in centralized control, comprehensive management capabilities, and a software ecosystem tailored to educational needs, all supported by dedicated development.

---
## Full list of packages (June 2025)


**1. Educational Software**

*   **General & Cross-Disciplinary Learning:**
    *   `abicus` (Often used for mind mapping/concept mapping in education)
    *   `cmaptools` (Concept mapping)
    *   `kantti` (Finnish educational platform/content)
    *   `ohjelmointi-opetuksessa` (Finnish: "programming in teaching" - likely resources or a platform)
    *   `openclipart` (Clipart for projects)
    *   `schoolstore-ti-widgets` (Likely widgets for Texas Instruments calculators used in schools)

*   **STEM (Science, Technology,Engineering, Math):**
    *   `celestia` (Space simulator)
    *   `filius` (Network simulator for education)
    *   `geogebra` (Interactive geometry, algebra, statistics, and calculus)
    *   `geogebra6` (Newer version of GeoGebra)
    *   `globilab` (Data logging and analysis for science experiments)
    *   `lmaths` (Mathematical software, possibly for younger students)
    *   `logicsim3` (Digital logic circuit simulator)
    *   `m3dviewer` (3D model viewer, useful in STEM)
    *   `mafynetti` (Finnish platform for math, physics, chemistry - often high school)
    *   `mandelbulber` (3D fractal generator - math/art exploration)
    *   `marvinsketch` (Chemical drawing software)
    *   `mathpix` (Convert images of math to LaTeX, etc.)
    *   `openscad-nightly` (Programmatic ตรฐาน CAD software, useful for STEM projects)
    *   `phywe-measureapp` (Data acquisition for PHYWE science experiments)
    *   `sparkvue` (Data collection and analysis for science education)
    *   `structorizer` (Nassi-Shneiderman diagram editor for algorithm design)

*   **Programming, Robotics & Creative Coding (Educational Focus):**
    *   `appinventor` (Block-based programming for Android apps)
    *   `arduino-ide` (Original Arduino development environment)
    *   `arduino-ide2` (Newer Arduino development environment)
    *   `arduino-ottodiylib` (Library for Otto DIY robots with Arduino)
    *   `arduino-radiohead` (Arduino library for radio communication)
    *   `arduino-tm1637` (Arduino library for TM1637 display drivers)
    *   `aseba` (Programming environment for robots like Thymio)
    *   `bluej` (Java IDE designed for introductory teaching)
    *   `enchanting` (Scratch modification for programming LEGO Mindstorms NXT)
    *   `gdevelop` (Open-source, cross-platform game engine for beginners)
    *   `greenfoot` (Java IDE with 2D actor simulation for education)
    *   `hamstersimulator` (Learn Java programming with a virtual hamster)
    *   `javakara` (Programming with Kara the ladybug, educational)
    *   `kojo` (Learning environment for Scala, programming, and math)
    *   `mindplus` (Graphical programming for microcontrollers like Arduino, micro:bit)
    *   `nightcode` (Simple IDE for Clojure, often for beginners)
    *   `otto-blockly` (Blockly-based programming for Otto DIY robots)
    *   `processing` (Flexible software sketchbook for creative coding)
    *   `pythonkara` (Kara environment using Python)
    *   `robboscratch` (Scratch for Robbo robotics kits)
    *   `robotmeshconnect` (Connects RobotMesh Studio to VEX robots)
    *   `s4a` (Scratch for Arduino)
    *   `scratux` (A block-based visual programming language, Scratch alternative)

*   **Literacy & Language:**
    *   `ekapeli-alku` (Finnish game for learning to read)

*   **Digital Assessment:**
    *   `abitti-naksu`, `abitti-naksu2` (Client for Abitti, Finnish digital matriculation examination system)

*   **Interactive Whiteboard & Classroom Display Software:**
    *   `airtame` (Wireless screen sharing)
    *   `clevertouch-lynx` (Software for Clevertouch interactive displays)
    *   `epson-easymp` (Epson projector network projection software)
    *   `eshare` (Wireless screen sharing and collaboration)
    *   `novoconnect` (Wireless presentation and collaboration solution)
    *   `promethean` (Software for Promethean interactive whiteboards)
    *   `smartboard` (Software for SMART Board interactive whiteboards)
    *   `visualizer` (Software for document cameras/visualizers)

*   **Learning Games:**
    *   `dragonbox_algebra_12`
    *   `dragonbox_algebra_5`
    *   `dragonbox_bignumbers`
    *   `dragonbox_koulu1`
    *   `dragonbox_koulu2`
    *   `dragonbox_koulu3`
    *   `dragonbox_numbers`

**2. Programming & Development Tools (More General/Professional):**
*   `docker-compose-plugin` (Tool for defining and running multi-container Docker applications)
*   `eclipse` (Integrated Development Environment for various languages)
*   `idid` (Tool for signing iOS binaries, potentially for development/deployment)
*   `lazarus-ide` (Free Pascal IDE)
*   `netbeans` (Integrated Development Environment for Java, PHP, etc.)
*   `pycharm` (Python IDE)
*   `unityhub` (Management tool for Unity game engine projects and versions)
*   `vagrant` (Tool for building and managing virtual machine environments)
*   `vscode` (Visual Studio Code - popular code editor)

**3. Productivity & Office Applications:**
*   `adobe-reader` (PDF viewer)
*   `bluegriffon` (WYSIWYG HTML editor)
*   `drawio-desktop` (Diagramming software)
*   `lumidesktop` (Could be a presentation tool or specific hardware software; assuming general productivity for now)
*   `obsidian-icons` (Icon pack, likely for the Obsidian note-taking app)
*   `projectlibre` (Project management software)
*   `t-lasku` (Finnish invoicing/accounting software)
*   `tilitin` (Finnish accounting software)
*   `xournalpp` (Handwritten note-taking and PDF annotation)

**4. Communication & Collaboration Tools:**
*   `bitwarden` (Password manager)
*   `bitwarden-cli` (Command-line interface for Bitwarden)
*   `discord` (Voice, video, and text communication service)
*   `dropbox` (Cloud storage and file synchronization)
*   `ffsend` (Simple command-line file sharing)
*   `mattermost-desktop` (Open-source team collaboration platform)
*   `nextcloud-desktop` (Desktop client for Nextcloud file sync and share)
*   `nextcloud-talk-desktop` (Desktop client for Nextcloud Talk)
*   `signal-desktop` (Secure messaging app)
*   `slack` (Team collaboration and communication platform)
*   `teamviewer` (Remote access and support software)
*   `telegram-desktop` (Messaging app)
*   `vidyo-client` (Video conferencing client)
*   `webex` (Web conferencing)
*   `zoom` (Video conferencing)

**5. Graphics, Multimedia & Design Software:**
*   `aversphere2` (Software for viewing/creating 360° panoramas)
*   `kdenlive-appimage` (Non-linear video editor)
*   `musescore-appimage` (Music notation software)
*   `openshot-appimage` (Video editor)
*   `shotcut` (Video editor)
*   `sonobus` (High-quality, low-latency peer-to-peer audio streaming)
*   `spotify-client` (Music streaming service client)

**6. 3D Printing & CAD/CAM Software:**
*   `cura-appimage` (3D printer slicing software)
*   `flashforge-flashprint` (Slicing software for FlashForge 3D printers)
*   `prusaslicer` (Slicing software for Prusa 3D printers)
*   `qcad-cam` (2D CAD/CAM software)

**7. Security & Privacy Tools:**
*   `cryptomator` (Client-side encryption for cloud files)
*   `veracrypt` (Disk encryption software)

**8. System Utilities & Tools:**
*   `balena-etcher` (Tool for writing OS images to SD cards and USB drives)
*   `pyscrlink` (Python screen link, likely for screen sharing/mirroring)
*   `rustdesk` (Open source remote desktop software)
*   `wifiman-desktop` (Wi-Fi network analysis tool)

**9. Hardware-Specific Software & Drivers (Peripherals, not core system):**
*   `canon-cque` (Canon printer driver/utility)
*   `cnijfilter2` (Canon IJ printer driver)
*   `kmbeu` (KartenManagementBasisEuropa - smart card middleware, often for German identity cards)

**10. System Libraries, Fonts & OS Components:**
*   `extra-xkb-symbols` (Additional XKB keyboard layout symbols)
*   `firmware-sof-signed` (Sound Open Firmware - audio drivers)
*   `hp-bios-utils` (Utilities for HP BIOS management)
*   `msttcorefonts` (Microsoft TrueType core fonts for Linux)
*   `openjdk-11-jre` (Java Runtime Environment)
*   `tela-icon-theme` (Icon theme)
*   `tmux-plugins-battery` (Battery status plugin for tmux)
*   `ubuntu-focal-libs` (Compatibility libraries from Ubuntu Focal)
*   `ubuntu-trusty-libs` (Compatibility libraries from Ubuntu Trusty)
*   `ubuntu-wallpapers` (Default Ubuntu wallpapers)
*   `ubuntu-wallpapers-bullseye` (Ubuntu wallpapers for Debian Bullseye)
*   `wine-gecko` (Wine's built-in browser engine)
*   `wine-mono` (Wine's .NET implementation)
*   `wine-mono-bookworm` (Wine's .NET implementation for Debian Bookworm)

**11. Puavo System & Maintenance Packages:**
*   `launcherone` (Likely a custom application launcher for the Puavo environment)
*   `puavo-firmware` (Firmware specific to Puavo hardware or configurations)
*   `puavo-pkg-update-repository` (Script/tool to update Puavo package repositories)
*   `template` (Likely a template package for Puavo system configurations or new packages)
*   `update_package_version` (Script/tool for updating package versions within the Puavo system)

**12. Games (Recreational):**
*   `supertuxkart` (Kart racing game)
