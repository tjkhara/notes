# Building custom images through docker server

First create a Dockerfile -> Pass onto the docker client (the cli on our terminal) -> Docker server (does heavy lifting) -> Builds usable image

## Creating a docker file

1. Specify a base image
2. Run some commands to install additional programs
3. Specify a command to run on container setup

## Create an image that runs a redis server

In a directory create this Dockerfile

    # Use an existing docker image as a base
    FROM alpine

    # Download and install a dependency
    RUN apk add --update redis


    # Tell the image what to do when it starts as a container
    CMD ["redis-server"]

Then issue the command

    docker build .

You should see a message like

    Successfully built f4abc85fc04b

Then run it

    docker run f4abc85fc04b

### Let's understand what happened in the Dockerfile

Format

    {instruction} {argument to the instruction}

Example:

    FROM alpine

This says base image is alpine

    RUN apk add --update redis

This says run this command

## Writing a Dockerfile is like being given a computer with no OS and then installing chrome

Installing the OS is specifying a base image

Then we run the commands to download additional programs

Executing chrome.exe is the last command. That is the command to run on startup.

### Looking into this command a little more

    RUN apk add --update redis

apk is a package manager for alpine linux

We user this package manager to download and install redis for us

# The build process in detail

Why do we use docker build?

This is where we give our Dockerfile to the cli.

The . specifies the build context. The site of files or folders that belong to our project.

    CMD sets the primary process for the new container.

This is just saying to the container that if you were ever to run for real your main command is

    redis-server

After this whole process it shuts down the container and takes a snashot of its file system and its primary command.

This is the result:

    Successfully built f4abc85fc04b

The end result is:

    An image with an id

    That has the file system snapshot

    And a startup command

# Recap

Right before the CMD instruction we have created an alpine image that has redis added on top.

The RUN command is used to execute instructions inside the contianer.

The CMD command is used to tell the container what it needs to do when it is started up as a container.
Whenever you are started up in the future you should try to execute the command redis-server.

The output is the image that was generated from the last step.

## Rebuilds with cache

They are fast.

Changes in sequence of commands need rebuilding.

## Tagging an image

Format

    -t stephengrider/redis:latest

    -t {docker id}/{repo or project name}:{version}

    docker build -t tkhara/redis:latest .

Output:

    Successfully built 691f1ae1f156
    Successfully tagged tkhara/redis:latest

## Manual image generation with Docker Commit

You can generate a container out of an image and you can take an image and generate a container.

    docker run -it alpine sh

Manually install redis

    apk add --update redis

    docker ps

Get id of the running container af7fe77dea26

    docker commit -c 'CMD ["redis-server"]' af7fe77dea26

Output is 

    sha256:47b6dc662e23caed9c7528689e41b24e98c7943cfe47850605c1a4f6055ea13e

    docker run 47b6dc662e23



