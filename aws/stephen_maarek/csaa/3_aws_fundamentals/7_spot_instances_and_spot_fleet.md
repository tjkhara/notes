# Spot instances and spot fleet

- Can get a discount of up to 90% compared to on demand
- We come up with a max spot price
- If instance price is less than spot then we are okay
- Is spot goes up, then we have two options.

1) Either we stop our instance.
2) Or terminate.

## Or we can do Spot Block.

- block a spot during a specified time frame (1 to 6 hours) without interruptions
- in rare situations the instance may be reclaimed.

## When do we use spot instances?

- Batch jobs
- Data analysis
- Workloads that are resilient to failures

- Not great for critical jobs or databases

## How to terminate a spot instance?

Two types of a requests:

1) One time

Instance launched and request goes away.

2) Persistent

If instance gets stopped, then request goes back into action.

### You can only cancel spot instances that are open, active, or disabled.

Not failed, cancelled or closed.

To properly terminate

1) First cancel the spot request
2) Then terminate associated spot instances

## Spot fleets
### Ultimate way to save money

Spot feelts = set of spot instances + optional on demand instances

The spot fleet will try to meet the target capacity with price constraints

It launches from possibel launch pools. The fleet will choose the best.

### Strategies to allocate spot instances

1) Lowest price

from the pool that has the lowest price. Good option for a short workload.

2) Diversified

distributed across all pools (great for availability and long workloads).

3) Capacity optimized

pool with the optimal capacity for the number of instances.

**Spot fleets allow us to automatically request spot instances with the lowest price**