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

### Top 8 Must-Know Docker Concepts

#### Dockerfile

**Definition**: A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image. It's the blueprint for creating Docker images.

**Key Points**:
- **Base Image**: The starting point for your image, usually an existing image from Docker Hub.
- **Instructions**: Commands such as `FROM`, `RUN`, `COPY`, `CMD`, etc., define what the image contains and what it does.
- **Layered Build**: Each instruction in a Dockerfile creates a new layer in the image, contributing to Docker's efficient storage and transfer mechanisms.

**Example**:
```Dockerfile
FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

---

#### Docker Image

**Definition**: A Docker image is a read-only template that contains a set of instructions for creating a container. It includes the application code, libraries, dependencies, and other files needed for the application to run.

**Key Points**:
- **Layered Architecture**: Images are built in layers, which can help with storage efficiency and quicker deployments.
- **Immutability**: Once built, images do not change. Any changes require creating a new image.
- **Versioning**: Images can be versioned with tags, making it easy to manage different versions of an application.

**Example Command**:
```sh
docker build -t myapp:1.0 .
```

---

#### Docker Container

**Definition**: A Docker container is a runnable instance of a Docker image. It encapsulates the application along with its environment and dependencies, ensuring that it runs consistently across different environments.

**Key Points**:
- **Isolation**: Containers run in isolation from each other and the host system, providing a secure environment.
- **Ephemeral Nature**: Containers are designed to be transient. They can be stopped and started quickly, and any data not stored in volumes or persistent storage is lost when the container stops.
- **Portability**: Containers can run on any system that has Docker installed, making them highly portable.

**Example Command**:
```sh
docker run -d -p 8080:80 myapp:1.0
```

---

#### Docker Registry

**Definition**: A Docker registry is a centralized repository where Docker images are stored, shared, and managed. Docker Hub is the default public registry, but private registries can also be set up.

**Key Points**:
- **Public and Private**: Docker Hub offers public repositories, while private registries can be hosted on-premises or in the cloud.
- **Versioning and Tagging**: Registries support tagging images, which helps in version control and easy retrieval of specific image versions.
- **Access Control**: Private registries provide mechanisms to control who can access or push images.

**Example Commands**:
```sh
docker push myapp:1.0
docker pull myapp:1.0
```

---

#### Docker Volumes

**Definition**: Docker volumes are used to persist data generated by and used by Docker containers. Volumes are stored outside the container’s file system, allowing data to persist even after the container is deleted.

**Key Points**:
- **Persistence**: Volumes ensure that data is not lost when a container stops or is removed.
- **Sharing Data**: Volumes can be shared between multiple containers, facilitating data exchange and consistency.
- **Decoupling**: By decoupling storage from the container lifecycle, volumes provide more flexibility in managing data.

**Example Command**:
```sh
docker run -d -v myvolume:/data myapp:1.0
```

---

#### Docker Compose

**Definition**: Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application’s services, networks, and volumes.

**Key Points**:
- **Multi-Container Applications**: Simplifies the management of applications that require multiple services running in different containers.
- **Configuration**: Uses a `docker-compose.yml` file to define services, networks, and volumes.
- **Orchestration**: Provides commands to manage the full lifecycle of the application, including starting, stopping, and rebuilding services.

**Example `docker-compose.yml`**:
```yaml
version: '3'
services:
  web:
    image: myapp:1.0
    ports:
      - "8080:80"
    volumes:
      - myvolume:/data
  db:
    image: postgres:13
    volumes:
      - dbdata:/var/lib/postgresql/data
volumes:
  myvolume:
  dbdata:
```

---

#### Docker Networks

**Definition**: Docker networks enable communication between Docker containers and between containers and the host system. Networks can be created to isolate containers or allow selective communication.

**Key Points**:
- **Network Types**: Bridge, host, and overlay networks each serve different purposes, from single-host setups to multi-host clusters.
- **Isolation**: By default, containers on different networks cannot communicate with each other, enhancing security.
- **Customization**: Custom networks can be created to meet specific application requirements, such as enabling specific containers to communicate while isolating others.

**Example Command**:
```sh
docker network create mynetwork
docker run -d --network=mynetwork myapp:1.0
```

---

#### Docker CLI

**Definition**: The Docker Command Line Interface (CLI) is the primary tool for interacting with Docker. It provides commands to build images, run containers, manage volumes, and perform other Docker operations.

**Key Points**:
- **Comprehensive Command Set**: The CLI supports a wide range of operations, from basic tasks like building images and running containers to advanced tasks like configuring networks and managing Swarm clusters.
- **Interactive and Scriptable**: Commands can be run interactively in a terminal or included in scripts for automation.
- **Help and Documentation**: The CLI includes built-in help for all commands, making it easier to learn and use Docker effectively.

**Example Commands**:
```sh
docker build -t myapp:1.0 .
docker run -d -p 8080:80 myapp:1.0
docker volume create myvolume
docker network create mynetwork
```

<!-- Keywords -->
#docker #kubernetes #dockerfiles #dockerfile
<!-- /Keywords -->
