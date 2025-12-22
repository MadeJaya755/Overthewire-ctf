# Bandit Level 12 → Level 13

## Objective
Retrieve the password for the next level from a file that has been **compressed multiple times** using common Linux compression formats.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access

## Challenge Overview
The password is hidden inside a file named `data.txt` that is **heavily compressed**.  
File extensions and `file` command hints show nested compression formats like:
- gzip (.gz)  
- bzip2 (.bz2)  
- tar (.tar)  

Simply `cat` or `less` will not reveal the password.

## Approach
1. Inspect the file type:
```bash
file data.txt
