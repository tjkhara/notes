# Connect to mysql container

    docker exec -it served_blog_mysql bash

    tkhara@tkhara-lenovo:~$ docker exec -it served_blog_mysql bash
    root@1aa3491d4b99:/# mysql -u root -p
    Enter password: password

## Connecting via command line

    mysql -h 127.0.0.1 -P 33007 -u root -p laravel