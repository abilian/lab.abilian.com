Fedora Silverblue is an official variant of Fedora Linux that offers an **immutable desktop operating system**. This means the core operating system files (everything under `/usr`, `/etc` mostly, except for specific configurations) are read-only by default during normal operation. The goal is to provide a highly stable, reliable, and predictable system that is more resistant to accidental breakage and easier to update or roll back.

## References

https://fedoraproject.org/atomic-desktops/
https://fedoraproject.org/atomic-desktops/silverblue/

TODO: refactor this note. The conceptual part is "Atomic Desktops for Fedora", SilverBlue is just a profile.

## How it Works

1.  **Image-Based with `rpm-ostree`:** Instead of traditional package-by-package updates (like `dnf update`), Silverblue uses `rpm-ostree`. This system treats the OS as a whole "image" or "commit" (like Git). Updates are atomic: either the entire new OS version is successfully deployed, or the system remains on the current version. If an update causes issues, you can easily roll back to the previous working "commit" of your OS.
2.  **Applications via Flatpak:** The primary way to install graphical applications is through Flatpak. Flatpaks are containerized applications that bundle their dependencies and run in a sandboxed environment, isolated from the base OS and each other. This keeps the core OS clean and allows apps to be updated independently.
3.  **Development & CLI Tools via Toolbx/Distrobox:** For command-line tools, development environments, or software not available as a Flatpak, Silverblue promotes the use of Toolbx (or the more versatile Distrobox). These tools create mutable containerized environments (often based on Fedora or other distributions) where you can install traditional packages using `dnf`, `apt`, etc., without altering the immutable host system. Your home directory is shared with these containers.
4.  **Package Layering (as a last resort):** If absolutely necessary, `rpm-ostree` allows you to "layer" traditional RPM packages onto the base OS image. This is generally discouraged for most use cases to maintain immutability benefits but provides an escape hatch.
5.  **Writable `/var` and `/home`:** While the core OS is read-only, your user data in `/home` and system-specific variable data in `/var` (like logs, container images) remain writable and persist across updates.

## Differences with Nix/Guix and Docker/Podman

### Vs. Nix/Guix (e.g., NixOS, Guix System)

*   **Configuration:** Nix/Guix aim for a *fully declarative* system configuration. You write code (in Nix language or Guile Scheme) that describes your entire system, from kernel modules to installed packages and user dotfiles. Silverblue's base OS is an image provided by Fedora; while `rpm-ostree` deals with system states, it's not a rich declarative language for the *entire* OS configuration in the same way.
*   **Reproducibility:** Nix/Guix focus on *build reproducibility*, ensuring packages are built identically every time. Silverblue ensures OS *state reproducibility* and predictability through its image-based approach and rollbacks.
*   **Package Management:** Nix/Guix use their own functional package managers that create isolated environments for each package. Silverblue relies on Flatpak for GUI apps (sandboxed) and `rpm-ostree` for the base OS (layered).
*   **Scope:** NixOS/Guix System are complete operating systems built from the ground up with these principles. Silverblue is a *variant* of Fedora, adapting an existing ecosystem to an immutable model.

### Vs. Docker/Podman (as an OS approach)

*   **Role:** Docker/Podman are primarily tools for creating, deploying, and running *application containers* on top of a host OS. Fedora Silverblue *is* the host OS itself.
*   **Immutability Focus:** Silverblue's immutability applies to the base operating system. Docker/Podman provide immutable application images.
*   **Usage of Containers:** Silverblue *uses* container technology (via Toolbx/Distrobox with Podman) to provide mutable environments for development and CLI tools, keeping the host OS pristine. Docker/Podman can *also* be run *on* Silverblue to manage application services, just like on any other Linux distribution. The key difference is that Silverblue's core OS immutability is a distinct concept from running Dockerized apps. Silverblue isn't "an OS made of Docker containers"; rather, it's an immutable OS that leverages container tech for specific use cases (like development environments).

## Other "Fedora Atomic Desktops" Distributions

The difference between Fedora Silverblue and other Fedora Atomic Desktops (like **Fedora Kinoite**, **Fedora Sericea**, or **Fedora Onyx**) is primarily the **default desktop environment** they ship with.

Under the hood, they are all built on the **same foundational "Atomic" principles and technology**:

1.  **Immutable Base System:** The core OS is read-only, managed by `rpm-ostree`.
2.  **Image-Based Updates:** Updates are atomic and the system can be easily rolled back.
3.  **Application Delivery:**
    *   Graphical applications are primarily installed via **Flatpak**.
    *   CLI tools and development environments are typically managed using **Toolbx** or **Distrobox** (which uses Podman).
4.  **Package Layering:** `rpm-ostree install <package>` can be used to add RPMs to the base image if absolutely necessary, though it's generally discouraged for many packages.

**So, what *is* the difference?**

*   **Fedora Silverblue:** Ships with the **GNOME** desktop environment.
*   **Fedora Kinoite:** Ships with the **KDE Plasma** desktop environment.
*   **Fedora Sericea:** Ships with the **Sway** tiling window manager (a Wayland compositor popular with keyboard-driven users).
*   **Fedora Onyx:** Ships with the **Budgie** desktop environment.
    *(And there may be others, like Sway (Sericea) or Pantheon, etc.)*

**This difference in desktop environment impacts:**

*   **Look and Feel:** The visual appearance, window management, and overall user interface.
*   **Default Applications:** The set of pre-installed applications (e.g., file manager, terminal, text editor) will be those typically associated with that desktop environment.
*   **System Settings and Configuration Tools:** The tools you use to configure your desktop (e.g., display settings, keyboard layouts, themes) will be specific to GNOME, KDE Plasma, Budgie, or how Sway is configured.

**In essence:**

Think of Fedora Silverblue, Kinoite, Sericea, and Onyx as different "flavors" of the same immutable Fedora base. You choose the one whose desktop environment you prefer, but you get the same underlying stability, atomic updates, and application management strategy.

The term **"Fedora Atomic Desktops"** is the umbrella term for these `rpm-ostree` based desktop variants. The older term "Spins" is more commonly used for *traditional, mutable* Fedora variants that offer different desktop environments (e.g., Fedora KDE Spin, Fedora Xfce Spin). So, Kinoite isn't just an "Atomic Spin" in the old sense; it's a fully-fledged Atomic Desktop offering alongside Silverblue.

## Summary

Fedora Silverblue offers a robust and stable desktop experience by making the core OS immutable, managing applications primarily through Flatpaks, and providing containerized environments for development needs. It prioritizes system integrity and easy rollbacks, contrasting with the full declarative nature of Nix/Guix and the application-centric containerization of Docker/Podman.
