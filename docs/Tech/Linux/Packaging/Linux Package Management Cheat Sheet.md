## Intro

Packages are essentially bundles of files containing everything a program needs to run: the executable code, libraries, configuration files, and documentation. They are like neatly prepared kits ready to be assembled on your system.

**Why is Package Management Important?**

*   **Simplicity:** Instead of complex manual installations, you can install software with a single command.
*   **Dependency Resolution:** Packages often rely on other packages (dependencies). Package managers automatically handle finding and installing these dependencies, preventing conflicts and ensuring programs run correctly.
*   **Consistency:**  Package managers ensure that software is installed in standard locations, making it easier to manage and maintain.
*   **Security:**  Packages are usually sourced from trusted repositories, reducing the risk of installing malicious or corrupted software. Updates are also easily managed, keeping your system secure.
*   **Clean Removal:**  Uninstalling software is just as easy, removing all associated files without leaving behind clutter.

## The Cheat Sheet

Different Linux distributions use different package management systems, but the underlying principles are similar. Here are a few prominent ones:

*   **Debian/Ubuntu (apt, dpkg):** Known for its user-friendliness, `apt` (and its older counterpart `apt-get`) is the command-line tool you'll use to interact with the package system. `dpkg` is a lower-level tool for handling individual `.deb` package files.
*   **Fedora/Rocky/RHEL (dnf, yum, rpm):** `dnf` (and previously `yum`) is the primary package manager, while `rpm` handles individual `.rpm` package files. These distributions focus on stability and enterprise use cases.
*   **Alpine (apk):**  Alpine Linux is designed to be lightweight and secure. `apk` is its efficient package manager.
*   **Nix (nix-env, nix-shell):** Nix takes a unique, declarative approach to package management, emphasizing reproducibility and allowing multiple versions of the same package to coexist. It uses the concepts of "profiles" and "generations."
*   **Guix (guix package, guix shell):** Similar to Nix, Guix offers transactional upgrades and rollbacks, ensuring system consistency. It also focuses on using free software.

**I. Debian / Ubuntu (apt, apt-get, dpkg)**

*   **Update package lists:** `sudo apt update` or `sudo apt-get update`
*   **Upgrade installed packages:** `sudo apt upgrade` or `sudo apt-get upgrade`
*   **Full upgrade (dist-upgrade):** `sudo apt full-upgrade` or `sudo apt-get dist-upgrade`
*   **Search for a package:** `apt search <package_name>` or `apt-cache search <package_name>`
*   **Install a package:** `sudo apt install <package_name>` or `sudo apt-get install <package_name>`
*   **Install a local package:** `sudo dpkg -i <package_file.deb>`
*   **Remove a package:** `sudo apt remove <package_name>` or `sudo apt-get remove <package_name>`
*   **Remove a local package:** `sudo dpkg -r <package_name>`
*   **Purge a package (remove config files):** `sudo apt purge <package_name>` or `sudo apt-get purge <package_name>`
*   **Purge a local package:** `sudo dpkg -P <package_name>`
*   **List installed packages:** `apt list --installed` or `dpkg --list` or `dpkg -l`
*   **Show package information:** `apt show <package_name>` or `apt-cache show <package_name>`
*   **Show local package information:** `dpkg -s <package_name>`
*   **Autoremove unused packages:** `sudo apt autoremove` or `sudo apt-get autoremove`
*   **Clean the package cache:** `sudo apt clean` or `sudo apt-get clean`
*   **Download a package without install it:** `sudo apt download <package_name>` or `sudo apt-get download <package_name>`
*   **Reinstall a package:** `sudo apt reinstall <package_name>` or `sudo apt-get install --reinstall <package_name>`
*   **List files included in a package:** `dpkg -L <package_name>`
*   **Find the package a file belongs to:** `dpkg -S <path/to/file>`

**II. Fedora / Rocky / RHEL (dnf, yum)**

*   **Update package lists:** `sudo dnf check-update` or `sudo yum check-update`
*   **Upgrade installed packages:** `sudo dnf upgrade` or `sudo yum update`
*   **Search for a package:** `dnf search <package_name>` or `yum search <package_name>`
*   **Install a package:** `sudo dnf install <package_name>` or `sudo yum install <package_name>`
*   **Remove a package:** `sudo dnf remove <package_name>` or `sudo yum remove <package_name>`
*   **List installed packages:** `dnf list installed` or `yum list installed`
*   **Show package information:** `dnf info <package_name>` or `yum info <package_name>`
*   **Autoremove unused packages:** `sudo dnf autoremove` or `sudo yum autoremove`
*   **Clean the package cache:** `sudo dnf clean all` or `sudo yum clean all`
*   **Download a package without install it:** `sudo dnf download <package_name>`
*   **Reinstall a package:** `sudo dnf reinstall <package_name>`
*   **List files included in a package:** `rpm -ql <package_name>`
*   **Find the package a file belongs to:** `rpm -qf <path/to/file>` or `dnf provides <path/to/file>`
*   **List available repositories:** `dnf repolist`
*   **Install a local package:** `sudo dnf localinstall <package_name.rpm>`
*   **Downgrade a package:** `sudo dnf downgrade <package_name>`

**III. Alpine (apk)**

*   **Update package lists:** `sudo apk update`
*   **Upgrade installed packages:** `sudo apk upgrade`
*   **Search for a package:** `apk search <package_name>` (Use `-v` for verbose output with descriptions)
*   **Install a package:** `sudo apk add <package_name>`
*   **Remove a package:** `sudo apk del <package_name>`
*   **List installed packages:** `apk info`
*   **Show package information:** `apk info <package_name>` (Use `-v` for verbose output)
*   **List files of a package:** `apk info -L <package_name>`
*   **Find package a file belongs to:** `apk info -W <path/to/file>`

**IV. Nix (nix-env, nix-shell)**

*   **Search for a package:** `nix-env -qaP <package_name>`
*   **Install a package:** `nix-env -iA <attribute>` (e.g., `nixpkgs.hello`)
*   **List installed packages:** `nix-env -q`
*   **Upgrade installed packages:** `nix-env -u` or `nix-env -u --leq`
*   **Remove a package:** `nix-env -e <package_name>` or `nix-env -e <attribute>`
*   **Show package information:** `nix-env -qa --description <package_name>`
*   **Rollback to previous profile:** `nix-env --rollback`
*   **Garbage collect unused packages:** `nix-collect-garbage` or `nix-store --gc`
*   **Enter environment with a package (temporary):** `nix-shell -p <package_name>`
*   **Build a package from source:** `nix-shell '<nixpkgs>' -A <package> --run 'make'`

**V. Guix (guix package, guix shell)**

*   **Search for a package:** `guix search <package_name>`
*   **Install a package:** `guix package -i <package_name>`
*   **List installed packages:** `guix package -l`
*   **Upgrade installed packages:** `guix pull && guix package -u`
*   **Remove a package:** `guix package -r <package_name>`
*   **Show package information:** `guix show <package_name>`
*   **Rollback to previous profile:** `guix package --roll-back`
*   **Garbage collect unused packages:** `guix gc`
*   **Enter environment with a package (temporary):** `guix shell <package_name>`
*   **Build a package from source:** `guix shell <package_name> -- sh -c 'make'`
