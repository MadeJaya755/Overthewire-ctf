# Bandit Level 2 → Level 3

## Objective
Retrieve the password for the next level from a file with spaces in its name.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The target file contains spaces in its filename, which prevents direct access without proper handling.

## Approach
After listing the files in the home directory, a file with spaces in its name was identified.  
To read the file correctly, the filename was enclosed in quotes to ensure it was interpreted as a single argument.

## Commands Used
```bash
ls
cat "spaces in this filename"
