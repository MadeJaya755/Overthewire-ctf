# Bandit Level 26 → Level 27

## Objective
Retrieve the password for the next level by exploiting a SUID binary that relies on the `PATH` environment variable.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- SUID-enabled binary owned by bandit27
- Restricted permissions

## Challenge Overview
Binary `bandit27-do`:
- Memiliki **SUID bit**
- Menjalankan perintah tertentu di dalam environment
- Mengandalkan `PATH` untuk menemukan executable

Jika PATH bisa dimanipulasi, binary akan mengeksekusi **script kita**, memungkinkan membaca password yang seharusnya tidak bisa diakses.

## Approach
1. Buat script payload di direktori yang bisa kita tulis:
```bash
echo "cat /etc/bandit_pass/bandit27 > /tmp/output27" > /tmp/myscript.sh
chmod +x /tmp/myscript.sh
