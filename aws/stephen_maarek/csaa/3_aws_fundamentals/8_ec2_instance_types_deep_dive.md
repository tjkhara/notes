# EC2 instance types deep dive

R - they need a lot of RAM

Example: in-memory caches

C - good cpu or compute

Example: compute/database

M - middle. Between RAM and CPU.

Example: general/web app.

I - good I/O

Example: databases

G - applications that need a GPU

Examples: video rendering/machine learning

T2/T3 - burstable instances (up to a capacity)

Burst means a good performance for a short while. Can't overuse it.

T2/T3 unlimited - unlimited burst

Real world - ec2instances.info

---

## Bustable instances T2/T3

- Burst means that overall the instance has OK performance (CPU)
- When the machine needs to process something unexpected it can burst and CPU can be very good
- Machine uses burst credits
- If they are all gone, it becomes terrible
- Credits are accumulated over time
- The bigger the instance the faster you accumulate credits