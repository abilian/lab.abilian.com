
## On ARM

https://nixos.wiki/wiki/NixOS_on_ARM/QEMU
→ Fail.

## On Ubuntu

There is a `nix-bin` package.

https://launchpad.net/ubuntu/noble/+package/nix-bin

" NOTE: This package only provides the nix binaries. One still needs  
 to setup directories, environments variables and configuration files  
 to use nix as described in the nix manual.  
 The package nix-setup-systemd provides such a setup using systemd  
 mechanisms, also see /usr/share/doc/nix-bin/README.Debian."

https://news.ycombinator.com/item?id=32602772
"The package you want on Debian is called nix-systemd-setup or something like that, not nix-bin. (nix-bin just gives you the Nix binary, and I guess if you created /nix yourself you could use it for a single-user install.) The expectation is that you want a multiuser install, which requires a running daemon and the creation of some system users, and the nix setup package handles that. I think the package descriptions do outline this, and FTR you almost never want just a `-bin` package on Debian-based distros. The convention is used to allow minimal installation of just the binaries from packages when they're likely to be used by other parts of the system rather than end users.

The Nix package for Debian has some other deviations in the way it's plugged into the system and the initial setup. The default channel (source of packages) doesn't get set up for you, the PATH ordering is different, and NIX_PATH and the NIX_PROFILES_PATH (and maybe PATH?) aren't configured for `env_keep` with PAM's `sudo` configuration so interactions with `sudo` are different. Anyway failure to find any packages is probably due to the lack of enabled channels or the setup not being completed (needing that systemd-setup package).

(All of this stuff is up to the maintainers of the Debian package and Debian policy. It's fine, but it violates the assumptions of some third-party Nix tooling.)"


→ It seems to be frowned upon by Nix developers: https://discourse.nixos.org/t/question-about-nix-bin-package-in-ubuntu/41806

<!-- Keywords -->
#nixos_on_arm #nix_path #nix #nixos #nix_profiles_path
<!-- /Keywords -->
