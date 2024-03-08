#docker

1.  `FROM`: Specifies the base image to use for the build.
2.  `RUN`: Runs a command during the build process.
3.  `COPY`: Copies files or directories from the host machine to the container.
4.  `ENV`: Sets an environment variable in the container.
5.  `EXPOSE`: Exposes a port or ports to be used by the container.
6.  `ENTRYPOINT`: Specifies the command to run when the container starts.
7.  `CMD`: Specifies default arguments for the `ENTRYPOINT` command.
8.  `USER`: Sets the user and group to run the container as.
9.  `WORKDIR`: Sets the working directory for commands run in the container.
10.  `VOLUME`: Creates a mount point for a volume in the container.

Example:

```Dockerfile
FROM alpine
RUN apk update && apk add python3
COPY myfile.txt /app
ENV MY_ENV_VAR=value
EXPOSE 8080
ENTRYPOINT ["python3"]
CMD ["app.py"]
USER 1001
WORKDIR /app
VOLUME /data
```

Note: Always try to use specific version of base images and package to avoid any unexpected behaviour.

## Other cheat sheets and official doc
- https://kapeli.com/cheat_sheets/Dockerfile.docset/Contents/Resources/Documents/index
- https://docs.docker.com/engine/reference/builder/

