Deploy FastAPI Application via Docker
=====================================

Following [FastAPI docs](https://fastapi.tiangolo.com/deployment/docker/)

Build the image
```bash
docker build -t myimage .
```

Start Docker container
```bash
docker run -d --name mycontainer -p 80:80 myimage
```