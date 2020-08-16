# Process management

## Understanding linux processes and jobs

The first is the init process the systemd process.

The PID is 1.

Everything else starts from this.

Like webserver, sshd.

What is a thread?

Process within a process

Job

Process that is running in the current shell.

Ordinary users can manage their own jobs.

Every job is a process.

## Managing interactive shell jobs

Jobs are commands that are started from the shell.

	dd if=/dev/zero of=/dev/null

dd copies block devices

This command copies nothing to nowhere. It takes forever.

Use

	control + z

to stop the job temporarily.

	bg

Will help to run it in the background.

You can also from the start run the job in the background by putting & behind it

	dd if=/dev/zero of=/dev/null &

You can type

	jobs

to see the list of jobs.

From background to get to foreground

	fg

To bring job no 2

	fg 2

If you don't like the job do control + c to terminate it.

## Monitoring processes with top

	top

	top -u tkhara

Press f to see fields.


