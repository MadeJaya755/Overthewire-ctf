# OverTheWire Bandit — Level 2

## Objective

Retrieve the password stored in a file with spaces in its filename.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit2

## Method

The target file contains spaces in its name, which requires proper escaping or quoting to be accessed correctly via the shell.

By enclosing the filename in quotes, the file can be read without issues.

## Result

Password for the next level retrieved successfully.

```
MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx
```

## Key Takeaway

* Filenames with spaces must be quoted or escaped.
* Shell parsing rules matter in real environments.
