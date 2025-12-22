# OverTheWire Leviathan Write-up

## Leviathan Level 5 → Level 6

## Objective
Retrieve the password for the next level by abusing a poorly designed SUID binary that relies on file existence checks instead of proper access control.

Level ini menguji:
- Pemahaman permission Linux
- Cara kerja SUID binary
- Kenapa “cek file ada atau tidak” itu bukan mekanisme keamanan

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan5`
- SUID executable binary
- No source code provided
- Standard Linux utilities available

---

## Challenge Overview
Di home directory user `leviathan5` terdapat sebuah binary bernama:

```text
leviathan5
