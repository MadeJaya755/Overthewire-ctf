# OverTheWire Leviathan Write-up

## Leviathan Level 1 → Level 2

## Objective
Retrieve the password for the next level by analyzing and exploiting a password-checking binary.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan1`
- Executable binary with restricted access
- No source code provided

---

## Challenge Overview
Di home directory terdapat sebuah binary bernama `check`.

Binary ini meminta input password dan melakukan validasi internal.  
Tidak ada source code, tidak ada error detail, dan tidak ada petunjuk eksplisit.

Namun binary ini memiliki konfigurasi yang ceroboh.

---

## Reconnaissance
Enumerasi isi home directory:

```bash
ls -la
