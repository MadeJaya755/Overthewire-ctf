# Bandit Level 11 → Level 12

## Objective
Retrieve the password for the next level from a file where all lowercase and uppercase letters have been rotated by 13 positions (ROT13).

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access

## Challenge Overview
The password is stored in a file named `data.txt`.  
The content appears readable, but the characters are shifted, making the text meaningless at first glance.

This is a classic **ROT13** transformation:
- a ↔ n  
- A ↔ N  

No encryption, no mystery. Just letter rotation.

## Approach
1. Display the file to confirm it contains ROT13-encoded text.
2. Use the `tr` command to translate characters back to their original positions.
3. Read the decoded output to obtain the password.

## Commands Used
```bash
cat data.txt
cat data.txt | tr 'A-Za-z' 'N-ZA-Mn-za-m'
