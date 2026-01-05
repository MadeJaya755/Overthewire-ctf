# OverTheWire Bandit — Level 6

## Objective

Locate the password stored somewhere on the system outside the home directory.

## Access

* Host: bandit.labs.overthewire.org
* Port: 2220
* Username: bandit6

## Method

The password is hidden in the filesystem and can only be found by searching with specific attributes:

* Owned by a specific user
* Belongs to a specific group
* Exact file size

A targeted system-wide search based on these constraints reveals the correct file.

## Result

Password for the next level retrieved successfully.

```
morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj
```

## Key Takeaway

* Precise search criteria are essential when the scope expands beyond a single directory.
* Broad searches without filters waste time and attention.
