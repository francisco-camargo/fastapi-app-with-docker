Deploy FastAPI Application via Docker
=====================================

Following [FastAPI docs](https://fastapi.tiangolo.com/deployment/docker/)

Following [How to create a great dev environment with Docker](https://youtu.be/0H2miBK_gAk?si=lllFonixFqUq58Eq)

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
