# docker logging

Get jenkins running

    docker run -dit --name busylogs -p 8080:8080 -p 50000:50000 jenkins/jenkins:lts

The forward slash in the image name - before / is the user id after is image name after colon is tag

    {user_id}/{image_name}:{tag}

How to get the password? From the logs

    docker logs busylogs

    7362312f33b44f258795eafe526a0b47

Combine options:

    docker logs -tf busylogs

After a date

    docker logs -t --since 2011-11-11 busylogs

## viewing more logs

    /var/log/syslog

    grep -i docker /var/log/syslog

This is where docker will put log information.

    journalctl -n 25