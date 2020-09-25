# ec2 user data

This script is run when the machine is started for the first time.

	#!/bin/bash
	yum update -y
	yum install -y httpd.x86_64
	systemctl start httpd.service
	systemctl enable httpd.service
	echo "Hello World from $(hostname -f)" > /var/www/html/index.html

All these commands are run with sudo by default.