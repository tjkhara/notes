# EC2 AMI

AWS comes with a lot of base images.

How to create our own image?

This is an AMI.

## Advantages of using a custom AMI

- Preinstalled packages
- Faster boot time
- Machines comes configured with monitoring/enterprise software
- Security concerns - control over the machines in a network
- Control of maintenance and updates
- Active directory
- Install app ahead of time
- Or use someone else's AMI

AMI's are only for a specific region.

You can rent expertise from AMI creators.

## AMI Storage

They live in S3.

Most of your backups with live in S3.

By default AMI's are private and locked for your region.

You can make them public and share them with other AWS accounts or sell them on the AMI marketplace.

## AMI Pricing

Charged for space in S3.

Cheap to store private AMIs.

## Cross account AMI copying

Sharing the account does not change ownership.

If they copy the AMI into another region, then they become an owner.

## On the video search for note billing product

The difference is either people can directly copy your AMI.

Or they can make an instance and then make their own AMI.