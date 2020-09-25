# ec2 introduction

security group is a firewall around the instance

## ssh and connecting to ec2

## introduction to security groups

They control how traffic is allowed into EC2 machines.

Control inbound and outbound traffic.

By default there are no rules. We have to add rules.

## security groups deep dive

They regulate

- access to ports
- authorized ip ranges
- control of inbound network (from other to instance)
- control of outbound network (from instance to other)

Security group is a firewall outside your EC2 instance.

### Good to know points about security groups

- Can be attached to multiple instances
- And an instance can have multiple security groups as well
- Locked down to a region/VPC combination
- Lives outside the EC2 instance
- Good advice: it is good to maintain one security group for SSH access
- If you get timeout issues you have a security group issue
- If you receive a connection refused error, then it is an application error or instance is not launched. The traffic did go through and SG is working.
- By default all inbound traffic is blocked and all outbound traffic is authorized.


### How to reference security groups from other security groups?

We can have a security group that allows other security groups

SG1 can allow SG1 and SG2 to connect inbound to our instance.

This is great because you can forget about IPs and just attach different instances to security groups and then just allow those security groups.

