# OverTheWire Bandit — Level 26

## Objective
Escape from a restricted shell environment (`/usr/bin/showtext`) to gain full command access and retrieve the password for the next level.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit26
* **Authentication:** SSH Private Key (retrieved in Level 25)

## Method
Upon logging in, the system immediately executes a script that displays text using the `more` command and then closes the connection, preventing standard shell access.

1.  **Trigger Interactive Mode:** Resize the terminal window to be very small before connecting. This forces `more` to pause and wait for user input (paging).
2.  **Launch Editor:** While `more` is paused, press `v`. This launches the **Vim** text editor.
3.  **Spawn Shell:** Inside Vim, type `:set shell=/bin/bash` followed by `:shell`. This spawns a fully interactive Bash shell, bypassing the restrictions.
4.  **Retrieve Password:** With the shell active, execute the binary `./bandit27-do` (found in the home directory) to read the password file:
    `./bandit27-do cat /etc/bandit_pass/bandit27`

## Result
Password for the next level retrieved successfully.

`upsNCc7vzaRDx6oZC6GiR6ERwe1MowGB`

## Key Takeaway
* **Restricted Shells:** Systems can restrict users to specific commands, but these environments often have "escape" mechanisms via editors or pagers (like `more`, `less`, `vim`, `man`).
* **Vim Shell Escape:** The ability of Vim to execute external shell commands is a classic method for breaking out of restricted environments.
