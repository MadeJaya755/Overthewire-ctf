# OverTheWire Bandit — Level 11

## Objective

Recover the password from a file where all letters have been rotated.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit11

## Method

The file content is obfuscated using a simple letter rotation (ROT13).

By reversing the character substitution, the original readable text and password can be restored.

## Result

Password for the next level retrieved successfully.

```
7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4
```

## Key Takeaway

* Obfuscation is not security.
* Simple substitution ciphers offer no real protection.
