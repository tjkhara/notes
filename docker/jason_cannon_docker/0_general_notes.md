# General notes

Workflow seems to be

You build an image

You run a container based on that image

And you can push the image to the registry


## ssh into a container

    docker exec -it readcontainer bash

## Common commands

List all containers

    docker ps -aq

Stop all running containers

    docker stop $(docker ps -aq)

Remove all containers

    docker rm $(docker ps -aq)

Remove all images

    docker rmi $(docker images -q)