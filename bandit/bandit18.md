# OverTheWire Bandit — Level 18

## Objective
Retrieve the password from a file named `readme` in the home directory, despite being immediately logged out upon establishing an SSH connection.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit18

## Method
The user's shell configuration (likely `.bashrc`) has been modified to instantly terminate the session upon login, displaying a "Byebye !" message.

To bypass this, commands can be executed directly via the SSH client without launching the interactive shell. By appending the command `'cat readme'` (or forcing a shell like `'/bin/sh'`) to the end of the SSH connection string, the system executes the command and returns the output before the logout script triggers.

## Result
Password for the next level retrieved successfully.

`0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO`

## Key Takeaway
* SSH allows for remote command execution without requiring a full interactive shell session.
* This technique is critical for bypassing restricted shells or broken startup scripts that prevent standard logins.
