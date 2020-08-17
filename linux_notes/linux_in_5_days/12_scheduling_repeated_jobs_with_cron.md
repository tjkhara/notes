# Scheduling repeated jobs with cron

crontab is a configuration file that specific when commands are to be run.

### Run every monday at 07:00AM

	0 7 * * 1 /opt/sales/bin/weekly-report

![crontab](pictures/crontab.png)

### Output is generally sent to your email but you can also do the following if you don't want email

Run at 02:00 every day and send output to a log file.

	0 2 * * * /root/backupdb > /tmp/db.log 2>&1

### Run a command every 15 minutes

	0,15,30,45 * * * * /opt/acme/bin/15-min-check

### Another way to do the same thing

	*/15 * * * * /opt/acme/bin/15-min-check

### Running for the first 5 minutes of the hour

	0-4 * * * * /opt/acme/bin/first-five-mins



