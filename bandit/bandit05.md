# Bandit Level 5 → Level 6

## Objective
Retrieve the password for the next level by locating a file that matches specific criteria.

## Environment
- Remote Linux system (OverTheWire Bandit)
- Access via SSH

## Challenge Overview
The target directory contains many files spread across multiple subdirectories.  
Only one file meets all required conditions:
- Human-readable
- Specific file size
- Not executable

## Approach
Instead of manually checking each file, file attributes were filtered using search criteria.  
By narrowing down the results based on size, readability, and permissions, the target file was efficiently identified.

## Commands Used
```bash
find . -type f -size 1033c ! -executable
cat ./inhere/maybehere07/.file2
