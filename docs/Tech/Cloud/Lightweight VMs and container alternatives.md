#cloud #virtualisation #cloud #public

## Lighweight VMS

- https://firecracker-microvm.github.io/
- Kata containers
- https://github.com/newsnowlabs/runcvm

## Unikernels

- https://nanos.org/
- https://github.com/solo-io/unik

## Posts

- https://mergeboard.com/blog/2-qemu-microvm-docker/

- https://fly.io/blog/docker-without-docker/

https://hocus.dev/blog/qemu-vs-firecracker/
> Firecracker, the microVM hypervisor, is renowned for being lightweight, fast, and secure. It's excellent for running short-lived workloads, which is why it's the backbone of AWS Lambda. After weeks of testing, we decided to entirely replace it with QEMU. A little-known fact about Firecracker is its lack of support for many modern hypervisor features, such as dynamic RAM management, which is vital for long-lived workloads. In this post, I will explain why Firecracker might not be the best hypervisor choice and when you should avoid it.

## Jail

- https://github.com/fsquillace/junest = The lightweight Arch Linux based distro that runs, without root privileges, upon any Linux distro

## Other approaches

- Nixos
- https://www.freedesktop.org/software/systemd/man/systemd-nspawn.html
- LXC

<!-- Keywords -->
#qemu #docker #hypervisor #virtualisation #microvm
<!-- /Keywords -->
