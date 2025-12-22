# Leviathan Level 2 → Level 3

## Objective
Retrieve the password for the next level by exploiting improper handling of filenames in a SUID binary.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan2`
- SUID-enabled binary owned by `leviathan3`
- Limited permissions on password file

---

## Challenge Overview
Di home directory terdapat binary SUID:
