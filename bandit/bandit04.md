# Bandit Level 4 → Level 5

## Objective
Retrieve the password for the next level from a file that is human-readable among multiple files.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The directory contains multiple files, most of which are not human-readable.  
Only one file contains readable text and holds the password.

## Approach
After listing the directory contents, each file was inspected to determine its type.  
By identifying the file with readable text, the password could be extracted safely.

## Commands Used
```bash
ls
file ./*
cat ./-file07
