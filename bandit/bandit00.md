# Bandit Level 0 → Level 1

## Objective
Retrieve the password for the next level by performing basic file enumeration.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Approach
After connecting to the server, basic directory listing was performed to identify available files.  
A readable file containing the credentials was found in the home directory.

## Commands Used
```bash
ls
cat readme
