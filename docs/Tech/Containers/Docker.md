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
