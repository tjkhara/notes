# Container images

## Searching docker for an image

    docker search {TERM}

Container images keep track of the changes.

Layering is similar to git.

## Downloading an image

    docker pull nginx

This is just downloading the image and not creating a container.

## Listing images

    docker images

## History

    docker history nginx

## Creating tags

You can research this

    docker tag --help

This is like a git commit. If we have an nginx version that is working perfectly, we can tag that and use it later.

    docker tag nginx:latest nginx:myblog_stable

The latest is the existing tag. The myblog_stable is the new tag we're creating.

## Removing images

    docker rmi nginx:myblog_stable 

The format is docker rmi {image_name}:{tag_name}

This command will just untag the image and not delete it.

There is a force option also:

    docker rmi -f nginx:myblog_stable

To get a list of the images you can do

    docker images

Then you can see the image names and the tags.

### Getting rid of dangling images

    docker image prune

### Getting rid of dangling images and unused images use this command [Use with great care]

    docker system prune -a