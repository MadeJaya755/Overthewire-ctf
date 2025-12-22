# Bandit Level 3 → Level 4

## Objective
Retrieve the password for the next level from a hidden file.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The password is stored in a hidden file, which is not displayed by default when listing directory contents.

## Approach
After checking the home directory, standard listing did not reveal any readable files.  
By using an option to display hidden files, the target file became visible and could be accessed normally.

## Commands Used
```bash
ls
ls -a
cat .hidden
