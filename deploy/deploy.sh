#!/bin/bash

cd ~/anam-earth/deploy

# Stop and remove containers
docker compose down

# Import configurations and Docker Hub login
source config.sh
docker login -u $DOCKER_HUB_USERNAME -p $DOCKER_HUB_ACCESS_TOKEN

# Install backend docker image and erase previous image
docker compose pull

# Create and run docker containers
docker compose up -d
docker image prune -f
# Migrate Database
docker exec anam-earth-backend bash -c "python manage.py migrate --settings=config.settings.prod"
# Reload Nginx in docker container
docker exec nginx bash -c "nginx -s reload"