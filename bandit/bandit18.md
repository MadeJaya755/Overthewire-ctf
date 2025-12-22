# Bandit Level 18 → Level 19

## Objective
Retrieve the password for the next level despite being immediately logged out after SSH login.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Auto-logout mechanism enabled on login

## Challenge Overview
Saat login ke Bandit Level 18:
- SSH berhasil
- Tapi langsung **auto-logout**
- Tidak ada kesempatan mengetik perintah

Ini disengaja. Tujuannya ngetes apakah lu ngerti kalau SSH bisa **menjalankan command langsung tanpa shell**.

## Approach
1. Jangan login interaktif.
2. Gunakan SSH untuk langsung mengeksekusi perintah.
3. Baca file password untuk level berikutnya.
4. Ambil output sebelum koneksi ditutup.

## Commands Used
Langsung eksekusi command lewat SSH:
```bash
ssh bandit18@bandit.labs.overthewire.org -p 2220 cat /etc/bandit_pass/bandit19
