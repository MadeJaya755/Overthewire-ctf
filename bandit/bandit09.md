# Bandit Level 9 → Level 10

## Objective
Retrieve the password for the next level from a binary file by extracting human-readable strings.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The password is stored inside a binary file.  
Directly displaying the file output produces unreadable characters.

## Approach
Instead of reading the file directly, a utility was used to extract printable strings.  
The output was then filtered to locate the line containing the password.

## Commands Used
```bash
strings data.txt
strings data.txt | grep "="
