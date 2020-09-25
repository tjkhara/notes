# Private vs Public vs Elastic IPs

IPv4 - 4 number separated by 3 dots.

A server can have a public ip.

Another server can also have a public ip.

Using these public IPs these two servers can talk to each other.

A private network has a private ip range.

All computers can talk to each other using those private ips.

Public ip - machine can be accessed over the internet. IP is unique on the internet.

Private ip - ip can be connected to each other on network.

---

Machines connect to www using an internet gateway (a proxy).

Only a specified range of ips can be used as a private ip.

---

## Elastic ip

stop and start instance you will see the public ip change.

If you need a fixed ip, you will need an elastic ip.

Elastic ip - is a public ipv4 address.

You can only have 5 elastic ips in your account.

Try to avoid using elastic ips. They are poor architectural decision.

We can use a load balancer and no private ip as well.

---

## EC2 machine

- will come with a private ip
- a public ip


When we do an SSH into our EC2 machines:

- we can't use a private IP because we are not on the same network
- we can only use the public ip

If your machine is stopped and then started the public ip can change.