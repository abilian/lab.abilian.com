OSTree is an upgrade system for Linux-based operating systems that performs atomic upgrades of complete filesystem trees. It is not a package system; rather, it is intended to complement them. A primary model is composing packages on a server, and then replicating them to clients.

The underlying architecture might be summarized as “git for operating system binaries”. It operates in userspace, and will work on top of any Linux filesystem. At its core is a git-like content-addressed object store with branches (or “refs”) to track meaningful filesystem trees within the store. Similarly, one can check out or commit to these branches.

Layered on top of that is bootloader configuration, management of `/etc`, and other functions to perform an upgrade beyond just replicating files.

You can use OSTree standalone in the pure replication model, but another approach is to add a package manager on top, thus creating a hybrid tree/package system.

## References

- https://ostreedev.github.io/ostree/
- https://fedoraproject.org/atomic-desktops/
- https://community.sap.com/t5/open-source-blogs/can-garden-linux-benefit-from-ostree-for-in-place-upgrades/ba-p/13554431 / https://github.com/gardenlinux/ostree-image-builder
- http://linux-vserver.org/index.php?title=util-vserver:Vhashify&oldid=2285
