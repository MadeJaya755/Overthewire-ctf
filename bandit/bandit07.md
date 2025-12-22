# Bandit Level 7 → Level 8

## Objective
Retrieve the password for the next level by locating a specific string within a text file.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The password is stored inside a large text file.  
The correct line can be identified by a specific keyword.

## Approach
Instead of manually scrolling through the file, a search utility was used to locate the line containing the required keyword.  
This approach allows fast and accurate extraction of relevant information.

## Commands Used
```bash
ls
grep "millionth" data.txt
