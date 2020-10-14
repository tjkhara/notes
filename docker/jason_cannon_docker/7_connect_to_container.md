# Connecting to running containers and managing container output

## Entering a container at launch time via the shell

    docker run -it --name apache httpd /bin/bash

    -it for interactive shell
    Did not use d because we do not want to detach
    --name gives name
    image is httpd
    command for docker is /bin/bash

To  get out

    exit

or

    control + d

You will not see this on the docker ps output.

## Run another container with the d option

    docker run -dit --name second_apache httpd /bin/bash

No point in doing this. We are not attached to the container.


Docker Exec Command
--------------------

Start another apache container

    docker run -dit httpd

Using the docker exec command to start a shell on an already running container.

    docker exec -it {container_id} /bin/bash

Old style shell

    docker exec -it {container_id} sh

### Creating an empty text file in the container

    docker exec -d {container_name} touch /root/hello

Now check if that worked by entering the container using bash

    docker exec -it {container_name} bash


Installing stuff in the container
-----------------------------------

Login through the shell first

    docker exec -it {container_name} bash

Then install what you need

    apt update

    apt install -y vim

This is for the running container only. If you want to create an image of this you need to do the following:

## Creating tags

You can research this

    docker tag --help

This is like a git commit. If we have an nginx version that is working perfectly, we can tag that and use it later.

    docker tag nginx:latest nginx:myblog_stable

The latest is the existing tag. The myblog_stable is the new tag we're creating.

installing stuff end
-----------------------

## How to view processes within a container

    docker top execution {container name or id}

