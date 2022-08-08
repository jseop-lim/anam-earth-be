#!/bin/bash

# Import configurations
source config.sh

# Install backend docker image and erase previous image
#docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_ACCESS_TOKEN
docker compose pull

if [ "$(docker ps -aq -f name=anam-earth-backend)" ]; then
    # Stop and remove backend container
    docker compose rm backend -sf
fi

# Create and run docker containers
docker compose up -d
docker image prune -f
# Migrate Database
docker exec -it anam-earth-backend bash -c "python manage.py migrate --settings=config.settings.prod"
# Reload Nginx in docker container
docker exec -it nginx bash -c "nginx -s reload"