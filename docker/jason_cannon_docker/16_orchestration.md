# Orchestration

    docker swarm init

We have to specify ip

    docker swarm init --advertise-addr 192.168.1.100

This node becomes a manager.

To make another node join as a worker you will use something like:

    docker swarm join --token SWMTKN-1-5ao8ns38k5f0jq2jfbspf030108lsbu4d5w65o3davs9qoy2yh-afy40lp6vdpfxgyp5pppqv7io 192.168.1.100:2377

Use docker info to confirm that you are a part of the swarm.

    docker info

List the nodes from the manager's perspective:

    docker node ls

To get another token

    docker swarm join-token worker

To get another manager to join

    docker swarm join-token manager

## Creating a service

    docker service create --name web -p 8081:80 nginx:latest

This is very similar to the run command.

This creates one or more containers on one or more hosts.

### Listing different services

    docker service ls

Take a look at all the containers

    docker service ps {service_name}

    docker service ps web

## Inspecting

    docker service inspect --pretty web

    docker service inspect --pretty {name_of_service}

## Sclaing the service

    docker service scale web=2

## Removing a service

    docker service rm web