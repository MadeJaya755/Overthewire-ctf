# OverTheWire Bandit — Level 22

## Objective
Retrieve the password for the next level by analyzing a Cron job script that generates a dynamic filename based on the username.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit22

## Method
Similar to the previous level, a Cron job is running for the next user.
1.  **Investigate Cron:** Checked `/etc/cron.d/cronjob_bandit23` which points to the script `/usr/bin/cronjob_bandit23.sh`.
2.  **Analyze Script Logic:** The script does not use a static filename. Instead, it generates a filename using the MD5 hash of the string: `I am user bandit23`.
    * Code snippet: `echo I am user $myname | md5sum | cut -d ' ' -f 1`
3.  **Replicate Calculation:** Since we cannot run the script as bandit23, we manually calculate the target filename:
    `echo I am user bandit23 | md5sum | cut -d ' ' -f 1`
4.  **Retrieve Password:** The command outputs a hash (`8ca319486bfbbc3663fe02b561c274d8`). The password is located in `/tmp/8ca319486bfbbc3663fe02b561c274d8`.

## Result
Password for the next level retrieved successfully.

`gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8`

## Key Takeaway
* **Shell Script Analysis:** Being able to read and reverse-engineer shell scripts is essential to predict where automated tasks store data.
* **Dynamic Filenames:** Automated logs or backups often use hashes or timestamps to create unique filenames.
