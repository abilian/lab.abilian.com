

https://sidhion.com/blog/posts/nixos_server_issues/

The blog post discusses the author's journey with using NixOS as a server operating system, highlighting both its strengths and limitations. Initially, they were bothered by the large default installation size, even for minimal and headless configurations. The post details efforts to minimize disk usage, starting with a basic NixOS configuration that took up around 900MB of disk space.

Through a detailed investigation, the author uses various Nix tools (such as `nix-store --query` and custom visualizations) to analyze package dependencies and their disk sizes. Over time, they make several adjustments to the system, such as:

- Removing Nix itself, which reduced the system size by ~179MB.
- Eliminating Python and Perl, which further cut ~242MB.
- Resolving redundant package installations, like having both `systemd` and `systemd-minimal`, and removing unneeded services like udev, LVM, and security wrappers, reducing an additional ~44MB.

After significant reduction efforts, the system's size was reduced to approximately 447MB. However, the process revealed the complexity and limitations of configuring NixOS for a minimal, server-focused deployment. Some packages and utilities, like `util-linux` and security wrappers, were difficult to remove or manage, and there was still more potential for optimizations.

Despite these successes, the author ultimately concluded that while NixOS is powerful for managing server configurations, it is not well-suited for achieving extreme minimalism without extensive manual configuration. They reflect on the idea of creating a more specialized, server-focused version of NixOS, but express reservations about forking the project. The overall sentiment is that while NixOS is effective in many ways, it may not always be the best choice for highly optimized, lean server systems.

## Comments from Hacker News

https://news.ycombinator.com/item?id=41717050

The Hacker News comments on the blog post offer valuable insights into various aspects of NixOS, particularly regarding its use as a server OS. Key takeaways include:

1. **Language Concerns**: Several users discuss the Nix language's complexity and lack of discoverability, noting poor typing, syntax issues, and difficulty learning idioms in `nixpkgs`. Some appreciate its domain-specific design but suggest better IDE integration, debuggability, and typing improvements. Alternatives like Guix (which uses Scheme) and efforts like Nickel (which aims to improve Nix with types) are also mentioned as potential solutions for language-related issues.

2. **Managing Dependencies and Configuration**: The original blog’s discussion about slimming down NixOS resonates with readers. Many share strategies to minimize disk usage, such as using a single-binary coreutils, disabling unused services, and optimizing storage. The complexity of slimming down NixOS, while maintaining functionality, is acknowledged, but users emphasize the benefits of declarative configuration and repeatability.

3. **System Complexity**: Several comments address the challenges of managing complex systems with NixOS, particularly regarding system-wide configuration, lazy evaluation, and the challenge of keeping minimal server configurations stable. Others praise NixOS for its deterministic builds and powerful rollback mechanisms, but some argue that simpler systems like Alpine may be more practical for minimalist server deployments.

4. **Alternatives and Tools**: Various alternatives and tools for NixOS are highlighted, such as Guix for a Scheme-based approach, microVMs, `nixos-rebuild`, and `nix-anywhere` for deploying configurations. Users discuss integrating ZFS, cloud-init, and utilizing Proxmox with bash scripts for server management, illustrating the broader ecosystem and customization possibilities with NixOS.

5. **Stability and Rolling Releases**: Some users express concerns about the stability of NixOS in production environments, especially due to its rolling release nature. The blog’s author also acknowledges the difficulty of maintaining a lean server image over time. Several contributors argue that frequent updates and the lack of long-term support (LTS) releases complicate the maintenance of stable server environments.

Overall, while many appreciate NixOS for its innovation and flexibility, its complexity, steep learning curve, and challenges in managing minimal, stable server environments are recurrent themes.

## Solutions

- https://github.com/cleverca22/not-os = An operating system generator, based on NixOS, that, given a config, outputs a small (47 MB), read-only squashfs for a runit-based operating system, with support for iPXE and signed boot

<!-- Keywords -->
#nixos #nix #nixpkgs #linux
<!-- /Keywords -->
