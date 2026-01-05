# OverTheWire Bandit — Level 1

## Objective

Access the file containing the password for the next level.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit1

## Method

The password is stored in a file named `-`, which cannot be read directly without explicitly specifying the path.

By referencing the file with a relative path, the content can be accessed normally.

## Result

Password for the next level retrieved successfully.

```
263JGJPfgU6LtdEvgfWU1XP5yac29mFx
```

## Key Takeaway

* Filenames starting with special characters require explicit path handling.
* Understanding basic shell behavior prevents simple mistakes.
