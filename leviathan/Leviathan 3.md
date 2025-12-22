# Leviathan Level 3 → Level 4

## Objective
Retrieve the password for the next level by discovering and exploiting a hidden SUID binary.

---

## Environment
- Remote Linux system (OverTheWire Leviathan)
- SSH access
- User: `leviathan3`
- Hidden directory with executable files
- SUID-enabled binary owned by `leviathan4`

---

## Challenge Overview
Home directory terlihat kosong kalau cuma pakai `ls` biasa.
Namun terdapat **direktori tersembunyi** yang berisi binary penting.

Tidak ada hint eksplisit.
Tidak ada error message ramah.
Ini murni soal **ketelitian enumerasi**.

---

## Approach

### 1. Enumerate hidden files
```bash
ls -la
