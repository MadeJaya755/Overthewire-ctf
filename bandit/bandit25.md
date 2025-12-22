# Bandit Level 25 → Level 26

## Objective
Retrieve the password for the next level by escaping a restricted shell environment.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Restricted shell (`rbash`)
- SSH private key provided

## Challenge Overview
Saat login ke **bandit25**, kita:
- Dipaksa masuk ke **restricted shell**
- Tidak bisa:
  - ganti directory
  - set PATH
  - menjalankan banyak command
- Terlihat seperti buntu

Padahal enggak.  
Restricted shell itu **kosmetik**, bukan penjara.

## Approach
1. Login menggunakan SSH key yang disediakan.
2. Perhatikan bahwa shell dibatasi.
3. Manfaatkan program yang **masih diizinkan** untuk escape shell.
4. Dapatkan shell normal sebagai user **bandit26**.
5. Ambil password level berikutnya.

## Commands Used

Login dengan key:
```bash
ssh -i bandit26.sshkey bandit26@localhost
