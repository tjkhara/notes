# Copy files over network

	SCP

or

	SFTP

These are both extensions of the secure shell protocol.

sftp will provide a more interactive experience.

	scp source destination

This will copy source to destination.

	sftp host

Start a secure file transfer session with host.

	sftp jason@host

There is an ftp command line utility as well.

	ftp host

Start a file transfer session with host.

This is not a secure transfer protocol. Login credentials are sent in plain text over the network.

	sftp 192.168.1.105

	pwd

Will show you working directory on the remote server - you will be in the home directory.

	ls 

Will show you files on remote.

	lpwd

Will show you pwd on local.

	lls

Will show you files on local.

	put z.txt

This command will put a file onto the server.

To exit just type

	quit

## scp

You need to know the source and destination.

	scp z.txt 192.168.1.105:/home/tkhara

Transfer the file to a remote server as a different user

	scp z.txt adminuser@192.168.1.105:/home/adminuser

To connect via sftp

	sftp adminuser@192.168.1.105


