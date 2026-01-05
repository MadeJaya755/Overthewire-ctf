# OverTheWire Bandit — Level 23

## Objective
Retrieve the password for the next level by creating a script and placing it in a directory where a scheduled Cron job will execute it.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit23

## Method
A Cron job running as **bandit24** executes and deletes any scripts found in the directory `/var/spool/bandit24/foo`.

1.  **Analyze Script:** The cron script (`/usr/bin/cronjob_bandit24.sh`) iterates through files in the spool directory and runs them.
2.  **Create Payload:** Created a shell script in a temporary directory (e.g., `/tmp/myscript/getpass.sh`) containing:
    ```bash
    #!/bin/bash
    cat /etc/bandit_pass/bandit24 > /tmp/myscript/pass.txt
    ```
3.  **Set Permissions:** Made the script executable and world-readable/writable (`chmod 777`).
4.  **Deploy:** Copied the script to the target spool directory (`cp /tmp/myscript/getpass.sh /var/spool/bandit24/foo/`).
5.  **Wait:** Waited ~60 seconds for the Cron job to trigger.
6.  **Retrieve:** Checked `/tmp/myscript/pass.txt` for the output.

## Result
Password for the next level retrieved successfully.

`iCi86ttT4KSNe1armKiwbQNmB3YJP3q4`

## Key Takeaway
* **Cron Abuse:** Scheduled tasks that execute arbitrary files from writable directories are a major security vulnerability.
* **Automation:** Writing scripts to automate data retrieval is a core skill in exploitation.
* **Permissions:** Always ensure your scripts have the executable permission (`+x`) before deployment.
