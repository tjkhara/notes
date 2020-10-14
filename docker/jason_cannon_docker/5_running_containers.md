# Running containers

---

# Main and common commands

Running a container

    docker run -dit redis

Check to see the list of containers

    docker ps

Start a container with a name

    docker run -dit --name=redis_container redis

The name here is redis_container

Check again that this is running

    docker ps

Stop a container with a name

    docker stop redis_container


---

    -d is detach or daemonize

    docker run -dit debian

    -i is interactive
    -t for terminal

## Using a custom name

    docker run -dit --name={your_custom_name} debian

Example

    docker run -dit --name=web debian

## Seeing continers

See running containers

    docker ps

To see stopped containers also

    docker ps -a

To see the latest container

    docker ps -l

## Stopping and removing containers

stop
    docker stop web

see all
    docker ps -a

Remove the container
    docker rm web

Cleaning up all stopped containers

    docker system prune

Auto clean

    docker run --rm hello-world

### Stopping and starting

    docker stop web

    docker start web

Using the kill command:

    docker kill third_container

stop is a graceful shutdown.

## Restarting containers automatically

    docker run -dit --restart=always --name=fourth_container debian

Using grep
---

    docker inspect fourth_container | grep -A3 RestartPolicy

## Logs

    docker logs --help

    docker logs -t {container_id}

This is with time stamps.

To follow the output in real time

    docker logs -f {container_id}

To get a timestamp and follow the output you can do

    docker logs -tf {cont_id}