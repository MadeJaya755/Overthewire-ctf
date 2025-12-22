# Bandit Level 20 → Level 21

## Objective
Retrieve the password for the next level by interacting with a SUID binary that communicates over a TCP connection.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- SUID-enabled binary
- Local TCP connection

## Challenge Overview
Di home directory terdapat binary SUID bernama `suconnect`.

Karakteristiknya:
- Binary dijalankan sebagai **bandit21**
- Binary akan:
  1. Membuka koneksi ke port tertentu
  2. Menunggu input berupa password level saat ini
  3. Jika benar, mengirimkan password level berikutnya

Masalahnya:  
lu harus **menyediakan listener dulu**. Kalau gak, binary ini cuma bengong.

## Approach
1. Buka **dua terminal / dua session SSH**.
2. Terminal pertama:
   - Siapkan listener menggunakan `nc`.
3. Terminal kedua:
   - Jalankan binary SUID dan arahkan koneksi ke listener.
4. Kirim password level 20 lewat listener.
5. Tangkap response berisi password level 21.

## Commands Used

### Terminal 1 – Listener
```bash
nc -lvp 1234
