# using ssh to login remotely

ssh is secure shell

The connection is encrypted.

	- Identity of the target server is verified through host keys.

	- After initial connection, host key is stored in ~/.ssh/known_hosts

	ssh -X

	ssh -Y

These two are for graphical remote connections.

Use ssh -Y

