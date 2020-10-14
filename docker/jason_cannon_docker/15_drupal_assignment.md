# Drupal assignment

    Running container example:

    docker run --name web --network blog -p 80:80 --mount src=blog_web_data,dst=/var/www/html -dit php:apache

    Setting environment variables example:

    docker run --name db --network blog -e MYSQL_ROOT_PASSWORD=pw123 -e MYSQL_DATABASE=wordpress --mount src=blog_db_data,dst=/var/lib/mysql -d mariadb

# Start a db container

    Command used:

    docker run -d --name db --network drupal -e POSTGRES_USER=drupal -e POSTGRES_PASSWORD=pw123 -e POSTGRES_DB=drupal --mount src=db,dst=/var/lib/postgresql/data postgres:11.5

## Start a drupal application container

    docker run -d --name drupal --network drupal -p 7070:80 drupal:8.7.7

