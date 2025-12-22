# Bandit Level 1 → Level 2

## Objective
Retrieve the password for the next level from a file with an unusual filename.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The target file does not follow standard naming conventions, which may cause issues when accessed using common commands.

## Approach
After listing the files in the home directory, a file with a name resembling a dash (`-`) was identified.  
Because filenames starting with special characters can be misinterpreted as command options, an explicit method was required to read the file safely.

## Commands Used
```bash
ls
cat ./-
