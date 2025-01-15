## Tutorials

### On MacOS

https://blog.6nok.org/how-i-use-nix-on-macos/

### Flakes

https://www.youtube.com/watch?v=cw4wJjjQYMU
https://www.youtube.com/watch?v=S3VBi6kHw5c

## For devops / CD

https://lewo.abesis.fr/posts/from-push-to-pull-deployment/

## Evangelisation

https://www.youtube.com/watch?v=CwfKlX3rA6E "One day, as happens now and then with a bleeding-edge rolling release distro, a systemd update reversed my mouse buttons. The great thing about rolling-release and cutting-edge distributions like Arch Linux, is that you get to be a beta tester, whether you like it or not! I thought this was the way it had to be on Linux: Stability or cutting-edge features, not both. But that wasn't right at all, with NixOS you can have everything, everywhere all at once!"

## Comments

- https://lwn.net/Articles/962788/ "A look at Nix and Guix"
- https://www.dgt.is/blog/2025-01-10-nix-death-by-a-thousand-cuts/ "Nix - Death by a thousand cuts"
    - The author, a seasoned software engineer with extensive Linux experience, details their two-year journey using NixOS as their primary operating system. They praise Nix's declarative configuration, reproducibility, easy service management, and ephemeral development shells. However, they ultimately conclude that NixOS, in its current state (2025), is not recommended for desktop use, even for experienced Linux users. The author highlights issues such as the complexity of the Nix language, inconsistent package quality and documentation, resource usage, and a fragmented workflow due to multiple ways of achieving the same task. They also describe numerous specific problems encountered with desktop integration, ZFS setup, symbolic links, development tools like npm and Conda, and various applications. Despite appreciating Nix's potential and the helpful community, the author decides to scale back their NixOS usage, citing the constant need for troubleshooting and the feeling of being stuck in "Nix Purgatory" – aware of Nix's benefits but burdened by its complexities.
- https://news.ycombinator.com/item?id=42666851 HN comments on the previous post

## Tools

- https://github.com/hercules-ci/arion "a tool for building and running applications that consist of multiple docker containers using NixOS modules. It has special support for docker images that are built with Nix, for a smooth development experience and improved performance."

- https://github.com/tweag/genealogos "a Nix sbom generator"

- https://github.com/nix-community/vulnix Vulnerability (CVE) scanner for Nix/NixOS.

- https://github.com/nix-community/dream2nix Simplified nix packaging for various programming language ecosystems
- Also: poetry2nix, gradle2nix, etc.

## References

### Meta

- [Awesome Nix](https://github.com/nix-community/awesome-nix)

### Nix  tutorials / intros

- [Learn Nix the Fun Way](https://fzakaria.com/2024/07/05/learn-nix-the-fun-way.html)
- [Nix Tutorials](https://nix.dev/tutorials/#tutorials)
- [NixOS Wiki - Main Page](https://nixos.wiki/wiki/Main_Page)
- [Nix Manual (Stable)](https://nixos.org/manual/nix/stable/)
- [Nix Pills](https://nixos.org/guides/nix-pills/)
- https://serokell.io/blog/what-is-nix
- [Nix by example](https://mimoo.github.io/nixbyexample/)
- https://nixos.asia/en/blog/replacing-docker-compose

### Nixpkgs

- [Nixpkgs Manual (Stable)](https://nixos.org/manual/nixpkgs/stable/)
- [Nixpgs on GitHub](https://github.com/NixOS/nixpkgs)

### NixOS

- [NixOS Manual (Stable)](https://nixos.org/manual/nixos/stable/)
- [NixOS Installation Guide](https://nixos.org/manual/nixos/stable/#sec-installation)

### Flakes

- [NixOS Wiki - Flakes](https://nixos.wiki/wiki/Flakes)
- [Practical Nix Flake Anatomy: A Guided Tour of flake.nix](https://vtimofeenko.com/posts/practical-nix-flake-anatomy-a-guided-tour-of-flake.nix/)
- [Learn Flakes the Fun Way](https://lyte.dev/blog/learn-flakes-the-fun-way/)
- [Nix Flakes RFC](https://github.com/NixOS/rfcs/pull/49)
- [Flakes on Discourse](https://discourse.nixos.org/t/nix-flakes-impressions-feedback/6521)
- https://serokell.io/blog/practical-nix-flakes
- [Flakes in Action](https://www.tweag.io/blog/2020-05-25-flakes/)
- [Nix Flakes and Purely Functional Package Management](https://serokell.io/blog/nix-flakes)

### Nickel

- https://www.tweag.io/blog/2024-06-20-nickel-modules/

### Blogs

- [NixOS Blog](https://nixos.org/blog.html)
- https://www.tweag.io/blog/tags/nix/
- https://serokell.io/blog/nix

<!-- Keywords -->
#nixos #nix #nixpkgs #docker
<!-- /Keywords -->
