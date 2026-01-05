# OverTheWire Bandit — Level 25

## Objective
Retrieve the authentication credential for the next level, which is provided as an SSH private key rather than a text password.

## Access
* **Host:** bandit.labs.overthewire.org
* **Port:** 2220
* **Username:** bandit25

## Method
The home directory contains a file named `bandit26.sshkey`. The instructions indicate that the shell for the next user (`bandit26`) is not a standard bash shell, but for this level, the goal is simply to obtain the key.

1.  **Identify Key:** Verify the file exists (`ls -l`).
2.  **Usage:** This key must be used to authenticate as the next user.
    Command: `ssh -i bandit26.sshkey bandit26@localhost`

## Result
SSH Private Key obtained successfully.
s0773xxkk0MXfdqOfPRVr9L3jJBUOgCZ.

## Key Takeaway
* **SSH Identity Files:** Private keys (`.pem`, `id_rsa`, etc.) can be used for login without a password prompt.
* **Permissions:** SSH keys generally require strict file permissions (readable only by the owner) to function correctly.
