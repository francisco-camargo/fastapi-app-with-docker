docker run \
  -d \
  --name mycontainer \
  -p 80:80 \
  -v /${PWD}/app:/code/app \
  myimage
