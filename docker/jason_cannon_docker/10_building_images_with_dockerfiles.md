# Building images with docker files

Building an image from a dockerfile

    docker build -t jasonc/dockerping:latest .

Contents of the Dockerfile are:

    FROM debian:latest
    LABEL maintainer="Jason Cannon"
    ENTRYPOINT ["/bin/ping"]
    CMD ["www.docker.com"]

Explanation of the command
-----------------------------

    docker build

is to build an image

    -t

Allows us to specify a tag or an image name

    {docker_userid}/{repo_name}:{tag_name}

Syntax:

    docker build -t {docker_userid}/{repo_name}:{tag_name} {path_to_Dockerfile}

For me this will be

    docker build -t tkhara/dockerping:latest .

## Uploading the image to Docker hub

    docker push jasonc/dockerping:latest

For me

    docker push tkhara/dockerping:latest

## Running this image

    docker run tkhara/dockerping:latest

Revise the contents of the Dockerfile
---------------------------------------

    FROM debian:latest
    LABEL maintainer="Jason Cannon"
    ENTRYPOINT ["/bin/ping"]
    CMD ["www.docker.com"]

The option of CMD can be overridden on the command line

To ping google.com we could do

    docker run tkhara/dockerping:latest google.com

Command thats gets executed in the container is

    /bin/ping google.com

## Building a second image

This is where we have to add commands

Building this image

    docker build -t tkhara/nettools nettools/

Running this image

    docker run -it tkhara/nettools

## Overriding an entry point

    docker run --entrypoint /usr/bin/curl -it tkhara/nettools google.com

This just curled google.com

We can use the CMD instruction without the entry point.

---

## How to provide docker the name of a custom file

    docker build -t tkhara/nettools:allow-override -f Custom_File_Name .

Put the path in the end since the file is in the current directory.

### Running a container based on this image



---