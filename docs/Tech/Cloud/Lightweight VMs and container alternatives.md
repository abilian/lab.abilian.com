#cloud #virtualisation #cloud #public

## Lighweight VMS

- https://firecracker-microvm.github.io/
- Kata containers: https://katacontainers.io/
- https://github.com/newsnowlabs/runcvm

## Unikernels

- https://nanos.org/
- https://github.com/solo-io/unik

## More

- https://github.com/containers/bubblewrap
- https://github.com/opencontainers/runc
- https://github.com/netblue30/firejail
- https://libriscv.no/
- https://github.com/varnish/tinykvm/

## Posts

- https://mergeboard.com/blog/2-qemu-microvm-docker/

- https://fly.io/blog/docker-without-docker/

- https://hocus.dev/blog/qemu-vs-firecracker/

> Firecracker, the microVM hypervisor, is renowned for being lightweight, fast, and secure. It's excellent for running short-lived workloads, which is why it's the backbone of AWS Lambda. After weeks of testing, we decided to entirely replace it with QEMU. A little-known fact about Firecracker is its lack of support for many modern hypervisor features, such as dynamic RAM management, which is vital for long-lived workloads. In this post, I will explain why Firecracker might not be the best hypervisor choice and when you should avoid it.

## Jail

- https://github.com/fsquillace/junest = The lightweight Arch Linux based distro that runs, without root privileges, upon any Linux distro
- https://nsjail.dev/ "NsJail is a lightweight process isolation tool leveraging Linux namespaces and seccomp-bpf to enhance security and resource management across our infrastructure."
    - → [[Nsjail]]

## Other approaches

- Nixos
- https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html
- LXC

## Specific to one language

### Python

- https://github.com/zopefoundation/RestrictedPython (still actively developped, actually)

## Historical (obsolete) approaches

- https://en.wikipedia.org/wiki/ZeroVM


<!-- Keywords -->
#qemu #vms
<!-- /Keywords -->
