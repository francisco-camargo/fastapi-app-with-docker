Deploy FastAPI Application via Docker
=====================================

Following [FastAPI docs](https://fastapi.tiangolo.com/deployment/docker/)

Following [How to create a great dev environment with Docker](https://youtu.be/0H2miBK_gAk?si=lllFonixFqUq58Eq) by Patrick Loeber.

In it's current state, you run the app via `docker-compose` as detailed below.

# Docker Image and Container

This section is for reference, and is not the recommended way to run the app.

Build the image

```bash
docker build -t fastapi-app-with-docker .
```

Run Docker container using

```bash
. /start_container.sh
```

View docs at [http://localhost/docs](http://localhost/docs)

To check if a container was made, run

`docker inspect <container tag>`

# docker-compose

Docker compose is how this app will actually run since it will use both the app image and the redis image.

Kick things off with

```bash
docker-compose up
```

Use the `--build` option to rebuild the image. Use `-d` option for detached mode.

Can stop the container with `Ctrl+C`, then to get rid of the container stack, use

```bash
docker-compose down
```

# Use VSCode via WSL
[dev-workflow/vscode](https://github.com/francisco-camargo/dev-workflow/blob/main/src/vscode/README.md)
