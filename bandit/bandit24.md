# Bandit Level 24 → Level 25

## Objective
Retrieve the password for the next level by brute-forcing a 4-digit PIN required by a local service.

## Environment
- Remote Linux system (OverTheWire Bandit)
- SSH access
- Local TCP service with PIN verification

## Challenge Overview
Terdapat service yang berjalan di localhost:
- Meminta **password level 24**
- Meminta **PIN 4 digit (0000–9999)**
- Jika benar, service akan mengembalikan password level berikutnya

Masalahnya:
- Gak ada feedback detail
- Harus brute force
- Tapi **masih manusiawi**, bukan rate-limit neraka

## Approach
1. Siapkan loop untuk generate semua kemungkinan PIN (0000–9999).
2. Kirim password + PIN ke service menggunakan `nc`.
3. Filter output yang **bukan pesan gagal**.
4. Tangkap response yang berisi password level 25.

## Commands Used

Buat brute force sederhana:
```bash
for pin in $(seq -w 0000 9999); do
  echo "bandit24_password $pin"
done
