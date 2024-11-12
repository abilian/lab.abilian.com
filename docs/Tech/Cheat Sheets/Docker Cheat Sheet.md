
1.  `docker run`: Runs a container from an image.
2.  `docker start`: Starts a container that has been stopped.
3.  `docker stop`: Stops a running container.
4.  `docker restart`: Restarts a running container.
5.  `docker rm`: Removes a container.
6.  `docker rmi`: Removes an image.
7.  `docker ps`: Lists all running containers.
8.  `docker images`: Lists all images on the system.
9.  `docker exec`: Runs a command in a running container.
10.  `docker build`: Builds an image from a Dockerfile.
11.  `docker pull`: Pulls an image from a registry
12.  `docker push`: Pushes an image to a registry.
13.  `docker login`: Logs in to a registry.
14.  `docker logout`: Logs out of a registry.
15.  `docker cp`: Copies files or directories between a container and the host machine.
16.  `docker volume`: Manages volumes for containers.
17.  `docker network`: Manages networks for containers.

Example:

```shell
# Run a container from the image "myimage"
docker run -it myimage

# Start a container named "mycontainer"
docker start mycontainer

# Stop a container named "mycontainer"
docker stop mycontainer

# Remove a container named "mycontainer"
docker rm mycontainer

# Remove an image named "myimage"
docker rmi myimage

# List all running containers
docker ps

# Build an image from the Dockerfile in the current directory
docker build -t myimage .

# Pull an image named "myimage" from the "myregistry" registry
docker pull myregistry/myimage

# Push an image named "myimage" to the "myregistry" registry
docker push myregistry/myimage
```

Note: (Almost) Always use `--rm` option while running the container to remove the container automatically when it exits.

#docker

<!-- Keywords -->
#docker #dockerfile
<!-- /Keywords -->
