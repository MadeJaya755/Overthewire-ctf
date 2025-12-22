# Bandit Level 19 → Level 20

## Objective
Retrieve the password for the next level by exploiting a SUID binary to read a protected file.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- SUID-enabled executable

## Challenge Overview
Di home directory terdapat sebuah binary bernama `bandit20-do`.

Binary ini:
- Dimiliki oleh user **bandit20**
- Memiliki **SUID bit** aktif
- Bisa menjalankan perintah sebagai owner binary, bukan sebagai user kita

Artinya: kalau dipakai dengan benar, kita bisa membaca file yang normalnya **tidak punya izin akses**.

## Approach
1. List file dan cek permission.
2. Identifikasi binary dengan SUID bit (`s`).
3. Jalankan binary tersebut untuk mengeksekusi perintah sebagai user bandit20.
4. Gunakan binary untuk membaca file password level berikutnya.

## Commands Used
```bash
ls -l
