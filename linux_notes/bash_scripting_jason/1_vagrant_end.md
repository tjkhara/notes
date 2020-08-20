# Setting up the vargrant environment

	vagrant box add USER/BOX

	vagrant box add jasonc/centos7

A box is an operating system image.

## Vagrant project

Must have a folder

	mkdir vm1

	cd vm1

	vagrant init jasonc/centos7

	vagrant up

Vagrant will import the box and start it.

When it is started it is started in headless mode no GUI.

## Multi machine setup

	vagrant up [vm_name]

	vagrant up master

	vagrant up server1

Just 

	vagrant up

would bring both systems up.

## Connecting 

	vagrant ssh [vm_name]

For single machine

	vagrant ssh

## Stopping

	vagrant halt

Shut down all machines in the vagrant file.

For single one

	vagrant halt [vm_name]

	vagrant up [vm]

Starts the vm.

With no name it operates on all the vms defined in the project.

## suspend

	vagrant suspend

	vagrant resume

## to start again

	vagrant destroy

Work is lost.

## Getting help

Just run the

	vagrant

command to see options.

## Simple vagrant file

	Vagrant.configure(2) do |config|
		config.vm.box = "jasonc/centos7"
	end

The (2) is the configuration version.

To set the hostname do this

	Vagrant.configure(2) do |config|
		config.vm.box = "jasonc/centos7"
		config.vm.hostname = "linuxsvr1"
	end


### To assign a static ip address


	Vagrant.configure(2) do |config|
		config.vm.box = "jasonc/centos7"
		config.vm.hostname = "linuxsvr1"
		config.vm.network "private_network", ip: "10.2.3.4"
	end


### Setting more defaults
#### Setting gui and ram

	Vagrant.configure(2) do |config|
		config.vm.box = "jasonc/centos7"
		config.vm.hostname = "linuxsvr1"
		config.vm.network "private_network", ip: "10.2.3.4"
		config.vm.provider "virtualbox" do |vb|
			vb.gui = true
			vb.memory = "1024"
		end
	end

### Provisioning 
#### ssh
#### This is how you can write a post installation shell script to configure a new system

	Vagrant.configure(2) do |config|
		config.vm.box = "jasonc/centos7"
		config.vm.hostname = "linuxsvr1"
		config.vm.network "private_network", ip: "10.2.3.4"
		config.vm.provision "shell", path: "setup.sh"
	end


### Setting up a multi machine setup in vagrant

	Vagrant.configure(2) do |config|
		config.vm.box = "jasonc/centos7"

		config.vm.define "server1" do |server1|
			server1.vm.hostname = "server1"
			server1.vm.network "private_network", ip: "10.2.3.4"
		end

		config.vm.define "server2" do |server2|
			server2.vm.hostname = "server2"
			server2.vm.network "private_network", ip: "10.2.3.5"
		end
	end
