# Docker volumes


## Command workflow

    docker volume create localvolume

    docker volume inspect localvolume

This one shows you the path on the local system and the docker container.

Create a file on the local system:

    echo "This file exists" > /var/lib/docker/volumes/localvolume/_data/file.txt

Then run a container and attach a volume to it

    docker run -d --name mountvolume --mount src=localvolume,dst=/data httpd

Now to get into the mountvolume container. This is called attaching.

    docker exec -it mountvolume /bin/bash

Check the volumes in the container:

    df -h

Check that the file created on the local system exists here

    cat /data/file.txt


Running a container with an ephemeral volume:

    docker run -d --name tempvolume --mount type=tmpfs,dst=/tempdata httpd

Inspecting a volume:

    docker inspect tempvolume | grep Mounts -A 10

-----------------------------------------------------------------------------------

Command:

    docker run --mount /dbdir:/var/lib/mysql -d mariadb

Using the -v option is deprecated but you still need to know it:

    docker run -p 8080:80 --name nginx-with-vol -v /root/webpages:/usr/share/nginx/html:ro -d nginx

Help

    docker volume --help

## Creating a volume

    docker volume create testdata

## List volumes

    docker volume ls

## Delete volume

    docker volume rm testdata

## Inspect command for further information

    docker volume inspect mydata1

This is the command that will tell you where this data is on your localhost.

-----------------------------------------------------------------------------------

## Starting a container and attaching the volume to it

    docker run -d --name withvolume --mount source=mydata1,destination=/root/volume nginx

Do not use a space in the above command in the part after source.

Inspecting the container and looking at the mount section:

    docker inspect withvolume | grep Mounts -A 10

-----------------------------------------------------------------------------------

## The same volume can be mounted to multiple containers

    docker run -d --name withvolume2 --mount src=mydata1,dst=/root/volume nginx

This will make the container run.

Now attaching to the container.

    docker exec -it withvolume2 bash

-----------------------------------------------------------------------------------

## Read only access to a volume

Note if the volume does not exist docker creates it for you

    docker run -d --name readcontainer --mount src=newestvolume,dst=/usr/share/nginx/html,readonly nginx

-----------------------------------------------------------------------------------

## Pruning volumes

    docker volume prune