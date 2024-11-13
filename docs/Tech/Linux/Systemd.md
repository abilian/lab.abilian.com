
## References

https://christine.website/talks/systemd-the-good-parts-2021-05-16
https://seb.jambor.dev/posts/systemd-by-example-part-1-minimization/


## Discussion

Systemd is a modern init system and service manager for Linux-based operating systems. Initially introduced as a replacement for the traditional initd system, systemd has evolved into a powerful supervisor that includes functionalities such as logging, network configuration, and network time synchronization. It provides a flexible, portable way to define daemons and their dependencies, and a uniform interface to control the configuration. This post delves into the architecture, key features, and practical usage of systemd, highlighting its importance in contemporary Linux distributions.

## Historical Context

Before systemd, Linux systems predominantly used the System V init system. This traditional init system, while functional, suffered from several limitations:

- **Sequential Initialization:** System V init starts services in a strictly sequential manner, which can lead to slow boot times.
- **Lack of Dependency Management:** Dependencies between services are managed manually via scripting, increasing complexity and potential for errors.
- **Limited Functionality:** The traditional init system lacks many modern features such as socket activation, parallel service startup, and dynamic management of service states.

Systemd was introduced to address these issues, offering a more dynamic and efficient approach to service management. Almost all current Linux distributions have adopted systemd, including Fedora (since May 2011), openSUSE (since September 2012), CentOS (since April 2014), RHEL (since June 2014), SUSE Linux (since October 2014), Debian (since April 2015), and Ubuntu (since April 2015).

## Architecture of Systemd

Systemd's architecture is composed of several components and design principles that contribute to its robustness and flexibility:

1. **Unit Files:** The core concept in systemd, units represent system resources such as services, sockets, devices, and mount points. Units are defined in configuration files with extensions such as `.service`, `.socket`, `.device`, and others.

2. **Systemd Daemon (`systemd`):** This is the central management process that starts and supervises other processes. It uses unit files to manage the services and system states.

3. **Journal (`journald`):** A logging service that captures logs from the kernel, services, and other system components, providing a centralized log management system.

4. **Socket Activation:** Systemd can start services on-demand when a socket receives a connection, improving system performance and reducing resource usage.

5. **D-Bus Integration:** Systemd integrates with D-Bus, allowing for inter-process communication and dynamic interaction between services.

6. **Targets:** Targets group units into logical entities, allowing for complex dependencies and ordered startup sequences. Examples include `multi-user.target` and `graphical.target`.

7. **cgroups (Control Groups):** Systemd uses cgroups to manage resource allocation and limit resources for services, enhancing system stability and security.

## Key Features

Systemd offers numerous features that enhance the functionality and management of Linux systems:

- **Parallel Service Startup:** Systemd can start multiple services concurrently, significantly reducing boot times.
- **Dependency Management:** Automatic handling of service dependencies ensures that services are started and stopped in the correct order.
- **On-Demand Activation:** Services can be started on-demand using socket, bus, path, and timer activation.
- **Unified Logging:** `journald` provides a centralized logging mechanism, simplifying log management and analysis.
- **Snapshot and Restore:** System states can be saved as snapshots and restored, facilitating system recovery and testing.
- **Resource Control:** Integration with cgroups allows fine-grained resource control and monitoring for services.

## Units in Systemd

A unit in systemd is a logical grouping with different semantics depending on its function and/or the resource it targets. Systemd distinguishes a number of units based on the target resource:

- **Service Units:** Describe how to manage a service or application.
- **Target Units:** Capture dependencies.
- **Mount Units:** Define a mount point.
- **Timer Units:** Define timers for scheduled tasks.
- **Socket Units:** Describe a network or IPC socket.
- **Device Units:** For udev or sysfs filesystems.
- **Automount Units:** Configure automatic mount points.
- **Swap Units:** Describe swap space.
- **Path Units:** For path-based activation.
- **Snapshot Units:** Allow for reconstructing the current state of the system after changes.
- **Slice Units:** Associated with cgroups.
- **Scope Units:** Manage sets of system processes created externally.

## Configuration Files

To be recognized by systemd, a unit needs to be serialized into a file. Systemd looks for unit files in multiple locations:

- **/lib/systemd/system:** Package-installed units.
- **/etc/systemd/system:** System admin–configured units.
- **/run/systemd/system:** Nonpersistent runtime modifications.

## Management with systemctl

The primary tool for interacting with systemd to manage services is `systemctl`. Below are some often-used commands:

- **Enable the service:**
  ```bash
  sudo systemctl enable <service_name>.service
  ```
- **Reload all unit files:**
  ```bash
  sudo systemctl daemon-reload
  ```
- **Start the service:**
  ```bash
  sudo systemctl start <service_name>.service
  ```
- **Stop the service:**
  ```bash
  sudo systemctl stop <service_name>.service
  ```
- **Restart the service:**
  ```bash
  sudo systemctl restart <service_name>.service
  ```
- **Reload service configuration:**
  ```bash
  sudo systemctl reload <service_name>.service
  ```
- **Stop service execution:**
  ```bash
  sudo systemctl kill <service_name>.service
  ```
