Docker is an open-source platform that uses OS-level virtualization to deliver software in packages called containers. Containers are lightweight, making it easier to create, deploy, and run applications by using containers.

### Why Docker?

- **Solves local development issues:** Ensures consistency by packaging the application and its dependencies into a container.
- **Simplifies deployment:** Containers run the same, regardless of where they are deployed.
- **Scalability and efficiency:** Containers can be easily scaled and are more resource-efficient than traditional virtual machines.
## Why NOT Docker?

1. **Performance Overhead**: Containers can introduce slight overhead, impacting high-performance applications that demand maximum resource efficiency.
2. **Security Concerns**: Sharing the host OS kernel poses security risks. If a container is compromised, it could potentially threaten the host system or other containers.
3. **Complexity in Large Systems**: Managing a vast number of containers and microservices can become challenging, requiring advanced orchestration tools like Kubernetes, which add their own complexity.
4. **Persistent Data Management**: Handling persistent data for stateless containers requires additional strategies, such as mounting volumes, which can complicate deployment and management.
5. **Compatibility and Limitations**: Docker may face compatibility issues on non-Linux systems and might not suit applications with specific hardware access needs.
6. **Learning Curve**: Docker and its ecosystem have a significant learning curve, requiring time and effort to master.
7. **Operational Changes**: Integrating Docker into existing workflows and infrastructure demands operational adjustments and possible retraining of staff.
8. **Network Complexity**: Setting up networking for containers, especially in complex architectures, can be daunting and requires a solid understanding of Docker's networking capabilities.

Alternatives like direct virtual machine usage, other container technologies (e.g., Podman), or platform-specific deployment solutions might better suit certain projects, depending on specific needs and constraints.

### Key Docker Concepts / Components

- **Container:** An isolated environment for running an application, including all necessary code, runtime, system tools, libraries, and settings.
- **Image:** A lightweight, standalone, executable package that includes everything needed to run a piece of software, including the code, runtime, libraries, environment variables, and config files.
- **Dockerfile:** A script containing a series of instructions on how to build a Docker image.
- **Docker Compose:** A tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application's services, and then, with a single command, create and start all the services from your configuration.
- **Docker Hub:** A cloud-based registry service for building and shipping containerized applications.

### Understanding Containers and Virtual Machines (VMs)

- **Containers vs. VMs:** Containers share the host system’s kernel, while VMs include a full copy of an operating system, a virtual copy of the hardware that the OS requires to run. This makes containers much more lightweight and faster than VMs.

### Getting Started with Docker

To begin using Docker, you create a Dockerfile to specify the environment of your application, build an image from this Dockerfile, and then run the image as a container. Containers can be easily distributed and run on any system that has Docker installed, facilitating easy deployment and scaling.

### Docker and the Cloud

Docker images can be stored in Docker Hub or any other container registry, making it easy to share and deploy them across various environments, including cloud platforms. Containers can be orchestrated using services like Kubernetes to manage and scale applications dynamically across clusters of hosts.

## Cheat sheet

- Cleanup: `docker container prune` & `docker image prune`

See also: [[Dockerfile Cheat Sheet]]

## Sample dockerfiles

- https://github.com/postgis/docker-postgis

## Tutorial

- <https://container.training/>

## Best practices

- https://docs.docker.com/engine/reference/builder/
- https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
- https://github.com/RedCoolBeans/dockerlint

## Tools

- https://gitlab.com/stavros/harbormaster : Harbormaster is a small utility that lets you easily deploy multiple Docker-Compose applications on a single host. It does this by taking a list of git repository URLs that contain Docker Compose files and running the Compose apps they contain. It will also handle updating/restarting the apps when the repositories change.
- https://github.com/goldmann/docker-squash.git : Docker image squashing tool

#docker 


## TIL

### `expose` vs. `ports`

The `expose` and `ports` directives in a Docker Compose configuration file allow you to specify how Docker handles networking between the containers themselves and between the containers and the host machine. They are used to define how network connections are handled, but they function in subtly different ways:

1. `expose`: This directive is used to inform Docker that the container listens on the specified network ports at runtime. However, this does not mean these ports are accessible from the host or other networks. It's more like a documentation between the person who builds the image and the person who runs the container, about which ports are intended to be used.

2. `ports`: This directive actually publishes the port to the host machine, meaning the specified ports on the container are accessible on the host machine. They are bound to an interface on the host. The `ports` directive allows you to map a port on the host machine to a port on the container.

Here's a small example illustrating the difference:

```yaml
version: '3'
services:
  web:
    image: nginx:latest
    expose:
      - "8000"
    ports:
      - "8080:80"
```

In this case, the `nginx` service is exposing port `8000` within the Docker network (though the `nginx` image doesn't actually use this port), but this port is not accessible on the host. On the other hand, the service is also mapping port `8080` on the host to port `80` on the container, so you can access the `nginx` server at `http://localhost:8080` on the host machine.

### Working with Docker Containers Made Easy with the dexec Bash Script

> One of the powerful features [Docker](https://www.docker.com/) offers is the ability to interact with running containers. However, manually entering the necessary commands to access a container can be clunky. This motivated me to write this simple `dexec` script to make running commands through my Docker containers less clunky. I’ll show you what dexec is and how to use it!
> https://spin.atomicobject.com/2023/06/26/dexec-docker/