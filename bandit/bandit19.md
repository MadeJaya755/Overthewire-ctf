# OverTheWire Bandit — Level 19

## Objective
Retrieve the password for the next level by leveraging a binary with SUID (Set User ID) permissions to execute commands as another user.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit19

## Method
The home directory contains a binary named `bandit20-do`. Checking its permissions (`ls -la`) reveals it is owned by the user **bandit20** and has the **SUID bit** set (`-rwsr-x---`). This allows the program to run with the privileges of its owner rather than the current user.

By executing the binary followed by the command to read the password file (`./bandit20-do cat /etc/bandit_pass/bandit20`), the file is read with `bandit20`'s permissions, revealing the content.

## Result
Password for the next level retrieved successfully.

`EeoULMCra2q0dSkYj561DX7s1CpBuOBt`

## Key Takeaway
* **SUID (Set User ID)** is a permission bit that allows users to execute a file with the permissions of the file owner.
* While useful for system administration (e.g., `sudo`), misconfigured SUID binaries are a common vector for **Privilege Escalation**.
