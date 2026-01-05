# OverTheWire Bandit — Level 3

## Objective

Locate and read the password stored in a hidden file.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit3

## Method

The password is located inside a hidden file within the target directory. Hidden files are not shown by default and require explicit listing.

By enabling the display of hidden files, the password file becomes visible and accessible.

## Result

Password for the next level retrieved successfully.

```
2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ
```

## Key Takeaway

* Hidden files are commonly used to conceal sensitive data.
* Always enumerate directories thoroughly, including hidden entries.
