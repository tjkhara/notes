# Installing packages


Update repo

    apt-get update

Upgrade will download package

    apt-get upgrade

Install will install them

    apt-get install

Work flows:

    apt-get update -> apt-get upgrade -> apt-get install -> apt-get remove

Combining the commands:

    apt-get update && apt-get upgrade

You may also need to do:

    sudo apt-get dist-upgrade

