# Networking and deploying apps

Start a container

    docker run -dit -p 8080:80 php:apache

Docker chain

    iptables -nL "DOCKER"

Stopping docker networking

    docker run -dit --network host php:apache

This option should not be used. Just means if port 80 is open on the container it will open up on the host as well.

## list

    docker network ls

    docker network inspect {network_name}
    docker network inspect bridge

## create network

    docker network create blog


-------------------------------------------------------------------------------------------------------------

## Part 1

1. Create network

    docker network create blog

2. Create volume

    docker volume create blog_web_data

3. Run container

    docker run --name web --network blog -p 80:80 --mount src=blog_web_data,dst=/var/www/html -dit php:apache

4. Inspect blog network

    docker network inspect blog

## Part 2

Create a container that will act as a database server for our blog

Using mariadb

We will create our own volume

1. Create the volume for the database

    docker volume create blog_db_data

Check it

    docker volume ls

2. Create container

This is an example of setting environment variables using the -e option (do not use space)
Note that no -p option is used as we do not want this database to be exposed to the world.

    docker run --name db --network blog -e MYSQL_ROOT_PASSWORD=pw123 -e MYSQL_DATABASE=wordpress --mount src=blog_db_data,dst=/var/lib/mysql -d mariadb

## Part 3

Inspect blog network

    docker network inspect blog

Inspect the volume for the db container

    docker volume inspect blog_db_data

This is the mountpoint

    "Mountpoint": "/var/lib/docker/volumes/blog_db_data/_data"

Perform an ls there to see the files

**Note: You can delete a container and still the volume will be there and you can start a new container from it.**

## Part 4

Connecting to database server from webserver

    docker exec -it web bash

Install a mysql client

    apt update

    apt install -y default-mysql-client

Connecting to mysql

    mysql -h {ip_address_of_host} -p 

    mysql -h 172.18.0.3 -p

The -h option gives us space to put the host we want to connect to.

When we build our own network we can use the container name as well:

    mysql -h db -p

**This is the better way to do it use the container name**

The -p option will have us prompt for a password.

-------------------------------------------------------------------------------------------------------------

## You can attach a container to multiple networks

    docker network connect --help

## Part 5

Installing wordpress

Log in to the web container

    docker exec -it web bash

Install the myqli extension

    docker-php-ext-install mysqli

Restart apache

Just stop and start the container

    exit

    docker stop web

    docker start web

See processes by doing

    docker top web

Get wordpress application files into the web server container

First see where you need to put these files

    docker volume inspect blog_web_data

    "Mountpoint": "/var/lib/docker/volumes/blog_web_data/_data",

Download files

    wget https://wordpress.org/latest.tar.gz

Uncompress

    tar zxvf latest.tar.gz

Change the ownership to www-data:www-data

    chown -R www-data:www-data wordpress

# Part 6 

Make an image

    docker build -t tkhara/php:mysqli .

Push this to docker hub

    docker login

    docker push tkhara/php:mysqli

Then stop and remove web

    docker stop web

    docker rm web

Then run a container with the new image

    docker run --name web --network blog -p 80:80 --mount src=blog_web_data,dst=/var/www/html -dit tkhara/php:mysqli
