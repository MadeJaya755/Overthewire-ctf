# Bandit Level 14 → Level 15

## Objective
Retrieve the password for the next level by submitting the current password to a local TCP service.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Local TCP service on port 30000

## Challenge Overview
The password for the next level is obtained by:
- Connecting to a TCP service running on **localhost**
- Sending the current level’s password
- Receiving the next password as a response

No web. No file. Murni network I/O.

## Approach
1. Read the current password from `/etc/bandit_pass/bandit14`.
2. Connect to the local TCP service using `nc` (netcat).
3. Send the password exactly as is.
4. Read the server response containing the next password.

## Commands Used
```bash
cat /etc/bandit_pass/bandit14
