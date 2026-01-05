# OverTheWire Bandit — Level 17

## Objective
Retrieve the password for the next level by comparing two files to identify the line that has been modified.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit17 (Accessed via the SSH private key retrieved in Level 16)

## Method
The home directory contains two files: `passwords.old` and `passwords.new`. The password for the next level is the only line that has changed between these two files.

By using the **`diff`** command (`diff passwords.old passwords.new`), the system compares the contents line-by-line. The output displays the difference, revealing the new password string found in `passwords.new`.

## Result
Password for the next level retrieved successfully.

`cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3j8`

## Key Takeaway
* Comparing file contents is a common task in system administration and forensics.
* The `diff` tool is efficient for identifying changes, patches, or modifications between file versions.
