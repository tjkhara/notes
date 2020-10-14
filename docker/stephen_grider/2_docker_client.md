# Docker client

## run

    docker run hello-world

## override

    docker run {image name} {command}

    docker run busybox echo hello there

    docker run busybox ls

## listing running containers

    docker ps

    docker ps -a

    docker ps --all

## container lifecycle

Creating a container and running it are separate processes

docker run = docker create + docker start

Create a container

    docker create

Starting a container

    docker start

Example:

    docker create hello-world

    docker start -a 5aac8aad8b1c8ddabd0762fe077cecbf52bc238f990cb0a1dd8ffa82a91f7e00

What is the -a?

This attaches to the container and watches for the output and puts it on my terminal.

## restarting stopped containers

We can restart an exited container.

    docker start -a aec62d2cdaba

## removing stopped containers

    docker ps --all

See all containers.

    docker system prune

This will delete stopped containers. This will delete the build cache also (images).

## retrieving log outputs

Getting output without the -a flag.

    docker logs {container id}

    docker logs e7....

This will show us the output.


