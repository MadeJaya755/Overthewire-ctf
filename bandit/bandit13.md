# OverTheWire Bandit — Level 13

## Objective

Use an SSH private key to access the next level and retrieve the password.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit13

## Method

Instead of a password, access to the next level is granted via an SSH private key provided in the home directory.

By using key-based authentication, a secure login can be established without relying on a plaintext password.

## Result

Password for the next level retrieved successfully.

```
MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS
```

## Key Takeaway

* SSH key-based authentication is stronger than passwords.
* Proper handling of private keys is critical for system security.
