# Managing networking

Start with network basics.

Managing and troubleshooting runtime network configurations.

Manage hostname and hostname resolution.

## Understanding IPv4 basics

Routers connect networks.

Total 32 bits

Subnet masks tell you which is the network address and which is the address nodes

For example the network address could be 192.168.100.0/24

Node address will be 192.168.100.10/24

The node will not send a packet to 192.168.90.100 This packet will be sent to the router.

The router is the default gateway. It is the door to get outside.

Many routers have the ip ending in 254 like 192.168.100.254

### DNS - domain name system

Using name instead of a number.

www.linux.com the request will go to DNS nameserver and that will give us the ip address.

## IPv6

128 bits are written in hexadecimal

You can skip zeros.

	fe80::1

is a valid address.

If you are addressing a port, then write it like this

	[fe80::1]:80

Default subnet mask is /64 - nobody uses this. Everyone uses /64.

Node bit may contain the device MAC address.

### Reserved IPv6 addresses

localhost
	::1/128

unspecified address (0.0.0.0)
	::

default route
	::/0

global unicast address
	2000::/3

unique local address (private addresses)
	fd00::/8

link-local address
	fe80::/64

multicast
	ff00::/8

### Obtaining an IPv6 address

fe80:: address is used by default.

Through static addressing.

DHCPv6

Multicast is sent out to ff02::1:2 port 547/UDP. This is all-DHCP multicast group. The DHCP server sends a packet back to client 546/UDP.

SLAAC (Stateless auto address configuration)

Router solicitation is sent to ff02::2; the all-routers multicast group. The router sends back an IP address, which allows the host to learn the network prefix.
Install the radvd package to use this.

### Applying runtime network configuration

Analyze and troubleshoot what is happening here and now.

	ip a

First is loop back.

In the old days processes communicated with each other using ip addresses.

	127.0.0.1

#### You need to have a router also along with ip address

	route

To see the router's ip address

	ip route show

This configuration file is also important

	cat /etc/resolv.conf

This contains the ip address of the dns nameserver.

You can delete a route like this

	ip route del default via 192.168.4.2

Now if you do

	ping google.com

It will show

	network is unreachable

Then do

	ip route show

	ip route add default via 192.168.4.2

Notice now that this is not added via dhcp, but manually.

Shortcut for 

	ip addr show

is

	ip a

You can run 

	dhclient

In case you want to regenerate automatic ip.

When the dhcp server is not available you can set an ip address manually

	ip addr add dev ens33 10.0.0.10/24

This is assigning a secondary ip address.

Multiple ip addresses on one network card.


#### The command you should never use ifconfig

This is a very old command.

## Understanding network device naming

biosdevname

	systemd-udevd

	em123

	p<port>p<slot> (PCI, PCI port)

	eno123 (EtherNet Onboard)

If driver does not reveal sufficient information

	eth0 is used

### Managing host names

	hostname

This returns the FQDN

	hostname --help

You can also see information in some distributions in

	cat /etc/hostname

This utility works on all linux systems

	hostnamectl

This command is close to the uname command

	uname -a

This gives you the kernel information.

The

	hostnamectl status

command is kind of a merger between the

	uname -a

and

	hostname

hostnamectl can also be used to set the hostname.

	hostnamectl set-hostname newcentos.example.com

You will have to close shell and open it again to see the change in the prompt.

### Managing hostname resolution

	/etc/resolv.conf

This has dns information.

There is a local alternative also

	/etc/hosts

For an internal network you can do the following to go to a URL on your network

	192.168.4.229 ubuntu.example.com ubuntu

	192.168.4.229 google.com

How to make a certain server in accessible on your network?

You can create a fake entry in /etc/hosts file like the above for google.com

	vim /etc/nsswitch.conf

This file defines the order in which you should be looking for information.

If in this file you change the order to

	hosts: dns files myhostname

This will then tell the system to first look at the dns server.

### Using common network tools

	ping google.com

	ping --help

	ping -f google.com

This is a ping float

	ping -f -s 4096 ubuntu

This is like putting a ping bomb on the ubuntu machine.

	netstat

This is an old command, but good.

	netstat -tulpen | less

This gives an overview of everything that is listening on this computer.

The more modern alternative is

	ss -tuna | less

This gives us socket stats.

Here we can see which ports are available and on which ip address they are listening.

#### Another utility that is quite useful for network analysis is nmap

Not installed by default

	yum install nmap

This can easily be abused.

This is a very rich network scanner to find out which services are being offered by other machine.

Do not use it on public networks.

	nmap 192.168.4.2

will do a port scan.

nmap helps us to get the perspective of an external user on what is offered by your server.

#### Another one is dig

dig is about dns

If you want to make sure your dns is working okay, you can do dig.

	dig nu.nl

### Command review

This will show current network configuration.

	ip a
### Lab

#### Verify your current network configuration






