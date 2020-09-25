# ec2 instance launch types

## on demand

- short workload
- predictable pricing

## reserved

- known time
- minimum for 1 year
- long workload

There is also a 

### convertible workload

can convert from one type to another

## scheduled

- every Thursday betweed 3 to 6 pm on Thursday

## spot

- very cheap
- can lose them
- not reliable

## dedicated

- no customer will share hardware

## dedicated host

- book an entire server.
- control instance placement.

---

### on demand

- pay for what you use
- billing is per second after the first minute
- highest cost (no upfront payment and no long term commitment)
- good for when you can't predict

### reserved

- This is more like traditional IT.
- up to 75% savings
- For long period of time.
- Need to pay upfront or partial reservation.
- Reserve for 1 or 3 years.
- Reserve specific instance type.
- Like database.

### convertible reserved

- can evolve it
- up to 54% discount

### scheduled reserved instances

- launch within a time window when you reserve
- fraction of a day, week or month

### EC2 spot instances

- Can get upto 90% discount
- You can lose at any time
- You lose if your max price is less than the current spot price
- The most cost efficient
- Good for workloads that have resiliency to failure
- Examples: image processing, batch jobs, data processing. Things you can retry.
- Not great for critical jobs or databases.

### Good combo

- Reserved instances for baseline + on demand (or spot)

### Dedicated hosts
**In Exams This is More Imp**

- Dedicated physical EC2 server
- Visibility into underlying sockets and physical cores of the hardware
- Full control of EC2 instance placement
- Allocated for a 3 year reservation
- Good for some license models
- If you have some regulatory or compliance needs

### Dedicated instances

- May share hardware with other instance but only within your account
- No control over instance placement

---

On demand if like a hotel and you come and go as you please.

Reservation is long term.

Spot - just before the night starts. They will let you bid. You can get kicked out at any time.

Dedicated hosts - book entire wing of a resort.