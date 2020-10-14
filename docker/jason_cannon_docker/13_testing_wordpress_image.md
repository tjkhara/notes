# Testing wordpress image

    docker run --name some-wordpress --network some-network -d wordpress

    docker run --name first_wordpress --network wordpress1 -d wordpress

    docker run --name some-wordpress -p 8080:80 -d wordpress

    docker run --name wordpress1 --network wordpress1 -p 8080:80 -dit wordpress



You need to create a new network first.

    docker network create wordpress1


Create network
Create volume for web and for db

Set environment variables use this example as reference:

    Setting environment variables example:

    docker run --name db --network blog -e MYSQL_ROOT_PASSWORD=pw123 -e MYSQL_DATABASE=wordpress --mount src=blog_db_data,dst=/var/lib/mysql -d mariadb

# Commands to use

    docker network create wordpress

    docker run --name wordpress_site --network wordpress -e WORDPRESS_DB_HOST=db -e WORDPRESS_DB_USER=dbuser -e WORDPRESS_DB_PASSWORD=dbpassword -e WORDPRESS_DB_NAME=wpdb -e WORDPRESS_TABLE_PREFIX=wptp -p 7001:80 -d wordpress

    docker run --name some-wordpress --network wordpress -p 8080:80 -e WORDPRESS_DB_HOST=db -e WORDPRESS_DB_USER=dbuser -e WORDPRESS_DB_PASSWORD=dbpassword -e WORDPRESS_DB_NAME=wpdb -e WORDPRESS_TABLE_PREFIX=wptp -d wordpress