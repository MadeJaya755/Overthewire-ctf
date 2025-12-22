# Bandit Level 22 → Level 23

## Objective
Retrieve the password for the next level by analyzing a cron job script and locating where it writes the password.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Cron job running periodically

## Challenge Overview
Terdapat cron job yang dijalankan oleh user **bandit23**.  
Cron job ini menjalankan sebuah script yang **menyalin password** ke sebuah file di `/tmp`.

Tidak ada exploit aneh.  
Masalahnya cuma satu: **di mana file output‑nya?**

## Approach
1. Lihat daftar cron job.
2. Baca script yang dijalankan cron.
3. Pahami logika penentuan nama file output.
4. Baca file tersebut dari `/tmp`.

## Commands Used

Lihat cron job:
```bash
ls -l /etc/cron.d
cat /etc/cron.d/cronjob_bandit22
