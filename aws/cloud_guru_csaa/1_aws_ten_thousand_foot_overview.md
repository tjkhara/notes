# AWS 10,000 foot overview

Global infrastructure

19 regions

57 availability zones

In 2020

24 regions

72 availability zones

An AZ is just a data center.

An AZ can be several data centers.

A flood might be able to take out these 2-3 data centers close to each other. But then there will be another AZ.

What is a region?

A region is a geographical area. Each region consists of 2 or more AZs.

Examples:

London region

N Virginia region

Oregon region

Sydney region

Singapore region

Tokyo region

You will always have more edge locations than you have regions.

Edge locations:

These are endpoints for AWS which are used for caching content. Typically this consists of CloudFront, Amazon's content delivery network (CDN).

Currently there are over 150 edge locations.

The high level services that we need to know:

1. AWS Global Infrastructure
2. Compute
3. Storage
4. Databases
5. Migration and transfer
6. Network and content delivery
7. Management and governance
8. Machine learning
9. Analytics
10. Security Identity and Compliance
11. Desktop and app streaming

Out of these the core services are:

1. AWS Global Infrastructure
2. Compute
3. Storage
4. Databases
6. Network and content delivery
10. Security Identity and Compliance
