# Multi command containers

Start a redis container

    docker run redis

How can we execute a second command inside the container?

    docker exec

Docker execute - execute an additional command inside of a container

    docker exec -it

The -it gives us the ability to type a command inside the container (interactive and terminal)

    docker ps

Get the container's id 7dcbff7a9509

Command:

    docker exec -it 7dcbff7a9509 redis-cli

Format is

    docker exec -it {container id} redis-cli

# The purpose of the -it flag

When we type the -it flag then we are attached to the std in channel of the redis-cli.

# Getting a command prompt in a container

    docker exec -it {container id} {command}

How to open up a shell in a running container?

    docker ps

Get container id 7dcbff7a9509

    docker exec -it 7dcbff7a9509 sh

sh is a command processor

Only some will have bash

# Starting with a shell

We can start a shell immediately when a container starts up

    docker run -it busybox sh

This will stop other processes.

The more common thing to do is what we did above. Start a container with a primary service running.

Then attach to it using a running shell.