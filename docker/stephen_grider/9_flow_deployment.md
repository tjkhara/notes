# Deployment flow


Create a git hub repo

Two branches:

1. feature - development branch
2. master - very clean working copy of code base. These will be automatically deployed.

pull and push only to feature branch.

The make a pull request.

The changes will be merged to the master branch.

The pull request will set off a series of actions:

Travis CI - continuous integration provider.

Pulls down code and runs tests.

Travis CI will push it over to AWS.

## Docker's purpose:

Docker is a tool in a normal development workflow.

Docker makes some of the tasks a lot easier.

## Project generation

Generate project.

Wrap it inside a Docker container.

1. nodejs 

    node -v

2. Create react app

    npx create-react-app frontend

    cd frontend

3. Three commands

    npm run start

This is a dev only command. Starts a dev server.

    npm run test

Runs tests associated with the project.

    npm run build

Build a production version of the application.

Take the JS files and concatenate them into one file.

## Dockerfiles

We will have two different Dockerfiles.

1. Development
2. Production

Docker build command for a different Dockerfile name:

    docker build -f Dockerfile.dev .

The -f means we are specifying the file.

## Running the container

    docker run -it -p 3000:3000 CONTAINER_ID

