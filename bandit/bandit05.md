# OverTheWire Bandit — Level 5

## Objective

Find the file that meets specific conditions and extract the password for the next level.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit5

## Method

The password is hidden somewhere in the directory tree. Only one file matches all required conditions:

* Human-readable
* Exactly 1033 bytes in size
* Not executable

By searching based on file attributes instead of filenames, the correct file can be efficiently identified and read.

## Result

Password for the next level retrieved successfully.

```
HWasnPhtq9AVKe0dmk45nxy20cvUa6EG
```

## Key Takeaway

* Attribute-based searching is faster than manual inspection.
* Efficient enumeration saves time and reduces mistakes.
