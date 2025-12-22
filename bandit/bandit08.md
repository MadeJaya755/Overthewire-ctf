# Bandit Level 8 → Level 9

## Objective
Retrieve the password for the next level from a file where only one line is unique.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The file contains many repeated lines, but only one line appears once.  
That unique line contains the password.

## Approach
The file content was sorted to group identical lines together.  
After sorting, a utility was used to extract the line that appears only once.

## Commands Used
```bash
sort data.txt | uniq -u
