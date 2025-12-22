# Bandit Level 13 → Level 14

## Objective
Retrieve the password for the next level by using an SSH private key instead of a password.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- SSH private key provided in the home directory

## Challenge Overview
Unlike previous levels, **no password is given**.  
Instead, an SSH private key file named `sshkey.private` is provided.

This level tests understanding of:
- SSH authentication
- File permissions
- Key-based login

If you try to log in with a password, you’re wasting time.

## Approach
1. List files in the home directory to locate the SSH private key.
2. Ensure the key has correct permissions (SSH is strict).
3. Use the key to authenticate to the next level via SSH.
4. Retrieve the password stored on the remote system.

## Commands Used
```bash
ls
chmod 600 sshkey.private
