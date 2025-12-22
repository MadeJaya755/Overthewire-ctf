# Bandit Level 23 → Level 24

## Objective
Retrieve the password for the next level by abusing a cron job that executes scripts placed in a specific directory.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Cron job executing scripts from a writable directory

## Challenge Overview
Cron job milik **bandit24** berjalan berkala dan:
- Mengeksekusi **semua file executable** di sebuah direktori
- Menghapus file tersebut setelah dieksekusi

Tidak ada password disalin otomatis.  
Artinya: **kita harus menyisipkan script kita sendiri** ke direktori yang dipantau cron.

Kalau nunggu, ya gak dapet apa‑apa.

## Approach
1. Identifikasi cron job dan direktori target.
2. Buat script sederhana yang:
   - Membaca `/etc/bandit_pass/bandit24`
   - Menyimpan output ke file yang bisa kita baca
3. Pastikan script executable.
4. Letakkan script di direktori cron.
5. Tunggu cron job mengeksekusi script tersebut.

## Commands Used

Lihat cron job:
```bash
cat /etc/cron.d/cronjob_bandit23
