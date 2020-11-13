# Deployment

Video: https://www.youtube.com/watch?v=-pOKTtAfJ8M&list=PLAPEtbmG9XgQWcKmAGTMKGoThvio2Egzk&index=1&t=567s

Deploying the site starts here: https://youtu.be/-pOKTtAfJ8M?t=1553

To do list:

1. Set up git hub repo in wordpress_sites.yml
2. Change this line: https://github.com/roots/trellis/blob/a4cbce18b7b5902e033730eb33e732c76c595dd7/group_vars/production/wordpress_sites.yml#L14


Commands to deploy:

Install ansible

    pip  install -r requirements.txt

Install some things that ansible needs

    ansible-galaxy install -r galaxy.yml

Provisioning the server

    ansible-playbook server.yml -e env=production


## Set up git hub sync

Login to the server as web

Generate a key

    ssh-keygen -t rsa -b 4096 -C "tkhara@gmail.com"

Copy this key and paste it into your github repo's deployment key.

## Actual deploy

From your local system

From the trellis folder run:

    ./bin/deploy.sh production tjkhara.xyz