- **Get a summary of service state:**
  ```bash
  systemctl status <service_name>.service
  ```

## Additional Command-Line Tools

The systemd ecosystem includes several other command-line tools:

- **bootctl:** Check boot loader status and manage available boot loaders.
- **timedatectl:** Set and view time- and date-related information.
- **coredumpctl:** Process saved core dumps, useful for troubleshooting.

## Monitoring with journalctl

The journal, managed by the `systemd-journald` daemon, provides a centralized location for all messages logged by systemd components. Use `journalctl` to view logs:

- **View logs for a specific service:**
  ```bash
  journalctl -u <service_name>.service
  ```
- **Follow logs in real-time:**
  ```bash
  journalctl -f -u <service_name>.service
  ```

## Example: Scheduling a Greeter Application

To illustrate systemd in action, consider the example of launching a greeter application every hour.

1. **Define a service unit file (`greeter.service`):**

```ini
[Unit]
Description=My Greeting Service

[Service]
Type=oneshot
ExecStart=/home/user/greeter.sh
```

1. **Define a timer unit file (`greeter.timer`):**

```ini
[Unit]
Description=Runs Greeting service at the top of the hour

[Timer]
OnCalendar=hourly
```

1. **Copy both unit files to `/run/systemd/system`:**

```bash
sudo cp greeter.service greeter.timer /run/systemd/system/
```

4. **Enable and start the timer:**

```bash
sudo systemctl enable greeter.timer
sudo systemctl start greeter.timer
```

5. **Check the status of the timer:**

```bash
sudo systemctl status greeter.timer
```

6. **Verify the greeter service logs:**

```bash
journalctl -f -u greeter.service
```

## Controversies

Systemd has been at the center of several controversies and debates within the Linux and open-source communities since its inception. These controversies often stem from systemd's design decisions, its impact on the Linux ecosystem, and philosophical disagreements among developers and users. Below, I outline some of the key controversies surrounding systemd:

### Monolithic Design

One of the main criticisms of systemd is its monolithic design. Unlike the traditional Unix philosophy of "do one thing and do it well," systemd integrates a wide range of functionalities, including:

- Init system
- Logging (`journald`)
- Network management (`networkd`)
- Time synchronization (`timesyncd`)
- Device management (`udevd` integration)
- Service management 
- and more

Critics argue that this violates the modular approach traditionally favored in Unix-like systems, where small, single-purpose tools work together. They fear that systemd's complexity and integration could lead to a single point of failure and make the system harder to debug and maintain.

### Complexity and Learning Curve

Systemd introduces a new set of concepts, terminologies, and configurations, which can be daunting for users and administrators familiar with traditional init systems. The steep learning curve and the departure from well-known tools and practices have been points of contention.

### Compatibility and Lock-In

Systemd's widespread adoption has led to concerns about lock-in and compatibility. As more Linux distributions and software projects depend on systemd, it becomes harder to switch to or support alternative init systems. This dependency can be seen as reducing the diversity and flexibility traditionally enjoyed by Linux users.

### Boot Speed vs. Reliability

While systemd promises faster boot times through parallel service startup and on-demand activation, some users have reported issues with reliability and stability. Critics argue that the pursuit of faster boot times should not come at the expense of a stable and reliable system.

### Security Concerns

The extensive functionality and complexity of systemd have raised security concerns. Critics argue that the larger codebase and increased attack surface could lead to more vulnerabilities. While systemd's developers are vigilant about security, the potential risks remain a point of debate.

### Controversial Decisions and Development Practices

Some of the controversies around systemd are also tied to the decisions and practices of its lead developers. For instance, the decision to replace the traditional syslog system with journald was met with resistance. Additionally, the perceived dismissiveness of criticism by some of the project's maintainers has fueled further discontent.

### Community Forks and Alternatives

The controversies surrounding systemd have led to the creation of forks and alternative init systems by those seeking to maintain traditional approaches. Some notable efforts include:

- **Devuan**: A fork of Debian that replaces systemd with sysvinit or other init systems, aiming to provide a systemd-free environment.
- **OpenRC**: A dependency-based init system used by Gentoo Linux, designed to work with the existing sysvinit.
- **runit**: A simple and fast init system that provides process supervision and is used by distributions like Void Linux.
- **s6**: A set of small utilities for process supervision, which can be used as an alternative init system.

### Lessons learned

The controversies surrounding systemd highlight the tension between innovation and tradition in the Linux ecosystem. While systemd brings numerous benefits in terms of performance, functionality, and modern system management, it also challenges long-standing practices and philosophies. The debates around systemd are likely to continue as the Linux community navigates the balance between embracing new technologies and preserving the principles that have long guided Unix-like systems.

## Conclusion

Systemd represents a significant advancement in Linux system management, addressing many of the deficiencies of older init systems. Its robust architecture, extensive feature set, and flexibility make it an essential tool for modern Linux administrators. Understanding and effectively utilizing systemd can lead to more efficient system management, improved performance, and greater stability.

<!-- Keywords -->
#systemd
<!-- /Keywords -->
