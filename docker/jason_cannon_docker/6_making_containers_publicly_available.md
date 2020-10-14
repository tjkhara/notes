# Making containers publicly available

First command

    docker run --name our_nginx -d -p 8080:80 {image_name}

    docker run --name our_nginx -d -p 8080:80 nginx

    -d is detached mode
Open up 8080 on the host machine and connect that to port 80 of the nginx container
Last thing in the run command is the image name.

## Running our own web page

First create an index.html

    docker run -p 8080:80 --name another_nginx -v ${PWD}/webpages:/usr/share/nginx/html:ro -d nginx

The -v option creates a volume for sharing files.

    docker run -p 8080:80 --name another_nginx -v {path_on_the_host_machine}:{path_inside_container}:{options} -d nginx

Options supplied here are ro which is read only. This mounts the volume in read only mode inside the container.
The container cannot alter the file. It can only read the data contained in the volume. The data can be changed from the host.

## Another example

Start a container

    docker run --name apache_welcome -d -p 9900:80 httpd:latest
