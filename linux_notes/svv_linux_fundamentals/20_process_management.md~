# Process management

## Understanding linux processes and jobs

![process heir](images/process_heirarchy.png)

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

## Changing top display properties

	top -u user

Top for a specific user.

	f

See all the fields.

Fields with asterisk are currently being displayed.

	Go to the filed and press spacebar

	When happy press q to get back to main screen

top by default sorts on CPU usage

	>

Process will sort on the next column

	<

Will go to the left

	VIRT

is virtual memory. The total amount of memory a process may be using.

	z

gives you colors.

	W

Will write the current settings to .toprc which is in the home directory.

## Monitoring process properties with ps

	ps aux

	ps aux | less

top is good, but this is the command line alternative.

Processes between

	[kernel_processes]

are kernel processes.

**You cannot manage the kernel processes using the kill command.**

If there is a 

	? under TTY

the process is not running in the terminal.

	ps aux | grep ssh

This will give you ssh process

	sshd

You will use the PID to manage the process.

    ps -ef

You will do

    ps -ef | less

You will like this because it shows the PPID, which is the parent process id.

The default sorting of the processes is done on PID.

    ps -fax | less

This gives you a forest display. It shows you the relationship between processes.

Before killing a process you can run this command to see what is dependent on the process.

### ps has a lot of filtering options

    ps aux --sort pmem

This is sorting on memory usage.

The highest memory usage is listed last.

    systemctl isolate multi-user.target

## Changing process priority

There are real time processes and there are normal processes.

Real time is kernel dont mess with them.

normal is everyone else.

    open top

    r key

    PID to renice

Current priority can be for example 20

Range is -20 to 19

10 means it will be friendlier towards other processes.

To give higher priority give renice it lower.

Like -10.

Requires root privileges to give negative niceness.

### renice command

    renice --help

    renice

Example

    renice -n 5 PID

    renice -n 4 12230

This will reset the priority.

Using the nice command when you start a process

    nice -n -20 dd if=/dev/zero of=/dev/null &

Now we have dd process running with priority of -20.

In top you can press k to issue the kill command.

## managing processes with kill

signals are commands that you can send to processes

SIGTERM is the termination signal

#### How to check signals?

    man 7 signal

You can use kill like

    kill PID

    kill -number PID

example:

    kill -9 1441

### -9 is a brutal way of stopping processes

Do not use this lightly.

No time to save files.

This is a last resort.

As an alternative just use

    kill PID

example

    kill 1220

### killing multiple processes with the same name

    killall dd

    killall process_name

This will kill everything that has dd in it.

## Command review

    top

performance dashboard for your server

    ps

command line utility to get information on processes

    jobs

command use to manage jobs. job is a process that is associated to a specific shell.

    fg

run processes in the foreground.

    bg

move process to the background.

bg relates to jobs.

    nice

adjust process priority.

    renice

operates on running processes.

    kill

allows you to send a signal to processes.

    killall

kill many processes with the same name.


## End of lesson lab

1. From a root shell, start three processes dd if=/dev/zero of=/dev/null as a background job.

    dd if=/dev/zero of=/dev/null &

Do this three times.


2. Use the appropriate command to show they are running as expected.

    top

or

You can also use the jobs command to verify these processes are running.

    jobs

or

    ps aux | grep dd

Sidenote:

use this regular expression instead for more precise results:

    ps aux | grep '\<dd\>'

This regular expression looks for a word starting with and ending with dd.

You can filter more by

    ps aux | grep '\<dd\>' | grep -v grep

This will get rid of the last grep result.

3. Change process priority so that one of these three jobs gets double the amount of CPU resources.

    top

    r

    Select PID to renice

    Then enter -20 for the first dd process

or

    renice -n -8 12682

    renice -n {priority_number} {PID}


4. Monitor the processes are running as expected.

    top

5. Terminate all three processes

    killall dd

