# Bandit Level 6 → Level 7

## Objective
Retrieve the password for the next level by locating a file owned by a specific user and group.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The password is stored somewhere on the system, but only one file matches all required conditions:
- Owned by a specific user
- Owned by a specific group
- Specific file size

## Approach
A system-wide search was performed while filtering files based on ownership and size.  
Permission errors were suppressed to keep the output clean and focused.

## Commands Used
```bash
find / -type f -user bandit7 -group bandit6 -size 33c 2>/dev/null
cat /var/lib/dpkg/info/bandit7.password
