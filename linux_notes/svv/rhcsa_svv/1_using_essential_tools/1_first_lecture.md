# login to the server

1. dont login as root by default
2. use su - to open a root shell when required
3. you can also use sudo to run tasks as root


The 

    $ 

is the prompt for an ordinary user

pwd is print working directory

    su -

open a shell as a root user

this will ask for a password - the root user password

The prompt changes to

    #

when the user logs in, he is sent to the root directory

    su - and not su

because the - gives us the environment variables

    exit

to get out of the root shell and into the shell of the ordinary user

# deploying RHEL in the cloud

from EC2 you can pick RHEL



