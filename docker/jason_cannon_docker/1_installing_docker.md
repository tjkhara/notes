# Installing docker

The video instructions work fine, but to add the proper repo use this command:

	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(. /etc/os-release; echo "$UBUNTU_CODENAME") stable"

## Check if docker is working

	docker version

## Installing docker compose

	sudo apt-get -y install docker-compose