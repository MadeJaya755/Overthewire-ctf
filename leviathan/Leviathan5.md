# Leviathan Level 5 → Level 6

## Objective
Retrieve the password for the next level by exploiting a SUID binary that uses an insecure temporary file.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan5`
- SUID-enabled binary owned by `leviathan6`
- Writable `/tmp` directory

---

## Challenge Overview
Di home directory terdapat sebuah binary SUID:
