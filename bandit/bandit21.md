# Bandit Level 21 → Level 22

## Objective
Retrieve the password for the next level by exploiting a scheduled cron job that runs with higher privileges.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Cron job owned by higher-privilege user

## Challenge Overview
- User **bandit21** memiliki akses ke sistem.  
- Terdapat **cron job** yang dijalankan oleh user lain atau root, secara otomatis.  
- Cron job menjalankan skrip tertentu pada interval tetap.  
- Skrip ini membaca file yang memuat password untuk level berikutnya.

Intinya: skrip **jalan otomatis**, kita tinggal “memanipulasi input / file” agar skrip mengeksekusi sesuatu yang menguntungkan.

## Approach
1. Identifikasi cron jobs yang dijalankan:
```bash
ls -la /etc/cron.d
