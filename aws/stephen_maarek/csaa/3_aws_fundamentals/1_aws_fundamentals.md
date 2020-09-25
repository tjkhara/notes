# aws fundamentals

## aws regions

Global cloud provider.

Data centers are called regions.

Naming convention for the regions is as follows:

us-east-1
eu-west-3

us-east-1 is northern virginia.

Region is a cluster of data centers.

Most aws services are region scoped.

## aws availability zones

Each region has many availability zones.

Usually 3, min is 2, max is 6.

ap-southeast-2 is Syndney.

The AZs are

ap-southeast-2a
ap-southeast-2b
ap-southeast-2c

The regions end with a number and the AZs end with a letter.

### What is an AZ?

Each AZ is one or more discrete data centers with redundant power, networking, and connectivity.

They are separate from one another so they are isolated from disasters.

They are still connected with high bandwidth, ultra low-latency network.

IAM is a global service.

EC2 is a regional service.