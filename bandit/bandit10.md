# Bandit Level 10 → Level 11

## Objective
Retrieve the password for the next level from a file that is encoded using Base64.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access

## Challenge Overview
The password is stored in a file named `data.txt`.  
The file does not contain readable plain text, but instead appears to be Base64-encoded.

Displaying the file directly shows encoded data that cannot be used as a password without decoding.

## Approach
1. Inspect the file contents to confirm it is not plain text.
2. Identify the encoding format (Base64).
3. Decode the file using the `base64` utility.
4. Extract the decoded password from the output.

## Commands Used
```bash
cat data.txt
base64 --decode data.txt
