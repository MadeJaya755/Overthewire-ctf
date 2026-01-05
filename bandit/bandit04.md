# OverTheWire Bandit — Level 4

## Objective

Identify and read the file containing human-readable data to obtain the next password.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit4

## Method

The target directory contains multiple files, most of which hold non-readable binary data.

By checking file types and focusing on human-readable content, the correct file can be identified and read.

## Result

Password for the next level retrieved successfully.

```
4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw
```

## Key Takeaway

* Not all files are plain text; identify file types before reading.
* Filtering noise is a core skill during enumeration.
