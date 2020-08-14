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
