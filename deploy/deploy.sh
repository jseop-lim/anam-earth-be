#!/bin/bash

# Stop backend docker container
docker compose down anam-earth-backend

# Install backend docker image and erase previous image
docker login -u qaws1000 -p clark0116*
docker compose pull
docker image prune -f
docker images

# Run backend docker container
docker compose up anam-earth-backend -d
docker exec -it anam-earth-backend bash -c "python manage.py migrate --settings=config.settings.prod"

# Reload Nginx in docker container
docker exec -it nginx bash -c "nginx -s reload"
nginx -s reload