# Docker common commands


## First command

    docker run -dit debian

Options:

d - detach. Run container in the background.
i - interactive. Docker keeps stdin open. Allows you to type commands into the container.
t - sudo tty or terminal.

You need to get a container id after you run a docker run command.

## Confirm container is running - docker ps

    docker ps

Lists details about containers.

## Stop the container

    docker stop {container_id}

## Display the images that have been downloaded

    docker images

## Inspect

    docker inspect {id}

## Help

    docker --help

    docker images --help

    docker image prune --help