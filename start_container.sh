docker run \
  -d \
  --name fastapi-app-with-docker \
  -p 80:80 \
  -v /${PWD}/app:/code/app \
  fastapi-app-with-docker
