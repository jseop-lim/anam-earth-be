#!/bin/bash

django_env_path=$GITHUB_WORKSPACE/backend/.env.prod

echo "SECRET_KEY=${{ secrets.SECRET_KEY }}" >> $django_env_path
echo "MYSQL_ROOT_PASSWORD=${{ secrets.MYSQL_ROOT_PASSWORD }}" >> $django_env_path
echo "MYSQL_DATABASE=${{ secrets.MYSQL_DATABASE }}" >> $django_env_path
echo "MYSQL_USER=${{ secrets.MYSQL_USER }}" >> $django_env_path
echo "MYSQL_PASSWORD=${{ secrets.MYSQL_PASSWORD }}" >> $django_env_path

deploy_config_file=$GITHUB_WORKSPACE/deploy/config.sh

echo "#!/bin/bash" >> $deploy_config_file
echo "DOCKER_HUB_USERNAME=${{ secrets.DOCKER_HUB_USERNAME }}" >> $deploy_config_file
echo "DOCKER_HUB_ACCESS_TOKEN=${{ secrets.DOCKER_HUB_ACCESS_TOKEN }}" >> $deploy_config_file
