# OverTheWire Bandit — Level 21

## Objective
Retrieve the password for the next level by investigating the system's scheduled tasks (Cron jobs).

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit21

## Method
A program is running automatically at regular intervals via **Cron**.
1.  **Investigate Cron Jobs:** Checked the directory `/etc/cron.d/` and found a configuration file named `cronjob_bandit22`.
2.  **Analyze Configuration:** Reading this file (`cat /etc/cron.d/cronjob_bandit22`) revealed it executes a shell script located at `/usr/bin/cronjob_bandit22.sh`.
3.  **Inspect Script:** Reading the script (`cat /usr/bin/cronjob_bandit22.sh`) showed that it copies the password from `/etc/bandit_pass/bandit22` into a temporary file in `/tmp/` (specifically `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`) and makes it readable.
4.  **Retrieve Password:** Read the content of that temporary file.

## Result
Password for the next level retrieved successfully.

`0Zf11ioIjMVN551jX3CmStKLYqjk54Ga`

## Key Takeaway
* **Cron** is a time-based job scheduler in Unix-like systems.
* Investigating scheduled tasks (`/etc/cron.d/`, `/var/spool/cron/`) is a crucial step in understanding system automation and finding potential privilege escalation paths.
