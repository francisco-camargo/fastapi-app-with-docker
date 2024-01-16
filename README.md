Deploy FastAPI Application via Docker
=====================================

Following [FastAPI docs](https://fastapi.tiangolo.com/deployment/docker/)

Following [How to create a great dev environment with Docker](https://youtu.be/0H2miBK_gAk?si=lllFonixFqUq58Eq)

Build the image

```bash
docker build -t myimage .
```

Start Docker container

```bash
docker run -d --name mycontainer -p 80:80 myimage
```

View docs at `http://localhost/docs`

To check if a container was made, run

`docker inspect <container tag>`

Was able to add a Docker volume via `start_container.sh`
